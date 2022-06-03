import os

path = "C:\\Users\\Oat\\Documents\\Project\\RenameFile\\Example\\"
print("Hello world")
print(f"Before Renaming: {os.listdir(path)}")
#os.rename(path+'StudentsMarks.txt', path+'Grades.txt')
#print(f"After Renaming: {os.listdir(path)}")

List = []
print("Blank List: ")
print(List)
  
# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)
  
# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])
  
# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)