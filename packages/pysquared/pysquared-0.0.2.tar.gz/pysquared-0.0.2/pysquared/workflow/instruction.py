class InstructionInfo(dict):
    """This thing allows access via attibutes (info.type = ...)

    Args:
        dict (_type_): _description_
    """
    def __init__(self, input={}):
        super(InstructionInfo, self).__init__(input)

    def __getattr__(self, name):
        return self.__getitem__(name)

    def __setattr__(self,name,value):
        self.__setitem__(name,value)


class Instruction:
    def __init__(self, data: dict):
        self.info = InstructionInfo(data)
        self.finished = False

    def activate_dependents(self, stack) -> None:
        if 'activates' not in self.info:
            return

        for instruction_name in self.info.activates:
            activated = False
            for instruction in stack.instructions:
                if instruction_name == instruction.info.name:
                    assert not activated
                    assert self.info.name in instruction.info.activated_by
                    index = instruction.info.activated_by.index(self.info.name)
                    del instruction.info.activated_by[index]
                    stack.log.info(f"Stack {repr(self.info.name)}: Activated instruction '{instruction.info.name}'")
                    activated = True
            assert activated
            
    @property
    def is_subframe(self):
        return self.info.type == 'subframe'

    @property
    def is_active(self):
        return not self.finished and (not 'activated_by' in self.info or len(self.info.activated_by) == 0)
