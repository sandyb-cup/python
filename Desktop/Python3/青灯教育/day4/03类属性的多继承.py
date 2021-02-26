# -*- conding: utf-8 -*-
# Author:ononok
# Time:2020/12/9
class GrandFather:
    def __init__(self, hall, hair, eat_food, hobby, woking):
        self.hall = hall
        self.hair = hair
        self.eat = eat_food
        self.hobby = hobby
        self.woking = woking


    def PP_fav(self):
        print(f'祖父的身高是{self.hall},头发是{self.hair}色的,喜欢的食物是{self.eat},爱好是{self.hobby}')

    @staticmethod
    def tt():
        print('tt是外祖父跟儿子共有的一个属性')


class Father(GrandFather):
    def __init__(self,hall, hair, eat_food, hobby, woking, company):
        super().__init__(hall,hair,eat_food, hobby, woking)
        self.woking = woking
        self.company = company

    def PP_fav(self):
        print(f'父亲的身高是{self.hall},头发是{self.hair}色的,喜欢的食物是{self.eat},爱好是{self.hobby},是否有公司{self.company}')

class Son(Father, GrandFather):
    def __init__(self,hall, hair, eat_food, hobby, woking, company):
        super().__init__(hall, hair, eat_food, hobby, woking, company)
        self.__repr__()
    def __repr__(self):
        print(f'儿子的身高是{self.hall},头发是{self.hair}色的,喜欢的食物是{self.eat},爱好是{self.hobby},是否有公司{self.company}, {self.tt}')

grandfath = GrandFather(hall = '1.75', hair = 'blank', eat_food = 'rise', hobby = 'finsh', woking = 'fame')

father = Father(hall = '1.80', hair = 'brown', eat_food = 'ice-create', hobby = 'swimming', woking = 'boss', company=True)

son = Son(hall = '1.80', hair = 'brown', eat_food = 'ice-create', hobby = 'swimming', woking = 'boss', company=True)
