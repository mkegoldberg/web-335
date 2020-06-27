
# == == == == == == == == == == == == == == == == == == == == == ==
# Title: Assignment 9.2
# Author: Mike Goldberg
# Date:  06/26/2020
# Description: Querying and Creating Documents
# == == == == == == == == == == == == == == == == == == == == == =

# start program

# expected output:

# generated ID - dynamic
# 'email': 'testy@test.com',
# 'employee_id': '1234567',
# 'first_name': 'John',
# 'last_name': 'Test'
# 'date_created': "2020, 6, 27"


from pymongo import MongoClient

import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client.web335

user = {
  "first_name": "John",
  "last_name": "Test",
  "email": "testy@test.com",
  "employee_id": "1234567",
  "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

# output
print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "1234567"}))

# end program
