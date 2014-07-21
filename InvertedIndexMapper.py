'''
Created on 19-Mar-2014

@author: sudhanshu.gupta
'''

import sys
oldKey = None;
count = 0;
node = [];

for line in sys.stdin:
    data = line.strip().split('\t');
    if len(data) != 2:
        continue;
    thisKey, thisValue = data;

    if oldKey and oldKey != thisKey:
        print oldKey,"\t",",".join(node),"\t",count;
        count = 0;
        node = [];
        oldKey = thisKey;

    oldKey = thisKey;
    count += 1;
    node.append(int(thisValue));

if oldKey != None:
    print oldKey,"\t",",".join(node),"\t",count;
