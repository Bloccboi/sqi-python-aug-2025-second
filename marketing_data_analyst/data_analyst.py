import re 
with open("reviews.txt", "r", encoding="utf-8") as file:
            content = file.read()
            email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            phone_pattern = r"\+234\s\d{3}\s\d{3}\s\d{4}"
            emails = re.findall(email_pattern,content)
            phone_no = re.findall(phone_pattern,content)

with open("emails.txt","w", encoding="utf-8") as file:
        file.write("\n".join(emails))

with open("phone_numbers.txt","w", encoding="utf-8") as file:
        file.write("\n".join(phone_no))

