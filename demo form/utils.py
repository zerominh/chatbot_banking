


class Utils():

	

	@staticmethod
	def load_data(file_data = ["hoiten.txt",  "hoingaysinh.txt", "hoicmnd.txt", "hoidiachi.txt"]):
		'''
		Return:
		questions -- list of list: [[[], [], ...], [[], [], ...], [[], [], ...], ...]
		
		'''
		questions = []
		for f in file_data:
			q = []
			file = open(f,mode ="r", encoding="utf8")
			for i in file:
				q.append(i)

			questions.append(q)

		return questions

	@staticmethod
	def kbhit():
		''' Returns True if keyboard character was hit, False otherwise.'''
		import sys
		if sys.platform.startswith('win32'):
			import msvcrt
			return msvcrt.kbhit()   
		else:
			dr,dw,de = select([sys.stdin], [], [], 0)
			return dr != []

	@staticmethod
	def input_time_out(time_out=10):
		import time
		import msvcrt
		import string
		begin = time.clock()
		end = begin + time_out
		input_string = ''
		while end >= time.clock():
			if Utils.kbhit():
				char = msvcrt.getwch()
				if char in '\x00\xE0':
					msvcrt.getwch()
				elif char in string.printable:
					char = char.replace('\r', '\n')
					if char != '\n':
						input_string += char
					else:
						input_string += ' '
					msvcrt.putwch(char)
				elif char == '\x08':
					input_string = input_string[:-1]
		return input_string



if __name__ == '__main__':
	# print(Utils.load_data())
	print(Utils.input_time_out())