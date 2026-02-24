import re

def hide_phone_numbers(text):
    pattern = r'\d{10}|\+84\d+'
    result = re.sub(pattern, "[REDACTED]", text)
    return result

text = "Call me at 0966759147 or +84966759147 tomorrow."
print(hide_phone_numbers(text))