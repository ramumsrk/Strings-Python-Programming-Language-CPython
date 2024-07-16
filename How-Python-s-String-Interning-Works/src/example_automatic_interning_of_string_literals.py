#! /usr/bin/python3.12

import logging_configuration

import logging

from typing import LiteralString

# User-defined function
def main() -> None:
  logging.debug(f'Inside user-defined function \'main()\'')
  first_string_literal: LiteralString = 'name'
  second_string_literal: LiteralString = 'name'
  logging.debug(f'{id(first_string_literal)=}')
  logging.debug(F'{id(second_string_literal)=}')  
  logging.debug(f'{first_string_literal is second_string_literal=}')
  logging.debug('Exiting user-defined function \'main()\'')
  return None

if __name__ == '__main__':
  logging.debug(f'Module name is: {__name__=}')
  logging.debug(F'File constituting module is {__file__=}')
  # Function call
  logging.debug(f'{main()=}')