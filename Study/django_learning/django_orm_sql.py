from weather.models import SavedCity
# ==================================================
# DJANGO ORM → SQL
# ==================================================


# --------------------
# SELECT *
# --------------------

# Django ORM:
SavedCity.objects.all()

# SQL:
# SELECT * FROM weather_savedcity;


# --------------------
# WHERE
# --------------------

# Django ORM:
SavedCity.objects.filter(name="Paris")

# SQL:
# SELECT *
# FROM weather_savedcity
# WHERE name = 'Paris';


# --------------------
# WHERE + LIKE
# --------------------

# Django ORM:
SavedCity.objects.filter(name__startswith="P")

# SQL:
# SELECT *
# FROM weather_savedcity
# WHERE name LIKE 'P%';


# --------------------
# CONTAINS
# --------------------

# Django ORM:
SavedCity.objects.filter(name__icontains="a")

# SQL:
# SELECT *
# FROM weather_savedcity
# WHERE name LIKE '%a%';


# --------------------
# SELECT specific columns
# --------------------

# Django ORM:
SavedCity.objects.values("name")

# SQL:
# SELECT name
# FROM weather_savedcity;


# --------------------
# ORDER BY
# --------------------

# Django ORM:
SavedCity.objects.all().order_by("name")

# SQL:
# SELECT *
# FROM weather_savedcity
# ORDER BY name;


# --------------------
# ORDER BY DESC
# --------------------

# Django ORM:
SavedCity.objects.all().order_by("-name")

# SQL:
# SELECT *
# FROM weather_savedcity
# ORDER BY name DESC;


# --------------------
# Get one object instead of a query
# --------------------

#Django ORM:
SavedCity.objects.get("name = Paris")

#SQL:
# SELECT *
# FROM weather_savedcity
# WHERE name='Paris'

# Get await only for one object. IF object hasn't been found => DoesNotExist

# --------------------
# EXCLUDE - exclude an object from the query
# --------------------
SavedCity.objects.exclude("name = Paris")

# SQL:
# SELECT *
# FROM weather_savedcity
# WHERE name != 'Paris'

# --------------------
# COUNT - count of objects
# --------------------
SavedCity.objects.count()

# SQL:
# SELECT 
# COUNT(*)
# FROM weather_savedcity

# --------------------
# FILTER + COUNT
# --------------------
SavedCity.objects.filter("name__icontains=a").count()

# SQL:
# SELECT 
# COUNT(*)
# FROM weather_savedcity
# WHERE name LIKE %a%

# --------------------
# View Generated SQL
# --------------------
queryset = SavedCity.objects.filter("name__icontains=a")

print(queryset)

# SQL:
# SELECT 
# weather_savedcity.id,
# weather_savedcity.name
# FROM weather_savedcity
# WHERE weather_savedcity.name LIKE %a%

# ==================================================

# Q OBJECTS — OR / AND / NOT

# ==================================================

from django.db.models import Q

# --------------------

# OR

# --------------------

SavedCity.objects.filter(
Q('name=Paris') | Q('name=Berlin')
)

# SQL:

# SELECT *

# FROM weather_savedcity

# WHERE name = 'Paris'

# OR name = 'Berlin';

# --------------------

# AND

# --------------------

SavedCity.objects.filter(
Q("name__icontains=a") &
 Q("name__startswith=L")
 )

# SQL:

# SELECT *

# FROM weather_savedcity

# WHERE name LIKE '%a%'

# AND name LIKE 'L%';

# --------------------

# NOT

# --------------------

SavedCity.objects.filter(
 ~Q("name=Paris")
 )

# SQL:

# SELECT *

# FROM weather_savedcity

# WHERE NOT name = 'Paris';

# ==================================================

# IN

# ==================================================

# --------------------

# IN

# --------------------

SavedCity.objects.filter(
 "name__in=[Paris, Madrid, Dresden]"
)

# SQL:

# SELECT *

# FROM weather_savedcity

# WHERE name IN ('Paris', 'Madrid', 'Dresden');

# ==================================================

# CREATE / UPDATE / DELETE

# ==================================================

# --------------------

# CREATE — create an object

# --------------------

SavedCity.objects.create(
 "name=Vienna"
 )

# SQL:

# INSERT INTO weather_savedcity (name)

# VALUES ('Vienna');

# create() returns created object.

# --------------------

# UPDATE — change an object

# --------------------

SavedCity.objects.filter(
"name=Dresden"
).update(
 "name=Dresden City"
)

# SQL:

# UPDATE weather_savedcity

# SET name = 'Dresden City'

# WHERE name = 'Dresden';

# update() return all changed rows.

# Example:

# Out: 1

# --------------------

# DELETE — delete an object

# --------------------
SavedCity.objects.filter(
"name=Dresden City"
).delete()

# SQL:

# DELETE FROM weather_savedcity

# WHERE name = 'Dresden City';

# delete() returns information about objects

# and all deleted objects.

# --------------------

# GET_OR_CREATE

