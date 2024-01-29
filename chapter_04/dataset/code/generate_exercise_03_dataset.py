import csv
import random
from faker import Faker

fake = Faker()

# Number of Henchclowns and Gotham Protectors
num_henchclowns = 50
num_protectors = 50

# Number of double agents (characters appearing in both lists)
num_double_agents = 14

# Generate random names for Henchclowns
henchclowns = [fake.first_name() for _ in range(num_henchclowns)]

# Generate random names for Gotham Protectors
protectors = [fake.first_name() for _ in range(num_protectors)]

# Select double agents randomly from both lists
double_agents = random.sample(henchclowns, num_double_agents)
double_agents += random.sample(protectors, num_double_agents)

# Shuffle the lists
random.shuffle(henchclowns)
random.shuffle(protectors)
random.shuffle(double_agents)

# Create a CSV file for Joker's Henchclowns
with open('jokers_henchclowns.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Character"])
    for character in henchclowns:
        writer.writerow([character])

# Create a CSV file for Gotham Protectors
with open('gotham_protectors.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Character"])
    for character in protectors:
        writer.writerow([character])

print("Datasets 'jokers_henchclowns.csv' and 'gotham_protectors.csv' generated successfully!")
