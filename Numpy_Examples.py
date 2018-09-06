
# coding: utf-8

# In[1]:


import numpy as np

a = np.array([1,2,3])
print(a)


# In[2]:


import numpy as np

a = np.array([[1,2],[3,4]])
print(a)


# In[3]:


import numpy as np

a = np.array([1,2,3,4,5], ndmin=2)
print(a)


# In[4]:


import numpy as np

a = np.array([1,2,3,4,5], dtype=complex)
print(a)


# In[5]:


import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.shape)


# In[6]:


import numpy as np

a = np.array([[1,2,3],[4,5,6]])
a.shape=(3,2)
print(a)


# In[7]:


import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)


# In[10]:


import numpy as np

a = np.arange(24)
print(a)


# In[13]:


import numpy as np

a = np.arange(24)
print(a)
b = a.reshape(2,4,3)
print(b)


# In[19]:


import numpy as np

a = np.empty([3,2],dtype=int)
print(a)


# In[21]:


import numpy as np

a = np.zeros([2,2])
print(a)


# In[22]:


import numpy as np

a = np.ones([3,3], dtype=int)
print(a)


# In[23]:


import numpy as np

a = np.ones([3,3])
print(a)


# In[26]:


# convert list to ndarray

import numpy as np

x = [1,2,3]
a = np.asarray(x)
print(a)


# In[27]:


import numpy as np

x = [1,2,3]
a = np.asarray(x,dtype=float)
print(a)


# In[28]:


# ndarray from tuple
import numpy as np
x = (1,2,3)
a = np.asarray(x)
print(a)


# In[29]:


# ndarray from list of tuples
import numpy as np
x = [(1,2,3),(4,5)]
a = np.asarray(x)
print(a)


# In[31]:


#numpy.arange
#This function returns an ndarray object containing evenly spaced values within a given
#range. The format of the function is as follows:

#numpy.arange(start, stop, step, dtype)
# start
# The start of an interval. If omitted, defaults to 0
# stop
# The end of an interval (not including this number)
# step
# Spacing between values, default is 1
# dtype
# Data type of resulting ndarray. If not given, data type of input is used

import numpy as np

a = np.arange(10)
print(a)


# In[32]:


# start and stop parameters set
import numpy as np
x = np.arange(10,20,2)
print(x)


# In[33]:


#numpy.linspace

# This function is similar to arange() function. In this function, instead of step size, the
# number of evenly spaced values between the interval is specified. The usage of this
# function is as follows:
#numpy.linspace(start, stop, num, endpoint, retstep, dtype)
# start
# The starting value of the sequence
# stop
# The end value of the sequence, included in the sequence if endpoint set to
# true
# num
# The number of evenly spaced samples to be generated. Default is 50
# endpoint
# True by default, hence the stop value is included in the sequence. If false,
# it is not included
# retstep
# If true, returns samples and step between the consecutive numbers
# dtype
# Data type of output ndarray

import numpy as np
x = np.linspace(10,20,5)
print(x)


# In[34]:


# endpoint set to false
import numpy as np
x = np.linspace(10,20, 5, endpoint=False)
print(x)


# In[35]:


# find retstep value
import numpy as np
x = np.linspace(1,2,5, retstep=True)
print(x)
# retstep here is 0.25


# In[36]:


#numpy.logspace
# This function returns an ndarray object that contains the numbers that are evenly spaced
# on a log scale. Start and stop endpoints of the scale are indices of the base, usually 10.

#numpy.logscale(start, stop, num, endpoint, base, dtype)

# start
# The starting point of the sequence is basestart
# stop
# The final value of sequence is basestop
# num
# The number of values between the range. Default is 50
# endpoint
# If true, stop is the last value in the range
# base
# Base of log space, default is 10
# dtype
# Data type of output array. If not given, it depends upon other input
# arguments

import numpy as np
# default base is 10
a = np.logspace(1.0, 2.0, num=10)
print(a)


# In[37]:


# set base of log space to 2
import numpy as np
a = np.logspace(1,10,num=10, base=2)
print(a)


# In[39]:


#Basic Indexing
import numpy as np
a = np.arange(10)
s = slice(2,7,2)
print(a[s])
print(a)


# In[40]:


# slice single item
import numpy as np
a = np.arange(10)
b = a[5]
print(b)


# In[41]:


# slice items starting from index
import numpy as np
a = np.arange(10)
print(a[2:])


# In[42]:


# slice items between indexes
import numpy as np
a = np.arange(10)
print(a[2:5])


# In[44]:


import numpy as np
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
print(a[1:])


# In[45]:


