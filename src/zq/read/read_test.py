import json
fo = open("out.txt","w+")
file = '2020-01-01-0.json'
fin=open(file,'r')
line=fin.readlines()
fin.close()
data=[]
N = 34423
for i in range(0,N):
  str = json.loads(line[i])
  del str['payload']
  '''data.append(str)'''
  print(str,file =fo)
fo.close()
'''json.dump(data, open('data.json', 'w', encoding='utf-8'))'''