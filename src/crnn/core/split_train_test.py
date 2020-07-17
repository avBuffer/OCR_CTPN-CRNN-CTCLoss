import numpy as np

h1 = open('data/collect.txt', encoding='utf-8')
h2 = open('data/collect_train.txt', 'w', encoding='utf-8')
h3 = open('data/collect_test.txt', 'w', encoding='utf-8')

content = h1.readlines()
for line in content:
    if np.random.random()<0.05:
        h3.write(line)
    else:
        h2.write(line)
