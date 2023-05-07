import simpy
import random
#This code defines a Student class with several attributes and methods to simulate a student's behavior in a library system. 
class Student():
	# constructor
	#This method is the class constructor that initializes the student's env attribute (a simpy environment), name, membership, and membershipName. 
	# membership is an integer representing the level of the student's library membership, where -1 is gold membership and 0 is normal membership. 
	# membershipName is a string that describes the membership level of the student.
	def __init__(self,env,name,membership):
		self.__env = env
		self.__name = name
		self.__membership = membership
		self.__membershipName = ('Gold' if membership ==-1 else 'Normal') +' Membership'


    # getter & setter
	#These methods are getter and setter methods for the name and
	#  membership attributes of the student.
	def getName(self):
		return self.__name	
	def getMembership(self):
		return self.__membership

	def setName(self,name):
		self.__name = name
	def setMembership(self,membership):
		self.__membership = membership
		
	
	# Functions
	#This method simulates a student requesting a book from the library. 
	# It takes in the env (a simpy environment), book (a Book object), wait (an integer representing the time the student waits before requesting the book), and time (a Time object representing the current time in the simulation). 
	# env.timeout(wait) is a simpy method that simulates the student waiting for wait time units before requesting the book. book.getResource() is a method of the Book object that returns a simpy.
	# Resource object associated with the book.
	def requestBook(self,env,book,wait,time):
		#Student coming time
		yield env.timeout(wait)
		resource = book.getResource()
		
		#Request book with membership ant wait to get book.
		#This block of code is executed after the student has waited and is ready to request the book. 
		# It uses a with statement to acquire the resource associated with the book and requests it with the student's membership level as the priority. 
		# The yield req line simulates the student waiting until the book is available. Once the book is available, the student borrows it for a random amount of time using env.timeout(random.randint(5,10)). 
		# Finally, the student returns the book to the library using print('%s gave book back at %s to the library' % (self.__name, time.changeToClock(env.now))).
		with resource.request(priority=self.__membership) as req:
			#Request book
			print('%s has requested %s Book at %s with %s' % (self.__name, book.getTitle(),time.changeToClock(env.now), self.__membershipName))
			yield req
			#Borrow Book and read it in random time.
			print('%s has borrowed %s Book at %s' % (self.__name, book.getTitle(),time.changeToClock(env.now)))
			yield env.timeout(random.randint(5,10))
			#After finishing reading, give book to libray.
			print('%s gave book back at %s to the library' % (self.__name, time.changeToClock(env.now)))
	
	
