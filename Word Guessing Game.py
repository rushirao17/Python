import random

name = input("What is your name? ")

print("Good Luck ! ", name)

words = ['mathematics', 'player', 'condition',
		'python','rainbow', 'computer', 'science', 'programming',
		'reverse', 'water', 'board', 'robot','chemistry']
word = random.choice(words)


print("Guess the characters")
guesses = ''
# any number of turns can be used here
turns = 12

while turns > 0:
	# counts the number of times a user fails
	failed = 0

	for char in word:

		# comparing that character with
		# the character in guesses
		if char in guesses:
			print(char, end=" ")

		else:
			print("_",end=" ")

			# for every failure 1 will be
			# incremented in failure
			failed += 1

	if failed == 0:
		print("You Win")

		# this print the correct word
		print("The word is: ", word)
		break

	print()
	guess = input("guess a character:")

	# every input character will be stored in guesses
	guesses += guess

	# check input with the character in word
	if guess not in word:
		turns -= 1
		print("Wrong")

		print("You have", + turns, 'more guesses')

		if turns == 0:
			print("You Loose")
