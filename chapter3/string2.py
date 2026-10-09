name="vishal"  #this is a string
print(name) # Output: vishal
nameshort=name[0:3]    #this is a string slicing which will give the output from index 0 to 2
print(nameshort) # Output: vis
character1=name[4]   #this is a string indexing it means it will give the character at index 4
print(character1) # Output: a
nameshort=name[-4:]   #this is a string slicing which will give the output from index -4 to the end of the string
print(nameshort) # Output: shal
nameshort=name[:-1]   #this is a string slicing which will give the output from index 0 to -2
print(nameshort) # Output: visha
print(name[::2])  #this is a string slicing which will give the output from index 0 to the end of the string with a step of 2
print(name[1:5:2])  #this is a string slicing which will give the output from index 1 to 4 with a step of 2