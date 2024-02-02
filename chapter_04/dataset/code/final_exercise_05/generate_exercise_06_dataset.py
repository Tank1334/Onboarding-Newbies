import random
import pandas as pd
from datetime import datetime, timedelta

# Seed for reproducibility
random.seed(0)

# Constants
num_records = 500000
districts = ['Gotham North', 'Gotham South', 'Gotham Central']
crime_categories = ['MISSING PERSON', 'THEFT', 'ASSAULT', 'VANDALISM', 'FRAUD']
crime_types = {
    'MISSING PERSON': ['MISSING ADULT', 'MISSING CHILD'],
    'THEFT': ['GRAND THEFT', 'PETTY THEFT'],
    'ASSAULT': ['AGGRAVATED', 'BATTERY'],
    'VANDALISM': ['GRAFFITI', 'PROPERTY DAMAGE'],
    'FRAUD': ['CREDIT CARD', 'IDENTITY THEFT']
}
crime_resolutions = ['ARREST, BOOKED', 'UNRESOLVED', 'FOUND PERSON']

# Helper function to generate a random date
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

# Generate data
data = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

for _ in range(num_records):
    crime_category = random.choice(crime_categories)
    crime_type = random.choice(crime_types[crime_category])
    crime_resolution = random.choice(crime_resolutions)
    date = random_date(start_date, end_date)
    record = {
        'CrimeID': random.randint(100000000, 999999999),
        'CrimeCategory': crime_category,
        'CrimeType': crime_type,
        'CrimeResolution': crime_resolution,
        'CrimeDate': date.strftime('%Y-%m-%d'),
        'CrimeDayOfWeek': date.strftime('%A'),
        'CrimeMonth': date.strftime('%B'),
        'Address': f"{random.randint(100, 999)} {random.choice(['Arkham St', 'Wayne Ave'])}",
        'Latitude': round(random.uniform(40.7000, 40.8000), 4),
        'Longitude': round(random.uniform(-74.0100, -73.9900), 4)
    }
    data.append(record)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('gotham_crime_data.csv', index=False)
