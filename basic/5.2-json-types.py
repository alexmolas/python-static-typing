# Now let's use Pydantic for proper validation
import json
from pydantic import BaseModel, field_validator


class User(BaseModel):
    name: str
    age: int
    email: str

    @field_validator("email")
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Email must contain @")
        return v

    @field_validator("age")
    def validate_age(cls, v):
        if v < 0 or v > 130:
            raise ValueError(f"Age should be between 0 and 130, got {v}")
        return v


def compute_retirement_age(age: int) -> int:
    return 65 - age


def process_user_data(user: User):
    # Process validated data
    welcome_msg = f"Welcome {user.name}! We'll contact you at {user.email}"
    years_to_retirement = compute_retirement_age(user.age)

    return {"message": welcome_msg, "retirement_years": years_to_retirement}


with open("users.json", "r") as f:
    users = json.load(f)


for u in users:
    try:
        user = User(**u)
        r = process_user_data(user)
        print(r)

    except Exception:
        print(f"Got some problems processing user {user}")
