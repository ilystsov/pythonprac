with open('cal', 'rb') as f:
    size = f.seek(0, 2)
    content = f.read()

with open('cal', 'wb') as f:
    f.write(content[0:size // 2])
    f.write(content[size // 2:])
