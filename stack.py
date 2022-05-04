class Stack:

	def __init__(self, data):
		self.data = data

	def push(self, x):
		self.data.append(x)

	def pop(self):
		if self.data != []:
			element = self.data[-1]
			del self.data[-1]
			return element


s = Stack([1, 2, 4])

s.push(8)
s.push(5)

for i in range(3) :
	print(s.pop())