# -*- coding: utf-8 -*-
"""Copy of Day2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1riupOUovyrsd3WttQMrTxu9ssONvLWhP

### Question_1 LISt
1.append()   
2.insert()  
3.pop()  
4.max()   
5.min()
"""

L=[1,6,45,3,9,5]
L.append(51)
print(L)

L.insert(2,4)
print(L)

L.pop()

max(L)

min(L)

"""###  Question_2 DICTIONARY
1.keys()   
2.items()  
3.values()  
4.update()   
5.clear()
"""

D={"rool_no":552,"name":"Ramya","branch":"CSE","college":"UCET"}
K=D.keys()
print(K)

I=D.items()
print(I)

V=D.values()
print(V)

X={"city":"Guntur"}
D.update(X)
print(D)

D.clear()
print(D)

"""### Questions_3 SET
1.uinion()    
2.intersection()   
3.difference()   
4.discard()   
5.symmetric_difference()
"""

S={8,9,3,6,10}
X={1,2,3,4,5,6}
U=S.union(X)
print(U)

I=S.intersection(X)
print(I)

D=S.difference(X)
print(D)

S.discard(10)
print(S)

s=S.symmetric_difference(X)
print(s)

"""### Question_4 TUPLE
1.min()   
2.max()   
3.count()  
4.index()  
5.sorted()
"""

T=(42,49,23,30,55,23)
print(min(T))

print(max(T))

print(T.count(23))

print (T.index(23))

print(sorted(T))

"""###Question_5 STRING
1.isalnum()   
2.isalpha()   
3.decimal()   
4.digit()   
5.replace()
"""

S="apple142396"
s=S.isalnum()
print(s)
A="apple"
a=A.isalnum()
print(a)
n="12357 abc"
print(n.isalnum())
X="12389"
print(X.isalnum())

print(S.isalpha())
print(A.isalpha())
print(n.isalpha())
print(X.isalpha())

print(S.isdecimal())
print(A.isdecimal())
print(n.isdecimal())
print(X.isdecimal())

print(S.isdigit())
print(A.isdigit())
print(n.isdigit())
print(X.isdigit())

f='let us do ,let us do ,let us do'
f.replace('let us','let we')
print(f)

