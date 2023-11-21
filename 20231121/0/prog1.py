with open('cal', 'r') as f:
    content = f.read()

a = len(content) // 3
pos = content.find('\n', a)
print(content[:pos])