import json


def compute_retirement_age(age):
    return 65 - age


def process_user_data(user):
    welcome_msg = f"Welcome {user['name']}! We'll contact you at {user['email']}"
    years_to_retirement = compute_retirement_age(user["age"])

    return {"message": welcome_msg, "retirement_years": years_to_retirement}


with open("users.json", "r") as f:
    users = json.load(f)


for u in users:
    try:
        r = process_user_data(u)
        print(r)

    except Exception:
        print(f"Got some problems processing user {u}")
