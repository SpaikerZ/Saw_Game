from textwrap import dedent
import time
from playsound import playsound
import threading

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
		
		
		playsound('./audio/ru/рулетка.wav')
		
		def _playSound():
			playsound('./audio/eng/SAW(3).mp3')
		saw_play_sound = threading.Thread(target=_playSound)
		saw_play_sound.start()
		
		print('Вы заряжаете револьвер')
		time.sleep(1)
		print('...')
		time.sleep(1)
		print('Крутите барабан')
		time.sleep(1)
		print('Прикладываете к холодному виску')
		time.sleep(1)
		
		
		
		
		
		# crate revolver
			# array with slot
			# array with 
		
		