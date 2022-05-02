from pyclbr import Function
import decorator


def twice_decorator(func: Function):
    """
    Decorator that calls the function twice

    Args:
        func (Function): Function to be decorated
    """
    def wrapper(function, argument) -> list:
        """
        Wrapper function

        Args:
            function (Function): Function to be decorated
            argument (int): Argument to be passed to the function

        Returns:
            int: Result of the function
        """
        return [function(argument), function(argument)]

    return decorator.decorator(wrapper, func)


@twice_decorator
def mul_int_by_2(num: int) -> int:
    """
    multiply int by 2
    Args:
        num (int): number to multiply

    Returns:
        int: result of multiplication
    """
    return num * 2


@twice_decorator
def print_int(num: int):
    """
    print int
    Args:
        num (int): number to print
    """
    print(num)


if __name__ == '__main__':

    print(mul_int_by_2(1))
    print_int(5)
