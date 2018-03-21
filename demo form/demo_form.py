import numpy as np
from utils import Utils

class Demo:
	questions = Utils.load_data()
	title = ['Họ và tên', 'Ngày sinh', 'CMND', 'Địa chỉ']


	def __init__(self):
		self._doneQuestions = np.zeros(len(Demo.questions))
		self._informations = [None]*len(Demo.questions)
		self._currentQuestion = 0
		self._endConversation = False

	def isEnd(self):
		return self._endConversation


	def hasMissedInfor(self):
		for i in self._doneQuestions:
			if i == 0:
				return True
		return False

	def whereIsMissedInfor(self):
		for i in self._doneQuestions:
			if i == 0:
				return i
		return -1

	def isGotTrueInfo(self, ans):
		return True


	def update(self, ans):
		if self.isGotTrueInfo(ans):
			self._doneQuestions[self._currentQuestion] = 1
			self._informations[self._currentQuestion]= self.getInformation(ans)

	def getInformation(self, ans):
		return ans

	def display(self):
		for indx, i in enumerate(Demo.title):
			print('%s: %s'%(i, self._informations[indx]))

	def getInput(self, inputQuestion):

		# timeout = 5

		inputString = input(inputQuestion)

		# inputString += Utils.input_time_out(timeout)

		return inputString

	def conversation(self):
		while not self.isEnd():
			for indx, q in enumerate(Demo.questions):
				self._currentQuestion = indx
				rand_id_question = np.random.randint(0, len(q))
				
				answer = self.getInput(q[rand_id_question])

				print('update.......')
				self.update(answer)

			if self.hasMissedInfor():
				id_question = self.whereIsMissedInfor()
			else:
				self._endConversation = True

		self.display()


if __name__ == '__main__':
	de = Demo()
	de.conversation()






