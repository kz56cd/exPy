import sys

while True:
    print('終了するにはexitと入力していください：')
    response = input()
    if response == 'exit':
        sys.exit()
    print(response + 'と入力されました。')
