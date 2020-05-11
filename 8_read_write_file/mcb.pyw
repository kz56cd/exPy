#! python3

# .pywという拡張子は、Pythonを実行するときにターミナル ウィンドウを表示しないことを表す

# mcb.pyw - クリップボードのテキストを保存・復元
# Usage:
# py.exe mcb.pyw save <keyword> - クリップボードをキーワードに紐づけて保存 ❶
# py.exe mcb.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー # py.exe mcb.pyw list - 全キーワードをクリップボードにコピー

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    print('saved [' + sys.argv[2] + '] : ' + mcb_shelf[sys.argv[2]])
elif len(sys.argv) == 2:
    # キーワード一覧、内容の読み込み
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print('key list:\n')
        for k in mcb_shelf:
            print(k.ljust(10, '-') + ' : ' + mcb_shelf[k])
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print('copyed!')
mcb_shelf.close() 