
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switch_lights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), '赤信号がない！ ' + str(stoplight)

# どちらもassertにひっかかる
switch_lights(market_2nd)
switch_lights(mission_16th)

# > アサートは Python に -O(アルファベットのオー。Optimize 最適化の意味)を渡して実行すれば無効化できます