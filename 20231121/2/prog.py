import sys

sys.stdout.write(
    sys.stdin.buffer.read()
    .decode('UTF-8', errors='replace')
    .encode('latin1', errors='replace')
    .decode('CP1251', errors='replace')
)
# print(
#     sys.stdin.read()
#     .encode('CP1251', errors='replace')
#     .decode('latin1', errors='replace')
#     
# )