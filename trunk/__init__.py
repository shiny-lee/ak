#!/user/bin/evn python3

import json, random

#read infile.txt
infile = open('infile.txt')
lines = infile.readlines()

infile.close()


#
map = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
maps = map.rsplit(',')

changestrat = []
for i in lines:
    changestrat.append(json.loads(i.strip()))

abchange1 = {}
abcount = {}
for i in range(0, len(changestrat)):
    ab = changestrat[i]
    abchange1[ab['class']] = 0
    abchange2 = {}
    for j in range(0, len(ab['fields'])):
        abchange2[ab['fields'][j]] = maps[j]
        abchange2['$'] = maps[j]
    abcount[ab['class'] + ab['subject']] = abchange2
    print(abchange2)
abchange = list(abchange1.keys())
print(abchange)
print(abcount)





#
php = open('ab.php', 'w')
php.write('<?php\n')

for i in range(0,len(abchange)):
    php.write("$ab['" + abchange[i] + "']=array(" + ");\n")

for i in range(0, len(changestrat)):
    ab = changestrat[i]
    abphp = str(abcount[ab['class'] + ab['subject']]).replace('{', '(').replace(':', '=>').replace('}', ')')
    php.write("$ab['" + ab['class'] +"']['" + ab['subject'] + "'] = array" + abphp + ";\n")

php.close()


#
js = open('ab.js', 'w')

for i in range(0,len(abchange)):
    js.write("ab['" + abchange[i] + "']={" + "};\n")

for i in range(0, len(changestrat)):
    ab = changestrat[i]
    js.write("ab['" + ab['class'] + "']['" + ab['subject'] + "']=" + str(abcount[ab['class'] + ab['subject']]) + ";\n")

js.close()