import yaml
import random
from googletrans import Translator, constants
from pprint import pprint
from sys import exit

vocabulary = {}

#End the game
def end():
	print('See you later!')
	print('...................')
	exit(0)

#Calculate percentage
def percentage(numerator, denominator): #this should not work
	return 100*(float(numerator)/float(numerator+denominator))

#Start the Greek translation version
def start_Gr():
	#Specify number of rounds 
	max_rounds = int(input('Number of rounds to study? Enter number: '))
	print('...................')
	print('Let\'s get started!')
	print('...................')

	#Tables for vocab that were guessed right and wrong
	right = []
	wrong = []

	#Read CSV and add to dictionary
	with open(filename,'r') as readFile:
		reader =yaml.safe_load(readFile)
		for row in reader:
			vocabulary[row['characters']] = row['greek']

	#Take a test with x rounds
	turns = 0	
	while turns < max_rounds: 
		for key in vocabulary:
			turns += 1
			print(turns)
			vocab = str(random.choice(list(vocabulary.keys())))
			translation = str(vocabulary[vocab])
			print(vocab)
			guess = input('Translate this: ')
			if guess == translation:
				print('Correct!')
				right.append(vocab)
			elif guess != translation: #User gets one more try
				guess2 = input('Wrong. Try again: ') 
				if guess2 == translation: 
					print('Correct!')
					right.append(vocab)
				else:
					print('Wrong. Move on.')
					wrong.append(vocab)	
			else: 
				print('Error. Try again.')
				break
			break 

	#Provide summary of test performance	
	right_count = len(right)
	wrong_count = len(wrong)
	print('...................')
	print('Test results: ')
	print('Correct: %d' % right_count) #How many values are correct
	print('Wrong: %d' % wrong_count) #How many values are wrong
	print('Your score:'), percentage(right_count, wrong_count), ('%') #Test score
	print('...................')

	#Print list of words that were wrong, if any
	print('')
	if not wrong:
		next = input('Great job! Study again? Type y/n: ')
		print('...................')
		if next == 'y':
			start_Gr()
		elif next == 'n':
			end()
	else:
		print('Great job! Study these words again:')
		study_again = ','.join(wrong)
		print(study_again)
		print('...................')
		next = input('Great job! Study again? Type y/n: ')
		print('...................')
		if next == 'y':
			start_Gr()
		elif next == 'n':
			end()

# def translate():
# 	translation = translator.translate(givenWord)

#Start the German language test
def start_De():
	#Specify number of rounds 
	max_rounds = int(input('Number of rounds to study? Enter number: '))
	print('...................')
	print('Let\'s start!')
	# print('Type \'y\' then ENTER if you get it correct, \'n\' if incorrect.')
	print('...................')

	#Tables for vocab that was right and wrong
	right = []
	wrong = []

	#Read YAML and add to dictionary
	with open(filename,'r') as readFile:
		reader =yaml.safe_load(readFile)
		for row in reader:
			vocabulary[row['characters']] = row['german']

	#Take a test with x rounds
	turns = 0	
	while turns < max_rounds: 
		for key in vocabulary:
			turns += 1
			print(turns)
			vocab = str(random.choice(list(vocabulary.keys())))
			translation = str(vocabulary[vocab])
			print(translation)
			guess = input('Translate this: ')
			if guess == 'y':
				print('Correct!')
				right.append(vocab)
			elif guess != 'n': #User gets one more try
				guess2 = input('Wrong. Try again: ') 
				if guess2 == 'y': 
					print('Correct!')
					right.append(vocab)
				else:
					print('Wrong. Move on.')
					wrong.append(vocab)	
			else: 
				print('Error. Try again.')
				break
			break 

	#Provide summary of test performance	
	right_count = len(right)
	wrong_count = len(wrong)

	print('...................')
	print('Test results: ')
	print('Correct: %d' % right_count) #How many values are correct
	print('Wrong: %d' % wrong_count) #How many values are wrong
	print('Your score:'), percentage(right_count, wrong_count), ('%') #Test score
	print('...................')
	#return wrong

	#Print list of words that were wrong, if any
	print('')
	if not wrong:
		next = input('Great job! Study again? Type y/n: ')
		print('...................')
		if next == 'y':
			start_De()
		elif next == 'n':
			end()
	else:
		print('Great job! Study these words again:')
		study_again = ','.join(wrong)
		print(study_again)
		print('...................')
		next = input('Great job! Study again? Type y/n: ')
		print('...................')
		if next == 'y':
			start_De()
		elif next == 'n':
			end()
	
#Specify YAML full file name, use translate.yaml
filename = input('File name you want to study: ')

#Specify if you'd like to practice translating to Greek or German language
practice = input('Practice German translation, or Greek translation? Type \'German\' or \'Greek\': ')

# Option to use yaml file or given word
# givenWord = input('Give a world for translation')
#Choose to practice english translations, or foreign lang translations
if practice == 'German':
	start_Gr()
elif practice == 'Greek':
	start_De()
else:
	print('Not a valid input, please restart the program.')
	end(0)