# array to begin with
import numpy as np
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print('Our array is:')
print(a)
print('\n')
# this returns array of items in the second column
print('The items in the second column are:')
print(a[...,1])
print('\n')
# Now we will slice all items from the second row
print('The items in the second row are:')
print(a[1,...])
print('\n')
# Now we will slice all items from column 1 onwards
print('The items column 1 onwards are:')
print(a[...,1:])


# In[47]:


#Advance Indexing using Integer
import numpy as np
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0,1,2], [0,1,0]]
print(x)
print(y)


# In[48]:


#Advance Indexing using Integer
import numpy as np
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0,2], [0,1]]
print(x)
print(y)


# In[60]:


#Advance Indexing using Boolean
import numpy as np
x = np.array([[ 0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 10, 11]])
print('Our array is:')
print(x)
print('\n')
# Now we will print the items greater than 5
print('The items greater than 5 are:')
print(x[x>5])


# In[61]:


import numpy as np
a = np.array([np.nan, 1,2,np.nan,3,4,5])
print(a[~np.isnan(a)])


# In[62]:


import numpy as np
a = np.array([1, 2+6j, 5, 3.5+5j])
print(a[np.iscomplex(a)])


# In[63]:


#Broadcasting
import numpy as np
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a*b
print(c)


# In[64]:


import numpy as np
a = np.array([[ 0.0, 0.0, 0.0],[10.0,10.0,10.0],
[20.0,20.0,20.0],[30.0,30.0,30.0]])
b = np.array([1.0,2.0,3.0])
print('First array:')
print(a)
print('\n')
print('Second array:')
print(b)
print('\n')
print('First Array + Second Array')
print(a+b)


# In[65]:


import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('Original array is:')
print(a)
print('\n')
print('Modified array is:')
for x in np.nditer(a):
    print(x)


# In[66]:


import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('Original array is:')
print(a)
print('\n')
print('Transpose of the original array is:')
b = a.T
print(b)
print('\n')
print('Modified array is:')
for x in np.nditer(b):
    print(x)


# In[68]:


import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('Original array is:')
print(a)
print('\n')
print('Transpose of the original array is:')
b = a.T
print(b)
print('\n')
c = b.copy()
print(c)
for x in np.nditer(c):
    print(x)


# In[69]:


#numpy.reshape
# This function gives a new shape to an array without changing the data. It accepts the
# following parameters:
# numpy.reshape(arr, newshape, order)
# arr
# Array to be reshaped
# newshape
# int or tuple of int. New shape should be compatible to the original shape

import numpy as np
a = np.arange(8)
print('The original array:')
print(a)
print('\n')
b = a.reshape(4,2)
print('The modified array:')
print(b)
    


# In[72]:


#numpy.ndarray.flat
# This function returns a 1-D iterator over the array. It behaves similar to Python's built-in
# iterator.
import numpy as np
a = np.arange(8).reshape(2,4)
print('The original array:')
print(a)
print('\n')
print('After applying the flat function:')
# returns element corresponding to index in flattened array
print(a.flat[7])


# In[73]:


#numpy.ndarray.flatten
# This function returns a copy of an array collapsed into one dimension. The function takes
# the following parameters.
# ndarray.flatten(order)

import numpy as np
a = np.arange(8).reshape(2,4)
print('The original array is:')
print(a)
print('\n')
# default is column-major
print('The flattened array is:')
print(a.flatten())
print('\n')


# In[74]:


#numpy.ravel
# This function returns a flattened one-dimensional array. A copy is made only if needed.
# The returned array will have the same type as that of the input array. The function takes
# one parameter.
#numpy.ravel(a, order)
import numpy as np
a = np.arange(8).reshape(2,4)
print('The original array is:')
print(a)
print('\n')
print('After applying ravel function:')
print(a.ravel())


# In[75]:


#numpy.transpose
#numpy.transpose(arr, axes)
import numpy as np
a = np.arange(12).reshape(3,4)
print('The original array is:')
print(a)
print('\n')
print('The transposed array is:')
print(np.transpose(a))


# In[76]:


#numpy.concatenate
# Concatenation refers to joining. This function is used to join two or more arrays of the
# same shape along a specified axis.
# numpy.concatenate((a1, a2, ...), axis)
# a1,a2.. Sequence of arrays of the same type
# axis Axis along which arrays have to be joined. Default is 0
import numpy as np
a=np.array([[1,2],[3,4]])
print('First array:')
print(a)
print('\n')
b = np.array([[5,6],[7,8]])
print('Second array:')
print(b)
print('\n')
# both the arrays are of same dimensions
print('Joining the two arrays along axis 0:')
print(np.concatenate((a,b)))
print('\n')
print('Joining the two arrays along axis 1:')
print(np.concatenate((a,b),axis=1))


# In[77]:


