# 1303_pickle.py

import pickle

lolchar_file = 'lolchar.data'
lolchar = ['Tank', 'Fighter', 'Slayer', 'Mage', 'Controller', 'Marksman']

# Write pickle
f = open(lolchar_file, 'wb')
pickle.dump(lolchar, f) # Make pickle
f.close()

# Delete lolchar
del lolchar

# Read pickle
f = open(lolchar_file, 'rb')
loldata = pickle.load(f)

print(loldata)
f.close()







