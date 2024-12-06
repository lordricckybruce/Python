#!/bin/python3

class Name():
	def __init__(self,firstname,lastname):
		self.firstname = firstname
		self.lastname = lastname
	def snit(self):
		print(f'My name is {self.firstname} {self.lastname}')
name_obj1 = Name('Adebayo','Adeleke')
print(name_obj1.snit())
#creating a simple calculator with class

class Cal():
	def __init__(self,add,sub,div,mul,ind):
		self.add = add
		self.sub = sub
		self.div = div
		self.mul = mul
		self.ind = ind
	def add(self):
		def add(a,b):
				c = a+b
				return(c)
		g = sum(a,b)
		print(g)
	def minus(self):
		def min(a,b):
				c = a-b
				return(c)
		f = min(a,b)
		print(f)
	def divide(self):
		def div(a,b):
				c = a/b
				return(c)
		t = divide(a,b)
		print(t)
myopt = Cal(3,4,5,4)
print(myopt.add())
