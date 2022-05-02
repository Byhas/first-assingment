testList =['Network','Math','Programming','Physics','Music']
findP = 'P'
print("the list:"+str(testList))
res = [idx for idx in testList if idx[0].lower() == findP.lower()]
print("the list of matching first letter:" + str(res))