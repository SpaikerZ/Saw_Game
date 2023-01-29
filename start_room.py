import time 

from datetime import datetime
from datetime import timedelta

import threading
from textwrap import dedent
from playsound import playsound

class start(object):

	# this 'succes' global variable. If player die or doing something wrong
	# this wariable will be changed and make game end 
	succes = True

	def enter():
		
		while True:
			#printing text
			print(dedent("""
				You slowly open your eyes. 
				Something prickly metal on the neck.
				Where I am? Why is it so dark?
				I seem to have blood on my hands	
			"""))
			time.sleep(10) 
			print('. . .')
			time.sleep(1)
			playsound('./audio/ru/привет.wav')
			print('What???')
			print('Where I am??!!')
			time.sleep(2)
			print('Help!!!')
			
			print(dedent("""
				You have a key between your two legs.
				Use it to open the collar.
				You have 15 seconds
			"""))	
			playsound('./audio/ru/возьми ключ.wav')	
			
			time_before_mission = time.time()
			
			#asinc play music on the backgrounds
			"""
			def _playSound():
					playsound('./audio/eng/SAW(3).mp3')
			saw_play_sound = threading.Thread(target=_playSound)
			saw_play_sound.start()
			"""			
			
			
			print(dedent("""
					What hell is going on?
					Ok ... Where is the key?
					...
					Yes! I find it!
					This collar has 3 holes but which one to choose?
			"""))
			
			# this cycle take choice from player and if player choice was a correct. Cycle be breaking
			while True:
				time_after_mission = time.time()
				choice = str(input('>')).strip()
				if choice == '1':
					print('This hole does not fit.')
					if int(time_after_mission - time_before_mission) > 15:
						print('Yoy die')
						exit(0)
				elif choice == '2':
					print('Yes, collar is open')
					break
				elif choice == '3':
					print("This hole does not fit")
					if int(time_after_mission - time_before_mission) > 15:
						print('Yoy die')
						exit(0)
				else:
					print('not understand')
					if int(time_after_mission - time_before_mission) > 15:
						print('Yoy die')
						break
						  
			
			#if player write Yes, he continue the game		
			print('-' * 70)
			print('Go to the next room?')
			choice_go = str(input('>')).strip()
			if choice_go == 'Yes' or choice_go == 'yes':
				time.sleep(6)
			else:
				exit(0)
						  
			#break all enter function and go to the next room			  
			break


