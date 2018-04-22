import heapq
def mergeKLists(lists):
    heap = []
    for linkedlists in lists:
        for nodes in linkedlists:
            heapq.heappush(heap,nodes)
    
    head = None
    curr = head
    while heap:
        if not curr:
            curr = heapq.heappop(heap)
        else:
            curr.next = 