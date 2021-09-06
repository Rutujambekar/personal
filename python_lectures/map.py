# def square(num):
#     return num**2
# list1=[1,2,3,4,5]

# new_list=list(map(square,list1))
# print(new_list)
#---------------------------------

names=['sham','sonu','ram','sam']

def even_odd(name):
    if(len(name)%2==0):
        return 'even'
    else:
        return name[0]
a=list(map(even_odd,names))
print(a)    