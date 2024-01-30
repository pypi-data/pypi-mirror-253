class InterfaceConstant:
    pass

class Interface(type):
    classes = {}
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        for base in bases:
            if (funcs := cls.classes.get(base)) != None:
                for func in funcs:
                    if not func in vars(x):
                        raise NotImplementedError(f"Class {name} must implement method {func} (defined in interface {base.__name__})")
        cls.classes[x] = []
        for k, v in dct.items():
            if v == InterfaceConstant:
                cls.classes[x].append(k)
        return x
    

def implement(func):
    return InterfaceConstant