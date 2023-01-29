from textwrap import dedent
import time
from playsound import playsound
import threading
from random import randint

class roulette(object):

	succes = True
	def enter():
		
		time.sleep(1)
		print('You slowky go with spangbob to next room in fully darkness')
		time.sleep(1)
		print(dedent("""
			 	Помнишь я тебе говорил что вы ответите за это сполна
				Настал час расплаты 
				Перед вами лежит револьвер
				Сыграйте в русскую рулетку по одному разу, если вы останетесь живы
				То такова судьба
		"""))
		
		array_slot = ['0', '1', '2', '3', '4', '5']
		patron = randint(0, int(len(array_slot)-1))
		#print('patron is:', patron)
		array_slot[patron] = 'patron'
		current_slot = randint(0, int(len(array_slot)-1))
		#print('current slot is:', current_slot)
		
		playsound('./audio/ru/рулетка.wav')
		
		def _playSound():
			playsound('./audio/eng/SAW(3).mp3')
		saw_play_sound = threading.Thread(target=_playSound)
		saw_play_sound.start()
		
		print('Вы заряжаете револьвер')
		time.sleep(2)
		print('...')
		time.sleep(2)
		print('Крутите барабан')
		time.sleep(2)
		print('Прикладываете к холодному виску')
		time.sleep(2)
		if array_slot[current_slot] == 'patron':
			print('HAHAHAHAHA')
			print('You die')
			exit(1)
		print('Ничего...')
		time.sleep(4)
		print('Spanch bob заряжает револьвер ')
		time.sleep(3)
		print('крутит барабан')
		time.sleep(5)
		print('...')
		time.sleep(1)
		print('губке бедному не повезло')
		time.sleep(3)
		print('...')
		print('Вы идете в следующую комнату ')
		
		
		