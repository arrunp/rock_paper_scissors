import random

#rock 0, paper 1, scissors 2, lizard 3, spock 4

class Play:
	def __init__(self):
		self.player_score = 0
		self.comp_score = 0
		self.choices_string = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
		self.comp_choice = random.randint(0,4)
		self.player_move = 0
		self.result = 0

	def computer_move(self):
		return self.choices_string[self.comp_choice]

	def player(self, move):
		self.player_move = move
		return self.player_move

	def winner(self, player_move):
		if player_move == self.comp_choice:
			self.result = "You tied"
		elif player_move == 0 and (self.comp_choice == 2 or self.comp_choice == 3):
			self.player_score += 1
			self.result = "You win!"
		elif player_move == 1 and (self.comp_choice == 0 or self.comp_choice == 4):
			self.player_score += 1
			self.result = "You win!"
		elif player_move == 2 and (self.comp_choice == 1 or self.comp_choice == 3):
			self.player_score += 1
			self.result = "You win!"
		elif player_move == 3 and (self.comp_choice == 1 or self.comp_choice == 4):
			self.player_score += 1
			self.result = "You win!"
		elif player_move == 4 and (self.comp_choice == 0 or self.comp_choice == 2):
			self.player_score += 1
			self.result = "You win!"
		else:
			self.comp_score += 1
			self.result = "You lost"

		self.comp_choice = random.randint(0,4)

