import os, sys
import shutil
import time
import json
import copy
import ntpath
import types
import string
import inspect
import tarfile
from typing import List
import numpy as np
import pandas as pd

from autopy import TransformStateFactories as ret
from autopy import TransformState
from .abstract_transform import Transform

from chemscripts.excelutils import ExcelSheet
from chemscripts.nbo.isosurfaces import generate_isosurface
from chemscripts.nbo import NBO3LogParser, NBO6LogParser, NboSymmMatrix, generate_reorder_map
from chemscripts import utils, nbo
from chemscripts import fchkutils
IRC_SKIP_POINTS = 40

NBO_PAIRING = {
    'dmmo': 419,
    'dmnbo': 420,
    'fmo': 699,
    'fnbo': 69,
    'aomo': 228,
    'aonbo': 288,
}


item_to_str = lambda i: i if isinstance(i, str) else i.name

# def if_check(condition, result, other=None):
#     if condition:
#         return (result,)
#     elif other is None:
#         return tuple()
#     else:
#         return (other,)


def nonblocking_subprocess(name,
        input,
        output,
        command_prepare,
        output_process,
        aware_keys=[],
        merged_keys=[],
        nproc=1,
        calcdir=None,
    ):
    if not isinstance(input, list):
        input = [input]
    if not isinstance(output, list):
        output = [output]

    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(x) for x in input],
        TARGET_ITEMS = [item_to_str(x) for x in output],
        AWARE_KEYS = aware_keys,
        MERGED_KEYS = merged_keys,
    )

    def RunSubprocess_exec(thread_manager, **kw):
        full_kwargs = {**kw}
        if calcdir is not None:
            id, current_calcdir = thread_manager.prepare_new_job()
            full_kwargs[calcdir] = current_calcdir
        else:
            id = thread_manager.prepare_new_job(use_calcdir=False)
        full_kwargs['id'] = id

        execution_command = command_prepare(**full_kwargs)

        thread_manager.run_nonblocking(
            id=id,
            command=execution_command,
            nproc=nproc
        )

        return ret.transform_later(comeback='wait', id=id)
    
    def RunSubprocess_wait(thread_manager, id, **kw):
        if not thread_manager.is_finished(id):
            return ret.transform_later(comeback='wait', id=id)
        else:
            return ret.transform_repeat(comeback='finish', id=id)

    def RunSubprocess_finish(thread_manager, id, **kw):
        full_kwargs = {'id': id, **kw}
        if calcdir is not None:
            current_calcdir = thread_manager.id_to_calcdir(id)
            full_kwargs[calcdir] = current_calcdir
        output_process(**full_kwargs)
        thread_manager.finalize_task(id)
        return ret.transform_finished()
    
    res.set_method({
        'exec': RunSubprocess_exec,
        'wait': RunSubprocess_wait,
        'finish': RunSubprocess_finish,
    })
    
    return res


def function_to_script(f, subs={}):
    defaults = {
        'module_dir': os.getcwd()
    }
    script_text = inspect.getsource(f)
    script_lines = script_text.split('\n')[1:]

    starting_spaces = None
    for i, line in enumerate(script_lines):
        if len(line.replace(' ', '')) == 0:
            continue
        cur_spaces = len(line) - len(line.lstrip())
        if starting_spaces is None or starting_spaces > cur_spaces:
            starting_spaces = cur_spaces

    for i, line in enumerate(script_lines):
        script_lines[i] = script_lines[i][starting_spaces:]
    
    replacements = set()
    for i, line in enumerate(script_lines):
        if 'INSERT_HERE' not in line:
            continue

        assert line.count('=') == 1
        var_name = line.split('=')[0].strip()
        assert var_name in subs or var_name in defaults, f"Variable '{var_name}' of script template '{f.__name__}' was not defined"
        assert line.split('=')[1].strip() == 'INSERT_HERE'
        
        if var_name in subs:
            value = subs[var_name]
        else:
            value = defaults[var_name]

        script_lines[i] = line.replace('INSERT_HERE', repr(value))
        replacements.add(var_name)
    # assert len(replacements) == len(subs)

    return '\n'.join(script_lines)

def write_py_function(file, f, args, subs={}) -> str:
    assert os.path.isabs(file), f"Path '{file}' must be absolute"

    script_text = function_to_script(f, subs=subs)
    with open(file, 'w') as f:
        f.write(script_text)

    args_text = ' '.join([f'"{x}"' if isinstance(x, str) else f'"{repr(x)}"' for x in args])
    execution_command = f"{sys.executable} {file} {args_text}"
    return execution_command

def get_arg_extension(mapping):
    if isinstance(mapping, dict):
        key_change = mapping
    elif isinstance(mapping, str):
        mapping = '\n'.join([
            line
            for line in mapping.splitlines()
            if not line.lstrip().startswith('#') # Ignore comment lines
        ])
        key_change = {}
        for part in mapping.split():
            sides = part.split('->')
            key_change[sides[1]] = sides[0] # Maps 'parent_key' -> 'child_key'
    
    def extension(input):
        return {
            key if key not in key_change
            else key_change[key]
                : value
            for key, value in input.items()
        }
    return extension

def pyfunction_subprocess(name,
        input,
        output,
        output_process,
        custom_command=None,
        pyfunction=None,
        argv_prepare=None,
        pyfile=None,
        aware_keys=[],
        merged_keys=[],
        calcdir=None,
        subs=None,
        nproc=1,
    ):
    assert pyfile is not None or calcdir is not None
    assert custom_command is not None or \
        (pyfunction is not None and argv_prepare is not None)
    if custom_command is not None:
        assert pyfunction is None and argv_prepare is None
    if subs is not None:
        assert pyfunction is not None
    
    if not isinstance(input, list):
        input = [input]
    if not isinstance(output, list):
        output = [output]
    if pyfile is not None:
        output.append('pyfile')

    arg_renames = []
    if pyfile is not None:
        arg_renames.append(f"{item_to_str(pyfile)}->pyfile")
    arg_extend = get_arg_extension(' '.join(arg_renames))

    def command_prepare(**kw):
        if pyfile is not None:
            pyfile_fname = kw['pyfile'].get_path()
        
        if calcdir is not None:
            script_path = os.path.join(kw[calcdir], 'script.py')
        elif pyfile is not None and calcdir is None:
            script_path = pyfile_fname

        if custom_command is not None:
            execution_command = custom_command(file=script_path, **arg_extend(kw))
        else:
            if subs is not None:
                subs_optional = {'subs': subs(**arg_extend(kw))}
            else:
                subs_optional = {}
            execution_command = write_py_function(
                file=script_path,
                f=pyfunction,
                args=argv_prepare(**arg_extend(kw)),
                **subs_optional
            )

        if pyfile is not None and calcdir is not None:
            shutil.copy2(script_path, pyfile_fname)
        if pyfile is not None:
            kw['pyfile'].include_element(pyfile_fname)

        return execution_command

    def output_process_raw(**kw):
        output_process(**arg_extend(kw))

    template = nonblocking_subprocess(
        'pyfunction_subprocess_template',
        input=input,
        output=output,
        command_prepare=command_prepare,
        output_process=output_process_raw,
        aware_keys=aware_keys,
        merged_keys=merged_keys,
        nproc=nproc,
        calcdir=calcdir,
    )
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = template.specs['SOURCE_ITEMS'],
        TARGET_ITEMS = [item_to_str(x) if x != 'pyfile' else pyfile for x in template.specs['TARGET_ITEMS']],
        AWARE_KEYS = template.specs['AWARE_KEYS'],
        MERGED_KEYS = template.specs['MERGED_KEYS'],
    )
    res.extend(template, ' '.join(arg_renames))
    return res

#
# EXCEL
#
def parse_xlsx(name, input, output, block_name='Main'):
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )

    def ParseXlsx_exec(xlsx, df):
        xlsx_path = xlsx.access_element()
        sheet = ExcelSheet()
        sheet.read_xlsx(xlsx_path)
        block = sheet.block(block_name)
        df.include_element(block['data'])
        return ret.transform_finished()

    ParseXlsx_template = Transform(
        NAME = 'ParseXlsxtemplate',
        SOURCE_ITEMS = ['xlsx'],
        TARGET_ITEMS = ['df'],
    )
    ParseXlsx_template.set_method({'exec': ParseXlsx_exec})

    res.extend(ParseXlsx_template, f"""\
        {item_to_str(input)}->xlsx
        {item_to_str(output)}->df
    """)
    return res

