import time
from playsound import playsound
from textwrap import dedent
from random import randint

class friend(object):

	succes = True
	
	def enter():
		print('You slowly go to next, touch everething in this darknes')
		time.sleep(2)
		print('. . .')
		time.sleep(1)
		playsound('./audio/ru/Scream.mp3')
		print('Spanch Bob?')
		time.sleep(1)
		print('He need a help')
		playsound('./audio/ru/друг_приветствие.wav')
		time.sleep(1)
		print('Whata fu** is going on')
		playsound('./audio/ru/Scream.mp3')
		print(dedent("""
				Перед тобой лежат буквы
				Собери из них слово
				У тебя 15 секунд 
				Если ты не соберешь слово правильно с первого раз твоего друга разорвет на части
		"""))
		playsound('./audio/ru/друг.wav')
		
		print('Время пошло ...')
		time_before = time.time()
		
		true_word = 'Scream'
		array_letters = ['S','c','r','e', 'a', 'm']
		array_random_letters = 
		str = ''
		lenth = int(len(array_letters))
		
		for i in range(lenth):
			a = randint(0, lenth)
			item = array_letters[a]
			
		
		
		
		# take random letter from array 
		# append to array.random
		# create str from array random
		# print string
		# give input 
		# check input 
		
		
		
		
		
		
		
		
		