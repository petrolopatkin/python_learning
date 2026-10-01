# itertools module in python

import itertools
import operator

# itertools.count() method
# counter = itertools.count(start=5, step=-5)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

data = [100, 200, 300, 400, 500]

# itertools.count() with zip function
# daily_data = list(zip(itertools.count(), data))

# itertool.zip_longest method
daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)

# itertools.cycle method

# counter = itertools.cycle(('On', 'Off'))

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# itertools.repeat method

# counter = itertools.repeat(2, times=3)

# itertools.starmap method
# squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])

# print(list(squares))

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# itertools.combinations method

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3]
names = ['Peter', 'Corey']
true_false_age = [17, 16, 22, 10, 18, 20, 13]

selectors = [True, True, False, True, False, False, True]

result = itertools.combinations(letters, 2)

for item in result:
    print(item)

# itertools.permutation method

result2 = itertools.permutations(letters, 2)

for item in result2:
    print(item)

# itertools.product method

result3 = itertools.product(numbers, repeat=4)

for item in result3:
    print(item)

# itertools.combinations_with_replacement method

result4 = itertools.combinations_with_replacement(numbers, 4)

for item in result4:
    print(item)

# itertools.chain method

combined = itertools.chain(letters, numbers, names)

for item in combined:
    print(item)

# itertools.islice method

result5 = itertools.islice(range(10), 5)

for item in result5:
    print(item)

# itertools.compress method

result6 = itertools.compress(true_false_age, selectors)

for item in result6:
    print(item)

# itertools.accumulate method

result7 = itertools.accumulate(numbers, operator.mul)

for item in result7:
    print(item)

# itertools.groupby() method

def get_state(person):
    return person['state']


people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

person_group = itertools.groupby(people, get_state)

for key, group in person_group:
    print(key, len(list(group)))
    # for person in group:
    #     print(person)
    # print()

# itertools.tee (not sure how correctly use it)