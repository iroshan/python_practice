
def alphabetize_names(data):
    '''return the list of dicts, but sorted by last name and then by first name.'''
    data.sort(key= lambda x: [x['last'],x['first']] )
    return data



PEOPLE = [{'first':'Reuven', 'last':'Lerner',
'email':'reuven@lerner.co.il'},
 {'first':'Donald', 'last':'Trump',
'email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin',
'email':'president@kremvax.ru'}
]
print(alphabetize_names(PEOPLE))

