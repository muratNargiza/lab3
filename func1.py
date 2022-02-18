#1
def myfunc(g):
    g = int(input())
    x = 28.3495231*g
    print(x)
myfunc(0)

#2
def myfunc(f):
    f = int(input())
    print((5/9)*(f - 32))
myfunc(0)

#3
def solve(numheads, numlegs): 
    for i in range(numheads): 
        for j in range(numheads): 
            if i + j == numheads and 2*i + 4*j == numlegs: 
                print(f'number of chickens - {i}') 
                print(f'number of rabbits - {j}') 
                return 


#4
def isPrime(n):
    if n<=1: return False
    for i in range(2, n/2+1):
        if n%i==0:
            return False
    return True

def Prime(l):
    p=[]
    for i in l:
        for j in i:
            if isPrime(j):
                p.append(j)
    return p

l=list(map(int,input().split()))
print(Prime(l))

#5

#6
def my_function(*w):
    w = list( input().split())
    w.reverse()
    print(*w)
my_function()

#7
def has_33(arr): 
    for i in range(len(arr)-1): 
        if arr[i] == 3 and arr[i+1] == 3: 
            return True 
    return False   

#8
def con_007(arr): 
    l = [] 
    for i in arr: 
        if i == 0 or i == 7: 
            l.append(i) 
 
    for i in range(len(l)-2): 
        if l[i] == 0 and l[i+1] == 0 and l[i+2] == 7: 
            return True   
 
    return False 
    
#9
import math
math.pi
pi = math.pi
def myfunc(r):
    r = int(input())
    x = pi*(4/3)
    v = x*(r**3)
    print(v)
myfunc(0)

#10
def unique_list(l):
    l = list(input().split())
    x = [ ]
    for i in l:
        if i not in x:
            x.append(i)
    return x
print(unique_list([]))

#11
def ispol(s): 
    if s == s[::-1]: 
        return True 
    return False 

#12
def func(arr): 
    for i in arr: 
        print('*' * i)