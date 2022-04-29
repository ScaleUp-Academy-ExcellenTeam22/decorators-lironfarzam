 
def decorator_surprise(func):
    """
        Decorator that will make the function print “surprise!” instead of its original functionality.
    Args:
        func (function): function to be decorated
    """

    def wrapper(*args, **kwargs) -> None:
        """
            Wrapper function that will print “surprise!” instead of its original functionality.
        """
        print("surprise!")
    return wrapper


if __name__ == '__main__':
    @decorator_surprise
    def say_hello(name: str) -> None:
        """
            Function that will print “Hello, {name}”.
        Args:
            name (str): name of the person to greet

        Returns:
            _type_: None
        """
        print(f"Hello {name}")
    
    say_hello("Liron")
