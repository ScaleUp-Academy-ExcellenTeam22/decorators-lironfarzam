from functools import cache

"""
 - cache(decorator) - 

    Cache decorator is used to cache the result of a function.
    in this case, the Fibonacci sequence is the sum of the previous two numbers.
    each time the function is called, the result is cached and returned and not
    calculated again.

- property (decorator) - 

    Property decorator is used to create a property of a class instance that can be
    accessed as an attribute.

- staticmethod (decorator) -

    Staticmethod decorator is used to create a static method of a class instance that
    can be accessed as an attribute.
"""


@cache
def my_fibonacci(the_n_number_in_the_fibonacci_series: int) -> int:
    """
    This function returns the n-th number in the Fibonacci series.
    
    Args:
        the_n_number_in_the_fibonacci_series (int): The n-th number in the Fibonacci series.

    Returns:
        int: The n-th number in the Fibonacci series.
    """
    return (the_n_number_in_the_fibonacci_series if the_n_number_in_the_fibonacci_series <= 1 else
            my_fibonacci(the_n_number_in_the_fibonacci_series - 1) +
            my_fibonacci(the_n_number_in_the_fibonacci_series - 2))


class Person:
    """
    This class is used to create a Person.
    """
    def __init__(self, first_name: str, last_name: str, age: int, person_id: int):
        """
        This function is used to initialize the Person.
        
        Args:
            first_name (str): The first name of the Person.
            last_name (str): The last name of the Person.
            age (int): The age of the Person.
            person_id (int): The id of the Person.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id = person_id

    @property
    def get_email(self):
        """
        This function is used to get the email of the Person.
        
        Returns:
            str: The email of the Person.
        """
        return f"{self.first_name}_{self.last_name}@gmail.com"

    @staticmethod
    def get_planet_name() -> str:
        """
        This function returns the name of the planet the Person live on.
        
        Returns:
            str: The name of the planet.
        """
        return "Earth"


if __name__ == "__main__":

    print("start the fibonacci sequence")
    for i in range(1, 200):
        print(i, my_fibonacci(i))
    print("done the fibonacci sequence")

    print("-" * 20)

    temp_person = Person("Liron", "Farzam", 26, 123)
    print(temp_person.get_email)

    print(temp_person.get_planet_name())
    print(Person.get_planet_name())