def construct_excel_sheet(name, input, block_name, sheet=None, xlsx=None, block_sort_key=None, merged_keys=[]):
    additional_targets = []
    additional_targets_renamed = []
    additional_renames = []
    assert sheet is not None or xlsx is not None

    if sheet is not None:
        sheet_name = item_to_str(sheet)
        additional_targets.append('sheet')
        additional_targets_renamed.append(sheet_name)
        additional_renames.append(f'{sheet_name}->sheet')

    if xlsx is not None:
        xlsx_name = item_to_str(xlsx)
        additional_targets.append('xlsx')
        additional_targets_renamed.append(xlsx_name)
        additional_renames.append(f'{xlsx_name}->xlsx')

    template = Transform(
        NAME = name,
        SOURCE_ITEMS = ['data'],
        TARGET_ITEMS = [*additional_targets],
        MERGED_KEYS = merged_keys
    )

    def ConstructExcel_exec(data, **kw):
        excelsheet = ExcelSheet()

        blocks = []
        for block_data, keys in data:
            cur_blockname = block_name(block_data)
            blocks.append({
                'data': block_data,
                'keys': keys,
                'name': cur_blockname,
            })

        if block_sort_key is not None:
            blocks.sort(key=block_sort_key)
        else:
            blocks.sort(key=lambda x: x['name'])

        for full_dict in blocks:
            block_data, keys, cur_blockname = full_dict['data'], full_dict['keys'], full_dict['name']
            column_names = list(set(
                key
                for element in block_data
                for key in element.keys()
            ))
            excelsheet.add_block(
                blockname=cur_blockname,
                cols=column_names
            )
            for element in block_data:
                excelsheet.add_row(blockname=cur_blockname, data=element)
        if sheet is not None:
            kw['sheet'].include_element(excelsheet)
        if xlsx is not None:
            res_fname = kw['xlsx'].get_path()
            excelsheet.save_xlsx(res_fname)
            kw['xlsx'].include_element(res_fname)
        return ret.transform_finished()
    
    template.set_method({'exec': ConstructExcel_exec})
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [*additional_targets_renamed],
        MERGED_KEYS = merged_keys
    )
    res.extend(template, f"""\
        {item_to_str(input)}->data
        {' '.join(additional_renames)}
    """)
    return res

#
# DF OPERATIONS
#

# Extract rows
def ExtractDfRows_exec(df, rows):
    df_object = df.access_element()
    assert isinstance(df_object, list)
    row_keys = rows.public_keys
    for item in df_object:
        key_values = {
            key: value
            for key, value in item.items()
            if key in row_keys
        }
        short_item = {
            key: value
            for key, value in item.items()
            if key not in row_keys
        }
        rows.include_element(short_item, **key_values)
    return ret.transform_finished()

ExtractDfRows_template = Transform(
    NAME = 'ExtractDfRowstemplate',
    SOURCE_ITEMS = ['df'],
    TARGET_ITEMS = ['rows'],
)
ExtractDfRows_template.set_method({'exec': ExtractDfRows_exec})

def extract_df_rows(name, input, output):
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )
    res.extend(ExtractDfRows_template, f"""\
        {item_to_str(input)}->df
        {item_to_str(output)}->rows
    """)
    return res


# Extract specific column
def extract_df_column(name, input, output, column_name):
    template = Transform(
        NAME = name,
        SOURCE_ITEMS = ['df'],
        TARGET_ITEMS = ['column'],
    )
    def ExtractDfColumn_exec(df, column):
        df_object = df.access_element()
        assert isinstance(df_object, list)
        column_keys = column.public_keys
        for item in df_object:
            key_values = {
                key: value
                for key, value in item.items()
                if key in column_keys
            }
            column.include_element(item[column_name], **key_values)
        return ret.transform_finished()
    template.set_method({'exec': ExtractDfColumn_exec})
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )
    res.extend(template, f"""\
        {item_to_str(input)}->df
        {item_to_str(output)}->column
    """)
    return res

#
# BASIC DATA OPERATIONS
#

def select(name, input, output, select_method, merged_keys=None):
    if merged_keys is None:
        add_kw = {}
    else:
        add_kw = {'MERGED_KEYS': merged_keys}

    template = Transform(
        NAME = name,
        SOURCE_ITEMS = ['data'],
        TARGET_ITEMS = ['selected'],
        **add_kw
    )
    def Select_exec(data, selected):
        selected.include_element(
            select_method([x for x in data])
        )
        return ret.transform_finished()
    template.set_method({'exec': Select_exec})
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
        **add_kw
    )
    res.extend(template, f"""\
        {item_to_str(input)}->data
        {item_to_str(output)}->selected
    """)
    return res

def exec(name, input, output, method, note=[], aware_keys=[], merged_keys=[]):
    if isinstance(input, list):
        input_array = [item_to_str(x) for x in input]
    else:
        input_array = [item_to_str(input)]
        
    if isinstance(output, list):
        output_array = [item_to_str(x) for x in output]
    else:
        output_array = [item_to_str(output)]

    if isinstance(note, list):
        note_array = [item_to_str(x) for x in note]
    else:
        note_array = [item_to_str(note)]

    res = Transform(
        NAME = name,
        SOURCE_ITEMS = input_array,
        TARGET_ITEMS = output_array,
        NOTE_ITEMS = note_array,
        AWARE_KEYS = aware_keys,
        MERGED_KEYS = merged_keys
    )

    def method_wrapper(**kw):
        res = method(**kw)
        if res is None:
            return ret.transform_finished()
        else:
            assert isinstance(res, TransformState), f"Value returned by exec method '{method}' is not a TransformState"
            return res

    res.set_method({'exec': method_wrapper})
    return res

def verify_type_consistency(*items):
    assert all(item.is_file for item in items) or all(item.is_object for item in items), \
        f"Inconsistent typing of items: {', '.join(f'item.name' for item in items)}"

def map(name,
        input,
        output,
        mapping, 
        aware_keys=[],
        note_items=[],
        ensure_one_to_one=False, 
        ensure_new_keys=None,
        include_none=True
    ):
    if isinstance(input, list):
        input_array = [item_to_str(x) for x in input]
    else:
        input_array = [item_to_str(input)]
    assert not isinstance(output, list)
    output_item = item_to_str(output)

    res = Transform(
        NAME = name,
        SOURCE_ITEMS = input_array,
        TARGET_ITEMS = [output_item],
        NOTE_ITEMS = note_items,
        AWARE_KEYS = aware_keys
    )
    
    if ensure_new_keys is not None:
        ensure_new_keys = set(ensure_new_keys)

    def Map_exec(**kw):
        add_args = {}
        if kw[output_item].is_file:
            add_args[output_item] = kw[output_item].get_path()
        
        for note_item in note_items:
            assert kw[note_item].is_path, f"Expected path (file/dir) as note item. Got '{note_item}'"
            assert len(kw[note_item].public_keys) == 0, f"Note item '{note_item}' has some unresolved keys: {kw[note_item].public_keys}"
        
        result = mapping(
            **{
                inp_item: kw[inp_item].access_element()
                for inp_item in input_array
            },
            **{
                note_item: kw[note_item].get_path()
                for note_item in note_items
            },
            **{
                aware_key: kw[aware_key]
                for aware_key in aware_keys
            },
            **add_args
        )

        expansion = isinstance(result, types.GeneratorType)
        if expansion:
            assert not ensure_one_to_one, f"Unexpected expansion during map '{name}'"
            for value, keys in result:
                if ensure_new_keys is not None:
                    assert set(keys.keys()) == ensure_new_keys, \
                        f"Mismatch between created keys '{set(keys.keys())}' and expected ones '{repr(ensure_new_keys)}'"
                
                if value is not None or include_none:
                    kw[item_to_str(output)].include_element(value, **keys)
        else:
            if result is not None or include_none:
                kw[item_to_str(output)].include_element(result)

        return ret.transform_finished()
    
    res.set_method({'exec': Map_exec})
    return res

def forward_file(target, input_file=None, keys={}, input=None, copy_method=None):
    assert (input is None) ^ (input_file is None)

    if input is not None:
        old_path = input.access_element(**keys)
    else:
        old_path = input_file

    new_path = target.get_path(**keys)

    if copy_method is not None:
        copy_method(old_path, new_path)
    else:
        shutil.copy2(old_path, new_path)
    
    target.include_element(new_path)

def forward_object(target, input_object=None, keys={}, input=None, copy_method=None):
    assert (input is None) ^ (input_object is None)

    if input is not None:
        old_object = input.access_element(**keys)
    else:
        old_object = input_object

    if copy_method is None:
        new_object = copy.deepcopy(old_object)
    else:
        new_object = copy_method(old_object)

    target.include_element(new_object, **keys)

def forward_any_type(target, input=None, input_element=None, file_copy=None, object_copy=None, **kwargs):
    if input is not None:
        verify_type_consistency(target, input)
    
    if target.is_file:
        forward_file(target=target, input=input, input_file=input_element, copy_method=file_copy, **kwargs)
    elif target.is_object:
        forward_object(target=target, input=input, input_object=input_element, copy_method=object_copy, **kwargs)
    else:
        raise RuntimeError(f"Unknown type of '{target.name}'")


