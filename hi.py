def readlist(arr):
    for i in arr:
        if isinstance(i,list):
            readlist(i)
        else:
            print(i,end=" ")

def preorder(arr):
    temp = []
    for i in arr:
        if type(i) == list:
            temp.append(i)
        else:
            print(i,end=" ")
    if temp:
        for j in temp:
            preorder(j)

def postorder(arr):
    temp = []
    for i in arr:
        if type(i) != list:
            temp.append(i)
        else:
            postorder(i)
    if temp:
        for j in temp:
            print(j,end=" ")

def inorder(arr):
    temp = []
    count = 0
    temp2=[]
    for i in arr:
        if type(i) != list:
            temp.append(i)
        else:
            if count == 0:
                inorder(i)
            else:
                temp2.append(i)
            count +=1
    if temp:
        temp.reverse()
        for j in temp:
            print(j,end=" ")
    if temp2:
        for k in temp2:
            if len(k) <= 2:
                preorder(k)
            else:
                inorder(k)
i_dont_want_readlist = readlist
i_dont_want_readlist([1,2,3,4,5])
print()
def false():
    return True
it_is_false = false
print(it_is_false())
def it_is_my_addres():
    return it_is_my_addres
print(it_is_my_addres())
def i_dont_want_print_my_addres():
    print(i_dont_want_print_my_addres)
i_dont_want_print_my_addres()
def print_addres(addr):
    print(addr)
    return 0
print_addres(print)
print_addres(readlist)
print_addres(list)
print_addres(int)
print_addres([1,2,4,5,6])
arr = [readlist,preorder,inorder,postorder,print,print_addres]
def array(arr,num,arg):
    arr[num](arg)
    return 0
