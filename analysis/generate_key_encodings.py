
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

encoded_keys = dict()
i = 0
for key in keys:
    # encoding = [0] * len(keys)
    # encoding[i] = 1
    # encoded_keys[key] = encoding
    encoded_keys[key] = i
    i = i + 1

print(encoded_keys)
