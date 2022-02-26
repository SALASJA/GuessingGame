from random import randint
def main():
	game = GuessingGame()
	guess = input("enter your guess: ")
	while guess != game.get_mystery_number():
		guess = input("enter your guess: ")
	print("You Won")




class GuessingGame:
	def __init__(self):
		self.mystery_number = randint(0,10)
	
	def round(self, guess):
		pass
	
	def get_mystery_number(self):
		return self.mystery_number
		
main()