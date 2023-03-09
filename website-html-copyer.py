import requests
c = []
a = input('enter your link: ')
for i in range(len(a)):
    c.append(a[i])

if c[0] != 'h' and c[2] != 't' and c[3] != 't' and c[4] != 'p' and c[5] != 's' and c[6] != ':' and c[7] != '/' and c[8] != '/':
    a = 'https://'+ a

elif c[0] != 'h' and c[2] != 't' and c[3] != 't' and c[4] != 'p' and c[5] != 's' and c[6] != ':' and c[7] != '/' and c[8] != '/' and d[9] != 'w' and d[10] != 'w' and d[11] != 'w' and d[12] != '.':
    a = "https://www."+ a

b = requests.get(a)
a = open('website_codes.txt','w')
a.write(b.text)

print(b.text)