import inspect
import copy
import functools
import itertools

from ..dataitems import DataItem


class Transform:
    DEFAULTS = { # TODO This part really lacks descriptive comments on wtf is this
        'NAME': 'UNTITLED',
        'SOURCE_ITEMS': [],
        'TARGET_ITEMS': [],
        'NOTE_ITEMS': [],
        'AWARE_KEYS': [],
        'AWARE_ENFORCED_KEYS': [],
        'MERGED_KEYS': [],
        'GREEDY_TARGETS': [],

        'IS_PROXY': False,
    }

    def __init__(self, **attrs):
        self.specs = {}
        self.methods = {}

        for key, value in attrs.items():
            self._add_new_spec(key, value)
        for key, value in Transform.DEFAULTS.items():
            if key not in attrs:
                self._add_new_spec(key, copy.copy(value))
        
        self.specific_args = {
            'self': self,
        }
    
    def set_method(self, arg):
        """Specify method(s) for the transform

        Args:
            arg (Callable or Dict[str, Callable]): Function or Dict of functions to be included as methods

        Raises:
            AssertionError: Failed typechecks or unexpected function name
            ValueError: arg of unexpected type
        """
        new_methods = {}

        if callable(arg):
            formatting_error = 'Expected the method to have format "{Name}_{Method}"'
            if arg.__name__.count('_') == 1:
                if self.NAME != self.DEFAULTS['NAME']:
                    assert arg.__name__.split('_')[0] == self.NAME, formatting_error
                new_methods[arg.__name__.split('_')[1]] = arg
            elif arg.__name__.count('_') == 0:
                new_methods[arg.__name__] = arg
            else:
                raise AssertionError(formatting_error)
        elif isinstance(arg, dict):
            for name, f in arg.items():
                assert isinstance(name, str), f'{repr(name)} is not a string'
                assert callable(f), f'{repr(f)} is not callable'
            new_methods = arg
        else:
            raise ValueError(f"Cannot set {repr(arg)} as method")
        
        for name, f in new_methods.items():
            self._add_new_method(name, f)
        return self
    
    def extend(self, base_transform, keys_mapping={}, inherit_methods=None):
        """Implements inheritance for transforms

        Args:
            base_transform (Transform): The parent transform
            keys_mapping (str/dict, optional): Mapping from old keys to new in the form
            `"OldA->NewA OldB->NewB"`. Defaults to "".
            inherit_methods (List[str], optional): Names of methods to be inherited. Defaults to None - inherit all methods.
        """

        # Basic processing of the base transform 
        assert 'base' not in self.specific_args, f"'{self.NAME}' already inherits from '{self.specific_args['base'].NAME}'"
        assert isinstance(base_transform, Transform), f"'{self.NAME}' transform can extend only transform objects"

        # Forwarding of methods from the base transform
        # (1) if they are NOT declared within self: create proxy and access as self.f(...)
        # (2) if they ARE declared within self: create proxy and access as self.base.f(...)
        
        # each key mapping renames either names of '*_ITEMS' or '*_KEYS'
        if isinstance(keys_mapping, dict):
            key_change = keys_mapping
        elif isinstance(keys_mapping, str):
            keys_mapping = '\n'.join([
                line
                for line in keys_mapping.splitlines()
                if not line.lstrip().startswith('#') # Ignore comment lines
            ])
            key_change = {}
            for part in keys_mapping.split():
                sides = part.split('->')
                key_change[sides[1]] = sides[0] # Maps 'parent_key' -> 'child_key'
        else:
            raise AssertionError('Unexpected type of key mapping')
        
        # Maps 'child_key' -> 'parent_key' (internal -> external)
        key_change_inverse = {value: key for key, value in key_change.items()}

        self.specific_args['base'] = base_transform._get_transform_proxy(key_change)

        def assign_proxy_method(method_name, unused_parent_keys):
            method = getattr(base_transform, method_name)
            assert callable(method), f'{repr(method)} is not a callable method prototype'
            
            specific_args = {}
            args_list = inspect.getfullargspec(method)[0]
            if 'self' in args_list:
                specific_args['self'] = self.base
            if 'base' in args_list:
                specific_args['base'] = base_transform.base
            
            corrected_argnames = [
                argname
                for argname in args_list
                if argname in key_change
            ]
            for argname in corrected_argnames:
                if argname in unused_parent_keys:
                    del unused_parent_keys[unused_parent_keys.index(argname)]

            keep_argnames = [
                argname
                for argname in args_list
                if argname not in specific_args and argname not in corrected_argnames
            ]
            new_arglist = [
                *[
                    key_change[arg]
                    for arg in corrected_argnames
                ],
                *keep_argnames,
            ]

            # This decorator is the sugar to keep metadata of the parent method
            @functools.wraps(method)
            def proxy_method(**args):
                corrected_args = {
                    old_argname: args[key_change[old_argname]]
                    for old_argname in corrected_argnames
                }
                kept_args = {
                    argname: args[argname]
                    for argname in keep_argnames
                }
                complete_args = {**corrected_args, **kept_args, **specific_args}

                for argobject in complete_args.values():
                    if isinstance(argobject, DataItem):
                        argobject.with_renamed_keys(key_change_inverse)
                
                # Execution itself
                result = method(**complete_args)

                for argobject in complete_args.values():
                    if isinstance(argobject, DataItem):
                        argobject.release_keyname_layer()
                
                return result

            new_params = [
                inspect.Parameter(argname, inspect.Parameter.POSITIONAL_OR_KEYWORD)
                for argname in new_arglist
            ]

            proxy_method.__signature__ = inspect.signature(proxy_method).replace(parameters=new_params)

            self.base._add_new_method(method_name, proxy_method)
            if method_name not in self.methods:
                self._add_new_method(method_name, proxy_method)
            if self.specs['NAME'] == 'get_nbo_cube':
                print('HI')

        if inherit_methods is None:
            methods_iter = base_transform.methods.keys()
        else:
            for method_name in inherit_methods:
                assert method_name in base_transform.methods, \
                    f"Requested method '{method_name}' is not present in the parent transform '{base_transform.NAME}'"
            methods_iter = inherit_methods
        
        unused_parent_keys = list(key_change.keys())
        for method_name in methods_iter:
            assign_proxy_method(method_name, unused_parent_keys)

        unused_maps = {
            key: key_change[key]
            for key in unused_parent_keys
        }
        # Disabled this asserting since it doesn't account for renamed keys of DataItems
        # TODO Make optional format with ==> or something to indicate that this renaming must be checked
        # assert len(unused_maps) == 0, f"Unused key mappings: {repr(unused_maps)}"

    def _add_new_spec(self, spec_name, value):
        """Add specification to this transform

        Args:
            spec_name (str): Name of the new attr. Prefer UPPER_CASE. Can later acces it via self.SPEC_NAME
            f (Callable): Calls will be redirected to this callable object
        """
        assert spec_name == spec_name.upper(), f'Prefer UPPER_CASE transform specs. Got "{repr(spec_name)}"'
        assert spec_name not in self.specs, f'Attempting to reassign spec {spec_name} of transform {self.NAME}'
        self.specs[spec_name] = value
        
    def _add_new_method(self, method_name, f):
        """Add method to this transform.

        Args:
            method_name (str): Name of the method. Later can be called as `self.method_name`
            f (Callable): Calls will be redirected to this callable object
        """

        # In some cases inherited methods must be overwritten by implemented ones, so this assertion is not needed
        # assert method_name not in self.methods, f'Attempting to reassign method {method_name}{inspect.signature(f)} of {proxy_flag}transform {self.NAME}'

        # If '**something' is present in the argument list, we replace it with all missing necessary args
        argspec = inspect.getfullargspec(f)
        f_varkw = argspec.varkw
        if f_varkw is not None: # It is a string (name of the 'something') or None
            old_sig = inspect.signature(f)
            old_sig_paramnames = [
                param.name
                for param in old_sig.parameters.values()
            ]

            new_params = [
                param
                for param in old_sig.parameters.values()
                if param.kind != param.VAR_KEYWORD
            ] + [
                inspect.Parameter(argname, inspect.Parameter.POSITIONAL_OR_KEYWORD)
                for argname in self._minimum_expected_args()
                if argname not in old_sig_paramnames
            ]

            new_sig = old_sig.replace(parameters=new_params)
            f.__signature__ = new_sig

        # This will make error messages much clearer
        if self.IS_PROXY:
            proxy_flag = "proxy-"
        else:
            proxy_flag = ""

        # Check that all necessary args are present
        arg_names = inspect.getfullargspec(f)[0]
        for argname in self._minimum_expected_args():
            assert argname in arg_names, f"Required arg '{argname}' is not supported " \
                f"by method {f.__name__} of the {proxy_flag}transform {self.NAME}"

        self.methods[method_name] = f

    def _has_native_method(self, method_name):
        """Check if transform has this method implemented natively (accessible directly via `self.method_name`)

        Args:
            method_name (str): Name of the method to look for.

        Returns:
            bool: result
        """
        return method_name in self.methods

    def _get_transform_proxy(self, rename_map):
        """Create transform proxy of the base tranform (called from parent transform, obviously)
        so that it can be put in the `child_transform.specific_args['base']`.
        To do this, all the specs having different name in the child transform are renamed here.

        Args:
            rename_map (Dict[str, str/list]): renaming map (can be an empty dict)

        Returns:
            Transform: The proxy for base transform that can be accessed from child transform.
            It does not have any methods at this point, but they will be added in the 'extend'.
        """

        for key, value in self.specs.items():
            if key.endswith('_KEYS') or key.endswith('_ITEMS'):
                assert isinstance(value, list), f'Unexpected type of {key} spec'

        new_specs = {
            'NAME': self.NAME,
            'IS_PROXY': True,
            **{
                key: [
                    rename_map[item] if item in rename_map
                    else item
                    for item in value
                ]
                for key, value in self.specs.items()
                if isinstance(value, list) and (key.endswith('_KEYS') or key.endswith('_ITEMS'))
            },
        }

        result = Transform(**new_specs)
        if 'base' in self.specific_args:
            result.extend(self.base, rename_map)
        return result

    def _minimum_expected_args(self) -> list:
        """
        Get the minumum set of arguments that all methods of this transform must take

        Returns:
            List[str]: list of arguments
        """
        
        res = []
        for key in [
                    'SOURCE_ITEMS',
                    'TARGET_ITEMS',
                    'NOTE_ITEMS',
                    'AWARE_KEYS',
                    'AWARE_ENFORCED_KEYS',
                ]:
            res += self.specs[key]
        return res
        # return list(itertools.chain( # This is a 'short' way of list concatenation (:
        #     *(
        #         self.specs[key] for key in [
        #             'SOURCE_ITEMS',
        #             'TARGET_ITEMS',
        #             'NOTE_ITEMS',
        #             'AWARE_KEYS',
        #             'AWARE_ENFORCED_KEYS',
        #         ]
        #     )
        # ))

    def __contains__(self, attr_name):
        if attr_name in self.specs:
            return True
        
        if attr_name in self.methods:
            return True

        if attr_name in self.specific_args:
            return True
        
        if 'base' in self.specific_args and attr_name in self.base:
            return True

        return False

    def greedy_on(self, *args):
        # skip calling transform if at least one target with unmerged keys exists
        if len(args) == 0:
            self.GREEDY_TARGETS.append(set(x for x in self.TARGET_ITEMS))
        elif len(args) == 1 and callable(args[0]):
            self.GREEDY_TARGETS.append(args[0])
        else:
            for arg in args:
                assert arg in self.TARGET_ITEMS, f"'{arg}' is not a target of transform '{self.NAME}'"
            assert set(args) not in self.GREEDY_TARGETS
            self.GREEDY_TARGETS.append(set(args))
        return self

    def __getattr__(self, attr_name):
        if attr_name in self.specs:
            return self.specs[attr_name]
        
        if attr_name in self.methods:
            return self.methods[attr_name]

        if attr_name in self.specific_args:
            return self.specific_args[attr_name]
        
        if 'base' in self and attr_name in self.base:
            return self.base[attr_name]

        raise AttributeError(f"'{self.NAME}' transform does not have an attribute '{attr_name}'")
