def count_lines(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            if line.strip():
                count += 1
    return count


def find_keyword_lines(filename, keyword):
    lines = []
    with open(filename, "r") as file:
        for i, line in enumerate(file, start=1):
            if keyword in line:
                lines.append(i)
    return lines


def convert_to_uppercase(filename):
    with open(filename, "r") as infile:
        content = infile.read()
    with open("output.txt", "w") as outfile:
        outfile.write(content.upper())


def average_score(filename):
    total = 0
    count = 0
    with open(filename, "r") as file:
        for line in file:
            name, score = line.strip().split(",")
            total += float(score)
            count += 1
    return total / count if count > 0 else 0


print(count_lines("sample.txt"))
print(find_keyword_lines("sample.txt", "Python"))
convert_to_uppercase("sample.txt")
print(average_score("scores.txt"))