# Creation of Array
# importing "array" for array creations
 
import array as arr
 
#creating an array with integer type
 
a=arr.array('i',[1,2,3,4,5,6])
 
# printing original array
 
print("The Before extend array is :",end=" ")
 
for i in range(0,6):
   
    print(a[i],end=" ")
     
print()
 
# creating an array with using extend method
 
a.extend([7,8,9,10,11,12])
 
# printing original array
 
print("\nThe After extend array is :",end=" ")
 
for i in range(0,12):
   
    print(a[i],end=" ")
 
print()
 
#array with float type
 
b = arr.array('d', [2.1,2.2,2.3,2.4,2.5,2.6])
 
print("\nThe before extend array is :",end=" ")
 
for i in range(0,6):
   
  print(b[i],end=" ")
   
print() 
 
#extend function using pass the elements 
 
b.extend([2.6,2.7,2.8,2.9])
 
print("\nThe after extend array is :",end=" ")
 
for i in range(0,9+1):
   
  print(b[i],end=" ")
   
print()
