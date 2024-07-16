line_count = 0
with open('filename') as file:
    for line in file:
        line_count += 1
print("Line count:", line_count)
