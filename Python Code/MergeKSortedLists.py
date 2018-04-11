import heapq
def MergeKSortedListsDivideandConquer(lists):
    if not lists: return None
    s = ListNode('0')

    while len(lists)>1:
        merged =[]
        while len(lists)>1:
            merged.append(merger(lists.pop(),lists.pop(),s))
        lists += merged
    return lists[0]


def merger(x,y,s):
    curr = s
    while x and y:
        if x.val <y.val:
            curr.next = x.val
            x = x.next

        else:
            curr.next = y.val
            y = y.next
        curr = curr.next
    curr.next = x if x else y
    return s.next



def MergeKSortedListsHeap(lists):
    heap=[]
    res =[]
    for i in lists:
        while i:
            heapq.heappush(heap,i.val)
            i = i.next
    while len(heap)>0:
        res.append(heapq.heahpop(heap))
    retrun res