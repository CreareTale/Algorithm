"""
3-(1)

selectionSort(a[n],n)
    for(i<-1; i<n; i<-i+1) do {
        min <- i;
        for(j<-1; j<=n; j<-j+1) do {
            if (a[j+1] < a[j]) then
                min <- j;
            a[min]과 a[j]를 교환
        }
    }
end selectionSort()


"""

import sys
sys.setrecursionlimit(10**7)

def selectionSort(a, n):
    for i in range(1,n):
        minI= i
        for j in range(i+1,n+1):
            if a[minI] > a[j]:
                minI=j
            a[minI], a[j] = a[j], a[minI]


def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 완료")

import random, time

N = 20000
a = []
a.append(None)

"""
print("배열이 무작위 원소를 가질 때")
for i in range(N):

print("배열이 이미 정렬되었을 때")
for i in range(1, N+1):
    a.append(i)
"""
print("배열이 역순일 때")
for j in range(N, 0, -1):
    a.append(j)

start_time = time.time()
selectionSort(a, N)
end_time = time.time() - start_time
print('선택 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
checkSort(a, N)
        

