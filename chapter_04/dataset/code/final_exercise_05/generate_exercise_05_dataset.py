import random
import datetime

# List of possible HTTP request types
http_request_types = ["GET", "POST", "PUT", "DELETE"]

# List of Israeli news websites
israeli_news_websites = [
    "https://www.ynet.co.il",
    "https://www.haaretz.co.il",
    "https://www.ima.co.il",
    "https://www.jpost.com",
    "https://www.calcalist.co.il",
    "https://www.globes.co.il",
    "https://www.mako.co.il",
    "https://www.israelhayom.co.il",
]

# Generate a log file with random HTTP requests to Israeli news websites
log_file_path = "access.log"
num_requests = 1000

with open(log_file_path, 'w') as log_file:
    for _ in range(num_requests):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        http_request = random.choice(http_request_types)
        url = random.choice(israeli_news_websites)
        log_entry = f"{current_time} - Joker - {http_request} {url}\n"
        log_file.write(log_entry)

print(f"Log file '{log_file_path}' generated successfully with {num_requests} random HTTP requests to Israeli news websites.")
