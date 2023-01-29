from textwrap import dedent


class winner(object):
	# this variable means, if player succesfuly end the room, he can go next
	succes = True
	def enter():
		print(dedent("""
			Поздравляем вы победили
		"""))		
		exit(0)