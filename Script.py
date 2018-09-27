# coding:utf-8
import erajs.api as a

my_pet = {}


def start_new_game():
    a.page()
    a.h('玩家角色创建方式')
    a.t()
    a.t()
    a.b('使用默认主角', a.goto, default_person)


def default_person():
    a.page()
    a.h('默认玩家角色')
    a.t()
    a.t('姓名：Adam')
    a.t()
    a.t('性别：男')
    a.t()
    a.t('确定吗？')
    a.b('是', a.goto, init_pet)
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
        'gender': 'male'
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
        'gender': 'female'
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
    hash = a.add(pet)
    a.page()
    a.t('你将{}带回了家。'.format(pet['name']), True)
    a.goto(loop)


def loop():
    a.page()
    my_pet = a.get({})
    a.t('{}很乖。'.format(my_pet['name']))
    a.t()
    a.b('休息', rest)
    a.b('保存游戏', a.goto, save_game)


def rest():
    a.tick()
    a.repeat()


def save_game():
    a.page()
    a.h('保存游戏')
    a.t()
    a.show_save_to_save()
    a.b('返回', a.back)


def show_save():
    pass


a.init()
a.title('EraPet')
a.h('EraPet')
a.t()
a.t()
a.b('开始饲养', a.goto, start_new_game)
a.t()
a.b('继续饲养', a.goto, show_save)
