
'''Class: User

Fields:
	- first_name: user first name (str)
	- last_name: user last name (str)
	- id: unique id of the user (int)

Examples:
{‘id’: 1, ’first_name’: ‘Ed’, last_name: ‘Litvinchuk’}'''



class Users:

    def __init__(self, first_name, last_name, _id):
        self.first_name = first_name
        self.last_name = last_name
        self._id = _id


    def __str__(self):
        return f'First name - {self.first_name}, last name - {self.last_name}, id - {self._id} '
    

    def __repr__(self):
        return f'First name - {self.first_name}, last name - {self.last_name}, id - {self._id} '
