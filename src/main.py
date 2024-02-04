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
        return f''
	
	




if __name__ == '__main__':
    print("Hello world!")