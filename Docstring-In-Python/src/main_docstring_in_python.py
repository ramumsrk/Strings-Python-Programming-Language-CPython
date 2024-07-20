#! /usr/bin/python3.12

import logging

import logging_configuration
from example_of_using_a_docstring_in_python.add_two_numbers.add_two_numbers import add_two_numbers as add_two_numbers

# User-defined function
def main() -> None:
  """This user-defined function has all the important code that needs to be executed"""
  logging.debug(f'Inside user-defined function \'main()\'')
  logging.debug(F'{add_two_numbers.__doc__=}')
  logging.debug(f'{add_two_numbers=}')
  logging.debug(F'{type(add_two_numbers)=}')
  logging.debug(f'Exiting user-defined function \'main()\'')
  return None

if __name__ == '__main__':
  logging.debug(f'Module name is {__name__=}')
  logging.debug(F'File constituting module is {__file__=}')
  logging.debug(f'{main()=}')