def restrict(name, input, ref, output, merged_keys=[], copy_method=None):
    template = Transform(
        NAME = name,
        SOURCE_ITEMS = ['input', 'ref'],
        TARGET_ITEMS = ['output'],
        MERGED_KEYS = merged_keys
    )

    def Restrict_exec(input, ref, output, **kw):
        assert not ((input.is_object) ^ (output.is_object)), f"{input.name}.is_object = {input.is_object}, {output.name}.is_object = {output.is_object}"
        assert not ((input.is_file) ^ (output.is_file)), f"{input.name}.is_file = {input.is_file}, {output.name}.is_file = {output.is_file}"
        if copy_method is not None:
            assert input.is_object, "Object copy method is provided but we are not dealing with objects here"

        input_keys = set(input.public_keys)
        ref_keys = set(ref.public_keys)
        output_keys = set(output.public_keys)
        merged_set = set(merged_keys)
        restriction_set = input_keys.intersection(ref_keys).intersection(output_keys).intersection(merged_set)
        assert len(restriction_set) > 0, f"No keys to perform restriction"

        accepted_kvpairs = []
        for _, keys in ref:
            kvpair = {
                key: value
                for key, value in keys.items()
                if key in restriction_set
            }
            if kvpair not in accepted_kvpairs:
                accepted_kvpairs.append(kvpair)
        
        for accepted_kvpair in accepted_kvpairs:
            forward_any_type(
                input=input,
                keys=accepted_kvpair,
                target=output,
                object_copy=copy_method
            )
        return ret.transform_finished()

    template.set_method({'exec': Restrict_exec})
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input), item_to_str(ref)],
        TARGET_ITEMS = [item_to_str(output)],
        MERGED_KEYS = merged_keys
    )
    res.extend(template, f"""\
        {item_to_str(input)}->input
        {item_to_str(ref)}->ref
        {item_to_str(output)}->output
    """)
    return res


def substitute(name, input, substituent, output, merged_keys, copy_method=None):
    template = Transform(
        NAME = name,
        SOURCE_ITEMS = ['input', 'substituent'],
        TARGET_ITEMS = ['output'],
        MERGED_KEYS = merged_keys
    )

    def Substitute_exec(input, substituent, output, **kw):
        # Primary checks
        verify_type_consistency(input, substituent, output)
        if copy_method is not None:
            assert input.is_object, "Object copy method is provided but we are not dealing with objects here"

        input_keys = set(input.public_keys)
        substituent_keys = set(substituent.public_keys)
        output_keys = set(output.public_keys)
        assert input_keys == substituent_keys and substituent_keys == output_keys, \
            f"Keys mismatch: input_keys='{input_keys}', substituent_keys='{substituent_keys}', output_keys='{output_keys}'"
        
        # Forward all primary elements
        for start_element, keys in input:
            forward_any_type(
                input_element=start_element,
                keys=keys,
                target=output,
                object_copy=copy_method
            )

        # Borrow missing elements from substituent
        input_kvset = [keys for _, keys in input]
        for start_element, keys in substituent:
            if keys not in input_kvset:
                forward_any_type(
                    input_element=start_element,
                    keys=keys,
                    target=output,
                    object_copy=copy_method
                )
        return ret.transform_finished()

    template.set_method({'exec': Substitute_exec})
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input), item_to_str(substituent)],
        TARGET_ITEMS = [item_to_str(output)],
        MERGED_KEYS = merged_keys
    )
    res.extend(template, f"""\
        {item_to_str(input)}->input
        {item_to_str(substituent)}->substituent
        {item_to_str(output)}->output
    """)
    return res

class CustomTransformProxy:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    def _run_factory(self):
        assert 'factory' in self.kwargs, f"Custom transform is missing its factory: '{self.kwargs}'"
        factory = self.kwargs['factory']
        assert callable(factory), f"The transform factory '{factory}' is not callable"
        return factory(**{
            key: value
            for key, value in self.kwargs.items()
            if key != 'factory'
        })

    def _update_kwargs(self, modifying_kwargs: dict):
        for key, value in modifying_kwargs.items():
            self.kwargs[key] = value

    def customize(self, **modifying_kwargs) -> Transform:
        self._update_kwargs(modifying_kwargs)
        return self._run_factory()

    def use_default(self) -> Transform:
        return self._run_factory()

def custom(name, **kw):
    return CustomTransformProxy(name=name, **kw)


#
# RDKIT
#

# Create Mol instance
def RdkitMolFromSmiles_exec(smiles, mol):
    smiles_str = smiles.access_element()
    
    from rdkit import Chem
    params = Chem.SmilesParserParams()
    params.removeHs = False
    params.sanitize = True
    mol_object = Chem.MolFromSmiles(smiles_str, params)
    mol_object = Chem.AddHs(mol_object)

    mol.include_element(mol_object)
    return ret.transform_finished()

RdkitMolFromSmiles_template = Transform(
    NAME = 'RdkitMolFromSmilestemplate',
    SOURCE_ITEMS = ['smiles'],
    TARGET_ITEMS = ['mol'],
)
RdkitMolFromSmiles_template.set_method({'exec': RdkitMolFromSmiles_exec})

def rdkit_from_smiles(name, input, output):
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )
    res.extend(RdkitMolFromSmiles_template, f"""\
        {item_to_str(input)}->smiles
        {item_to_str(output)}->mol
    """)
    return res

# Perform conformational sampling
def rdkit_sampling(name, input, output, num_tries, postprocessing=None):
    template = Transform(
        NAME = name,
        SOURCE_ITEMS = ['mol'],
        TARGET_ITEMS = ['conformers'],
    )

    def RdkitSampling_exec(mol, conformers):
        from rdkit import Chem
        from rdkit.Chem import AllChem
        from ringo import Confpool

        mol_object = mol.access_element()
        assert isinstance(mol_object, Chem.rdchem.Mol)
        p = Confpool()

        for conformer_idx in range(num_tries):
            AllChem.EmbedMolecule(mol_object)

            geom = np.zeros((mol_object.GetNumAtoms(), 3))
            for i in range(mol_object.GetNumAtoms()):
                pos = mol_object.GetConformer().GetAtomPosition(i)
                geom[i, 0] = pos.x
                geom[i, 1] = pos.y
                geom[i, 2] = pos.z
            p.include_from_xyz(geom, f"Conformer {conformer_idx}")

        p.atom_symbols = [atom.GetSymbol() for atom in mol_object.GetAtoms()]
        if postprocessing is not None:
            postprocessing(p)

        conformers.include_element(p)
        return ret.transform_finished()
    template.set_method({'exec': RdkitSampling_exec})
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )
    res.extend(template, f"""\
        {item_to_str(input)}->mol
        {item_to_str(output)}->conformers
    """)
    return res

#
# CREST
#

# Perform conformational sampling
def crest_sampling(name, input, output, level, nproc=None):
    template = Transform(
        NAME = name,
        SOURCE_ITEMS = ['start'],
        TARGET_ITEMS = ['conformers_xyz'],
    )

    def CrestSampling_exec(start, thread_manager, **kw):
        start_data = start.access_element()
        xyz, syms = start_data['xyz'], start_data['sym']

        id, calcdir = thread_manager.prepare_new_job()
        utils.write_xyz(xyz, syms, os.path.join(calcdir, 'start.xyz'))
        if nproc is None:
            if thread_manager.maxproc < 8:
                nproc_local = thread_manager.maxproc
            else:
                nproc_local = 8
        else:
            nproc_local = nproc

        thread_manager.run_nonblocking(id, f'exec_crest.sh {calcdir} start.xyz {level} -T {nproc_local}', nproc_local)

        return ret.transform_later(comeback='wait', id=id)
    
    def CrestSampling_wait(thread_manager, id, **kw):
        if not thread_manager.is_finished(id):
            return ret.transform_later(comeback='wait', id=id)
        else:
            return ret.transform_repeat(comeback='finish', id=id)
    
    def CrestSampling_finish(conformers_xyz, thread_manager, id, **kw):
        calcdir = thread_manager.id_to_calcdir(id)
        conformers_file = os.path.join(calcdir, 'crest_conformers.xyz')
        assert os.path.isfile(conformers_file), f"Cannot find file '{conformers_file}'"

        final_xyz_name = conformers_xyz.get_path()
        shutil.copy2(conformers_file, final_xyz_name)
        conformers_xyz.include_element(final_xyz_name)

        thread_manager.finalize_task(id)
        return ret.transform_finished()
    
    template.set_method({
        'exec': CrestSampling_exec,
        'wait': CrestSampling_wait,
        'finish': CrestSampling_finish,
    })
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )
    res.extend(template, f"""\
        {item_to_str(input)}->start
        {item_to_str(output)}->conformers_xyz
    """)
    return res


#
# Confpool
#

# Save Confpool
def SaveConfpool_exec(confpool, xyz):
    p = confpool.access_element()
    xyzname = xyz.get_path()
    p.save(xyzname)
    xyz.include_element(xyzname)
    return ret.transform_finished()

SaveConfpool_template = Transform(
    NAME = 'SaveConfpooltemplate',
    SOURCE_ITEMS = ['confpool'],
    TARGET_ITEMS = ['xyz'],
)
SaveConfpool_template.set_method({'exec': SaveConfpool_exec})

def save_confpool(name, input, output):
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )
    res.extend(SaveConfpool_template, f"""\
        {item_to_str(input)}->confpool
        {item_to_str(output)}->xyz
    """)
    return res

