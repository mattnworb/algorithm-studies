"""
I have an continous integer array starting from 1. For example

1, 2, 3, 4.

First I reordered them, then I replaced one of the integer with another one in the range.

So, you end up with something like:

3, 1, 3, 2.

Write a program prints out the missing number and the duplicate number. Assume this is a giant array, we don't luxary to duplicate the array. (Memory issue). 

The order in the original order is not important to our business, so you can reorder them.
"""

from sorting import heapsort

def findMissingAndDuplicate(arr):

	heapsort.heapsort(arr)
	for i in xrange(len(arr)):
		#if the value is ok, the value at index i should be (i+1)
		if arr[i] != (i + 1):
			#duplicate is the value in this slot, missing is (i + 1)
			d = arr[i]
			m = i + 1
			return m, d
	

	
if __name__ == '__main__':
	
	def output(a):
		print '\nStarting array: ', a
		missing, duplicate = findMissingAndDuplicate(a)
		print 'Missing number: ', missing
		print 'Duplicate number: ', duplicate

	output([3, 1, 3, 4])
	output([7, 1, 3, 4, 2, 6, 6])
	