import random 
import linecache


def fileRowCount(fileName):

	file = open(fileName, "r") #open the file
	lineCounter = 0
	
	for line in file.readlines(): #iterate through each line of the file and count
		lineCounter +=1
		#print line
	
	file.close()
	return lineCounter

	
def selectName(fileName, number):
	file = open(fileName, "r") #open the file
	line = linecache.getline(fileName, number+1).strip('\n') #grab line from the random number generated
	
	file.close()
	
	return line

def getName(fileName, count):
	randomNumber = random.randint(0, count)
	# print randomNumber
	name = selectName(fileName, randomNumber)
	return name
	
	


def main():
	
	firstNameFile = "first_name.txt" 
	middleNameFile = "middle_name.txt" 
	lastNameFile = "last_name.txt" 

	firstNameCount = fileRowCount(firstNameFile) - 1
	middleNameCount = fileRowCount(middleNameFile) - 1
	lastNameCount = fileRowCount(lastNameFile) - 1
	
	"""
	#print firstNameCount , middleNameCount , lastNameCount
	
	#get first name
	firstRandInt = random.randint(0, firstNameCount)
	print firstRandInt
	firstName = selectName(firstNameFile, firstRandInt)
	
	#get middle name
	middleRandInt = random.randint(0, middleNameCount)
	print middleRandInt
	middleName = selectName(middleNameFile, middleRandInt)
	
	#get last name
	lastRandInt = random.randint(0, lastNameCount)
	print lastRandInt
	lastName = selectName(lastNameFile, lastRandInt)
	"""
	
	firstName = getName(firstNameFile, firstNameCount)
	middleName = getName(middleNameFile, middleNameCount)
	lastName = getName(lastNameFile, lastNameCount)
	print firstName + " " + middleName + " " +lastName
	
	




if __name__ == '__main__':
	main()