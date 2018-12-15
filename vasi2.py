st='Print only the words that start with s in this sentence'
s=st.split()
print(s)
for i in s:
    if(i[0]=='s'):
        print(i)

for i in s:
    if(i.__len__()%2==0):
        print('even')
    else:
        print(i)

for i in range(0,10):
    if(i%2==0):
        print(i)

d=[s  for s in range(0,50) if (s%3==0)]
print(d)

for v in range(1,100):
    if(v%3==0):
        print('Fizz')
    elif(v%5==0):
        print('Buzz')
    else:
        print(v)

sb = 'Create a list of the first letters of every word in this string'
sv=sb.split()
c=[i[0] for i in sv]
print(c)
