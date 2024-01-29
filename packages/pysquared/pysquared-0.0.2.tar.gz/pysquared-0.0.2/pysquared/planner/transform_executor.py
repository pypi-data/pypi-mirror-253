from .transform_concrete import TransformConcrete
from ..utils import get_logger_shortcuts

from .transform_utils import TransformState, TransformResult


class TransformExecutor:
    def __init__(self,
            transform_instance: TransformConcrete,
            transformator_name: str,
            transform_name: str,
            logger=None
        ) -> None:

        self.transform_instance = transform_instance
        self.transformator = transform_instance.transformator
        self.abstract_transform = self.transform_instance.cur_transform
        
        # Be default, the 'exec' method serves as entry point for all transforms
        self.next_method = 'exec'
        self.next_internals = {}

        self.transformator_name = transformator_name
        self.transform_name = transform_name

        self.logger = logger
        self.log = get_logger_shortcuts(logger)

        self.initialized_for = None

    def initialize_restrictions(self, unmerged_keys: dict, keys_control=None) -> None:
        keys_lists = self.transform_instance.keys_lists
        self.item_restrictions = {}
        for item_list in (self.abstract_transform.SOURCE_ITEMS, 
                          self.abstract_transform.TARGET_ITEMS,
                          self.abstract_transform.NOTE_ITEMS):
            for item_name in item_list:
                self.item_restrictions[item_name] = self.transformator.graph.nodes[item_name]['item'].get_restricted({
                    key: value for key, value in unmerged_keys.items() if key in keys_lists[item_name]
                }, keys_control=keys_control)
        
        skip = False
        for item_name in self.abstract_transform.SOURCE_ITEMS:
            if self.item_restrictions[item_name].is_empty:
                self.log.error(f"Item '{item_name}' is empty for keys '{repr(unmerged_keys)}'")
                skip = True
        if skip:
            raise RuntimeError('SKIP!?')

    def initialize_for_method(self, method_name: str, unmerged_keys: dict, forward: dict={}) -> None:
        args_list = self.transform_instance.args_list[method_name]

        aware_data = {
            key: value
            for key, value in unmerged_keys.items()
            if key in self.abstract_transform.AWARE_KEYS
        }

        forwarded_args = {
            key: value
            for key, value in forward.items()
            if key in args_list
        }
        
        specific_args = {
            key: value
            for key, value in self.abstract_transform.specific_args.items()
            if key in args_list
        }

        self.execution_args = {
            **self.item_restrictions, # Restricted items are universal for all method calls
            **aware_data, # Are also universal for all method calls
            **forwarded_args, # Passed if required
            **specific_args # Args that are supported by this abstract transform (self and base)
        }

    def execute(self, unmerged_keys: dict, forward: dict={}) -> TransformResult:
        # Only for the first execution
        if not hasattr(self, 'item_restrictions'):
            keys_control = None
            if 'keys_control' in forward:
                keys_control = forward['keys_control']
            self.initialize_restrictions(unmerged_keys, keys_control)
        
        if 'GREEDY_TARGETS' in self.abstract_transform.specs:
            for greedy_targets in self.abstract_transform.GREEDY_TARGETS:
                if callable(greedy_targets):
                    skip_allowed = greedy_targets({
                        key: value
                        for key, value in self.item_restrictions.items()
                        if key in self.abstract_transform.TARGET_ITEMS
                    })
                else: # It's a list of str then ...
                    assert len(greedy_targets) > 0, f"Set of greedy targets is present but it's empty"
                    skip_allowed = True
                    for target_item in greedy_targets:
                        skip_allowed = skip_allowed and (len(self.item_restrictions[target_item]) > 0)
                if skip_allowed:
                    return TransformResult.FINISHED

        if self.initialized_for != self.next_method:
            self.initialize_for_method(
                method_name=self.next_method,
                unmerged_keys=unmerged_keys,
                forward=forward
            )

        # Execute method and convert the returned value to TransformState instance
        self.log.info(f"Executing the method '{self.next_method}' of transform '{self.abstract_transform.specs['NAME']}'")
        state: TransformState = TransformState.returnvalue_to_state(
            self.abstract_transform.methods[self.next_method](**self.execution_args, **self.next_internals)
        )

        if state.result == TransformResult.FINISHED:
            for cur_target_name in self.abstract_transform.TARGET_ITEMS:
                if self.item_restrictions[cur_target_name].non_empty:
                    self.transformator.graph.nodes[cur_target_name]['item'] += self.item_restrictions[cur_target_name]
                else:
                    self.log.warning(f"Target '{cur_target_name}' is empty after executing '{self.abstract_transform.NAME}'. " \
                        f"Restriction={repr(unmerged_keys)}")
            for restricted_item in self.item_restrictions.values():
                restricted_item.retire()
            self.log.info(f"Step {self.transform_name} finished successfully for {repr(unmerged_keys)}")
        elif state.result == TransformResult.FAILED:
            for restricted_item in self.item_restrictions.values():
                restricted_item.retire()
        else: # either REPEAT or LATER
            self.next_method = state.comeback_method
            self.next_internals = state.internals

        return state.result
