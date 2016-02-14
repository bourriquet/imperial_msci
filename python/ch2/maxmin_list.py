def my_max(list):
    max_elem = list[0]
    for i in list[1:]:
        if i > max_elem:
            max_elem = i
    return max_elem

def my_min(list):
    min_elem = list[0]
    for i in list[1:]:
        if i < min_elem:
            min_elem = i
    return min_elem

a = [1,5,3,7,5,7,8,20,5]

print my_max(a)
print my_min(a)
