
class DotDict:
    def __init__(self, dictionary):
        self.__dict__.update(dictionary)

def get_logger_shortcuts(logger):
    if logger is not None:
        return DotDict({
            'debug': lambda message: logger.debug(message),
            'info': lambda message: logger.info(message),
            'warning': lambda message: logger.warning(message),
            'error': lambda message: logger.error(message),
        })
    else:
        return DotDict({
            'debug': lambda message: None,
            'info': lambda message: None,
            'warning': lambda message: None,
            'error': lambda message: None,
        })
