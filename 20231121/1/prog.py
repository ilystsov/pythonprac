import sys

first_byte = sys.stdin.buffer.read(1)
parts_number = first_byte[0]
data = sys.stdin.buffer.read()
if data[-1] == 10:
    data = data[:-1]

i = 0
left = 0
right = 0
parts = []
while i < parts_number and i < len(data):
    left = max(right, int(i * len(data) / parts_number))
    right = max(left + 1, int((i + 1) * len(data) / parts_number))
    parts.append(data[left:right])
    i += 1

result = [first_byte] + sorted(parts) + [b'\n']
sys.stdout.buffer.write(b''.join(result))
