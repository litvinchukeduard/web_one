from typing import List


class Answer:
    def __init__(self,
                 id_: str,
                 text: str,
                 is_correct: bool):
        self.id_ = id_
        self.text = text
        self.is_correct = is_correct

    def __str__(self):
        return (f"Answer: id {self.id_}, text {self.text},"
                + " is_correct {self.is_correct}")

    def __repr__(self):
        return (f"Answer: id {self.id_}, text {self.text},"
                + " is_correct {self.is_correct}")


class UserAnswer:
    def __init__(self, user_id, question_id, answer_id):
        self.user_id = user_id
        self.question_id = question_id
        self.answer_id = answer_id

    def __str__(self):
        return f'User id: {self.user_id}, Question id: {self.question_id}, Answer: {self.answer_id}'
    
    def __repr__(self):
        return f'User id: {self.user_id}, Question id: {self.question_id}, Answer: {self.answer_id}'
    
    
class Question:
    def __init__(self,
                 id_: str | int,
                 text: str,
                 answers: List[Answer] = []):
        self.id_ = id_
        self.text = text
        self.answers = answers

    def __str__(self):
        answers_id = [i.id_ for i in self.answers]
        return (f"Question: id {self.id_}, text {self.text}"
                + f"answers {','.join(answers_id)}")

    def __repr__(self):
        answers_text = [i.text for i in self.answers]
        return (f"Question: id {self.id_}, text {self.text}"
                + f"answers {','.join(answers_text)}")

    def add_answer(self, answer: Answer):
        self.answers.append(answer)

    def del_answer(self, answer: Answer):
        for index, answer in enumerate(self.answers):
            pass

class Questionnaire:

    def __init__(self, name, questions: List[Question] = []):
        self.name = name
        self.questions = questions

    def add_question(self, _id, question_text):
        self.questions.append(Question(_id, question_text))

    def number_of_questions(self):
        return len(self.questions)

    def __str__(self) -> str:
        questions_str = ', '.join(self.questions)
        return f'Questionaire name: {self.name}, Questions: {questions_str}'
    
    def __repr__(self) -> str:
        questions_str = ', '.join(self.questions)
        return f'Questionaire name: {self.name}, Questions: {questions_str}'
    

class Users:

    def __init__(self, first_name, last_name, _id):
        self.first_name = first_name
        self.last_name = last_name
        self._id = _id


    def __str__(self):
        return f'First name - {self.first_name}, last name - {self.last_name}, id - {self._id} '
    

    def __repr__(self):
        return f'First name - {self.first_name}, last name - {self.last_name}, id - {self._id} '



questionare = Questionnaire('Hello', [])

def add_question(question_text):
    question_id = questionare.number_of_questions() + 1
    questionare.add_question(question_id, question_text)


def add_answer_to_question(question: str, answer: str, is_correct: bool) -> None:
    answer_ids = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЮЯ"
    for entry in questionare.questions:
        if entry.text == question:
            for answer_entry in entry.answers:
                if answer_entry.text == answer:
                    return
            if len(answer_ids) == len(entry.answers):
                return
            answer_id = answer_ids[len(entry.answers)]
            answer_to_add = Answer(id_=answer_id,
                                   text=answer,
                                   is_correct=is_correct)
            entry.answers.append(answer_to_add)
            return


if __name__ == '__main__':
    print("Hello world!")