#using package translate

from translate import Translator

translator = Translator(to_lang='es')


try:
	with open('translator_test_en.txt',mode = 'r') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		with open('translator_test_es.txt',mode='w') as my_file2:
			my_file2.write(translation)
except FileNotFoundError as err:
		print("Wrong")	


