#! /usr/bin/python3.12

from pathlib import Path
import logging

# Logging configuration
logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
  datefmt='%A, %B %d, %Y %H:%M:%S %s %Z %z',
  filemode='+at',
  filename=f'{Path(__file__).parent.parent.parent}/logs/docstring_in_python.log'
)

logging.debug(f'Module name is: {__name__=}')
logging.debug(F'File constituting module is: {__file__=}')