import sys
sys.setrecursionlimit(10**7)

def insertionSort(a,l,r):
    for i in range (l+1, r+1):
        v, j = a[i], i
        while a[j-1] > v:
            a[j] = a[j-1]
            j-=1
        a[j] = v


def quickSort(a, l, r):
    if r-l <= M:
        insertionSort(a,l,r)
    else:
        v, i, j = a[r], l-1, r
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
        a[i], a[r] = a[r], a[i]
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)

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


N=250
M=15
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
print('작은 부분화일 고려한 퀵정렬 실행시간 (N=%d) : %0.6f'%(N,end_time))


