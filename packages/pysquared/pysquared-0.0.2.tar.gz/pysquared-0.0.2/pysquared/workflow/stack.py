import copy
import time
from typing import Callable

from enum import Enum

from .instruction import Instruction
from ..utils import get_logger_shortcuts


class HandlerStatus(Enum):
    DONE = 1
    REPEAT = 2
    LATER = 3


class InstructionStack(Instruction):
    # Inheriting Instruction because stacks can also serve as "instructions" being substacks in other stacks

    def __init__(self, data: Instruction=None, handlers: dict=None, parent_stack=None, logger=None):
        self.instructions = []
        self.handlers = handlers
        self.parent_stack = parent_stack
        assert (self.parent_stack is not None) ^ (self.handlers is not None), \
            f"InstructionStack must be initialized with either parent_stack or handlers"

        self.logger = logger
        self.log = get_logger_shortcuts(logger)

        self.current_instruction_idx = None
        self.next_instruction_idx = None

        if data is None:
            super().__init__({})
        else:
            super().__init__(data.info)
            
    def include_instructions(self, instr_list: list) -> None:
        for instr in reversed(instr_list):
            self.include_instruction(instr)
            
    def include_instruction(self, instruction: Instruction) -> None:
        assert isinstance(instruction, Instruction), \
            f"Attempting to include '{repr(instruction)}' of non-Instruction type"
        
        if 'name' in instruction.info:
            for item in self.instructions:
                if item.info['name'] == instruction.info['name']:
                    self.log.warning("Instruction with the name "
                        f"'{item.info['name']}' already registered in non-blocking stack")
        
        self.instructions.append(instruction)

        self.log.info(f"Stack {repr(self.info.name)}: Included instruction {repr(instruction.info.name)}")

    def __len__(self) -> int:
        return len(self.instructions)

    def followup_instruction(self, instruction: Instruction):
        assert self.current_instruction_idx is not None, \
            f"Cannot follow-up instruction {repr(instruction.info)}, when stack execution is not running"
        
        self.instructions[self.current_instruction_idx] = instruction

    def followup_substack(self, instruction: Instruction, blocking: bool=True):
        assert isinstance(instruction, Instruction)

        new_element = Instruction(data=copy.copy(instruction.info))
        new_element.info['type'] = 'subframe'

        if blocking:
            new_element = BlockingInstructionStack(new_element, parent_stack=self, logger=self.logger)
        else:
            new_element = NonBlockingInstructionStack(new_element, parent_stack=self, logger=self.logger)

        self.followup_instruction(new_element)
        return new_element
    
    def _get_handlers(self):
        if self.handlers is None:
            assert self.parent_stack is not None, "Both parent stack and instruction handlers are missing"
            return self.parent_stack._get_handlers()
        else:
            return self.handlers

    def _get_handler_for(self, instruction_type: str) -> Callable:
        handlers = self._get_handlers()
        assert instruction_type in handlers, \
            f"No handler for instruction of type '{instruction_type}'"
        return handlers[instruction_type]
    
    def _repr_instruction(self, instruction: Instruction, actual_index:int, show_index: int) -> list:
        if actual_index == self.current_instruction_idx and instruction.is_subframe:
            cur_flag = ' > '
        elif actual_index == self.current_instruction_idx and not instruction.is_subframe:
            cur_flag = '—> '
        else:
            cur_flag = '   '

        name = "<UNTITLED>"
        if 'name' in instruction.info:
            name = instruction.info.name

        if instruction.is_subframe:
            return [f"{cur_flag}{show_index+1}) {name}"] + [
                '  ' + line
                for line in instruction._repr_as_lines()
            ]
        else:
            return [f"{cur_flag}{show_index+1}. {name}"]

    def _repr_as_lines(self) -> list:
        lines = []
        show_index = 0
        for index in range(len(self.instructions) - 1, -1, -1):
            instruction = self.instructions[index]
            lines += self._repr_instruction(instruction, actual_index=index, show_index=show_index)
            show_index += 1

        return lines
    
    def print_stack(self, stream=None) -> None:
        newline = '\n'
        text = f"""
===============================
WORKFLOW STACK:
{newline.join(self._repr_as_lines())}
===============================

1) substack
1. task
 > active stack frame
—> active task
"""
        if stream is None:
            self.log.info(text)
        else:
            stream.write(text)
    
    @property
    def base_stack(self):
        if self.parent_stack is not None:
            return self.parent_stack.base_stack
        else:
            return self


