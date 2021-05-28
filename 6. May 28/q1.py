names= ['alan', 'john', 'tania', 'ahmad', 'ali', 'muddassar', 'raheel', 'hamza']
age= [12,13,14,15,17,16,13,13]

data = list(map(lambda x, y: {'name': x, 'age': y}, names, age))

print(data)