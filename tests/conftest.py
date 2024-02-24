from faker import Faker

fake = Faker()

def get_rand_vals():
    x = fake.random.randint(-100, 100)
    y = fake.random.randint(-100, 100)
    return x, y

def test_faker():
    pass

    