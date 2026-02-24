import re

def check_course_code(code):
    pattern = r'^[A-Z]{3}[0-9]{3}$'
    
    if re.match(pattern, code):
        return True
    else:
        return False

if __name__ == "__main__":
    print(check_course_code("TEC001"))   # True
    print(check_course_code("tec001"))   # False
    print(check_course_code("TE001"))    # False
    print(check_course_code("Tec001"))   # False
    print(check_course_code("TEc001"))   # False
    print(check_course_code("TEC0001"))  # False