# Load Confpool
def load_confpool(name, input, output, postprocessing=None, merged_keys=None, load_keys=[]):
    if merged_keys is None:
        add_kw = {}
    else:
        add_kw = {'MERGED_KEYS': merged_keys}
    
    LoadConfpool_template = Transform(
        NAME = 'LoadConfpooltemplate',
        SOURCE_ITEMS = ['xyz'],
        TARGET_ITEMS = ['confpool'],
        **add_kw
    )

    def LoadConfpool_exec(xyz, confpool, **kw):
        from ringo import Confpool
        p = Confpool()
        atom_symbols = None
        for elem, _ in xyz:
            if isinstance(elem, str):
                p.include_from_file(elem)
            elif isinstance(elem, dict):
                if atom_symbols is None:
                    atom_symbols = elem['sym']
                else:
                    assert atom_symbols == elem['sym']
                p.include_from_xyz(elem['xyz'], '')
                for key in load_keys:
                    assert key in elem
                    p[len(p) - 1][key] = float(elem[key])
            else:
                raise TypeError(f"Cannot process type '{type(elem)}'")
        if atom_symbols is not None:
            p.atom_symbols = atom_symbols
        
        if postprocessing is not None:
            postprocessing(p)
        
        confpool.include_element(p)
        return ret.transform_finished()
    
    LoadConfpool_template.set_method({'exec': LoadConfpool_exec})
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
        **add_kw
    )
    res.extend(LoadConfpool_template, f"""\
        {item_to_str(input)}->xyz
        {item_to_str(output)}->confpool
    """)
    return res

# Merge Confpools
def merge_confpools(name, inputs, output, postprocessing=None):
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(x) for x in inputs],
        TARGET_ITEMS = [item_to_str(output)],
    )

    def MergeConfpools_exec(**kw):
        from ringo import Confpool
        p = Confpool()
        atom_symbols = None
        for inp_item in inputs:
            for source_p, _ in kw[inp_item]:
                if atom_symbols is not None:
                    assert atom_symbols == source_p.atom_symbols
                else:
                    atom_symbols = source_p.atom_symbols
                
                for m in source_p:
                    p.include_from_xyz(m.xyz, m.descr)
        p.atom_symbols = atom_symbols

        if postprocessing is not None:
            postprocessing(p)

        kw[output].include_element(p)
        return ret.transform_finished()
    res.set_method({'exec': MergeConfpools_exec})
    return res

# Split Confpool
def split_confpool(name, input, output, keygen):
    template = Transform(
        NAME = name,
        SOURCE_ITEMS = ['confpool'],
        TARGET_ITEMS = ['structs'],
    )

    def SplitConfpool_exec(confpool, structs):
        p = confpool.access_element()

        keys = structs.public_keys
        assert len(keys) == 1
        key = keys[0]
        
        for m in p:
            structs.include_element({
                    'xyz': m.xyz,
                    'sym': p.atom_symbols,
                },
                **{key: keygen(m)}
            )
        return ret.transform_finished()
    template.set_method({'exec': SplitConfpool_exec})
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )
    res.extend(template, f"""\
        {item_to_str(input)}->confpool
        {item_to_str(output)}->structs
    """)
    return res

def xyz_to_file(name, input, output, merged_keys=[], description=None, sort_key=None):
    template = Transform(
        NAME = name,
        SOURCE_ITEMS = ['geom'],
        TARGET_ITEMS = ['xyzfile'],
        MERGED_KEYS = merged_keys
    )

    def XyzToFile_exec(geom, xyzfile):
        from ringo import Confpool
        p = Confpool()
        atom_symbols = None
        geom_elements = [x for x in geom]
        if sort_key is not None:
            geom_elements.sort(key=sort_key)

        for data, keys in geom_elements:
            if description is not None:
                kwargs = {
                    **keys,
                    **{
                        key: value
                        for key, value in data.items()
                        if key not in ('xyz', 'sym')
                    }
                }
                p.include_from_xyz(data['xyz'], description(**kwargs))
            else:
                p.include_from_xyz(data['xyz'], **keys)
            
            if atom_symbols is not None:
                assert atom_symbols == data['sym']
            else:
                atom_symbols = copy.copy(data['sym'])
                p.atom_symbols = data['sym']
        xyzname = xyzfile.get_path()
        p.save(xyzname)
        xyzfile.include_element(xyzname)
        return ret.transform_finished()
    
    template.set_method({'exec': XyzToFile_exec})
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
        MERGED_KEYS = merged_keys
    )
    res.extend(template, f"""\
        {item_to_str(input)}->geom
        {item_to_str(output)}->xyzfile
    """)
    return res

#
# GAUSSIAN
#

def xyz_from_gausslog(logname, get_scf=False, get_qh=False, keep_name=True):
    xyz, sym = utils.parse_gaussian_log(logname)
    res = {
        'xyz': xyz,
        'sym': sym,
    }
    if keep_name:
        res['log'] = logname
    if get_scf:
        res['scf'] = utils.get_gaussian_scfener(logname)
    if get_qh:
        res['qhG'] = utils.get_goodvibes_g(logname)
    return res

def load_gauss_scan(logname: str, gen_key, get_scf: bool=False, get_variable: bool=True):
    scan_data = utils.parse_gaussian_scan(logname=logname, keep_energy=get_scf, get_variable=get_variable)
    for i, data_item in enumerate(scan_data):
        res = {
            'xyz': data_item['xyzs'],
            'sym': data_item['syms'],
            'var': data_item['variable'],
        }
        if get_scf:
            res['scf'] = float(data_item['scfener'])
        yield res, gen_key(index=i, data=res)

def _irc_include_point(xyz, sym, energy, rxcoord, get_scf: bool=False, get_rxcoord: bool=False, get_parameters=None):
    res = {
        'xyz': xyz,
        'sym': sym,
    }
    if get_scf:
        res['scf'] = energy
    if get_rxcoord:
        res['rxcoord'] = rxcoord
    if get_parameters is not None:
        from ringo import Confpool
        p = Confpool()
        p.include_from_xyz(res['xyz'], '')
        p.atom_symbols = res['sym']
        res = {
            **res,
            **get_parameters(p[0])
        }
    return res

def load_gauss_irc(logname: str, gen_key, get_start: bool=True, **kwargs):
    irc_data = utils.parse_irc(logname=logname, verify=False)
    irc_points = irc_data['points']
    
    if get_start:
        res = _irc_include_point(xyz=irc_points['start'], sym=irc_data['syms'], energy=irc_points['start_energy'], rxcoord=0.0, **kwargs)
        yield res, gen_key(data=res, index=0)
        
    for index, (xyz, rxcoord, energy) in enumerate(zip(irc_points['f_geoms'], irc_points['f_rxcoord'], irc_points['f_energy'])):
        res = _irc_include_point(xyz=xyz, sym=irc_data['syms'], energy=energy, rxcoord=rxcoord, **kwargs)
        yield res, gen_key(data=res, index=index+1)

    for index, (xyz, rxcoord, energy) in enumerate(zip(irc_points['b_geoms'], irc_points['b_rxcoord'], irc_points['b_energy'])):
        res = _irc_include_point(xyz=xyz, sym=irc_data['syms'], energy=energy, rxcoord=rxcoord, **kwargs)
        yield res, gen_key(data=res, index=-index-1)


def prepare_gjf(gjftext: str, remove_chk, remove_oldchk):
    lines = gjftext.splitlines()
    kwline_index = None
    for i, line in enumerate(lines):
        if line.startswith('#'):
            kwline_index = i
            break
    assert kwline_index is not None
    for i in reversed(range(kwline_index)):
        if lines[i].startswith('%chk=') and remove_chk or \
           lines[i].startswith('%oldchk=') and remove_oldchk:
            del lines[i]
    return '\n'.join(lines)

def fstring_key_iter(input: str) -> List[str]:
    for t in string.Formatter().parse(input):
        if t[1] is not None:
            yield t[1]


