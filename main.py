import random

my_hp = 150
enemy_hp = 120

#整数か判断
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

#ルート
class Root(object):
    sequence = []
    node_count = 0

    def __init__(self,my_hp,enemy_hp):
        self.my_hp = my_hp
        self.enemy_hp = enemy_hp

    def add(self,node):
        self.sequence.append(node)
        self.node_count += 1

    def print_node(self):
        i = 0
        for node in self.sequence:
            if type(node[0]) == int:
                self.enemy_hp = self.enemy_hp - node[0]
            else:
                if(self.node_count-1 == i):
                    if node[1]():
                        for v in node[0](self.enemy_hp):
                            print(v, end="")
                        print("")
                else:
                    if node[1]():
                        for v in node[0]():
                            print(v,end="")
                        print("")
            i += 1


#スタート
start = lambda: "出発" ,lambda: True
#敵に近づく
get_closer_enemy = lambda : "敵に寄る" , lambda: True
#condition_node
my_hp_condition = lambda: get_closer_enemy[0](),lambda: True if my_hp >= 100 else False

#友達クラス
class Friend(object):
    def __init__(self,name):
        self.name = name
#parallelの処理
def parallel(parallel_node):
    count = 0
    node_num = len(parallel_node)
    result = []

    for node in parallel_node:
        if node:
            result.append(node.name)
            count += 1

    if count == node_num:
        return result
    else:
        return False
#parallelノード
parallel_node = []
parallel_node.append(Friend("友達A"))
parallel_node.append(Friend("友達B"))

parallel_lambda = lambda : parallel(parallel_node), lambda: True if parallel(parallel_node) != False else False

#RepeaterNode
def repeter(selector):
    for i in range(2):
        if selector[1]():
            result = selector[0]()
    return result,True

#skill1のActionNode
def skill1(enemy_hp,skill1_probability):
    l = [1]*skill1_probability
    l = l + [0]*(1-skill1_probability)
    result = random.choice(l)
    if result == 1:
        enemy_hp = enemy_hp - 50
    return enemy_hp


skill1_lambda = lambda enemy_hp,skill1_probability:skill1(enemy_hp,skill1_probability),lambda: True

#skill2のActionNode
skill2 = lambda: enemy_hp - 60, lambda: True

def skill_selector(skill1_lambda,skill2,enemy_hp,skill1_probability):
    l = [0,1]
    result = random.choice(l)
    if result == 0:
        return skill1_lambda(enemy_hp,skill1_probability)
    else:
        return skill2[0]()


skill_selector_lambda = lambda: skill_selector(skill1,skill2,enemy_hp,skill1_probability),lambda: True

#最終結果のActionNode
enemy_hp_jadge = lambda enemy_hp: "End1" if enemy_hp == 0 else "End2", lambda: True


if __name__ == "__main__":
    while(1):
        skill1_probability = input("skill1の発動確率(%)を入力してください\n")
        if is_integer(skill1_probability):
            skill1_probability = float(skill1_probability)
            skill1_probability = int(skill1_probability)
            if skill1_probability > 100 or skill1_probability < 0:
                print("発動確率(%)は整数(0以上100以下)で入力してください")
            else:
                break


    root = Root(my_hp,enemy_hp)
    root.add(start)
    root.add(my_hp_condition)
    root.add(parallel_lambda)
    root.add(repeter(skill_selector_lambda))
    root.add(enemy_hp_jadge)

    root.print_node()
