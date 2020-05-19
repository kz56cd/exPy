#! pytyon3

def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbolは1文字の文字列でなければならない')
    if width <= 2:
        raise Exception('widthは2より大きくなければならない')
    if height <= 2:
        raise Exception('heightは2より大きくなければならない')
    # if width <= 2:
    #     raise Exception('')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

# boxの描画
print('指定した文字 / 文字数でboxを描画します... \n')
box_list = (
  ('*', 4, 4),
  ('O', 20, 5),
  ('x', 1, 3),
  ('ZZ', 3, 3),
  ('Q', 13, 13)
)
for sym, w, h in  box_list:
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('例外が起こりました: ' + str(err))
