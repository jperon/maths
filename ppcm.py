#!/usr/bin/env python3

import sys
from pgcd import pgcd

def ppcm(a,b):
	return int(a * b / pgcd(a,b))

if __name__ == '__main__':
	print(ppcm(int(sys.argv[1]),int(sys.argv[2])))
