import sys
sys.setrecursionlimit(10**9)

def mergeSort(a,l,r):
    if r > l:
        mid = int((r+l)/2)
        mergeSort(a,l,mid)
        mergeSort(a,mid+1,r)
        for i in range(mid+1,l,-1):
            b[i-1]=a[i-1]
        i -= 1
        for j in range(mid, r):
            b[r+mid-j]=a[j+1]
        j += 1
        for k in range(l, r+1):
            if b[i] < b[j]:
                a[k] = b[i]
                i += 1
            else:
                a[k] = b[j]
                j -= 1
        

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

b=a.copy()
start_time=time.time()
mergeSort(a,1,N)
end_time=time.time()-start_time
print('합병정렬 실행시간 (N=%d) : %0.3f'%(N,end_time))
checkSort(a,N)    
