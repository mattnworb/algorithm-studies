"""
This heapsort is pretty blatently copied from Wikipedia: http://en.wikipedia.org/wiki/Heapsort
Could be re-written.
"""

def heapsort(a):

	heapify(a, len(a))
	
	end = len(a) - 1
	while end > 0:
		#swap the max value in the heap with the last element
		swap(a, end, 0)
		#put the heap back in max-heap order
		siftdown(a, 0, end - 1)
		#decrease the size of the heap by one so previous value will stay in proper place
		end = end - 1
	
def heapify(a, count):
	start = (count - 2) / 2
	
	while start >= 0:
		#sift down the node at this index to it's proper place
		siftdown(a, start, count-1)
		start = start - 1
		
	#when we are done sifting we have a heap
		
		
def siftdown(a, start, end):
	root = start
	# while the root has one child
	while (root * 2 + 1) <= end:
		
		child = root * 2 + 1 # start at left child
		
		#if the child has a sibling and the child's value is less than the sibling
		if child < end and a[child] < a[child + 1]:
			child = child + 1 #point at right child instead
		if a[root] < a[child]:
			#swap the two
			swap(a, root, child)
			
			#sift down next child now
			root = child
		else: return
			
def swap(arr, a, b):
	""" Swaps the values in array arr at index a and b"""
	tmp = arr[a]
	arr[a] = arr[b]
	arr[b] = tmp