def run_gaussian(name,
        inpgeom,
        gjf_template,
        log,
        output=None,
        output_method=None,
        gjf=None,
        chk=None,
        oldchk=None,
        additional_files=None, # raw generated file -> fileitem
        nproc=None,
        **kwargs
    ):
    assert utils.check_availability('exec_gaussian.sh')

    additional_sources = []
    additional_sources_renamed = []
    additional_targets = []
    additional_targets_renamed = []
    additional_renames = []

    if gjf is not None:
        additional_targets.append('gjf')
        additional_targets_renamed.append(item_to_str(gjf))
        additional_renames.append(f'{item_to_str(gjf)}->gjf')
    if chk is not None:
        additional_targets.append('chk')
        additional_targets_renamed.append(item_to_str(chk))
        additional_renames.append(f'{item_to_str(chk)}->chk')
    if oldchk is not None:
        additional_sources.append('oldchk')
        additional_sources_renamed.append(item_to_str(oldchk))
        additional_renames.append(f'{item_to_str(oldchk)}->oldchk')
    if output is not None:
        additional_targets.append('output')
        additional_targets_renamed.append(item_to_str(output))
        additional_renames.append(f'{item_to_str(output)}->output')
    
    if additional_files is not None:
        additional_files_str = {key: item_to_str(value) for key, value in additional_files.items()}
        for file in additional_files_str.values():
            additional_targets.append(file)
            additional_targets_renamed.append(file)
    else:
        additional_files_str = {}

    execute_gaussian = any(x is not None for x in (chk, oldchk, output, additional_files))
    assert execute_gaussian, f"Seems like you didn't request Gaussian execution (just gjf), but this is not implemented yet"

    def init_gaussian(inpstruct, calcdir, id, **kw):
        default_charge = 0
        default_mult = 1
        charge = default_charge
        mult = default_mult

        data = inpstruct.access_element()
        if isinstance(data, dict):
            xyzs, syms = data['xyz'], data['sym']
            coord_text = utils.to_xyz(xyzs, syms, include_header=False)
        elif isinstance(data, str) and data.endswith('.sdf'):
            from chemscripts.geom import Molecule
            mol = Molecule(sdf=data)
            charge = mol.total_charge()
            xyzs, syms = mol.as_xyz()
            coord_text = utils.to_xyz(xyzs, syms, include_header=False)
        else:
            raise ValueError(f"Unable to start Gaussian from '{repr(data)}'")

        template = open(gjf_template, 'r').read()
        template_keys = list(fstring_key_iter(template))
        current_kwargs = {}
        if charge != default_charge or 'chrg' in template_keys:
            current_kwargs['chrg'] = charge
        if mult != default_mult or 'mult' in template_keys:
            current_kwargs['mult'] = mult
        if 'nproc' in template_keys:
            assert nproc is not None, f"GJF template '{gjf_template}' requires 'nproc' to be provided"
            current_kwargs['nproc'] = nproc
        for key in current_kwargs.keys():
            assert key in template_keys, f"Template '{gjf_template}' "\
                f"does not support non-default values of '{key}'"

        gjf_string = template.format(
            xyz=coord_text,
            **current_kwargs,
            **kwargs
        )
        gjf_string = prepare_gjf(gjf_string, remove_chk=chk is None, remove_oldchk=oldchk is None)
        gjfname = os.path.join(calcdir, 'start.gjf')
        with open(gjfname, 'w') as f:
            f.write(gjf_string)
        
        if gjf is not None:
            gjf_backup_name = kw['gjf'].get_path()
            with open(gjf_backup_name, 'w') as f:
                f.write(gjf_string)
            kw['gjf'].include_element(gjf_backup_name)

        if oldchk is not None:
            oldchk_name = kw['oldchk'].access_element()
            shutil.copy2(oldchk_name, os.path.join(calcdir, 'old.chk'))
        
        return f'exec_gaussian.sh {calcdir} start.gjf {id}'

    def finish_gaussian(log, calcdir, **kw):
        conformers_file = os.path.join(calcdir, 'start.log')
        assert os.path.isfile(conformers_file), f"Cannot find file '{conformers_file}'"
        assert utils.is_normal_termination(conformers_file, '.gjf'), f"Failed '{conformers_file}'"

        final_log_name = log.get_path()
        shutil.copy2(conformers_file, final_log_name)
        log.include_element(final_log_name)

        if output is not None:
            kw['output'].include_element(output_method(final_log_name))

        if chk is not None:
            final_chk_name = kw['chk'].get_path()
            chkname = os.path.join(calcdir, 'current.chk')
            assert os.path.isfile(chkname), f"Cannot find file '{chkname}'"
            shutil.copy2(chkname, final_chk_name)
            kw['chk'].include_element(final_chk_name)

        for raw_filename, fileitem in additional_files_str.items():
            final_name = kw[fileitem].get_path()
            raw_fullname = os.path.join(calcdir, raw_filename)
            assert os.path.isfile(raw_fullname), f"Cannot find file '{raw_fullname}'"
            shutil.copy2(raw_fullname, final_name)
            kw[fileitem].include_element(final_name)
    
    if execute_gaussian:
        template = nonblocking_subprocess(
            name='RunGaussian_template',
            input=['inpstruct', *additional_sources],
            output=['log', *additional_targets],
            command_prepare=init_gaussian,
            output_process=finish_gaussian,
            calcdir='calcdir',
            nproc=nproc
        )
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(inpgeom), *additional_sources_renamed],
        TARGET_ITEMS = [item_to_str(log), *additional_targets_renamed],
    )
    res.extend(template, f"""\
        {item_to_str(inpgeom)}->inpstruct
        {item_to_str(log)}->log
        {' '.join(additional_renames)}
    """)
    return res


# Load gaussian logs independently from Gaussian calculation itself
def load_gaussian_logs(name, input, output, parse_method, **kwargs):
    return map(
        name=name,
        input=input,
        output=output,
        mapping=parse_method,
        **kwargs
    )


# chk->fchk conversion
def init_formchk(chk, calcdir, **kw):
    chk_fname = chk.access_element()
    shutil.copy2(chk_fname, os.path.join(calcdir, 'mol.chk'))
    return f'exec_gaussian_formchk.sh {calcdir} mol.chk'

def finish_formchk(fchk, calcdir, **kw):
    fchk_fname = os.path.join(calcdir, 'mol.fchk')
    assert os.path.isfile(fchk_fname), f"Cannot find file '{fchk_fname}'"
    final_fchk_name = fchk.get_path()
    shutil.copy2(fchk_fname, final_fchk_name)
    fchk.include_element(final_fchk_name)

def formchk_gaussian(name, input, output):
    assert utils.check_availability('exec_gaussian_formchk.sh')

    template = nonblocking_subprocess(
        name=name,
        input=['chk'],
        output=['fchk'],
        command_prepare=init_formchk,
        output_process=finish_formchk,
        calcdir='calcdir',
        nproc=1
    )
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )
    res.extend(template, f"""\
        {item_to_str(input)}->chk
        {item_to_str(output)}->fchk
    """)
    return res


# fchk->chk conversion
def init_unfchk(fchk, calcdir, **kw):
    fchk_fname = fchk.access_element()
    shutil.copy2(fchk_fname, os.path.join(calcdir, 'mol.fchk'))
    return f'exec_gaussian_unfchk.sh {calcdir} mol.fchk'

def finish_unfchk(chk, calcdir, **kw):
    chk_fname = os.path.join(calcdir, 'mol.chk')
    assert os.path.isfile(chk_fname), f"Cannot find file '{chk_fname}'"
    final_chk_name = chk.get_path()
    shutil.copy2(chk_fname, final_chk_name)
    chk.include_element(final_chk_name)

def unfchk_gaussian(name, input, output):
    assert utils.check_availability('exec_gaussian_unfchk.sh')

    template = nonblocking_subprocess(
        name=name,
        input=['fchk'],
        output=['chk'],
        command_prepare=init_unfchk,
        output_process=finish_unfchk,
        calcdir='calcdir',
        nproc=1
    )
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )
    res.extend(template, f"""\
        {item_to_str(input)}->fchk
        {item_to_str(output)}->chk
    """)
    return res

# NBO6 execution

# emplates.run_nbosix('nbo6_calc',
#                 input='nbogauss_47', output='nbo6_out', additional_output={'dmmo': 'nbo6_dmmo', 'fmo': 'nbo6_fmo'}
#             ),

NBO_MATRIX_CONVENTIONS = {
    'dmmo': 419,
    'dmnbo': 420,
    'fmo': 699,
    'fnbo': 69,
    'aomo': 228,
    'aonbo': 288,
}

