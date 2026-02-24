import re

def check_hex_color(color):
    pattern = r'^#[0-9A-Fa-f]{6}$'
    
    if re.match(pattern, color):
        return True
    else:
        return False
    
print(check_hex_color("#A1B2C3"))  # True
print(check_hex_color("#ff9900"))  # True
print(check_hex_color("A1B2C3"))   # False
print(check_hex_color("#GGGGGG"))  # False
print(check_hex_color("#EM1UAN4"))  # False