class BlockingInstructionStack(InstructionStack):
    def complete_workflow(self, forward: dict={}) -> None:
        while len(self) > 0:

            if self.next_instruction_idx is not None:
                self.current_instruction_idx = self.next_instruction_idx
                self.next_instruction_idx = None
            else:
                self.current_instruction_idx = len(self) - 1

            current_instruction = self.instructions[self.current_instruction_idx]
            if current_instruction.is_active:
                handling_method = self._get_handler_for(current_instruction.info.type)
                self.log.info(f"Stack {repr(self.info.name)} (blocking): Running type={repr(current_instruction.info.type)} name={repr(current_instruction.info.name)}")
                status: HandlerStatus = handling_method(instr=current_instruction, stack=self, forward=forward)
            else:
                raise NotImplementedError
            
            if status == HandlerStatus.DONE:
                self.instructions[self.current_instruction_idx].activate_dependents(stack=self)
                del self.instructions[self.current_instruction_idx]
            elif status == HandlerStatus.REPEAT:
                self.next_instruction_idx = self.current_instruction_idx
            else:
                raise RuntimeError("BlockingInstructionStack cannot process "
                    f"the returned HandlerStatus='{repr(status)}'")
        
        self.current_instruction_idx = None
        self.next_instruction_idx = None

        return HandlerStatus.DONE

    @property
    def is_blocking(self):
        return True


class NonBlockingInstructionStack(InstructionStack):
    def complete_workflow(self, hold: bool, forward: dict={}) -> HandlerStatus:
        if hold:
            while len(self) > 0:
                self._do_single_round(forward=forward)
                time.sleep(1)
        else:
            self._do_single_round(forward=forward)

        if len(self) == 0:
            return HandlerStatus.DONE
        else:
            return HandlerStatus.LATER # Can happen only when hold=False

    def include_instruction(self, instruction: Instruction) -> None:
        assert 'name' in instruction.info, \
            f"'{repr(instruction.info)}' must contain 'name' when it's included in non-blocking stack"
        
        for item in self.instructions:
            assert item.info['name'] != instruction.info['name'], \
                f"Instruction with the name '{item.info['name']}' already registered in non-blocking stack"
            assert 'activated_by' in instruction.info and 'activates' in instruction.info, \
                    "Instructions in nonblocking stack must contain 'activated_by' and 'activates' attrs"
        super().include_instruction(instruction)

    def _do_single_round(self, forward: dict={}) -> None:
        self.next_instruction_idx = len(self) - 1
        while self.next_instruction_idx != -1:

            self.current_instruction_idx = self.next_instruction_idx
            current_instruction = self.instructions[self.current_instruction_idx]
            if current_instruction.is_active:
                if 'stack_stream' in forward and forward['stack_stream'] is not None:
                    self.base_stack.print_stack(forward['stack_stream'])
                assert 'activated_by' in current_instruction.info and 'activates' in current_instruction.info, \
                    "Instructions in nonblocking stack must contain 'activated_by' and 'activates' attrs"
                handling_method = self._get_handler_for(current_instruction.info.type)
                self.log.info(f"Stack {repr(self.info.name)} (nonblocking): Running type={repr(current_instruction.info.type)} name={repr(current_instruction.info.name)}")
                status: HandlerStatus = handling_method(instr=current_instruction, stack=self, forward=forward)
                time.sleep(0.01) # This is for visual effect when live stack is printed
            else:
                status = HandlerStatus.LATER

            if status == HandlerStatus.DONE:
                # Remove instruction if we don't have to come back to it
                self.instructions[self.current_instruction_idx].activate_dependents(stack=self)
                del self.instructions[self.current_instruction_idx]
                self.next_instruction_idx = self.current_instruction_idx - 1
            elif status == HandlerStatus.REPEAT:
                self.next_instruction_idx = self.current_instruction_idx
            elif status == HandlerStatus.LATER:
                self.next_instruction_idx = self.current_instruction_idx - 1
            else:
                raise RuntimeError("NonBlockingInstructionStack cannot process "
                    f"the returned HandlerStatus='{repr(status)}'")
            
        self.current_instruction_idx = None
        self.next_instruction_idx = None

    @property
    def is_blocking(self):
        return False
