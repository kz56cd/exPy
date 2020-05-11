cat_names = []
while True:
    print('猫' + str(len(cat_names) + 1) + 'の名前を入力してください')
    print('（終了するにはEnterキーだけ押してください）')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]
print('猫の名前は次の通りです：')
for name in cat_names:
    print('    ' + name)