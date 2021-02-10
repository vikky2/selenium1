a=[1,2,3,4,5]
b=a.copy()
print(b)
b=a[:]
print(b)
print(a)

names=['google', 'yahoo', 'facebook', 'messanger', 'twitter']
names.sort()
print(names)

names.sort(reverse=True)
print(names)

sorted(names)

sorted(names, reverse=True)
print(names)

names.index('google')
print(names)
print('yahoo' in names)
print(names)

# iterating over multiple lists simultaneously
cities=['tokyo', 'Delhi', 'shanghai', 'sao paulo', 'mumbai']
population=['38001000', '25703168', '23740778', '525894670']

for city, population in zip(cities, population):
    print(city, population)

# iterating through multiple lists woith un-equal length  using zip function
a=[1,2,3,4]
b=['v', 'w', 'x', 'y', 'z']

for i in zip(a,b):
    print(i)


a=[1,2,3]
b=['x', 'y', 'z']
c=['alpha', 'beta', 'gamma']

for i in zip(a,b,c):
    print(i)


files=['youtube.txt', 'amazon.pdf', 'facbook.pdf', 'google.pdf']
for file in files:
    if file.endwith('pdf'):
        print(file)
