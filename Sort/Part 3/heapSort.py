import sys
sys.setrecursionlimit(10**9)

def heapify (a, h, m):
    v, j = a[h], 2*h
    while j <= m:
        if j < m and a[j] < a[j+1]:
            j += 1
        if v >= a[j]: break
        else:
            a[int(j/2)] = a[j]
        j *= 2
    a[int(j/2)] = v

def heapSort(a, n):
    for i in range(int(n/2),0,-1):
        heapify(a,i,n)
    for i in range(n-1,0,-1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify(a,1,i)


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

N=100000
a=[]
a.append(None)

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
heapSort(a,N)
end_time=time.time()-start_time
print('히프 정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
checkSort(a,N)    
