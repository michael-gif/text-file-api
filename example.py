import crossfile

cf = crossfile.Crossfile('database.txt')
cf.post('resource1', 'blueberry')
cf.post('resource2', 'table')
cf.post('resource3', 'orange')
print(cf.get())
cf.delete('resource1')
print(cf.get())
