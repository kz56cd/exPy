#! python3

import pyperclip
text = pyperclip.paste()

# TODO: 行を分割し、 * を追加する
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)