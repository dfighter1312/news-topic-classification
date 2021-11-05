from types import MethodType
from cfgs.path_configs import PATH 

class Configs(PATH):
    
    def __init__(self):
        super(Configs, self).__init__()
        self.init_params()


    def init_params(self):
        """Initialize parameters for models."""
        pass

    def parse_to_dict(self, args):
        args_dict = {}
        for arg in dir(args):
            if not arg.startswith('__') and not isinstance(getattr(args, arg), MethodType):
                if getattr(args, arg) is not None:
                    args_dict[arg] = getattr(args, arg)
        return args_dict

    def add_args(self, args_dict):
        for arg in args_dict:
            setattr(self, arg, args_dict[arg])

    def proc(self):
        assert self.RUN_MODE in ['train', 'test']


    def __str__(self):
        for attr in dir(self):
            if not attr.startswith('__') and not isinstance(getattr(self, attr), MethodType):
                print('{ %-17s }->' % attr, getattr(self, attr))

        return ''    