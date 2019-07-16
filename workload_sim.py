from faker import Faker
import sys
import pickle
import random

fake = Faker()
nb = random.randint(200, 300)

data = fake.texts(nb_texts=nb, max_nb_chars=50000, ext_word_list=None)
print (len(data))
ii = random.randint(0, 1000)
outfile = 'C:\data\outfile{0}.dat'.format(ii)

with open(outfile, 'wb') as fp:
    pickle.dump(data, fp)
