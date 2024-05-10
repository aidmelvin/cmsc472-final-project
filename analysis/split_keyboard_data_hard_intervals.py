
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


def process(filenames, final_output_file):
    vectors = []
    cur_vector = []
    for filename in filenames:
        # filename = f'april{i}_keylog_aidan.txt'
        with open(f'logs/{filename}', 'r') as fh:
            lines = fh.readlines()
        
        cur_time_interval = None
        for line in lines:
            if line.strip() != 'KeyLogger Started...' and len(line.strip().split(' ')) > 3 and line.strip().split(' ')[3] in keys:
                date_time = ' '.join([line.strip().split(' ')[0], line.strip().split(' ')[1]])
                date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')
                seconds = date_time.second

                rounded_seconds = seconds - (seconds % 5)
                rounded_date_time_obj = date_time.replace(second=rounded_seconds, microsecond=0)

                key_pressed = line.strip().split(' ')[3]
                updown = line.strip().split(' ')[2]
                
                if cur_time_interval is not None and (date_time - cur_time_interval).seconds >= 5 and (date_time - cur_time_interval).microseconds > 0:
                    if len(cur_vector) >= 5:
                        vectors.append(cur_vector)
                    cur_vector = [[(seconds % 5)+ date_time.microsecond/1e6, key_pressed, updown]]
                else:
                    cur_vector.append([(seconds % 5)+ date_time.microsecond/1e6, key_pressed, updown])
                
                cur_time_interval = rounded_date_time_obj

    with open(final_output_file, 'w') as fh:
        fh.write(json.dumps(vectors))

# process(['april7-9_keylog_eric.txt'], 'eric_final_data_hard_intervals.json')
# process(['april2-7keylog_srujan.txt'], 'srujan_final_data_hard_intervals.json')
process(['keylog1_tony.txt',
         'keylog2_tony.txt',
         'keylog3_tony.txt',
         'keylog4_tony.txt'], 'tony_final_data_hard_intervals.json')
