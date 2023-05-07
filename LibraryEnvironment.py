import simpy
import os
import yaml
import random
import datetime
from itertools import cycle
from Student import Student
from Book import Book
from Time import Time

#Get settings data from Settings.yml
configYamlPath = os.path.join(os.path.dirname(__file__),"Settings.yml")
with open(configYamlPath, "r") as configYaml:
	settingsConfig = yaml.safe_load(configYaml)

libraryInfo = settingsConfig["library"]
bookInfo = libraryInfo["book"]
studentInfo = settingsConfig["student"]

# Student & Book list to keep datas
studentList = []
bookList = []
def setupStudents(env):
	#Setup Students
	names = studentInfo["studentName"]
	surnames = studentInfo["studentSurname"]
	
	#Pairing name&surname lists and randomizing the pairs
	randomNames = list(zip(names, cycle(surnames))) if len(names) > len(surnames) else list(zip(cycle(names), surnames))
	random.shuffle(randomNames)
	
	#Adding Students to student list with their membership
	for randomName in randomNames:
		student = Student(env," ".join(randomName),libraryInfo["membershipOptions"][random.randint(0, 1)])
		studentList.append(student)

def setupLibrary(env):
	#Setup Library
	print('\n======= Welcome to %s. Library is open till %s =======' % (libraryInfo["name"], libraryInfo["closeHour"]))
	
	#Adding books to library's booklist
	for title in bookInfo["titles"]:
		book = Book(env,title,random.randint(1, 3))
		bookList.append(book)
	
	#Give Info about Books
	print('\nLibrary Books: \n\nTitle\t\t\tAmount\n==============================')
	for book in bookList:
		print('%s\t\t%s' %(book.getTitle(),book.getAmount()))
		
	print('\n=======================================================================================\n')
		

def main():
	#One second in Real World = One Env Time
	env = simpy.rt.RealtimeEnvironment(factor=1.0)
	setupLibrary(env)
	setupStudents(env)
	
	# One Env Time = 1 Day in Simulation
	t = Time(datetime.datetime.now())
	
	# Students come and request Books randomly. They can get books earlier depending on priority of membership.
	studentComeTime = 0
	for student in studentList:
		env.process(student.requestBook(env,random.choice(bookList),studentComeTime,t))
		studentComeTime += random.randint(1,3)
	
	env.run()
	
	print('\n=========================== Library will be closed for a while, Thanks for your patience! ===========================')

if __name__ == "__main__":
    main()
    

# The first line imports the required libraries: simpy for discrete event simulation, os for interacting with the operating system, yaml for parsing YAML configuration files, random for generating random numbers, datetime for working with dates and times, and cycle for iterating over a sequence repeatedly.
# The next three lines import three classes: Student from Student.py, Book from Book.py, and Time from Time.py.
# The next four lines load the configuration data from a YAML file named Settings.yml and assign it to variables for later use.
# The next two lines create empty lists to hold information about the students and books.
# The setupStudents function defines how to create the students. It gets the list of student names and surnames from the configuration file, pairs them up randomly, assigns a membership randomly, and adds the student to the student list.
# The setupLibrary function defines how to set up the library. It prints a welcome message with the library name and closing hour, creates a list of books with random quantities, and prints the list of books with their titles and amounts.
# The main function is the main entry point of the program. It sets up the simulation environment, sets the current time to the current real-world time, and then creates the students and the library. It then loops through the list of students, assigns a random arrival time for each student, and schedules a book request for each student. It finally runs the simulation environment and prints a closing message.
# The if __name__ == "__main__": statement at the end ensures that the code inside the main function is only executed if this file is run as the main program, and not if it is imported as a module by another program.