# --------------------

city, created = SavedCity.objects.get_or_create(
"name=Paris"
)

# If object exists:

# city    → found object

# created → False

# IF object doesn't exist:

# city    → created object

# created → True

# Steps:

# 1. Try to find an object

# 2. If not => create an object

# SQL:

# SELECT ...

# WHERE name = 'Paris';

# If object not found:

# INSERT INTO weather_savedcity (name)

# VALUES ('Paris');

# get_or_create() returns tuple:

# (object, created)

# ==================================================

# FIRST / LAST

# ==================================================

# --------------------

# FIRST — first object

# --------------------

SavedCity.objects.all().first()

# Returns the first object from the QuerySet.

# SQL idea:

# SELECT *

# FROM weather_savedcity

# LIMIT 1;

# --------------------

# LAST — last object

# --------------------

SavedCity.objects.all().last()

# Returns the last object from the QuerySet.

# SQL idea:

# SELECT *

# FROM weather_savedcity

# ORDER BY id DESC

# LIMIT 1;

# --------------------

# FIRST + FILTER

# --------------------

SavedCity.objects.filter(
"name__icontains=a"
).first()

# SQL idea:

# SELECT *

# FROM weather_savedcity

# WHERE name LIKE '%a%'

# LIMIT 1;

# --------------------

# LAST + FILTER

# --------------------

SavedCity.objects.filter(
"name__startswith=L"
).last()

# SQL idea:

# SELECT *

# FROM weather_savedcity

# WHERE name LIKE 'L%'

# ORDER BY id DESC

# LIMIT 1;

# --------------------

# FIRST + ORDER_BY

# --------------------

SavedCity.objects.filter(
"name__icontains=a"
).order_by("name").first()

# Returns the first object alphabetically.

# SQL:

# SELECT *

# FROM weather_savedcity

# WHERE name LIKE '%a%'

# ORDER BY name

# LIMIT 1;

# If no objects are found:

# first() / last() → None

# Aggregates

from django.db.models import Count, Max, Min, Avg, Sum

# Count

SavedCity.objects.aggregate(total=Count("id"))

# → {'total': 7}

# SQL:

# SELECT COUNT(id)

# FROM weather_savedcity;

# Max / Min

SavedCity.objects.aggregate(
"max_id=Max(id)",
"min_id=Min(id)"
)

# → {'max_id': 8, 'min_id': 1}

# SQL:

# SELECT MAX(id), MIN(id)

# FROM weather_savedcity;

# Avg

SavedCity.objects.aggregate(avg_id=Avg("id"))

# → {'avg_id': 4.2857}

# SQL:

# SELECT AVG(id)

# FROM weather_savedcity;

# Sum

SavedCity.objects.aggregate(total_id=Sum("id"))

# → {'total_id': Decimal('30')}

# SQL:

# SELECT SUM(id)

# FROM weather_savedcity;

# Multiple aggregates

SavedCity.objects.aggregate(
"total=Count(id)",
"max_id=Max(id)",
"min_id=Min(id)",
"avg_id=Avg(id)",
"sum_id=Sum(id)"
)

# → one dictionary with all results

# Important:

# aggregate() returns one overall result for the entire QuerySet.

# count() → 7

# aggregate(total=Count("id")) → {'total': 7}

# Count → number of records

# Max   → maximum value

# Min   → minimum value

# Avg   → average value

# Sum   → sum of values

# Avg/Sum/Max/Min are usually more useful with meaningful

# numeric fields such as price, quantity, salary, rating, etc.

# Using them with id here is only for learning the syntax.

# annotate()

# Add a calculated value to each object

from django.db.models.functions import Length

SavedCity.objects.annotate(
"name_length=Length(name)"
).values("name", "name_length")

# → <QuerySet [

# {'name': 'Paris', 'name_length': 5},

# {'name': 'Berlin', 'name_length': 6},

# {'name': 'London', 'name_length': 6},

# ...

# ]>

# SQL:

# SELECT

# name,

# LENGTH(name) AS name_length

# FROM weather_savedcity;

# annotate() vs aggregate()

# aggregate() → one overall result for the entire QuerySet

SavedCity.objects.aggregate(total=Count("id"))

# → {'total': 7}

# annotate() → adds a calculated value to each object/group

SavedCity.objects.annotate(
name_length=Length("name")
)

# → each SavedCity gets a calculated name_length

# annotate() with Count()

# Commonly used with related models.

# Example:

#Customer.objects.annotate(
# order_count=Count("orders")
# )

# → each Customer gets its own order_count

# SQL roughly:

# SELECT

# customer.name,

# COUNT(orders.id)

# FROM customer

# LEFT JOIN orders

# ON orders.customer_id = customer.id

# GROUP BY customer.name;

# Main idea:

# aggregate()

# ↓

# whole QuerySet

# ↓

# one result

# annotate()

# ↓

# each object / group

# ↓

# calculated value

# annotate(Count(...)) is commonly used

# for GROUP BY-like queries in Django ORM.