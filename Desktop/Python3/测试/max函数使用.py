testlist=[('123'),('1')]
print(testlist)
print(len(max((testlist),key=len).split()))
print(len(max(testlist,key=len)))
print(len(max(testlist,key=len).split()))
