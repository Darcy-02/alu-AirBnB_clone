#!/usr/bin/python3
"""Manual test for BaseModel"""

from models.base_model import BaseModel

# 1️⃣ Create instance
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89

# Print initial object (__str__ output)
print(my_model)

# 2️⃣ Call save() to update updated_at
my_model.save()
print(my_model)

# 3️⃣ Convert to dictionary (to_dict)
my_model_json = my_model.to_dict()
print(my_model_json)

# 4️⃣ Print JSON content with types
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
