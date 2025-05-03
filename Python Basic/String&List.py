#String operations and functions 
name = "Snehal@123"
name1 = "Snehal"
#check if all the char are numbers
print(name.isalnum())

#check if all the char are alphabet
print(name1.isalpha())

#test if string contains digits
print(name.isdigit())

#test if string contains uppercase words
print(name.istitle())

#to check is uppercase or lowercase 
print(name.isupper())
print(name1.islower())

#to check for space
print(name.isspace())

#test if string endswith given letter
print(name.endswith("l"))

#test if string start eith given letter
print(name.startswith("S"))

#List operations and functions

#List can contain different datatypes 
list = ["name","class",100,200]

#type check the datatype of variable
print(type(list))

#to calculate length of a variable
print(len(list))

#to add element at last in list
list.append("Hello")
print(list)

#entering ar any index and here index start from 0 to n-1
#and here length also start from -tive

print(list[1])#point at begining 
print(list[-1])#pinting at the end 

#printing the range of a function
print(list[0:-1])

#inserting element at index
list.insert(1,"inserted") #insert single index
list.insert(2,["hi",120]) #insert a list as nested list
print(list)

#using extend 
list.extend([2]) #extend list by 1 character
list.extend(['ji',"hu"]) #extend list with muliple values.
print(list)

#operations performed on list

#total sum of list
lst = [1,2,4,3,2,1,1,3,5,6]
print(sum(lst)) #calculate the sum

#pop the element
lst.pop(0) #pop the element at index 0
print(lst)

#count the occurence of given element
print(lst.count(1)) #return occurence of the element

#index to return the first occurence of element
print(lst.index(1,0,5))

#find min and max in a list
print(min(lst))#getting minimum
print(max(lst))#getting maximum

#to copy the list
print(lst*2) #list get printed twice





