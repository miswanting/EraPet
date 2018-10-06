import erajs.api as a


def train():
    pass


def shop():
    def buy(item):
        if a.data['db']['player']['money'] >= item['cost']:
            a.data['db']['player']['item'].append(item)
        a.page()
        a.t('你购买了{}。'.format(item['name']), True)
        a.repeat()
    a.page()
    a.h('商店')
    a.t()
    items = a.data['data.item']['物品']
    for each in items:
        a.b('{} - {}'.format(each['name'], each['cost']), buy, each)
    a.t()
    a.b('返回', a.back)
