print(' hello, welcome to the theory of object oriented programming ')

class MotorTransport(object) :
	def __init__(self, color, year, auto_type) :
		self.color = color
		self.year = year
		self.auto_type = auto_type

	def stop(self) :
		print(' pressing the stop pedal ')

	def drive(self) :
		print(' WRRRRUM! ')

ferrari_testarossa = MotorTransport(' red ', 1968, ' passenger car ')

ferrari_testarossa.drive()