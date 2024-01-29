from .instruction import Instruction

class InstructionFactories:
    def reach_target(
            target: str,
            sources: list=None,
            transformator: str=None,
            forward: dict={}
        ) -> Instruction:

        assert isinstance(target, str)
        assert isinstance(sources, list) or sources is None
        assert isinstance(transformator, str) or transformator is None

        name = f"Reach target '{target}'"

        return Instruction({
            'type': 'transformator_call',
            'name': name,
            'target': target,
            'sources': sources,
            'transformator_name': transformator,
            'forward': forward
        })
    
    def prepare_transform(
            transformator: str,
            transform: str,
            path: list,
            forward: dict={}
        ) -> Instruction:
        
        assert isinstance(transformator, str)
        assert isinstance(transform, str)

        return Instruction({
            'type': 'prepare_transform',
            'name': f"Prepare transform '{transform}' of transformator '{transformator}'",
            'transformator_name': transformator,
            'transform_name': transform,
            'transform_path': path,
            'forward': forward
        })
    
    def execute_transform(
            transformator: str,
            transform: str,
            unmerged_keys: dict,
            forward: dict={}
        ) -> Instruction:
        
        assert isinstance(transformator, str)
        assert isinstance(transform, str)
        
        keys_repr = ', '.join([
            f"{key}={unmerged_keys[key]}"
            for key in sorted(unmerged_keys.keys())
        ])

        return Instruction({
            'type': 'execute_transform',
            'name': f"Execute transform '{transform}' with unmerged keys {keys_repr}",
            'transformator_name': transformator,
            'transform_name': transform,
            'unmerged_keys': unmerged_keys,
            'forward': forward
        })
