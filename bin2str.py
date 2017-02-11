#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import re

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

def convert_bin_to_str(bin_str):
  bin_str = re.sub(ur'[^01]', '', bin_str)
  char_str = ''

  for i in range(0, len(bin_str), 8):
    char_str += chr(int(bin_str[i:i+8], 2))

  return char_str

if __name__ == '__main__':
  print(convert_bin_to_str(sys.stdin.read()))
