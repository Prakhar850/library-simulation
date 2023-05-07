import datetime   #module used to work with dates

class Time():
	#This is a Python class named Time.

	# constructor
	def __init__(self,startTime):
		self.__startTime = startTime
		#The __init__ method is the class constructor, which takes startTime as a parameter 
		# and initializes a private attribute called __startTime with this parameter.

	# Change env time to real time
	#The changeToClock method takes envTime as a parameter, which represents the simulated time in the simulation environment. 
	# It adds this time to the __startTime attribute and returns a formatted string representing the new time in the format of "Year/Month/Day".
	def changeToClock(self,envTime):
		newTime = self.__startTime + datetime.timedelta(days=envTime)
		return newTime.strftime("%Y/%m/%d")
