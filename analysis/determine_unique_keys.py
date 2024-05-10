# splits keyboard data into 5-second intervals and only saves the intervals
# with more than 5 keys pressed

# remove:
# '\x03'
# ''
# '\x14'
# 'Key.media_volume_mute' <-- INVESTIGATE
# '\x19'
# 'None'
# 'Key.media_play_pause'
# '\x12'
# '\x1a'
# 'Key.cmd_r'
# 'Key.cmd'
# 'Key.end'
# 'Key.alt' <-- INVESTIGATE
# 'Key.alt_l'
# 'Key.alt_r'
# '\x17'
# '\x01'
# '\x0e'
# '\x06'
# 'Key.insert'
# '\x13'
# '\x16'
# 'ç'
# 'Ï'
# 'Key.home'
# '\x03'
# '\x02'
# '\x18'

keys = set()

for i in range(1, 6):
    filename = f'april{i}_keylog_aidan.txt'
    with open(f'logs/{filename}', 'r') as fh:
        lines = fh.readlines()

    for line in lines:
        if line.strip() != 'KeyLogger Started...':
            keys.add(line.split(' ')[3].strip())


with open(f'logs/april2-7keylog_srujan.txt', 'r') as fh:
    lines = fh.readlines()

for line in lines:
    if line.strip() != 'KeyLogger Started...':
        keys.add(line.split(' ')[3].strip())


with open(f'logs/april7-9_keylog_eric.txt', 'r') as fh:
    lines = fh.readlines()

for line in lines:
    if line.strip() != 'KeyLogger Started...':
        keys.add(line.split(' ')[3].strip())


for i in range(1, 5):
    filename = f'keylog{i}_tony.txt'
    with open(f'logs/{filename}', 'r') as fh:
        lines = fh.readlines()

    for line in lines:
        if line.strip() != 'KeyLogger Started...':
            keys.add(line.split(' ')[3].strip())

print(keys)
