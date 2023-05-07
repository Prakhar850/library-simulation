import simpy

class Book():

	# constructor
	def __init__(self,env,title,amount):
		self.__env = env
		self.__title = title
		self.__amount = amount
		self.__resource = simpy.PriorityResource(env, capacity=amount)
		

    # getter & setter
	def getTitle(self):
		return self.__title	
	def getAmount(self):
		return self.__amount
	def getResource(self):
		return self.__resource


	def setTitle(self,title):
		self.__title = title
	def setAmount(self,amount):
		self.__amount = amount
	def setResource(self,resource):
		self.__resource = resource	

# This is a class definition for a Book in a library simulation. Here's what each part does:

# import simpy: This line imports the simpy library, which is used to create discrete event simulations.

# class Book():: This line defines a class called Book.

# def __init__(self,env,title,amount):: This line defines a constructor method that initializes a new Book object with three instance variables: env, title, and amount. env is a reference to the simulation environment, title is the name of the book, and amount is the number of copies of the book in the library.

# self.__env = env: This line sets the env instance variable to the value passed in to the constructor.

# self.__title = title: This line sets the title instance variable to the value passed in to the constructor.

# self.__amount = amount: This line sets the amount instance variable to the value passed in to the constructor.

# self.__resource = simpy.PriorityResource(env, capacity=amount): This line creates a PriorityResource object with the simpy library. A PriorityResource is a type of resource in simpy that represents a shared resource that can be used by multiple processes. In this case, the resource represents the book. The capacity parameter sets the maximum number of copies of the book that can be borrowed at the same time.

# def getTitle(self):: This line defines a getter method for the title instance variable.

# return self.__title: This line returns the value of the title instance variable.

# def getAmount(self):: This line defines a getter method for the amount instance variable.

# return self.__amount: This line returns the value of the amount instance variable.

# def getResource(self):: This line defines a getter method for the resource instance variable.

# return self.__resource: This line returns the value of the resource instance variable.

# def setTitle(self,title):: This line defines a setter method for the title instance variable.

# self.__title = title: This line sets the title instance variable to the value passed in to the method.

# def setAmount(self,amount):: This line defines a setter method for the amount instance variable.

# self.__amount = amount: This line sets the amount instance variable to the value passed in to the method.

# def setResource(self,resource):: This line defines a setter method for the resource instance variable.

# self.__resource = resource: This line sets the resource instance variable to the value passed in to the method.