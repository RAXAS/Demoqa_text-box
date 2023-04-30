from data.data import Person
from faker import Faker

fake = Faker()


def generated_person():
    return Person(
        full_name=fake.name(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address()
    )
