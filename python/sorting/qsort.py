def simplesort(array):
     #base case
     if len(array) <= 1: return array
     
     less = [], greater = []
     pivot = len(array) / 2
     for x in xrange(array):
          if x <= array[pivot]:
               less.append(x)
          else:    
               greater.append(x)
     return qsort(less) + array[pivot] + qsort(greater)

#in place partitioning:
def sort(array):
     quicksort(array, 0, len(array) - 1)

def quicksort(array, left, right):
     if (left < right):
          p = partition(array, left, right)
          quicksort(array, left, p - 1)
          quicksort(array, p + 1, right)

def partition(array, left, right):
     #select midpoint as pivot
     p = left + ((right - left) / 2)
     swap(array, p, right)
     store = left
     for i in xrange(left, right):
          if array[i] < array[right]:
               swap(array, i, store)
               store += 1	
     swap(array, store, right)
     return store
          

def swap(array, a, b):
     tmp = array[a]
     array[a] = array[b]
     array[b] = tmp
	 
	 
if __name__ == '__main__':
	a = [1, 4, 5, 3, 2]
	print a
	sort(a)
	print a
	
	a = [6, 5, 3, 1, 4, 2, 7]
	print a
	sort(a)
	print a