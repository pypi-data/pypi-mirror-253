REGISTERED_DATAITEM_TYPES = {}

CHILD_PROPERTIES = {
    'object': {
        'is_file': False,
        'is_object': True,
        'is_path': False
    },
    'file': {
        'is_file': True,
        'is_object': False,
    },
    'path': {
        'is_path': True,
        'is_object': False,
    }
}

def register_dataitem(class_alias: str):
    """TODO Docstring
    """
    def decorator(class_object):
        REGISTERED_DATAITEM_TYPES[class_alias] = class_object

        # Add @property methods to class, like is_file, is_object and
        # everything else that was specified in CHILD_PROPERTIES
        if class_alias in CHILD_PROPERTIES:
            for prop_name, prop_value in CHILD_PROPERTIES[class_alias].items():
                def create_property_method(value):
                    @property
                    def getter(self):
                        return value
                    return getter

                prop_getter = create_property_method(prop_value)
                setattr(class_object, prop_name, prop_getter)

        return class_object
    return decorator
