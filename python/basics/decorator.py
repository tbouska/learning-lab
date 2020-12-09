def decorator(decoratee):
    closure = True

    def wrap():
        print(f"Starting decoration\nBy the way, I think I'm a closure = "
              "{closure}")
        decoratee()
        print("Ending decoration")
    return wrap


@decorator
def decorate_me():
    print("I like to be decorated")


decorate_me()
