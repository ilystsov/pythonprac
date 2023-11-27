import sys

def is_wav(data):
    if len(data) < 44:
        return

    if data[:4] != b'RIFF':
        return

    if data[8:16] != b'WAVEfmt ':
        return

    if data[36:40] != b'data':
        return

    return True
        
data = sys.stdin.buffer.read()

def get_int(data):
    return int.from_bytes(data, 'little')

if is_wav(data):
    print(
        f'Size={get_int(data[4:8])}',
        f'Type={get_int(data[20:22])}',
        f'Channels={get_int(data[22:24])}',
        f'Rate={get_int(data[24:28])}',
        f'Bits={get_int(data[34:36])}',
        f'Data size={get_int(data[40:44])}',
        sep=', '
    )
else:
    print('NO')