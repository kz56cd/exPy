import os

for foldername, subfolders, filenames in os.walk('./'):
    print('the current folder is ' + foldername + '\n')

    for subfolder in subfolders:
        print('SUBFOLDER of '.ljust(20, '_') + ' ' + foldername + ': ' + subfolder)
    for filename in filenames:
        print('FILE inside '.ljust(20, '_') + ' ' + foldername + ': ' + filename)
    print('')