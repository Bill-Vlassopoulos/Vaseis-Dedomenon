import sqlite3
import random
from faker import Faker

fake = Faker()


# Συνάρτηση για τη δημιουργία ψευδοδεδομένων για κάθε πίνακα
def generate_dummy_data(table_name, num_rows=5):
    dummy_data = []
    for _ in range(num_rows):
        if table_name == "PELATIS":
            dummy_data.append(
                (
                    None,
                    fake.first_name(),
                    fake.last_name(),
                    fake.phone_number(),
                    fake.email(),
                )
            )
        elif table_name == "KRATISI":
            dummy_data.append(
                (
                    None,
                    fake.date_time_this_year(),
                    fake.date_time_this_year(),
                    random.randint(1, 5),
                )
            )
        elif table_name == "TRAPEZI":
            dummy_data.append(
                (None, fake.word(), random.randint(2, 8), random.randint(1, num_rows))
            )
        elif table_name == "KRITIKI":
            dummy_data.append(
                (
                    None,
                    fake.random_int(1, 5),
                    fake.text(),
                    fake.date_time_this_year(),
                    random.randint(1, num_rows),
                )
            )
        elif table_name == "PARAGGELIA":
            dummy_data.append(
                (
                    None,
                    fake.date_time_this_year(),
                    random.uniform(5.0, 50.0),
                    random.randint(1, num_rows),
                )
            )
        elif (
            table_name == "MAGEIRAS"
            or table_name == "SERVITOROS"
            or table_name == "PROMITHEYTIS"
        ):
            dummy_data.append(
                (
                    random.randint(100000, 999999),
                    fake.first_name(),
                    fake.last_name(),
                    random.randint(1000, 5000),
                    fake.phone_number(),
                    fake.time(),
                )
            )
        elif table_name == "YLIKA":
            dummy_data.append((None, fake.word(), fake.word(), random.randint(10, 100)))
        elif table_name == "FAGITO" or table_name == "POTO":
            dummy_data.append(
                (
                    None,
                    fake.word(),
                    random.uniform(5.0, 20.0),
                    random.randint(1, 50),
                    fake.sentence(),
                )
            )
        elif table_name == "PARASKEYAZEI":
            dummy_data.append(
                (random.randint(100000, 999999), random.randint(1, num_rows))
            )
        elif table_name == "APOTELEITAI":
            dummy_data.append(
                (random.randint(1, num_rows), random.randint(1, num_rows))
            )
        elif table_name == "PERILAMBANEI":
            dummy_data.append(
                (random.randint(1, num_rows), random.randint(1, num_rows))
            )
        elif table_name == "ANALAMBANEI":
            dummy_data.append(
                (random.randint(1, num_rows), random.randint(100000, 999999))
            )
        elif table_name == "EFODIAZEI":
            dummy_data.append(
                (random.randint(100000, 999999), random.randint(1, num_rows))
            )
        elif table_name == "PROMITHEVEI":
            dummy_data.append(
                (
                    random.randint(100000, 999999),
                    random.randint(1, num_rows),
                    fake.date_time_this_year(),
                )
            )

    return dummy_data


# Σύνδεση στη βάση
conn = sqlite3.connect("SmartRestaurant.db")
cursor = conn.cursor()

# Ονόματα πινάκων στη βάση
table_names = [
    "PELATIS",
    "KRATISI",
    "TRAPEZI",
    "KRITIKI",
    "PARAGGELIA",
    "MAGEIRAS",
    "SERVITOROS",
    "PROMITHEYTIS",
    "YLIKA",
    "FAGITO",
    "POTO",
    "PARASKEYAZEI",
    "APOTELEITAI",
    "PERILAMBANEI",
    "ANALAMBANEI",
    "EFODIAZEI",
    "PROMITHEVEI",
]

# Δημιουργία αρχείου txt
with open("dummy_data.txt", "w") as file:
    for table_name in table_names:
        dummy_data = generate_dummy_data(table_name)
        file.write(f"--- {table_name} ---\n")
        for row in dummy_data:
            file.write(str(row) + "\n")

# Κλείσιμο σύνδεσης
conn.close()