def run_nbosix(name,
        input,
        output=None,
        modified_input=None,
        matrix_files=None,
        nbo_keywords=[],
        **kwargs
    ):
    assert utils.check_availability('exec_nbo6.sh')

    additional_sources = []
    additional_sources_renamed = []
    additional_targets = []
    additional_targets_renamed = []
    additional_renames = []

    if output is not None:
        additional_targets.append('output')
        additional_targets_renamed.append(item_to_str(output))
        additional_renames.append(f'{item_to_str(output)}->output')

    if modified_input is not None:
        additional_targets.append('modified_input')
        additional_targets_renamed.append(item_to_str(modified_input))
        additional_renames.append(f'{item_to_str(modified_input)}->modified_input')

    generated_matrices = []
    for matrix_type, matrix_item in matrix_files.items():
        generated_matrices.append(matrix_type)
        additional_targets.append(matrix_type)
        additional_targets_renamed.append(item_to_str(matrix_item))
        additional_renames.append(f'{item_to_str(matrix_item)}->{matrix_type}')

    execute_nbo = (output is not None) or (len(matrix_files) > 0)
    assert execute_nbo, f"Seems like you didn't request NBO execution (just modified input), but this is not implemented yet"

    def init_nbosix(input, calcdir, id, **kw):
        inpfile = input.access_element()
        assert inpfile.endswith('.47'), f"Input for NBO6 must end with '.47'. Got this: '{inpfile}'"

        input_lines = open(inpfile, 'r').readlines()
        assert input_lines[1] == ' $NBO  $END\n', f"Unexpected start of file '{inpfile}'. Needed ' $NBO  $END'"
        keywords = [
            *nbo_keywords,
            *(
                f"{matrix_type.upper()}=W{NBO_MATRIX_CONVENTIONS[matrix_type]}" # For example, 'DMMO=W419'
                for matrix_type in generated_matrices
            )
        ]
        joined_keywords = ' '.join(keywords)
        assert '\n' not in joined_keywords, f"Unexpected linebreak found: '{joined_keywords}'"
        input_lines[1] = f' $NBO {joined_keywords} $END\n'
        input_worker_name = os.path.join(calcdir, 'calc.47')
        with open(input_worker_name, 'w') as f:
            f.write(''.join(input_lines))

        if modified_input is not None:
            modinput_backup_name = kw['modified_input'].get_path()
            with open(modinput_backup_name, 'w') as f:
                f.write(input_lines)
            kw['modified_input'].include_element(modinput_backup_name)
        
        return f'exec_nbo6.sh {calcdir} calc.47'

    def finish_nbosix(calcdir, **kw):
        output_worker_file = os.path.join(calcdir, 'NBO.OUT')
        assert os.path.isfile(output_worker_file), f"Cannot find file '{output_worker_file}'"
        assert utils.nbo_check_normal_termination(output_worker_file), f"Failed '{output_worker_file}'"

        if output is not None:
            final_output_name = kw['output'].get_path()
            shutil.copy2(output_worker_file, final_output_name)
            kw['output'].include_element(final_output_name)

        for matrix_type in generated_matrices:
            matrix_worker_file = os.path.join(calcdir, f'FILE.{NBO_MATRIX_CONVENTIONS[matrix_type]}')
            assert os.path.isfile(matrix_worker_file), f"Cannot find file '{matrix_worker_file}'"
            final_matrix_name = kw[matrix_type].get_path()
            shutil.copy2(matrix_worker_file, final_matrix_name)
            kw[matrix_type].include_element(final_matrix_name)
    
    if execute_nbo:
        template = nonblocking_subprocess(
            name='RunNBO6_template',
            input=['input', *additional_sources],
            output=[*additional_targets],
            command_prepare=init_nbosix,
            output_process=finish_nbosix,
            calcdir='calcdir',
            nproc=1
        )
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input), *additional_sources_renamed],
        TARGET_ITEMS = [*additional_targets_renamed],
    )
    res.extend(template, f"""\
        {item_to_str(input)}->input
        {' '.join(additional_renames)}
    """)
    return res


# Load NBO results (parser and matrices)
def load_nbo_results(name,
        input,
        parser,
        dmnbo=None,
        fnbo=None,
        dmmo=None,
        fmo=None,
        nbo_version=3
    ):
    assert nbo_version == 3 or nbo_version == 6, f"Only NBO3/Gaussian and NBO6 are supported"

    additional_sources = []
    additional_targets = []
    if dmnbo is not None:
        additional_sources.append(item_to_str(dmnbo[0]))
        additional_targets.append(item_to_str(dmnbo[1]))
    if fnbo is not None:
        additional_sources.append(item_to_str(fnbo[0]))
        additional_targets.append(item_to_str(fnbo[1]))
    if dmmo is not None:
        additional_sources.append(item_to_str(dmmo[0]))
        additional_targets.append(item_to_str(dmmo[1]))
    if fmo is not None:
        additional_sources.append(item_to_str(fmo[0]))
        additional_targets.append(item_to_str(fmo[1]))

    input_name = item_to_str(input)
    parser_name = item_to_str(parser)

    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [input_name, *additional_sources],
        TARGET_ITEMS = [parser_name, *additional_targets],
    )

    def LoadNboResults_exec(**kw):
        log_fname = kw[input_name].access_element()
        if nbo_version == 3:
            parser_obj = NBO3LogParser(log_fname)
        elif nbo_version == 6:
            parser_obj = NBO6LogParser(log_fname)
        kw[parser_name].include_element(parser_obj)

        if dmnbo is not None:
            dmnbo_file = kw[dmnbo[0]].access_element()
            kw[dmnbo[1]].include_element(NboSymmMatrix(dmnbo_file, parser_obj.nbasis))

        if fnbo is not None:
            fnbo_file = kw[fnbo[0]].access_element()
            kw[fnbo[1]].include_element(NboSymmMatrix(fnbo_file, parser_obj.nbasis))

        if dmmo is not None:
            dmmo_file = kw[dmmo[0]].access_element()
            kw[dmmo[1]].include_element(NboSymmMatrix(dmmo_file, parser_obj.nbasis))

        if fmo is not None:
            fmo_file = kw[fmo[0]].access_element()
            kw[fmo[1]].include_element(NboSymmMatrix(fmo_file, parser_obj.nbasis))

        return ret.transform_finished()
    
    res.set_method({'exec': LoadNboResults_exec})
    return res


# Gaussian Cubegen
def gaussian_cubegen(name, fchk, output, orb_data, orb_index, nbo_log=None, nproc=1):
    additional_sources = []
    additional_sources_renamed = []
    additional_renames = []

    if nbo_log is not None:
        nbo_log_name = item_to_str(nbo_log)
        additional_sources.append('nbo_log')
        additional_sources_renamed.append(nbo_log_name)
        additional_renames.append(f'{nbo_log_name}->nbo_log')

    def init_cubegen(fchk, orb_data, calcdir, **kw):
        fchk_fname = fchk.access_element()
        fchk_tempfile = os.path.join(calcdir, 'start.fchk')
        shutil.copy2(fchk_fname, fchk_tempfile)
        
        orb_index = orb_data.access_element()['index']
        if nbo_log is not None:
            nbo_log_fname = kw['nbo_log'].access_element()
            final_orb_index = generate_reorder_map(nbo_log_fname, nbo_indices=[orb_index])[orb_index]
        else:
            final_orb_index = orb_index + 1

        return f"exec_gaussian_cubegen.sh {calcdir} {nproc} " \
            f"MO={final_orb_index} start.fchk result.cube 100"

    def finish_cubegen(output, calcdir, **kw):
        cube_temp_file = os.path.join(calcdir, 'result.cube')
        assert os.path.isfile(cube_temp_file), f"Cannot find file '{cube_temp_file}'"

        final_cube_name = output.get_path()
        shutil.copy2(cube_temp_file, final_cube_name)
        output.include_element(final_cube_name)

    template = nonblocking_subprocess(
        name='Cubegen_template',
        input=['fchk', 'orb_data', *additional_sources],
        output=['output'],
        command_prepare=init_cubegen,
        output_process=finish_cubegen,
        calcdir='calcdir',
        aware_keys=[orb_index],
        nproc=nproc
    )
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(fchk), item_to_str(orb_data), *additional_sources_renamed],
        TARGET_ITEMS = [item_to_str(output)],
        AWARE_KEYS = [orb_index]
    )
    res.extend(template, f"""\
        {item_to_str(fchk)}->fchk
        {item_to_str(output)}->output
        {item_to_str(orb_data)}->orb_data
        {' '.join(additional_renames)}
    """)
    return res

# MCubes calc
def run_mcubes():
    import os, sys, json
    sys.path.append(os.getcwd())

    from chemscripts.nbo.isosurfaces import generate_isosurface
    cube_fname = sys.argv[1]
    isurf_fnames = json.loads(sys.argv[2].replace("'", '"'))
    isovalue = float(sys.argv[3])
    generate_isosurface(cubename=cube_fname, meshfile_files=isurf_fnames, ival=isovalue)

def isurf_item_to_files(isurf_item, sign_key, type_key, method='get_path', **kwargs):
    from chemscripts.nbo.isosurfaces import ISURF_SIGNS, ISURF_TYPES
    isurf_fnames = {}
    for sign in ISURF_SIGNS:
        isurf_fnames[sign] = {}
        for itype in ISURF_TYPES:
            isurf_fnames[sign][itype] = getattr(isurf_item, method)(**{
                sign_key: sign,
                type_key: itype,
                **kwargs
            })
    return isurf_fnames

def mcubes_isosurface(name, input, pyfile, output, sign_key, type_key, isovalue=0.05):
    
    def argv_prepare(cube, isurf, **kw):
        cube_fname = cube.access_element()
        isurf_fnames = isurf_item_to_files(isurf, sign_key=sign_key, type_key=type_key)
        return (cube_fname, isurf_fnames, isovalue)
    
    def output_process(isurf, **kw):
        isurf_fnames = isurf_item_to_files(isurf, sign_key=sign_key, type_key=type_key)
        for sign, isurf_sign_data in isurf_fnames.items():
            for itype, filename in isurf_sign_data.items():
                assert os.path.isfile(filename), f"Cannot find file '{filename}'"
                isurf.include_element(filename, **{
                    sign_key: sign,
                    type_key: itype,
                })
                
    template = pyfunction_subprocess(
        name='MCubestemplate',
        input='cube',
        output='isurf',
        pyfunction=run_mcubes,
        argv_prepare=argv_prepare,
        output_process=output_process,
        pyfile=pyfile,
        nproc=1
    )
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output), item_to_str(pyfile)]
    )
    res.extend(template, f"""\
        {item_to_str(input)}->cube
        {item_to_str(pyfile)}->pyfile
        {item_to_str(output)}->isurf
    """)
    return res


#
# BLENDER
#
DEFAULT_STYLES = {
    'red-blue': {
        'plus': {
            'color': "#DF4A4A",
        },
        'minus': {
            'color': "#64A7E7",
        }
    },
    'green-yellow': {
        'plus': {
            'color': "#5CCA59",
            'alpha': 0.2,
            'factor': 0.6,
        },
        'minus': {
            'color': "#FFA624",
            'alpha': 0.2,
            'factor': 0.6,
        }
    },
}

