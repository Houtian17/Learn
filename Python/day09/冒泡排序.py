def double_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped=False
        for j in range(len(items)-1-i):
            if comp(items[j],items[j+1]):
                items[j],items[j+1]=items[j+1],items[j]
                swapped=True
        if not swapped:
            break
    return

