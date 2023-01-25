from rooms import winner_room
from rooms import russian_roulette
from rooms import friend_room
from rooms import start_room
from sys import exit


class Engine(object):
	pass

# array which contain rooms and posibility to see rooms
class Map(object):
	
	scenes = [winner_room, russian_roulette,
	          friend_room, start_room]

	def show_scenes():
		join_scenes = ' - '.join(scenes)
		print(join_scenes)

		
class Scene():
	def enter():
		print('If u see it, this subclass hasn\t enter function')
		exit(0)
	
# here we need screamer
class Death(Scene):
	def enter():
		print('You die')
		exit(0)

