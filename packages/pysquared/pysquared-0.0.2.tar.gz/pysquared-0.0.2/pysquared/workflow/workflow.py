import copy

from ..utils import get_logger_shortcuts
from .stack import BlockingInstructionStack, HandlerStatus, InstructionStack
from .instruction import Instruction


class Workflow:
    def __init__(self,
            transformators: dict,
            storage,
            logger=None,
        ) -> None:
        
        self.transformators = transformators
        self.storage = storage

        self.logger = logger
        self.log = get_logger_shortcuts(logger)
        self.instruction_stack = BlockingInstructionStack(handlers={
            'subframe': self._handle_subframe_call,
            'transformator_call': self._handle_transformator_call,
            'prepare_transform': self._handle_transform_preparation,
            'execute_transform': self._handle_transform_execution,
        }, logger=self.logger)
        self.instruction_stack.info.name = 'Base stack'

    def _find_transformator_by_items(self, search_items: list) -> str:
        found_transformator = None
        for name, tr_obj in self.transformators.items():
            accepted = True
            for item_name in search_items:
                if not tr_obj.contains_dataitem(item_name):
                    accepted = False
                    break
            if accepted:
                assert found_transformator is None, \
                    f"{repr(search_items)} does not define transformator unambiguously"
                found_transformator = name
        
        assert found_transformator is not None, \
            f"Cannot find transformator containing dataitems {repr(search_items)}"
        return found_transformator

    def execute(self, commands: list, forward: dict={}):
        assert len(self.instruction_stack) == 0, 'Command stack is not empty'
        self.instruction_stack.include_instructions(commands)

        status: HandlerStatus = self.instruction_stack.complete_workflow(forward=forward)
        assert status == HandlerStatus.DONE
        self.log.info("Execution finished normally")
    
    @staticmethod
    def _merge_forwards(instr: Instruction, forward: dict):
        # Priority: instr.info['forward'] > _complete_workflow(forward)
        for key, value in forward.items():
            if key not in instr.info.forward:
                instr.info.forward[key] = value

    def _handle_subframe_call(self, instr: InstructionStack, stack: InstructionStack, forward: dict={}):
        assert instr.is_subframe
        
        self._merge_forwards(instr=instr, forward=forward)

        if instr.is_blocking:
            status: HandlerStatus = instr.complete_workflow(forward=forward)
        else:
            status: HandlerStatus = instr.complete_workflow(hold=stack.is_blocking, forward=forward)
        return status

    def _handle_transformator_call(self, instr: Instruction, stack, forward: dict={}) -> HandlerStatus:
        # Find an appropriate transformator if it is not assigned explicitly
        if instr.info.transformator_name is None:
            search_items = [instr.info.target]
            if instr.info.sources is not None:
                search_items += instr.info.sources
            instr.info.transformator_name = self._find_transformator_by_items(search_items)
        else:
            assert instr.info.transformator_name in self.transformators, \
                f"{instr.info.transformator_name} is not registered in workflow"
        self.log.info(f"Using '{instr.info.transformator_name}' transformator "
            f"to reach the target '{instr.info.target}'")
        
        self._merge_forwards(instr=instr, forward=forward)
        
        assert stack.is_blocking
        stack_frame = stack.followup_substack(instr, blocking=False)

        self.transformators[instr.info.transformator_name].plan_transformation(
            stack_frame=stack_frame,
            transformator_name=instr.info.transformator_name,
            target=instr.info.target,
            sources=instr.info.sources,
            forward=instr.info.forward
        )
        return HandlerStatus.REPEAT
    
    def _handle_transform_preparation(self, instr: Instruction, stack, forward: dict={}) -> HandlerStatus:
        self._merge_forwards(instr=instr, forward=forward)

        stack_frame = stack.followup_substack(instr, blocking=False)

        self.transformators[instr.info.transformator_name].prepare_transform(
            stack_frame=stack_frame,
            transformator_name=instr.info.transformator_name,
            transform_name=instr.info.transform_name,
            transform_path=instr.info.transform_path,
            forward=instr.info.forward
        )
        return HandlerStatus.LATER # Expand transforms asap, then come back to execute them

    def _handle_transform_execution(self, instr: Instruction, stack, forward: dict={}) -> HandlerStatus:
        self._merge_forwards(instr=instr, forward=forward)

        returned_status: HandlerStatus = self.transformators[instr.info.transformator_name].execute_transform(
            stack_frame=stack,
            instruction=instr,
            transformator_name=instr.info.transformator_name,
            transform_name=instr.info.transform_name,
            unmerged_keys=instr.info.unmerged_keys,
            forward=instr.info.forward
        )

        return returned_status
