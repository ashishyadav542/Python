names = ['Ashish','Biswa','Tajendar','Bipul']
jobs = ['Infosys','Otis','Army','Navy']

#list....       names_jobs = list(zip(names,jobs))
#set.....       names_jobs = set(zip(names,jobs))
#dictionary...  names_jobs = dict(zip(names,jobs))

names_jobs = zip(names,jobs)

for names,jobs in names_jobs:
    print(names,jobs)