class CheckNumber:
    @staticmethod
    def is_prime(num: int) -> bool:
        """Check if a number is prime.

        Args:
        num (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """

        if not isinstance(num, int):
            raise ValueError("Number must be an integer")

        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def sum_digits(num: int) -> int:
        """Sum up digits in a number

        Args:
        num (int): The number whose digits should be summed up

        Returns:
        int: The sum of the digits in the number
        """

        if not isinstance(num, int):
            raise ValueError("Number must be an integer")

        return sum(int(digit) for digit in str(num))


class CheckNumbers:
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """
        Calculate the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.

        Parameters:
        a (int): The first number.
        b (int): The second number.

        Returns:
        int: The Greatest Common Divisor of a and b.
        """

        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("Both numbers must be integers")

        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a: int, b: int) -> int:
        """
        Calculate the Least Common Multiple (LCM) of two numbers.

        Parameters:
        a (int): The first number.
        b (int): The second number.

        Returns:
        int: The Least Common Multiple of a and b.
        """
        return abs(a * b) // CheckNumbers.gcd(a, b)


