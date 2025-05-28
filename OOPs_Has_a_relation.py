class Gowtham:
	phone="sams"
	@classmethod
	def insta(cls):
		print("You are using Gowtham mobile",cls.phone)
class Adhitya:
	@classmethod
	def insta(cls):
		print("Adhitya is using Gowtham phone ",Gowtham.phone)
G=Gowtham()
G.insta()
A=Adhitya()
A.insta()