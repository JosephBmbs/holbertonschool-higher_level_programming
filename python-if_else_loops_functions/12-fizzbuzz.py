#!/usr/bin/python3

def fizzbuzz():
	for num in range(1, 101):
		if num % 3 == 0 and num % 5 == 0:
			print("FizzBuzz", end="\t")
		elif num % 3 == 0:
			print("Fizz", end="\t")
		elif num % 5 == 0:
			print("Buzz", end="\t")
		else:
			print(num, end="\t")
