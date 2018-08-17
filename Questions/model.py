from flask import Flask


from datetime import datetime

class Question(object):

    def __init__(self, title, content): 

        self.title = title

        self.content = content

        self.date_posted = datetime.now()

        self.questions = []

    def post_question(self,question_id, title, content,date_posted):

        new_question = {

            'question_id': question_id,

            'title': title,

            'content': content,

            'date_posted':date_posted}


        self.questions.append(new_question)

        return (self.questions)








questions = [
	{
	id: "01"
	Author: "Chris Njuguna"
	date_posted:""
	question:" "
	answer:

	}

	{
	id: "02"
	Author: ""
	date_posted:""
	question:" "
	answer:""

	}
	{
	id: "03"
	Author: "Chris Njuguna"
	date_posted:""
	question:" "
	answer:""

	}
	{
	id: "04"
	Author: "Chris Njuguna"
	date_posted:""
	question:" "
	answer:

	}
	{
	id: "05"
	Author: "Chris Njuguna"
	date_posted:""
	question:" "
	answer:

	}
	{
	id: "06"
	Author: "Chris Njuguna"
	date_posted:""
	question:" "
	answer:""

	}










]