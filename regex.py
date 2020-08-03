import re
textStr = "From john.doe@ab.etc Thu Jun 15 02:04:09 2010"
result = re.findall(r'@\S*', textStr)
for x in result:
    print(x.replace('@',''))

result = re.findall(r'\S+@\S+', textStr)
print(result)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

MathScores = '''
Ann got 99 and Maria got 95,
David got 84 and Jose got 21
'''
scores = re.findall(r'\d{1,3}', MathScores)
names = re.findall(r'[A-Z][a-z]*',MathScores)
print(scores)
print(names)
scoreDict = {}
x = 0
for eachname in names:
    scoreDict[eachname] = scores[x]
    x+=1
print(scoreDict)
