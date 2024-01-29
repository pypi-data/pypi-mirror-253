import copy

class KeynamingLayer:
    def __init__(self, key_mapping: dict, base=None):
        self.own_mapping = key_mapping
        self.base = base
        
        # just 'mapping' internal -> external
        # 'inverse mapping' external -> internal
        if self.base is None:
            self.total_mapping = key_mapping
        else:
            self.total_mapping = {
                internal_name: self.own_mapping[base_external_name]
                for internal_name, base_external_name in self.base.total_mapping.items()
            }
        
        self.inverse_total_mapping = {
            value: key
            for key, value in self.total_mapping.items()
        }

        self.is_ground = False
    
    def keyname_to_internal(self, keyname: str) -> str:
        return self.total_mapping[keyname]
    
    def keyname_to_external(self, keyname: str) -> str:
        return self.inverse_total_mapping[keyname]
    
    def map_to_external(self, keys: dict) -> dict:
        return {
            self.total_mapping[key] 
                if key in self.total_mapping 
                    else key 
                : value
            for key, value in keys.items()
        }
    
    def map_to_internal(self, keys: dict) -> dict:
        return {
            self.inverse_total_mapping[key] 
                if key in self.inverse_total_mapping 
                    else key 
                : value
            for key, value in keys.items()
        }
    
    def get_base(self):
        assert self.base is not None
        return self.base

    def get_public_keys(self) -> list:
        return list(key for key in self.total_mapping.values())


class GroundKeynamingLayer(KeynamingLayer):
    def __init__(self, keys: list):
        key_mapping = {
            keyname: keyname
            for keyname in keys
        }
        super().__init__(key_mapping=key_mapping)

        self.is_ground = True
    
    def get_base(self):
        raise RuntimeError('Attempted release of the ground keynaming layer')
