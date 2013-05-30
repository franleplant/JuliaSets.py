class Perro():
	"""esto es un comment"""
	
	name = ""

	# class atributtes
	i = 0

	# private function, __ counts!
	def __b(self):
		return "Bark!, Bark!"
	
	def __init__(self, name):
		self.name = name
		self.__class__.i += 1
		self.n =self.__class__.i

	# comments
	def bark(self):
		print self.__b();
		
	# __dict__ enumerates properties



