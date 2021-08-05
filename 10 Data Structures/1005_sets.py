# 1005_sets.py

asia = set(['Korea', 'China', 'Japan', 'Mongolia', 'Vietnam'])

print('India' in asia) # False
print('USA' not in asia) # True

asia.add('India')
print('India' in asia) # True

asia.add('North Korea')
print(asia)

olympic = asia.copy()
print(olympic)

olympic.remove('North Korea')
olympic.remove('Vietnam')
olympic.remove('Mongolia')

olympic.add('ROC')
asia.add('Russia')

print('Olympic is superset', olympic.issuperset(asia))
print('Olympic is subset', olympic.issubset(asia))

print('Countries in Asia & Olympics: ', (asia & olympic))
print('Countries NOT in both: ', (asia ^ olympic))







