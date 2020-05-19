import traceback

try:
    raise Exception('これはエラーメッセージです。')
except:
    error_file = open('./_output/errorInfo.txt', 'w')
    log_count = error_file.write(traceback.format_exc()) # エラー情報を文字列化して書込
    error_file.close()
    print('トレースバック情報をerrorInfo.txtに書込： ' + str(log_count) + '文字')