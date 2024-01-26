# coding = utf-8
"""
:Date: 2024-1-25 Latest
:Description: A package for calculate Math problem contain easy calculation and easy linear algebra problem,
              in the future author will add functions to solve easy geometry problems.
"""


class EC:
    @staticmethod
    def sum(x, y):
        """
        :param x: the first value, number or list and other are all OK
        :param y: the second value, number or list and other are all OK
        :return: the summary of the two values
        """
        return sum(x) + sum(y)

    @staticmethod
    def subtract(x, y):
        """
        :param x: the first value, number or list and other are all OK
        :param y: the second value, number or list and other are all OK
        :return: to subtract the two values
        """
        return sum(x) - sum(y)

    @staticmethod
    def multiply(x, y):
        """
        :param x: the first value, number or list and other are all OK
        :param y: the second value, number or list and other are all OK
        :return: multiply the two values
        """
        return sum(x) * sum(y)

    @staticmethod
    def divide(x, y, int_divide: int = None, decimal_places=None):
        """
        :param x: numerator, number or list and other are all
        :param y: denominator, number or list and other are all but cannot be zero !
        :param int_divide: bool value, to judge user whether need exact division
        :param decimal_places: the number of digits after decimal point
        :return: for division
        """
        if y == 0:
            return "Error! Division by zero is not allowed."
        elif int_divide == 0:
            result = x / y
            return round(result, decimal_places)
        elif int_divide == 1:
            int_result = x // y
            return int_result

    @staticmethod
    def square(x, y):
        """
        :param x: the truth of a matter
        :param y: index
        :return: for quadratic root
        """
        return x ** y

    @staticmethod
    def square_root(number, numerator, denominator, decimal_places: int = None):
        """
        :param number: the truth of a matter
        :param numerator: numerator of root
        :param denominator: denominator of root
        :param decimal_places: the number of digits after decimal point
        :return: for rooting
        """
        if number < 0 and number % 2 == 0:
            return "Error! Cannot calculate square root of a negative number."
        result = number ** (numerator / denominator)
        return round(result, decimal_places)


class EL:
    @staticmethod
    def inverse(arr: list):
        """
        :param arr: list, inverse number
        :return: count inverse number
        """
        inversions = sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr)) if arr[i] > arr[j])
        return inversions

    @staticmethod
    def determinant(arr: list) -> int:
        """
        :param arr: list, det determinant
        :return: result of determinant
        """
        dimension = len(arr)
        if dimension == 1:
            return arr[0][0]
        elif dimension == 2:
            return arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]
        else:
            det = 0
            for i in range(dimension):
                sub_matrix = [row[:i] + row[i + 1:] for row in arr[1:]]
                det += ((-1) ** i) * arr[0][i] * EL.determinant(sub_matrix)
            return det

    @staticmethod
    def cofactor(arr: list) -> list:
        """
        :param arr: list, det determinant
        :return: for algebraic cofactor
        """
        cofactor_matrix = []
        for i in range(len(arr)):
            cofactor_row = []
            for j in range(len(arr)):
                minor_matrix = [row[:j] + row[j + 1:] for row in (arr[:i] + arr[i + 1:])]
                cofactor_row.append(((-1) ** (i + j)) * EL.determinant(minor_matrix))
            cofactor_matrix.append(cofactor_row)
        return cofactor_matrix
