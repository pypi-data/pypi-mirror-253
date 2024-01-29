from enum import Enum

class TransformResult(Enum):
    FINISHED = 0
    FAILED = 1
    REPEAT = 2
    LATER = 3


class TransformState:
    def __init__(self,
            result: TransformResult,
            comeback_method: str=None,
            internals: dict={}
        ) -> None:

        self.result = result

        if self.result == TransformResult.FAILED or self.result == TransformResult.FINISHED:
            assert len(internals) == 0 and comeback_method is None, \
                f"Cannot repeat transform execution when the last result is '{repr(self.result)}'"
        
        self.internals = internals
        self.comeback_method = comeback_method
    
    @property
    def is_final(self):
        return self.result == TransformResult.FAILED or self.result == TransformResult.FINISHED

    @staticmethod
    def returnvalue_to_state(return_value):
        if isinstance(return_value, TransformState):
            return return_value
        else:
            assert return_value in TransformStateFactories.RETURN_VALUES, \
                f"'{return_value}' is not a valid return value from a transform"
            return TransformStateFactories.RETURN_VALUES[return_value]()


class TransformStateFactories:
    def transform_finished():
        return TransformState(TransformResult.FINISHED)

    def transform_failed():
        return TransformState(TransformResult.FAILED)

    def transform_repeat(comeback: str=None, **internals):
        return TransformState(TransformResult.REPEAT, comeback_method=comeback, internals=internals)
        
    def transform_later(comeback: str=None, **internals):
        return TransformState(TransformResult.LATER, comeback_method=comeback, internals=internals)

    RETURN_VALUES = {
        None: transform_finished,
        'done': transform_finished,
        'failed': transform_failed,
    }
