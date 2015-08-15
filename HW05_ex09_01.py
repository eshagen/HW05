#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def print_20_plus():
	fin = open('words.txt')	
	for line in fin:
		word = line.strip()	# strips whitespace characters
		if len(word) > 20: # only prints words with more than 20 chars
			print word
	



##############################################################################
def main():
    print print_20_plus()

if __name__ == '__main__':
    main()
