import time 
from textwrap import dedent
from playsound import playsound

class start(object):

	succes = True
	def enter():
		print(dedent("""
			You slowly open your eyes. 
			Something prickly metal on the neck.
			Where I am? Why is it so dark?
			I seem to have blood on my hands	
		"""))
		time.sleep(10)
		print('. . .')
		time.sleep(1)
		playsound('./audio/hello_my_dear(1).wav')
		print('What???')
		print('Where I am??!!')
		time.sleep(1)
		print('Help')
		playsound('./audio/open_collar_with_key(2).wav')
		print(dedent("""
			You slowly open your eyes. 
			Something prickly metal on the neck.
			Where I am? Why is it so dark?
			I seem to have blood on my hands	
		"""))		




