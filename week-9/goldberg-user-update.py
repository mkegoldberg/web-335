
# == == == == == == == == == == == == == == == == == == == == == ==
# Title: Assignment 9.3
# Author: Mike Goldberg
# Date:  06/26/2020
# Description: Updating and Deleting Documents
# == == == == == == == == == == == == == == == == == == == == == =

# start program

# expected output:

# "email": "migoldberg@my365.bellevue.edu"
# "employee_id": "1234567"
# "first_name": "John"
# "last_name" "Test"


from pymongo import MongoClient

import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client.web335

db.users.update_one(
    {"employee_id": "1234567"},
  {
    "$set": {
        "email": "migoldberg@my365.bellevue.edu"
    }
  }
)

# output
pprint.pprint(db.users.find_one(
  {"employee_id": "1234567"},
  {
    "email": "1",
    "employee_id": "1",
    "first_name": "1",
    "last_name": "1"
  }
))

# end program
