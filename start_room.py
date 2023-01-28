import time 
from textwrap import dedent
from playsound import playsound
import threading

class start(object):

	# this 'succes' global variavle. If player die or doing something wrong
	# this wariable will be changed and make game was end
	succes = True
	def enter():
		
		while True:
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
			print(dedent("""
				You have a key between your two legs.
				Use it to open the collar.
				You have 15 seconds
			"""))	
			playsound('./audio/open_collar_with_key(2).wav')	

			#asinc play music on the backgrounds
			def _playSound():
			 	playsound('./audio/SAW(3).mp3')
			t1 = threading.Thread(target=_playSound)
			t1.start()
			
			global remove_collar
			remove_collar = False
			
			# this function is asinc and check variable 'remove_collar' , if variable is false game end, if true game continue
			def this_is_end():
				global remove_collar
				if remove_collar == False:
					succes = False
					print('You Die')
					remove_collar = True 
				else:
					pass
			t2 = threading.Timer(15, this_is_end)
			t2.start()
			
			print(dedent("""
					What hell is going on?
					Ok ... Where is the key?
					...
					Yes! I find it!
					This collar has 3 holes but which one to choose?
			"""))	
			while True:
				choice = str(input('>')).strip()
				if choice == '1':
					print('This hole does not fit.')
					if remove_collar == True:
						break
				elif choice == '2':
					print('Yes, collar is open')
					break
					if remove_collar == True:
						break
				elif choice == '3':
					print('This hole does not fit.')
					if remove_collar == True:
						break
				else:
					print('not understand')
					if remove_collar == True:
						break
						
			print('-' * 70)
			print('Go to the next room?')
			choice_go = str(input('>')).strip()
			if choice_go == 'Yes' or choice_go == 'yes':
				time.sleep(3)
			else:
				exit(0)
			
			
			break


