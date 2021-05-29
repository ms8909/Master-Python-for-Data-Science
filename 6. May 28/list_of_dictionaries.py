# ARHAM RUMI

# Program to Change data structures

# Problem Statement

# --------------------------------------------------------------------------------------
# names= [“alan”, “john”, “tania”, “ahmad”, “ali”, “muddassar”, “raheel”, “hamza”]
# age= [12,13,14,15,17,16,13,13]

# Write a function that converts the above data in the following format.

# people = [ {“name”: “alan”, “age”: 12}, {“name”: “john”, “age”: 13}, ……]
# --------------------------------------------------------------------------------------

print("Here, we conbine the two lists into with related entities")
print("\r")


def dictionaryCreator(nameList, ageList):

    peopleList = []
    length = len(nameList)
    for i in range(0, length):
        peopleList.append({'Name': nameList[i], 'Age': ageList[i]})
    return peopleList


names = ["alan", "john", "tania", "ahmad", "ali", "muddassar", "raheel", "hamza"]
age = [12, 13, 14, 15, 17, 16, 13, 13]

peopleData = dictionaryCreator(names, age)
print("\r")
print(peopleData)