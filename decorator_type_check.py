from functools import wraps
from typing import Any, Type


def type_check(type_: Type[Any]) -> Any:
    """
    Decorator to check the type of the argument passed to the decorated function.

    Args:
        type_ (Type[Any]): The type of the argument to check.
    Returns:
        Any: The decorated function.
    """
    def decorator(func: Any) -> Any:
        """
        Decorator to check the type of the argument passed to the decorated function.

        Args:
            func (Any): The function to decorate.
        Raises:
            TypeError: If the argument passed to the decorated function is not of the
            expected type.
        Returns:
            Any: The decorated function.
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Decorator to check the type of the argument passed to the decorated function. 
            
            Raises:
                TypeError: If the argument passed to the decorated function is not of
                the expected type.
            Returns:
                Any: The decorated function.
            """            
            for arg in args:
                if not isinstance(arg, type_):
                    raise TypeError(f"Argument {arg} is not of type {type_}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


if __name__== "__main__":

    @type_check(int)
    def add(first_num: int, second_num: int) -> int:
        """
        Function to add two numbers

        Args:
            first_num (int): First number
            second_num (int): Second number

        Returns:
            int: Sum of first_num and second_num
        """

        return first_num + second_num

    @type_check(float)
    def div(first_num: float, second_num: float) -> float:
        """
        Function to divide two numbers

        Args:
            first_num (float): First number
            second_num (float): Second number

        Returns:
            float: Division of first_num and second_num
        """
        return first_num / second_num if second_num != 0 else 0

    try:
        print(add(1, 2))
        # print(add(1, "2"))
        # print(add(1, 2.0))
        # print(div(1, 2))
        # print(div(1, "2"))
        # print(div(1, 2.0))
        # print(div(8.0, 2.0))
        print(div(8.0, 1.0))

    except TypeError as exception:
        print(exception)
