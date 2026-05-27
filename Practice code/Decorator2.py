def debug(fn):
    def wrapper(*args, **kwargs):
        args_values = ", ".join(str(arg) for arg in args)
        kwargs_values = ", ".join(f"{key}={value}" for key, value in kwargs.items())
        print(f"Calling {fn.__name__} with args: {args_values} and kwargs: {kwargs_values}")
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} returned: {result}")
        return result
    return wrapper  


@debug
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(greet("Alice"))
