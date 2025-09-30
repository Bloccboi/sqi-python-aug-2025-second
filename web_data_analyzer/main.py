from data_processing.file_reader import read_data
from data_processing.web_fetcher import fetch_user_data

print("User data:")
print(read_data("data.txt"))

print("Usernames:")
print(fetch_user_data())