#numpy.stack
# This function joins the sequence of arrays along a new axis. This function has been added
# since NumPy version 1.10.0.
# numpy.stack(arrays, axis)
# arrays
# Sequence of arrays of the same shape
# axis
# Axis in the resultant array along which the input arrays are stacked
import numpy as np
a = np.array([[1,2],[3,4]])
print('First Array:')
print(a)
print('\n')
b = np.array([[5,6],[7,8]])
print('Second Array:')
print(b)
print('\n')
print('Stack the two arrays along axis 0:')
print(np.stack((a,b),0))
print('\n')
print('Stack the two arrays along axis 1:')
print(np.stack((a,b),1))


# In[79]:


#numpy.hstack and numpy.vstack
import numpy as np
a = np.array([[1,2],[3,4]])
print('First array:')
print(a)
print('\n')
b = np.array([[5,6],[7,8]])
print('Second array:')
print(b)
print('\n')
print('Horizontal stacking:')
c = np.hstack((a,b))
print(c)
print('\n')
print('vrtical stacking:')
c = np.vstack((a,b))
print(c)


# In[81]:


#numpy.split
import numpy as np
a = np.arange(9)
print('First array:')
print(a)
print('\n')
print('Split the array in 3 equal-sized subarrays:')
b = np.split(a,3)
print(b)
print('\n')
print('Split the array at positions indicated in 1-D array:')
b = np.split(a,[2,7])
print(b)


# In[82]:


#numpy.hsplit and numpy.vsplit
# The numpy.hsplit is a special case of split() function where axis is 1 indicating a horizontal
# split regardless of the dimension of the input array.
# Similarly, numpy.vsplit is a special case of split() function where axis is 1 indicating a
# vertical split regardless of the dimension of the input array.

import numpy as np
a = np.arange(16).reshape(4,4)
print('First array:')
print(a)
print('\n')
print('Horizontal splitting:')
b = np.hsplit(a,2)
print(b)
print('\n')
print('Vertical splitting:')
b = np.vsplit(a,2)
print(b)


# In[83]:


#numpy.resize
# This function returns a new array with the specified size. If the new size is greater than
# the original, the repeated copies of entries in the original are contained.
# numpy.resize(arr, shape)

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print('First array:')
print(a)
print('\n')      
print('The shape of first array:')
print (a.shape)
print('\n')
b = np.resize(a, (3,2))
print('Second array:')
print(b)
print('\n')
print('The shape of second array:')
print(b.shape)
print('\n')


# In[84]:


#numpy.append
# This function adds values at the end of an input array. The append operation is not inplace,
# a new array is allocated. Also the dimensions of the input arrays must match
# otherwise ValueError will be generated.
# numpy.append(arr, values, axis)
# arr Input array
# values To be appended to arr. It must be of the same shape as of arr (excluding
# axis of appending)
# axis The axis along which append operation is to be done. If not given, both
# parameters are flattened

import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print('First array:')
print(a)
print('\n')
print('Append elements to array:')
print (np.append(a, [7,8,9]))
print('\n')
print('Append elements along axis 0:')
print(np.append(a, [[7,8,9]],axis=0))
print('\n')
print('Append elements along axis 1:')
print(np.append(a, [[5,5,5],[7,8,9]],axis=1))


# In[85]:


#numpy.insert
# This function inserts values in the input array along the given axis and before the given
# index. If the type of values is converted to be inserted, it is different from the input array.
# Insertion is not done in place and the function returns a new array. Also, if the axis is not
# mentioned, the input array is flattened.

# numpy.insert(arr, obj, values, axis)

# arr
# Input array
# obj
# The index before which insertion is to be made
# values
# The array of values to be inserted
# axis
# The axis along which to insert. If not given, the input array is flattened

import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
print('First array:')
print(a)
print('\n')
print('Axis parameter not passed. The input array is flattened before insertion.')
print(np.insert(a,3,[11,12]))
print('\n')
print('Axis parameter passed. The values array is broadcast to match input array.')
print('Broadcast along axis 0:')
print(np.insert(a,1,[11],axis=0))
print('\n')
print('Broadcast along axis 1:')
print(np.insert(a,1,11,axis=1))


# In[86]:


#numpy.delete
# This function returns a new array with the specified subarray deleted from the input array.
# As in case of insert() function, if the axis parameter is not used, the input array is flattened.

# Numpy.delete(arr, obj, axis)

# arr Input array
# obj
# Can be a slice, an integer or array of integers, indicating the subarray to
# be deleted from the input array
# axis
# The axis along which to delete the given subarray. If not given, arr is
# flattened

import numpy as np
a = np.arange(12).reshape(3,4)
print('First array:')
print(a)
print('\n')
print('Array flattened before delete operation as axis not used:')
print(np.delete(a,5))
print('\n')
print('Column 2 deleted:')
print(np.delete(a,1,axis=1))
print('\n')

