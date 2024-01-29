import copy
import inspect

from ..utils import get_logger_shortcuts
from ..transforms import Transform


class TransformConcrete:
    def __init__(self,
            transformator,
            transform_name: str,
            logger=None
        ) -> None:
        
        self.transformator = transformator
        self.transform_name = transform_name

        self.logger = logger
        self.log = get_logger_shortcuts(logger)
    
    def prepare_instance(self, forward: dict={}) -> None:
            
        self.log.info(f"Preparing for '{self.transform_name}' transform")
        self.cur_transform: Transform = self.transformator.transformations[self.transform_name]

        self.args_list = {
            method_name: inspect.getfullargspec(method)[0]
            for method_name, method in self.cur_transform.methods.items()
        }
        assert 'exec' in self.args_list, \
            f"Entry point ('exec'-method) is not implemented for transform '{self.transform_name}'"
        
        aware_keys = self.cur_transform.AWARE_KEYS
        merged_keys = self.cur_transform.MERGED_KEYS
        assert len(set(aware_keys).intersection(merged_keys)) == 0, \
            f"Aware and Merge sets overlap. Aware={repr(aware_keys)}, Merged={repr(merged_keys)}"

        # Construct lists of keys
        self.keys_lists = {}
        self.source_keys = []
        for source_name in self.cur_transform.SOURCE_ITEMS:
            self.keys_lists[source_name] = self.transformator.graph.nodes[source_name]['item'].public_keys
            for key in self.keys_lists[source_name]:
                if key not in self.source_keys:
                    self.source_keys.append(key)
        for cur_target_name in self.cur_transform.TARGET_ITEMS:
            self.keys_lists[cur_target_name] = self.transformator.graph.nodes[cur_target_name]['item'].public_keys
        for note_name in self.cur_transform.NOTE_ITEMS:
            self.keys_lists[note_name] = self.transformator.graph.nodes[note_name]['item'].public_keys
        self.log.debug("keys_lists = " + repr(self.keys_lists))

        # Check that requested keys are present
        aware_okay = True
        for key in aware_keys:
            if key not in self.source_keys:
                aware_okay = False
                self.log.error(f"Requested aware key '{key}' is not involved in transform '{self.transform_name}'")
        merged_okay = True
        for key in merged_keys:
            if key not in self.source_keys:
                merged_okay = False
                self.log.error(f"Requested merged key '{key}' is not involved in transform '{self.transform_name}'")
        assert aware_okay and merged_okay, f"Failed key check on the stage '{self.transform_name}'"
        
        # Check for overlapping naming of keys, items, forwarded args, etc.
        itemnames_set = set()
        keys_set = set()
        forward_stuff = list(forward.keys())
        for l in self.keys_lists.values():
            keys_set.update(set(l))
        for l in [self.cur_transform.SOURCE_ITEMS, self.cur_transform.TARGET_ITEMS, self.cur_transform.NOTE_ITEMS]:
            itemnames_set.update(set(l))

        def check_overlap(**attrs):
            assert len(attrs) == 2
            names = list(attrs.keys())
            sets = list(attrs.values())
            intersection = sets[0].intersection(sets[1])
            assert len(intersection) == 0, f"{names[0]} and {names[1]} share element(s): {repr(intersection)}"
        check_overlap(item_names=itemnames_set, key_names=keys_set)
        check_overlap(item_names=itemnames_set, forwarded_keys=forward_stuff)
        check_overlap(key_names=keys_set, forwarded_keys=forward_stuff)

        # Check prerequisites for unaware, aware and merged keys
        for key in self.source_keys:
            each_source = True
            each_target = True
            one_source = False
            one_target = False # "one_target and not one_source" is a criteria for new key
            for source_name in self.cur_transform.SOURCE_ITEMS:
                if key in self.keys_lists[source_name]:
                    one_source = True
                else:
                    each_source = False
            for cur_target_name in self.cur_transform.TARGET_ITEMS:
                if key in self.keys_lists[cur_target_name]:
                    one_target = True
                else:
                    each_target = False
            
            if key in aware_keys: # aware
                assert each_target and one_source, f"Necessary condition for aware key is not satisfied for '{key}'"
                self.log.debug(f"Key '{key}' is in aware mode")
            elif key in merged_keys: # merged
                assert one_source, f"Necessary condition for merged key is not satisfied for '{key}'"
                self.log.debug(f"Key '{key}' is in merged mode")
            else: # unaware
                assert each_source and each_target, f"Necessary condition for unaware key is not satisfied for '{key}'"
                self.log.debug(f"Key '{key}' is in unaware mode")

        self.nonmerged_keys = copy.copy(self.source_keys)
        for key in merged_keys:
            del self.nonmerged_keys[self.nonmerged_keys.index(key)]
        if self.transform_name == 'get_nbo_cube':
            print('HERE')

    def get_key_combinations(self):
        return self.transformator.storage.key_combinations(
            items=self.cur_transform.SOURCE_ITEMS,
            nonmerged_keys=self.nonmerged_keys
        )