def blender_main_script():
    import bpy

    import sys
    module_dir = INSERT_HERE
    if module_dir not in sys.path:
        sys.path.insert(0, module_dir)

    scene_spec = INSERT_HERE
    STYLES = INSERT_HERE

    if scene_spec is not None:
        import chemscripts.blender as msblend
        # import chemscripts.blender.draw_objects.linal as mslinal

        DEFAULTS = {
            'orbitals': {},
            'molecules': {},
        }
        MOLECULE_KEYS = ['xyz', 'symbols', 'bonds', 'bondtypes', 'smallatoms']
        MOLECULE_DEFAULTS = {
            'smallatoms': []
        }
        
        # Primary checks
        assert not ('molecules' in scene_spec and any(key in scene_spec for key in MOLECULE_KEYS)), \
            f"Molecule can be specified via 'molecules' key or directly via '{MOLECULE_KEYS}', but not both"

        for key, value in DEFAULTS.items():
            if key not in scene_spec:
                scene_spec[key] = value
        
        if any(key in scene_spec for key in MOLECULE_KEYS):
            default_molname = 'mol'
            scene_spec['molecules'][default_molname] = {}
            for key in MOLECULE_KEYS:
                if key not in scene_spec:
                    continue
                scene_spec['molecules'][default_molname][key] = scene_spec[key]
                del scene_spec[key]
        for mol_name, mol_data in scene_spec['molecules'].items():
            for key, default_value in MOLECULE_DEFAULTS.items():
                if key not in mol_data:
                    mol_data[key] = default_value
            assert all(key in mol_data for key in MOLECULE_KEYS), \
                f"Molecule '{mol_name}' is partially specified: {mol_data}"

        msblend.cleanup(protect_collections=[
            mol_name
            for mol_name in scene_spec['molecules'].keys()
        ])
        for mol_name, mol_data in scene_spec['molecules'].items():
            m = msblend.Molecule(name=mol_name, small_atoms=mol_data['smallatoms'])
            m.from_dict(mol_data)
            bonds_obj = m.draw_bonds(caps=False, radius=0.1)
            atoms_obj = m.draw_atoms(scale=0.35)
            mol_collection = bpy.data.collections.new(mol_name)
            bpy.context.scene.collection.children.link(mol_collection)
            bpy.data.collections['Collection'].children.link(mol_collection)

            if bonds_obj.name not in bpy.data.collections[mol_name].objects:
                bpy.data.collections[mol_name].objects.link(bonds_obj)
            if atoms_obj.name not in bpy.data.collections[mol_name].objects:
                bpy.data.collections[mol_name].objects.link(atoms_obj)

        for name, style_data in STYLES.items():
            style_data['name'] = name

        for name, isurf_data in scene_spec['orbitals'].items():
            import chemscripts.blender.draw_objects.orbitals as msorbital
            msorbital.plot_nbo(name, isurf_data['files'], style=STYLES[isurf_data['style']], reverse=False)

    scene = bpy.context.scene

    BLEND_FINAL = INSERT_HERE
    if BLEND_FINAL is not None:
        bpy.ops.wm.save_as_mainfile(filepath=BLEND_FINAL)

    PNG_FINAL = INSERT_HERE
    NPROC = INSERT_HERE
    if PNG_FINAL is not None:
        scene.render.image_settings.file_format = 'PNG'
        scene.render.filepath = PNG_FINAL
        
        try:
            bpy.context.preferences.addons[
                "cycles"
            ].preferences.compute_device_type = "CUDA"
        except:
            pass

        if NPROC is not None:
            bpy.context.scene.render.threads = NPROC
        else:
            bpy.context.scene.render.threads = 1

        bpy.context.scene.render.threads_mode = 'FIXED'
        bpy.ops.render.render(write_still=1)

def blender_render(name, blend, png, nproc=1, **kw):
    return blender_for_scenes(
        name=name,
        scene_template=blend,
        png=png,
        nproc=nproc,
        **kw
    )

def blender_for_scenes(name,
        scene_template,
        scene_spec=None,
        blend=None,
        script=None,
        png=None,
        aware_keys=[],
        nproc=1,
        styles=None
    ):
    assert utils.check_availability('exec_blender.sh')
    assert blend is not None or png is not None

    additional_sources = []
    additional_sources_renamed = []
    additional_targets = []
    additional_targets_renamed = []
    additional_renames = []

    template_kwargs = {}

    if scene_spec is not None:
        scene_spec_name = item_to_str(scene_spec)
        additional_sources.append('scene_spec')
        additional_sources_renamed.append(scene_spec_name)
        additional_renames.append(f'{scene_spec_name}->scene_spec')

    if script is not None:
        script_name = item_to_str(script)
        additional_targets_renamed.append(script_name)
        additional_renames.append(f'{script_name}->script')
        template_kwargs['pyfile'] = 'script'

    if blend is not None:
        blend_name = item_to_str(blend)
        additional_targets.append('blend')
        additional_targets_renamed.append(blend_name)
        additional_renames.append(f'{blend_name}->blend')

    if png is not None:
        png_name = item_to_str(png)
        additional_targets.append('png')
        additional_targets_renamed.append(png_name)
        additional_renames.append(f'{png_name}->png')

    def blender_preparation(file, # This is the script filename
            scene_template, calcdir, **kw
        ):
        scene_template_path = scene_template.access_element()
        temp_template = os.path.join(calcdir, 'template.blend')
        shutil.copy2(scene_template_path, temp_template)

        script_subs = {
            'module_dir': os.getcwd(),
            'NPROC': nproc,
        }
        if styles is not None:
            script_subs['STYLES'] = styles
        else:
            script_subs['STYLES'] = DEFAULT_STYLES

        if scene_spec is not None:
            script_subs['scene_spec'] = kw['scene_spec'].access_element()
        else:
            script_subs['scene_spec'] = None

        if png is not None:
            script_subs['PNG_FINAL'] = 'done.png'
        else:
            script_subs['PNG_FINAL'] = None

        if blend is not None:
            script_subs['BLEND_FINAL'] = 'done.blend'
        else:
            script_subs['BLEND_FINAL'] = None

        script_code = function_to_script(blender_main_script, subs=script_subs)
        with open(file, 'w') as f:
            f.write(script_code)

        return f"exec_blender.sh {calcdir} template.blend -b -P {ntpath.basename(file)}"

    def output_process(calcdir, **kw):
        if blend is not None:
            temp_blend = os.path.join(calcdir, 'done.blend')
            assert os.path.isfile(temp_blend), f"Cannot find file '{temp_blend}'"
            blend_final_path = kw['blend'].get_path()
            shutil.copy2(temp_blend, blend_final_path)
            kw['blend'].include_element(blend_final_path)
        
        if png is not None:
            temp_png = os.path.join(calcdir, 'done.png')
            assert os.path.isfile(temp_png), f"Cannot find file '{temp_png}'"
            png_final_path = kw['png'].get_path()
            shutil.copy2(temp_png, png_final_path)
            kw['png'].include_element(png_final_path)

    template = pyfunction_subprocess(
        name='Blendertemplate',
        input=['scene_template', *additional_sources],
        output=additional_targets,
        custom_command=blender_preparation,
        output_process=output_process,
        nproc=nproc,
        calcdir='calcdir',
        aware_keys=aware_keys,
        **template_kwargs
    )

    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(scene_template), *additional_sources_renamed],
        TARGET_ITEMS = [*additional_targets_renamed],
        AWARE_KEYS = aware_keys
    )
    res.extend(template, f"""\
        {item_to_str(scene_template)}->scene_template
        {' '.join(additional_renames)}
    """)
    return res

def png_postprocess(name, input, output, settings, merged_keys=[]):
    template = Transform(
        NAME = 'PngProcesstemplate',
        SOURCE_ITEMS = ['startpng'],
        TARGET_ITEMS = ['donepng'],
        MERGED_KEYS = merged_keys,
    )

    DEFAULTS = {
        'fill_transparency': True,
        'brightness': None,
        'trim_white': True,
        'white_to_transparent': False,
        'shrink_factor': None,
    }
    final_settings = {
        key: settings[key] if key in settings else default_value
        for key, default_value in DEFAULTS.items()
    }

    def PngProcess_exec(startpng, donepng):
        from PIL import Image, ImageEnhance
        from chemscripts import imageutils

        assert len(merged_keys) == 0 or final_settings['trim_white']

        images = []
        for startpng_fname, keys in startpng:
            main_image = Image.open(startpng_fname)
            main_image.load()

            # Fills the transparency
            if final_settings['fill_transparency']:
                bg = Image.new("RGB", main_image.size, (255, 255, 255))
                bg.paste(main_image, mask=main_image.split()[3])
                main_image = bg

            # Increases brightness
            if final_settings['brightness'] is not None:
                enhancer = ImageEnhance.Brightness(main_image)
                main_image = enhancer.enhance(final_settings['brightness'])
            
            if final_settings['white_to_transparent']:
                main_image = main_image.convert("RGBA")
                data = main_image.getdata()
                new_data = []
                for item in data:
                    if item[:3] == (255, 255, 255):
                        new_data.append((255, 255, 255, 0))
                    else:
                        new_data.append(item)
                main_image.putdata(new_data)
            
            if final_settings['shrink_factor'] is not None:
                factor = final_settings['shrink_factor']
                main_image = main_image.resize((int(main_image.width / factor), int(main_image.height / factor)))
            images.append({
                'obj': main_image,
                'keys': keys
            })

        # Trims white space
        if final_settings['trim_white']:
            trimbox = imageutils.TrimmingBox()
            for elem in images:
                trimbox.extend(elem['obj'])
            for elem in images:
                elem['obj'] = elem['obj'].crop(trimbox.points)


        for elem in images:
            keys = elem['keys']
            donepng_fname = donepng.get_path(**keys)
            elem['obj'].save(donepng_fname, 'PNG', quality=100)
            donepng.include_element(donepng_fname, **keys)

        return ret.transform_finished()

    template.set_method({'exec': PngProcess_exec})
    
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
        MERGED_KEYS = merged_keys,
    )
    res.extend(template, f"""\
        {item_to_str(input)}->startpng
        {item_to_str(output)}->donepng
    """)
    return res

