with open('example.txt', 'w') as f:
    f.write('Hello, World!')

with open('example.txt', 'r') as f:
    content = f.read()
    print(content)



try:
    with open('example.txt', 'r') as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("File not found. Please check the file path and try again.")