#! /usr/bin/python3.12

from typing import Union

# User-defined function
def add_two_numbers(first_number: Union[int, float], second_number: float | int) -> Union[float, int]:
  """
  Determine sum of two numbers which are of type either int or float

  Input:
  ======
  first_number: int | float First number
  second_number: float | int Second number

  Output:
  =======
  int | float Sum of two numbers
  """
  return first_number + second_number