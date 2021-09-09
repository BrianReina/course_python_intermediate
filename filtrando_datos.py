DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run ():
    all_python_devs = [worked['name'] for worked in DATA if worked['language'] == 'python']
    all_platzi_workers = [worked['name'] for worked in DATA if worked['organization'] == 'Platzi']
    adults = list(filter(lambda worked: worked['age'] >18, DATA))
    adults = list(map(lambda worked: worked['name'],adults))
    old_people = list(map(lambda worked: worked | {'old': worked['age'] > 70}, DATA))

    #Challenge

    # #using filter and map
    # all_python_devs = list(filter(lambda worked: worked['language'] == 'python', DATA))
    # all_python_devs = list(map(lambda worked: worked['name'], all_python_devs))

    # all_platzi_workers = list(filter(lambda worked: worked['organization'] == 'Platzi', DATA))
    # all_platzi_workers = list(map(lambda worked: worked['name'], all_platzi_workers))

    # #using list comprehension
    # adults = [worked['name'] for worked in DATA if worked['age'] > 18]
    # old_people = [worked | {'old': worked['age'] > 70} for worked in DATA] 

    for worked in all_platzi_workers:
        print(worked)


if __name__ == '__main__':
    run()