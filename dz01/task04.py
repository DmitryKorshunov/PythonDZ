#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

print('введите длину шоколадки в дольках')
n = int(input())

print('введите ширину шоколадки в дольках')
m = int(input())

print('введите колличество долек которые нужно отломить')
k = int(input())

p1 = k % n
p2 = k % m

if p1 == 0 and k!=n*m:
    print('yes') 
elif p2 ==0 and k!=n*m:
    print('yes')
else:
    print('no')