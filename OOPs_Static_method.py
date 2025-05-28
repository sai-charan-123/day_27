class Method_variables:
	a=10
	def __init__(self,x):
		print("This is constructor :")
		self.x=x
	def instance_method(self):
		print("This is instance method :")
		print("Static variable is :",self.a)
		print("instance variable is :",self.x)
		d="Sai"
		print("local variable is :",d)
	@classmethod
	def class_method(cls):
		print("This is Class level :")
		print("Static variable is :",cls.a)
		d="Charan"
		print("local variable :",d)
	@staticmethod
	def static_method():
		print("This is Static method ")
		d="Sai Charan"
		print("local variable :",d)
m=Method_variables("sai charan")
m.instance_method()
m.class_method()
m.static_method()