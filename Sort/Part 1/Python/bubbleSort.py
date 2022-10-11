"""

bubbleSort(a[n], n)
    for (i<-n; i==1; i<-i-1) do {
        for (j<-1; j<i; j<-j+1) do {
            if (a[j] > a[j+1]) then
                a[j+1]와 a[j]를 교환;
end bubbleSort()


"""

def bubbleSort(a, n):
    for i in range(n, 0, -1):
        for j in range(1, i):
            if (a[j] > a[j+1]): a[j+1],a[j]=a[j],a[j+1]




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
        print("정렬 오류 발생")

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
bubbleSort(a, N)
end_time = time.time() - start_time
print('버블 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
checkSort(a, N)
