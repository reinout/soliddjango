some_file_text = """

Blank line above.
Here is some text

And some more

"""

lines = some_file_text.split('\n')
print len(lines)  # 8 lines

# Filtering empty lines with a loop:
result = []
for line in lines:
    line = line.strip()  # Strip end-of-line and spaces.
    if line:
        result.append(line)

print len(result)  # 3, three lines with actual text.

# Alternative: a list comprehension.
# START_HIGHLIGHT
comprehension = [line for line in lines if line.strip()]
# END_HIGHLIGHT
print len(comprehension)  # Also 3.

# You can also modify a list:
uppercase = [line.upper() for line in comprehension]
print uppercase[0]  # Returns BLANK LINE ABOVE.
