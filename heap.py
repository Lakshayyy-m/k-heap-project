#need to define a heap data type that each parent can have k amount of children (arbitrary)
#we need push (add an element) pop (remove root element)
#some sort of heapify (turn list into a heap)
#some analysis of the complexity of the operations
#min heap (root is smallest) and max heap (root is largest)

heap = []

def _validate_k(k):
    if k < 2:
        raise ValueError("k must be greater or equal to 2")
    
# this will add an element to the heap and then move it to the correct position
def heappush(heap, x, k):
    _validate_k(k)
    heap.append(x)
    sift_up(heap, len(heap) - 1, k)

# this will remove the root element
def heappop(heap, k):
    _validate_k(k)

    if not heap:
        raise IndexError("heap is empty")
    
    root = heap[0]
    last = heap.pop()

    if heap:
        heap[0] = last
        sift_down(heap, 0, k)

    return root

# move an element into its proper position by swapping
def sift_up(heap, idx, k):
    global comparison_count
    newitem = heap[idx]
    while idx > 0:
        parent = (idx - 1) // k
        comparison_count += 1

        if newitem >= heap[parent]:
            break
        heap[idx] = heap[parent]
        idx = parent
    heap[idx] = newitem

def sift_down(heap, idx, k):
    global comparison_count
    lastidx = len(heap)
    newitem = heap[idx]

    child = k * idx + 1
    
    #while atleast 1 child exists
    #find smallest among k children
    while child < lastidx:
        minchild = child
        last = min(child + k, lastidx)
        for c in range(child + 1, last):
            comparison_count += 1
            if heap[c] < heap[minchild]:
                minchild = c

        comparison_count += 1  # Count comparison with current idx
        if heap[idx] <= heap[minchild]:
            break

        heap[idx] = heap[minchild]
        idx = minchild
        child = k * idx + 1

    heap[idx] = newitem
    sift_up(heap, idx, k)

#this will turn a list into a heap with up to k children for each node
#the parent index will be (n-1)/k 
def heapify(heap, k):
    _validate_k(k)
    n = len(heap)

    #start from the last parent and sift down to the root
    for i in reversed(range((n-1) // k + 1)):
        sift_down(heap, i, k)

comparison_count = 0

def reset_counter():
    global comparison_count
    comparison_count = 0

def get_comparison_count():
    return comparison_count

def is_min_heap(heap, k):
    for i in range(len(heap)):
        for c in range(1, k+1):
            child = k*i + c
            if child < len(heap) and heap[i] > heap[child]:
                return False
    return True

import random
data = [random.randint(0, 100) for _ in range(1000)]
reset_counter()
heapify(data, 3) 
print(f"Heapify comparisons: {get_comparison_count()}")
print(is_min_heap(heap, 3))