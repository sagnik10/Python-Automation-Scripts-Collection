def log_methods(cls):
    for name, value in cls.__dict__.items():
        if callable(value):
            def wrapper(func):
                def inner(*a, **k):
                    print(f"Calling {func.__name__}")
                    return func(*a, **k)
                return inner
            setattr(cls, name, wrapper(value))
    return cls

@log_methods
class Test:
    def add(self, a, b):
        return a + b

t = Test()
print(t.add(2, 3))