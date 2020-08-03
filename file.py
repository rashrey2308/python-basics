'''with open("doc1.txt", 'r+') as f:
    s=f.read()
    l=s.split(" ")
    l1=[x for x in l if x not in '!@#$%^&*"+-~']
    print(l1)
    f.write("Editing the file through python scripting, wohoooo!")
    f.seek(0,0)
    s=f.read()
    print(s)
    f.close()'''
import re
file_name = 'doc1.txt'
spacial_chr= '!@#$%^&*"+-~'
with open('doc1.txt', 'r+') as file:
    file = open(file_name, 'r+')
    cleaned=[]
    for line in file:
        line = re.sub(r"[^a-zA-Z0-9]+\s",' ',line).rstrip().split(' ')
        cleaned += [w for w in line if w != '']
    print(cleaned)
    file.write('Editing the file through python scripting, wohoooo!')
    print(file.read())     
