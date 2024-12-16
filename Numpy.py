# Numpy in python
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))


# use of tuples
arr = np.array((1,2,3,4,5))
print(arr)
print(type(arr))



# dimension in arrays - 1,2,3

arr = np.array(10)
print(arr)
print(type(arr))
print(arr.ndim)

# 1 d arrays

arr = np.array([10,20,30])
print(arr)
print(type(arr))
print(arr.ndim)#check where the dimenction is (1d,2d,,3d)

# 2 d arrays

arr = np.array([[10,20,30],[40,50,60]])
print(arr)
print(type(arr))
print(arr.ndim)#check where the dimenction is (1d,2d,,3d)

# 3 d arrays

arr = np.array([[[10,20,30.2],[40,50,60],[70,80,90]]])
print(arr)
print(type(arr))

print(arr.ndim)  #check where the dimenction is (1d,2d,,3d)

# 5 dimension 
import numpy as np
arr = np.array([1,2,3,4] , ndmin = 5)
print(arr)
print("the numbers of dim is :" , arr.ndim)
#  Numpy inxeding 

# Array indexing is the same as accessing an array element
# you can access an array element by referring to its index

# get first element
arr = np.array([2,1,3,4,56])
print(arr[0])
arr = np.array([1,2,3,4,56,5,6,7,8,9,10,20,23,25,99,69])
print(arr[0])
print(len(arr))
print("the second element is :" , arr[2])
print("the six element is :", arr[5])
print("the eight element is :", arr[7])
print("the sum of the element is :", arr[2]+arr[5]+arr[7])
    # access 2-D arrays for indexing
            #      0             1        this is the  index position
            #    0,  1, 2   0,  1, 2      this is the  the element inside the index element 
arr = np.array([[10,20,30],[40,50,60]])
print('2 element on 1 row is :'  , arr[0,1]) 
 # arr[0,1] where 0 is (first breaket) and in first it has 10,20,30 and in it we print 1 row means 20 (index)
  
arr = np.array([[1,2,3,4,],[56,5,6,7]])
print('2 element on 1 row is :'  , arr[1,2]) 

arr = np.array([[1,2,3,4,],[56,5,6,7]])
print('2 element on 1 row is :'  , arr[1,2]) 
print('last element is :', arr[1,3])

 # access 3 -D arrays for indexing
                 #      0                 1        this is the  index position
                #  0,      1         0,         1  this is the this is the second index position 
                # 0,1,2   0,1,2     0,1,2    0 ,  1, 2   this is the  the element inside the index element 
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10.2,12,13]]])
print(arr[0,1,2])


# slicing of the numpy arrays 

arr = np.array ([1,2,3,4,5,6,7,8,9])
print(arr[1:5])
print(type(arr))
print("sum is :" , arr[1,2]+arr[1,3])

# spiking the element

arr = np.array ([1,2,3,4,5,6,7,8,9])
print(arr[::2])

# slicing in 2-d arrays

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,0:4])

 # checking the data type of the arrays

arr = np.array ([1,2,3,4,5,6,7,8,9])

print(arr.dtype)

arr = np.array(['animals','python'])
print(arr.dtype)

 # creating a array with defined data type

arr = np.array([1,2,3,4] , dtype = 'S')
print(arr)
print(arr.dtype)

#create an arrays with data types of 4 bytes interger

arr = np.array([1,2,3,4] , dtype = 'i4')
print(arr)
print(arr.dtype)

arr = np.array([1,2,3,4] , dtype = 'f4')
print(arr)
print(arr.dtype)

#  numpy array shape
# the shape of array is the number of the emement in each dimenstion


#print the shape of the 2-d array


arr = np.array([[1,2,3,4],[5,6,7,8]])         
print(arr.shape)


arr = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])         
print(arr.shape)

  #  joining numpy arrays 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.concatenate((arr1,arr2))
print(arr3)

# join 2-d arrys

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])

np.concatenate((arr1,arr2))

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])

np.concatenate((arr1,arr2),axis = 1)

# splitting numpy arrays

# spliting the arrys in 3 parts

arr = np.array([1,2,3,4,5,6])
narr  = np.array_split(arr,3)
print(narr)

arr = np.array([1,2,3,4,5,6])
np.array_split(arr,3)

        # ravel and flatten  (do the same thing)
# convert multi dim  array into 1 d arrays


m = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

print(m)
print('dimension is :' , m.ndim)

n = m.ravel()  # convert 3-d to 1-d
print(n)

m = np.array([[[1,2,3],[4,5,6],[7,8,9]]])

print(m)
print('dimension is :' , m.ndim)

n = m.flatten()  # convert 3-d to 1-d
print(n)
print('dimension is :' , n.ndim)

c = np.array([[[[1,2,3],[4,5,6],[7,8,9]]]])
print(c)
print('how many dimension is :',c.ndim)

print('the new dim is :' , c.ravel())

#  unique Function

arr = np.array([12,14,13,15,16,5,28,61,864,1,564,8,16,82,94,8,940,628,4,])
print(arr)
x = np.unique(arr)
print(x)

# find index position  (return function)

arr = np.array([12,14,13,15,16,5,28,61,864,1,564,8,16,82,94,8,940,628,4])
print(arr)
x = np.unique(arr , return_index = True)
print(x)

arr = np.array([12,14,13,15,16,5,28,61,864,1,564,8,16,82,94,8,940,628,4])
print(arr)
x = np.unique(arr , return_index = True ,return_counts = True)
print(x)

#  delete function

a = np.array([1,23,25,68,47,58])
d = np.delete(a,[2])
print(d)


a = np.array([[1,23,25],[68,47,58],[48,89,99]])
print(a)
d = np.delete(a,1,axis = 0)
print()
print(d)

a = np.array([[1,23,25],[68,47,58],[48,89,99]])
print(a)
d = np.delete(a,1,axis = 1)
print()
print(d)

a = np.array([[1,23,25],[68,47,58],[48,89,99]])
print(a)
d = np.delete(a,2,axis = 0)
print()
print(d)

a = np.array([[1,23,25],[68,47,58],[48,89,99]])
print(a)
d = np.delete(a,2,axis = 1)
print()
print(d)
