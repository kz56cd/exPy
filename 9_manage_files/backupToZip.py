#! python3

import zipfile, os

# フォルダ全体をzipファイルにバックアップ
def backup_to_zip(folder):
    folder = os.path.abspath(folder) # 絶対パス化
    print('Process: start backup, target: {}'.format(folder))

    # 既存ファイル名からファイル名の連番を決める
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1

    # zipの作成
    print('Creating: {}...'.format(zip_filename))
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # フォルダツリー内の検索
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files: in {}...'.format(foldername))
        backup_zip.write(foldername)

        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Process: done.')

backup_to_zip('./')