from winner_room import winner
from russian_roulette import roulette
from friend_room import friend
from start_room import start
from sys import exit


class Scene(object):
	def enter():
		print('If u see it, this subclass hasn\'t enter function')
		exit(0)

# array which contain rooms and posibility to see rooms
class Map(object):
		
	scenes = [#start, friend, 
		roulette, winner]

	def show_scenes():
		join_scenes = ' - '.join(scenes)
		print(join_scenes)

		
class Engine(Map):
	
	def __init__(self, map):
		self.map = map

# this function run room by index 0, after succes delte this room and again run room by index 0	
# work while list haves rooms
	def play(self):			
		while len(self.map.scenes) != 0:
			current_scene = self.map.scenes[0]
			#check enter function in sybclasses
			try:
				current_scene.enter()
			except AttributeError:
				print('-' * 20)
				print('Scene hasn\'t enter function')
				print('-' * 20)
				exit(0)
				
			if current_scene.succes:
				self.map.scenes.remove(current_scene)
			elif current_scene.succes == False:
				Death()
			else:
				print('#*#' * 50)
	
# here we need screamer
class Death(Scene):
	def enter():
		print('You die')
		exit(0)

a = Engine(Map)
a.play()
		
		
		
		
		
		