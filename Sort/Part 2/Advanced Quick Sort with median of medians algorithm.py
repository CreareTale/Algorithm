import sys
sys.setrecursionlimit(10**7)

def quickSort(a, l, r):
    if r-l > 1:
        mid = int((l+r)/2)
        if a[l] > a[mid]:
            a[l], a[mid] = a[mid], a[l]
        if a[mid] > a[r]:
            a[mid], a[r] = a[r], a[mid]
        if a[l] > a[mid]:
            a[l], a[mid] = a[mid], a[l]
        a[mid], a[r-1] = a[r-1], a[mid]
        v, i, j = a[r-1], l, r-1
        while True:
            i += 1
            while a[i] < v:
                i += 1
            j -= 1
            while a[j] > v:
                j-= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[i], a[r-1] = a[r-1], a[i]
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)
    elif a[l] > a[r]:
        a[l], a[r] = a[r], a[l]

def checkSort(a,n):
    isSorted=True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("Error")

import random, time

N=80000
a=[]
a.append(-1)

"""
print("배열이 무작위 원소를 가질 때")
for i in range(N):
    a.append(random.randint(1,N))

print("배열이 이미 정렬되었을 때")
for i in range(1, N+1):
    a.append(i)
"""

print("배열이 역순일 때")
for j in range(N, 0, -1):
    a.append(j)
    
start_time=time.time()
quickSort(a,1,N)
end_time=time.time()-start_time
print('중간값 분할  퀵정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
checkSort(a,N)    

