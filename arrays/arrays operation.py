a=[-1,5,3,2,1,0,7,6]
def maxavgsubarra(a,k):
  sum=0
  for i in range(k):
    sum+=a[i]
  maxavg=sum/k
  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]
    avg=sum/k
    if maxavg<avg:
      maxavg=avg
  print(maxavg)
a=maxavgsubarra(a,2)
a=[-1,5,3,2,1,0,7,6]
def maxavgsubarra(a,k):
  sum=0
  for i in range(k):
    sum+=a[i]
  maxavg=sum/k
  for i in range(k,len(a)):
    sum=sum+a[i]-a[i-k]
    avg=sum/k
    if maxavg>avg:
      maxavg=avg
  print(maxavg)
a=maxavgsubarra(a,2)
a=[1,2,3,4,5]
def search(el,a):
    for i in range(len(a)):
        if a[i]==el:
            print(f'{el} is found at {i} index')
            return
    print(f'{el} is not found')
a=search(2,a)

