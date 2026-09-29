# collection module in python
#imports
from collections import Counter
from collections import namedtuple
from collections import defaultdict
from collections import deque
#counter method

a = "aaabbbbcccccddfffff"
my_count = Counter(a)
print(my_count)
print(my_count.most_common(1))
print(list(my_count.elements()))

#namedtuple method

Point = namedtuple('Point', 'x,y')
pt = Point(6, 7)
print(pt.x, pt.y)

# defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print(d['c'])

# deque method

d = deque()

d.append(1)
d.append(2)
d.append(3)

print(d)

d.appendleft(4)

print(d)

d.popleft()

print(d)

d.extend([4, 5, 6])

print(d)