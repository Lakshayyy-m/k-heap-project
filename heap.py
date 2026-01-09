#need to define a heap data type that each parent can have k amount of children (arbitrary)
#we need push (add an element) pop (remove root element)
#some sort of heapify (turn list into a heap)
#some analysis of the complexity of the operations
#min heap (root is smallest) and max heap (root is largest)

heap = []

# this will add an element to the heap and then move it to the correct position
def push(heap, x, k):
    heap.append(x)

    sift_up(heap, len(heap) - 1, k)

# this will remove the element (not started)
def pop(heap):
    return

# move an element into its proper position by swapping (not finished)
def sift_up(heap, idx, k):
    while idx > 0:
        parent = (idx - 1) // k

        if (heap[idx] >= heap[parent]):
            break
        heap[idx], heap[parent] = heap[parent], heap[idx]
