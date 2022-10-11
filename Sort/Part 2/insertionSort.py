def insertionSort(a, n):
    for i in range (2, n+1):
        v, j = a[i], i
        while a[j-1] > v:
            a[j] = a[j-1]
            j-=1
        a[j] = v

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



N=40000
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
insertionSort(a,N)
end_time=time.time()-start_time
print('삽입정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
checkSort(a,N)    
