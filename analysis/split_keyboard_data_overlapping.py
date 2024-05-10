
from datetime import datetime
import json

keys = {'', 't', 'J', 'Q', 'Key.shift_r', '0', 'G', 'n', 'f', '6', 'Key.caps_lock', '.', 'D', 'Key.shift', 'v', 'Key.enter', '\x14', 'Key.media_volume_mute', 'Key.down', '-', '\x19', '3', 'Key.media_play_pause', 'Key.ctrl', 'm', 'Key.end', ']', '†', '1', ')', 'C', '2', '(', '\x12', 'Y', 'Key.cmd_r', 'Key.media_volume_down', '\x1a', "'", 'p', '%', 'L', 'V', '=', ';', '_', 'None', 'Key.backspace', 'Key.media_volume_up', 'E', '^', 'o', 'F', 'q', '>', 'a', 'M', '˜', 'j', '{', 'ƒ', 'K', 'Key.alt', 'A', '4', ':', 'h', 'Key.up', 'd', 'Key.ctrl_l', '+', 'x', '\x17', '\x01', 'Key.cmd', 'Key.ctrl_r', '\x0e', 'b', '!', 'z', 'y', 'i', '7', 'r', 'R', '`', '"', ',', 'Key.left', 's', 'T', 'g', 'SPACE', '#', 'Key.alt_l', '\x06', '/', 'I', 'Key.insert', '}', 'l', 'c', 'Key.right', 'X', 'B', '\x13', 'S', '&', '$', '*', '\x16', '\\', 'O', 'H', '5', '8', 'k', 'ç', 'Ï', '[', 'u', '?', 'Key.home', '\x03', 'w', 'Key.delete', '@', 'e', 'N', '9', 'Key.tab', 'Key.alt_r', '\x02', 'P', 'U', 'Z', 'W', '\x18', 'ESC', '<'}

keys_to_remove = [
    '\x03',
    '',
    '\x14',
    'Key.media_volume_mute',
    '\x19',
    'None',
    'Key.media_play_pause',
    '\x12',
    '\x1a',
    'Key.cmd_r',
    'Key.cmd',
    'Key.end',
    'Key.alt',
    'Key.alt_l',
    'Key.alt_r',
    '\x17',
    '\x01',
    '\x0e',
    '\x06',
    'Key.insert',
    '\x13',
    '\x16',
    'ç',
    'Ï',
    'Key.home',
    '\x02',
    '\x18'
]

for key in keys_to_remove:
    keys.remove(key)

# one-hot encode

from character_encodings import encodings

vectors = []
cur_vector = []

def format_data(filenames, output_filename):
    # for i in range(1, 6):
    for filename in filenames:
        # filename = f'april{i}_keylog_aidan.txt'
        with open(f'logs/{filename}', 'r') as fh:
            lines = fh.readlines()
        
        beg, end = 0, 0
        while beg < len(lines) and end < len(lines):
            end = beg
            date_time = ' '.join([lines[beg].strip().split(' ')[0], lines[beg].strip().split(' ')[1]])
            beg_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')

            date_time = ' '.join([lines[end].strip().split(' ')[0], lines[end].strip().split(' ')[1]])
            end_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')

            while end < len(lines) and (end_time - beg_time).seconds <= 4:
                date_time = ' '.join([lines[end].strip().split(' ')[0], lines[end].strip().split(' ')[1]])
                end_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')
                end = end + 1
            
            if end == len(lines):
                break
            end = end - 2

            i = beg
            cur_vector = []
            while i <= end:
                # try:
                #    keyname = lines[i].strip().split(' ')[3]
                # except IndexError:
                #     print(lines[i])
                #     print(lines[i].strip())
                #     print(lines[i].strip().split(' '))
                #     exit(1)
                if len(lines[i].strip().split(' ')) > 3 and lines[i].strip().split(' ')[3] in keys:
                    date_time = ' '.join([lines[i].strip().split(' ')[0], lines[i].strip().split(' ')[1]])
                    cur_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')

                    word = lines[i].strip().split(' ')[3]
                    upordown = 0 if lines[i].strip().split(' ')[2] == 'keydown' else 1

                    cur_vector.append([(cur_time - beg_time).seconds + (cur_time - beg_time).microseconds/1e6, encodings[word], upordown])
                i = i + 1

            if len(cur_vector) >= 5:
                vectors.append(cur_vector)

            beg = beg + 1

    with open(output_filename, 'w') as fh:
        fh.write(json.dumps(vectors))


format_data([
    'keylog1_tony.txt',
    'keylog2_tony.txt',
    'keylog3_tony.txt',
    'keylog4_tony.txt'
], 'tony_final_data_overlapping.json')

format_data([
    'april2-7keylog_srujan.txt'
], 'srujan_final_data_overlapping.json')

format_data([
    'april7-9_keylog_eric.txt'
], 'eric_final_data_overlapping.json')
