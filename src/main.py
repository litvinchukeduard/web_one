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


class Question:
    def __init__(self,
                 id_: str | int,
                 text: str,
                 answers: List[Answer]):
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


if __name__ == '__main__':
    print("Hello world!")