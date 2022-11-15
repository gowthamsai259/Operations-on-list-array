#operations on array
#inserting an element into an array into a specific place(method 1)
m = list(map(int,input("enter the elements into list: ").split()))
n = int(input("enter the element position that u want to insert:(method 1) "))
p = int(input("enter the element that u want to enter: "))
r = []
j = 1
for i in range(0,n):
    if j < n:
        r.append(m[i])
        j = j + 1
    elif j == n:
        r.append(p)
for k in range(n-1,len(m)):
    r.append(m[k])
print("your list after entering the element is: ",r)
#-----------------------------------------------------------
#inserting an element into the list/array (method 2)
n = int(input("enter the index of element: "))
m = int(input("enter the element: "))
r.insert(n,m) #syntax: list.insert(index,value)
print(r)
#-----------------------------------------------------------
#deleting the element from the list(method 1)
p = int(input("enter an element to delete from the list:(method 1) "))
y = []
a = 0
for i in range(len(r)):
    if p != r[i]:
        y.append(r[i])
        a = a + 1
if a == len(r) - 1:
    print("your list after deleting "+str(p)+"is: ")
    print(y)
else:
    print("element not in the list")
    print("but your final list is: ",y)
#------------------------------------------------------------
#method 2 for deleting the element from the list
p = int(input("enter an element to delete from the list:(method 2) "))
y.remove(p)
print("your array after deleting the element is: ",y)

#------------------------------------------------------------
#finding the maximum element in the list(method 1)
p = 0
for i in range(len(y)):
    if p < y[i]:
        p = y[i]
print("the maximum element present in the list is: ")
#-------------------------------------------------------------
#finding the maximum element in the list(method 2)
print(max(y))
#--------------------------------------------------------------
#concatenation of 2 lists(have many methods)
list1 = [1,2,4,5,6,7]
list2 = [2,5,8,11,13,15]
newlist = []
for i in list2:
    list1.append(i)
print("the final list after concatenation of 2 lists is: ",list1)
#--------------------------------------------------------------
#reversing a list(method 1)
m = [1,2,3,4,5,5,6]
m.reverse()
print(m)
#---------------------------------------------------------------
#reversing a list(method 2)
m = [1,2,3,4,5,6,6,7,8]
p = []
for i in range(len(m)-1,-1,-1):
    p.append(m[i])
print(p)
#----------------------------------------------------------------