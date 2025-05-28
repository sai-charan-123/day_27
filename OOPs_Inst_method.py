class Employee:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c
	def m1(self):
		d=self.a+self.b
		return d
a=Employee(10,20,30)
a.m1()
print(a.m1())