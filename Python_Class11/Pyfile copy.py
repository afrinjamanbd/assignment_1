import numpy as np

a = np.array([1,2,3]) 
b = np.array([(1.5,2,3), (4,5,6)], dtype = float) 
c = np.array([[(1.5,2,3), (4,5,6)],[(3,2,1), (4,5,6)]], dtype = float)


np.zeros((3,4)) #Create an array of zeros
np.ones((2,3,4),dtype=np.int16) #Create an array of ones
d = np.arange(10,25,5)#Create an array of evenly spaced values (step value)
# np.linspace(0,2,9) #Create an array of evenlyspaced values (number of samples)
# e = np.full((2,2),7)#Create a constant array
f = np.eye(2) #Create a 2X2 identity matrix
np.random.random((2,2)) #Create an array with random values
np.empty((3,2)) #Create an empty array


a.shape #Array dimensions 
len(a)#Length of array
b.ndim #Number of array dimensions
e.size #Number of array elements
b.dtype  #Data type of array elements
b.dtype.name  #Name of data type
b.astype(int). #Convert an array to a different type


np.int64 #Signed 64-bit integer types
np.float32. #Standard double-precision floating point
np.complex. #Complex numbers represented by 128 floats
np.bool  #Boolean type storing TRUE and FALSE values
np.object #P type
np.unicode_ #Fixed-length unicode type
ython object type
np.string_ #Fixed-length string

 = a.view()#Create a view of the array with the same data
np.copy(a) #Create a copy of the array
 = a.copy() #Create a deep copy of the array

a.sort() #Sort an array
c.sort(axis=0) #Sort the elements of an array's axis

a[2] #Select the element at the 2nd index
  3
b[1,2] #Select the element at row 1 column 2(equivalent to b[1][2])
  6.0

i = np.transpose(b) #Permute array dimensions
i.T #Permute array dimensions