# coding:utf-8
import erajs.api as a
import game.main as m
# 注意！不推荐在此处定义变量，而应在 a.init() 之后将变量定义在 a.data['db'] 中，以获得数据持久性支持。


def start_new_game():
    a.page()
    a.h('玩家角色创建方式')
    a.t()
    a.t()
    a.b('使用默认主角', a.goto, default_person)


def default_person():
    def add_default_person():
        a.data['db']['player'] = {
            'name': 'Adam',
            '性别': '男',
            "money": 1000,
            'item': [],
        }
        a.goto(init_pet)
    a.page()
    a.h('默认玩家角色')
    a.t()
    a.t('姓名：Adam')
    a.t()
    a.t('性别：男')
    a.t()
    a.t('确定吗？')
    a.b('是', add_default_person)
    a.t('/')
    a.b('否', a.back)


def init_pet():
    a.page()
    a.h('请选择你的初始宠物')
    a.t()
    a.b('猫', a.goto, init_cat)
    a.b('狗', a.goto, init_dog)


def init_dog():
    a.page()
    new_pet = {
        'name': 'Brane',
        'class': 'dog',
        'gender': 'male',
        'health': 100,
        'full': 100,
        'strenth': 0,
    }
    a.t('姓名：'+new_pet['name'])
    a.t()
    a.t('种类：'+new_pet['class'])
    a.t()
    a.t('性别：'+new_pet['gender'])
    a.t()
    a.t('确定吗？')
    a.b('是', a.goto, load_pet, new_pet)
    a.t('/')
    a.b('否', a.back)


def init_cat():
    a.page()
    new_pet = {
        'name': 'Cathy',
        'class': 'cat',
        'gender': 'female',
        'health': 100,
        'full': 100,
        'strenth': 0,
    }
    a.t('姓名：'+new_pet['name'])
    a.t()
    a.t('种类：'+new_pet['class'])
    a.t()
    a.t('性别：'+new_pet['gender'])
    a.t()
    a.t('确定吗？')
    a.b('是', a.goto, load_pet, new_pet)
    a.t('/')
    a.b('否', a.back)


def load_pet(pet):
    a.data['db']['player']['pets'] = [pet]
    a.page()
    a.t('你将{}带回了家。'.format(a.data['db']['player']['pets'][0]['name']), True)
    a.clear_gui()
    a.goto(loop)


def loop():
    a.page()
    a.t(a.get_full_time())
    a.t()
    a.t('{} {} {} {}/100 {}/100'.format(a.data['db']['player']['pets'][0]['name'],
                                        a.data['db']['player']['pets'][0]['gender'],
                                        a.data['db']['player']['pets'][0]['class'],
                                        a.data['db']['player']['pets'][0]['health'],
                                        a.data['db']['player']['pets'][0]['full']))
    a.t()
    a.b('训练', a.goto, m.train)
    a.b('商店', a.goto, m.shop)
    a.b('休息', rest)
    a.t()
    a.b('保存游戏', a.goto, save_game)
    a.b('读取游戏', a.goto, load_game)
    a.b('结束游戏', quit_game)


def rest():
    a.tick()
    a.page()
    a.t('经过了半天。', True)
    a.repeat()


def save_game():
    a.page()
    a.h('保存游戏')
    a.t()
    print(a.data['db'])
    a.show_save_to_save()
    a.b('返回', a.back)


def quit_game():
    pass


def load_game():
    a.page()
    a.h('读取游戏')
    a.t()
    a.show_save_to_load(loop)
    a.b('返回', a.back)


a.init()
a.title('EraPet')
a.h('EraPet')
a.t()
a.t()
a.b('开始饲养', a.goto, start_new_game)
a.t()
a.b('继续饲养', a.goto, load_game)
