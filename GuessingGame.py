from random import randint
def main():
	game = GuessingGame()
	guess = int(input("enter your guess: "))
	while guess != game.get_mystery_number():
		game.round(guess)
		guess = int(input("enter your guess: "))
	print("You Won")




class GuessingGame:
	def __init__(self):
		self.mystery_number = randint(0,10)
	
	def round(self, guess):
		if guess < self.mystery_number:
			print("Too small")
		if guess > self.mystery_number:
			print("Too big")
	
	def get_mystery_number(self):
		return self.mystery_number

main()