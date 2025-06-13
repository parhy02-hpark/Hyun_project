# ASML: rotation implementation 

def rotate(list_l: list, n: int):
    newlist_l = list_l
    for i in range(n):
        sublist1 = newlist_l[0:-1]
        print(sublist1)
        sublist2 = newlist_l[-1:]
        print(sublist2)
        merge_list = sublist2 + sublist1
        print(merge_list)
        newlist_l = merge_list
        print(merge_list)
    return merge_list

num = 4

#assert rotate([1,4,9,11,16,25,36], num) == [36,1,4,9,11,16,25]

#assert rotate([1,4,9,11,16,25,36], num) == [25,36,1,4,9,11,16]

#assert rotate([1,4,9,11,16,25,36], num) == [16,25,36,1,4,9,11]

assert rotate([1,4,9,11,16,25,36], num) == [11,16,25,36,1,4,9]