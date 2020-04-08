import random

DEBUG = True

if DEBUG:
	random.seed("aa")

for i in range(5):
	print(random.randint(0, 10))

for i in range(5):
	print(random.uniform(5, 25))

