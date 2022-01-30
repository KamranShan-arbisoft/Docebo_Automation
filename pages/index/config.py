from faker import Faker
import json

# Opening JSON file
with open('/Users/hafizkamran/Documents/Docebo_Automation/common/fixtures/new_user_credentials.json', 'r') as new_user:
    # Reading from json file
    json_object = json.load(new_user)

# Install Faker Package and create it's instance
fake = Faker()
user_name = fake.name()
email = fake.email()
first_name = json_object["credentials"]["first_name"]
last_name = json_object["credentials"]["last_name"]
client_name = json_object["credentials"]["client_name"]
client_id = json_object["credentials"]["client_id"]
wave_cohort = json_object["credentials"]["wave_cohort"]
group_work = json_object["credentials"]["group_work"]
custom_field1 = json_object["credentials"]["custom_field1"]
