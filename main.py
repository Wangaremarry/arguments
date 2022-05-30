def multiply_and_greet(*args, **kwargs):
    keys=kwargs.keys()
    num=1
    for x in args:
        num*=numbers
        return num
    if "country" in keys:
        return f"Hello {kwargs['name']} from {kwargs['country']}"
    elif "name" in keys:
        return f"Hello am {kwargs['name']} and i am {kwargs['age']}"
    elif "gender" in keys:
        return f"Hello, i am from {kwargs['country']} and I am {kwargs['gender']}"
    else:
        return f"Who are you?"
    