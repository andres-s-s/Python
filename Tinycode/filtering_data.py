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



python_developers = list(  map(  lambda x: x["name"] , filter(  lambda x: x["language"] == "python" , DATA  )  )  )

platzi_people = list( filter( lambda x: x["organization"] == "Platzi" ,DATA  )  )

adults = [i["name"] for i in DATA if i["age"] > 20]

true_false_old = list( map(  lambda x : x | { "old" : x["age"] > 50 } , DATA  )  )
#true_false_old = [ x | { "old" : x["age"] > 50 }  for x in DATA  ]

print("python_developers:  " , python_developers , "\n")
print("platzi_people:  " , platzi_people , "\n" )
print("adults:  " , adults , "\n" )
print("true_false_old:  " , true_false_old , "\n" )
