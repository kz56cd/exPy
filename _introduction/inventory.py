def display_inventory(inventory):
    print('持ち物リスト：')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('アイテム総数： ' + str(item_total))

stuff = {'ロープ': 1, 'たいまつ': 6, '金貨': 23, '手裏剣': 52, '矢': 34}
display_inventory(stuff)