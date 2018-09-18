# coding:utf-8
import erajs.api as a


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
    a.t()


a.init()
a.title('EraPet')
a.h('EraPet')
a.t()
a.t()
a.b('开始饲养', a.goto, start_new_game)
a.t()
a.b('继续饲养', None)
