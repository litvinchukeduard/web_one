'''
Class: Questionnaire

Fields:
	- name: questionnaire name (str)
	- questions: list of questionnaire questions (list)

Examples:
{‘name’: ‘Module 2’, ‘questions’: []}
{‘name’: ‘Module 3’, ‘questions’: [{‘id’: 1, ‘text’: ‘What is..?’, ‘answers’: []}]} 
'''

class Questionnaire:

    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def add_question(self, _id, question_text):
        question = Q

    def __str__(self) -> str:
        questions_str = ', '.join(self.questions)
        return f'Questionaire name: {self.name}, Questions: {questions_str}'
    
    def __repr__(self) -> str:
        questions_str = ', '.join(self.questions)
        return f'Questionaire name: {self.name}, Questions: {questions_str}'
