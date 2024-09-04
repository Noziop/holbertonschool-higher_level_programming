#!/usr/bin/python3

print(''.join([chr(i + 32) if i % 2 == 0 else chr(i) for i in range(90, 64, -1)]))