#
# FILE OPERATIONS
#

# Copy single files
def copy_file(name, input, output, condition=None):
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )

    def CopyFile_exec(start, finish):
        start_fname = start.access_element()
        assert os.path.isfile(start_fname), f"Source file '{start_fname}' does not exist"

        if condition is None or condition(start_fname):
            finish_fname = finish.get_path()
            shutil.copy2(start_fname, finish_fname)
            finish.include_element(finish_fname)
        return ret.transform_finished()

    CopyFile_template = Transform(
        NAME = 'CopyFiletemplate',
        SOURCE_ITEMS = ['start'],
        TARGET_ITEMS = ['finish'],
    )
    CopyFile_template.set_method({'exec': CopyFile_exec})

    res.extend(CopyFile_template, f"""\
        {item_to_str(input)}->start
        {item_to_str(output)}->finish
    """)
    return res


# Extract archive
def extract_archive(name, input, output, aware_keys=[], filename=None):
    ExtractArchive_template = Transform(
        NAME = 'ExtractArchivetemplate',
        SOURCE_ITEMS = ['archive'],
        TARGET_ITEMS = ['extracted_files'],
        AWARE_KEYS = aware_keys,
    )

    def ExtractArchive_exec(archive, extracted_files, **kw):
        start_fname = archive.access_element()
        assert os.path.isfile(start_fname), f"Source file '{start_fname}' does not exist"
        
        diritem = extracted_files.containing_dir()
        extract_dir = diritem.get_path()
        if diritem.restriction_id is not None:
            diritem.retire()

        # To create containing dir
        extracted_files.get_path(**{key: '' for key in extracted_files.public_keys})

        with tarfile.open(start_fname, 'r:gz') as tar:
            for member in tar.getmembers():
                if filename is not None:
                    member.name = filename(
                        original_name=member.name,
                        **kw
                    )
                tar.extract(member, path=extract_dir)
                extracted_files.include_element(os.path.join(extract_dir, member.name))
        return ret.transform_finished()

    ExtractArchive_template.set_method({'exec': ExtractArchive_exec})

    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
        AWARE_KEYS = aware_keys,
    )

    res.extend(ExtractArchive_template, f"""\
        {item_to_str(input)}->archive
        {item_to_str(output)}->extracted_files
    """)
    return res

def load_json(name, input, output):
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
    )

    def ReadJson_exec(input, output):
        input_fname = input.access_element()
        with open(input_fname, 'r') as f:
            data = json.load(f)
        
        output_keys_set = set(output.public_keys)
        if len(output_keys_set) == 0:
            output.include_element(data)
        else:
            for elem in data:
                keys = elem['keys']
                assert set(keys.keys()) == output_keys_set, \
                    f"Generated keys mismatch: '{keys}' vs. '{output_keys_set}'"
                output.include_element(elem['obj'], **keys)

        return ret.transform_finished()

    ReadJson_template = Transform(
        NAME = 'ReadJsontemplate',
        SOURCE_ITEMS = ['input'],
        TARGET_ITEMS = ['output'],
    )
    ReadJson_template.set_method({'exec': ReadJson_exec})

    res.extend(ReadJson_template, f"""\
        {item_to_str(input)}->input
        {item_to_str(output)}->output
    """)
    return res


def dump_json(name, input, output, merged_keys=[]):
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
        MERGED_KEYS = merged_keys,
    )

    merged_keys_set = set(merged_keys)

    def SaveJson_exec(input, output):
        if len(merged_keys) == 0:
            input_obj = input.access_element()
            save_obj = input_obj
        else:
            for obj, keys in input:
                assert set(keys.keys()) == merged_keys_set, \
                    f"Merged keys mismatch: '{keys}' vs. '{merged_keys_set}'"
            save_obj = [
                {
                    'obj': obj,
                    'keys': keys
                }
                for obj, keys in input
            ]

        output_fname = output.get_path()
        with open(output_fname, 'w') as f:
            json.dump(save_obj, f)
        output.include_element(output_fname)
        return ret.transform_finished()

    SaveJson_template = Transform(
        NAME = 'SaveJsontemplate',
        SOURCE_ITEMS = ['input'],
        TARGET_ITEMS = ['output'],
        MERGED_KEYS = merged_keys,
    )
    SaveJson_template.set_method({'exec': SaveJson_exec})

    res.extend(SaveJson_template, f"""\
        {item_to_str(input)}->input
        {item_to_str(output)}->output
    """)
    return res

def save_pandas(df, csvname):
    df.to_csv(csvname, index=False)
    return csvname

def pd_to_csv(name, input, output):
    return map(
        name=name,
        input=input,
        output=output,
        mapping=lambda **kw: save_pandas(df=kw[input], csvname=kw[output])
    )

def load_pandas(csvname):
    return pd.read_csv(csvname)

def pd_from_csv(name, input, output):
    return map(
        name=name,
        input=input,
        output=output,
        mapping=lambda **kw: load_pandas(csvname=kw[output])
    )

#
# MOVIES
#

def frames_to_mp4(name, input, output, ordering_key=None, aware_keys=[], merged_keys=[]):
    assert len(merged_keys) > 0, \
        f"Transition frames->mp4 implied the presence of at least one merged key but got none"
    
    template = Transform(
        NAME = name,
        SOURCE_ITEMS = ['frames'],
        TARGET_ITEMS = ['mp4'],
        AWARE_KEYS = aware_keys,
        MERGED_KEYS = merged_keys
    )

    def GetMP4_exec(frames, mp4, thread_manager, **kw):
        frames_data = [
            {
                'file': elem,
                'keys': keys,
            }
            for elem, keys in frames
        ]
        if ordering_key is not None:
            frames_data.sort(key=ordering_key)
        else:
            png_keys = frames.public_keys
            assert len(png_keys) == 1, f"Unable to sort automatically when have multiple keys '{png_keys}'. Specify 'ordering_key'"
            png_key = png_keys[0]
            frames_data.sort(key=lambda obj: obj['keys'][png_key])
        
        id, used_calcdir = thread_manager.prepare_new_job()
        number_of_elements = len(frames_data)
        number_of_digits = len(str(number_of_elements)) + 1
        frame_mask = f'frame_%{number_of_digits}d.png'
        frame_path_mask = os.path.join(used_calcdir, frame_mask)
        for i, item in enumerate(frames_data):
            raw_name = frame_path_mask % i
            temp_name = os.path.join(os.path.dirname(raw_name), ntpath.basename(raw_name).replace(' ', '0'))
            shutil.copy2(item['file'], temp_name)
        
        main_dir = os.getcwd()
        os.chdir(used_calcdir)
        command = f'ffmpeg -y -framerate 10 -i {frame_mask} -c:v libx264 -crf 17 -vf "format=yuv420p,pad=ceil(iw/2)*2:ceil(ih/2)*2" result.mp4'
        os.system(command)
        temp_result_file = os.path.join(used_calcdir, 'result.mp4')

        final_file = mp4.get_path()
        assert os.path.isfile(temp_result_file), f"Result file '{temp_result_file}' is not found"
        shutil.copy2(temp_result_file, final_file)
        mp4.include_element(final_file)
        
        os.chdir(main_dir)
        thread_manager.finalize_task(id, state='registered')
        return ret.transform_finished()

    template.set_method({'exec': GetMP4_exec})
    res = Transform(
        NAME = name,
        SOURCE_ITEMS = [item_to_str(input)],
        TARGET_ITEMS = [item_to_str(output)],
        AWARE_KEYS = aware_keys,
        MERGED_KEYS = merged_keys
    )
    res.extend(template, f"""\
        {item_to_str(input)}->frames
        {item_to_str(output)}->mp4
    """)
    return res


def frames_to_gif(name, input, output, aware_keys=[], merged_keys=[]):
    assert len(merged_keys) > 0, \
        f"Transition frames->mp4 implied the presence of at least one merged key but got none"
