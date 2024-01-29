import random
import string
from faker import Faker
import datetime

fake = Faker()

# Function to generate a random email address
def generate_random_email():
    username = fake.user_name()
    domain = fake.domain_name()
    
    return f"{username}@{domain}"

# Function to generate a random timestamp
def generate_random_timestamp():
    random_date = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

# Function to generate a fake email message as a CSV row
def generate_fake_spam_email():
    email = generate_random_email()
    name = fake.name()
    message = fake.paragraph()
    timestamp = generate_random_timestamp()
    
    return f"{name},{email},{timestamp},{message}\n"

# Function to generate a fake spam dataset in CSV format with specific percentages
def generate_fake_spam_dataset(output_file, total_emails):
    data = []  # Store the generated data in memory
    
    # Define the percentages for each email source
    email_sources = {
        generate_random_email(): 0.20,
        generate_random_email(): 0.15,
        generate_random_email(): 0.10,
        generate_random_email(): 0.02
    }
    
    # Calculate the number of emails for each source based on percentages
    num_emails_per_source = {source: int(total_emails * percentage) for source, percentage in email_sources.items()}
    
    # Generate emails for predefined sources
    for source, num_emails in num_emails_per_source.items():
        for _ in range(num_emails):
            fake_email = generate_fake_spam_email()
            data.append(fake_email)
    
    # Generate emails for random sources to fill the remaining percentage
    remaining_emails = total_emails - sum(num_emails_per_source.values())
    for _ in range(remaining_emails):
        random_email = generate_fake_spam_email()
        data.append(random_email)
    
    # Shuffle the data in memory
    random.shuffle(data)
    
    # Write the shuffled data to the output file
    with open(output_file, 'w') as f:
        f.write("Name,Email,Time,Message\n")  # Header row
        f.writelines(data)

if __name__ == "__main__":
    output_file = "fake_spam_dataset.csv"  # Specify the output file name
    total_emails = 500  # Specify the total number of fake spam emails
    
    generate_fake_spam_dataset(output_file, total_emails)
