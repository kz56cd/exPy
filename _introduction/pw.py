#! python3

PASSWORDS = {
  'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
  'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
  'luggage': '12345'
}

# print(PASSWORDS)
import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方： python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

accoount = sys.argv[1]

if accoount in PASSWORDS:
    pyperclip.copy(PASSWORDS[accoount])
    print(accoount + 'のパスワードをクリップにコピーしました')
else:
    print(accoount + 'というアカウント名はありません')

