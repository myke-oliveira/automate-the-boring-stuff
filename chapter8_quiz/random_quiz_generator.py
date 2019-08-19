#! python3
# random_quiz_generator.py - Creates quizzes with questions and answers in
# random order, algon with the answer key.

# The quiz data. Keys are states and values are their capitals.
from capitals import capitals
import os
import random

num_students = 35
num_questions = 10

for quiz_num in range(1, num_students + 1):
	with open(os.path.join('tests', f'test{quiz_num:0>2}.txt'), 'w') as test_file:
		with open(os.path.join('answers', f'answer{quiz_num:0>2}.txt'), 'w') as aswer_file:
			test_file.write(f'Test {quiz_num}\n\n')
			for num_question in range(1, num_questions + 1):
				test_file.write(f'Question {num_question}\n')
				state, capital = random.choice(list(capitals.items()))
				aswer_file.write(f'{num_question} - {state}: {capital}\n')
				options = list(capitals.values())
				options.remove(capital)
				options = random.sample(options, 4)
				options.append(capital)
				random.shuffle(options)
				test_file.write(f'Which one is the capital of {state}?\n')
				for index, option in enumerate(options, 1):
					test_file.write(f'{index} - {option}\n')
				test_file.write('\n')
