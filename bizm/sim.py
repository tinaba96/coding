'''
#1

import random

nb_sim = 50 #シミュレーション回数
M = 10 #人数
N = 1000000 #ループ処理回数
money_each = 100000
sim = []


for j in range(nb_sim):
    all = [money_each for i in range(M)]
    cnt = 0
    for i in range(N):
        give = random.randint(0, M-1)
        while True:
            get = random.randint(0, M-1)
            if get != give:
                break

        if all[give] >= 130:
            all[give] -= 130
            all[get] += 130

    #print(all)
    for money in all:
        if money == 0:
            #print('a')
            cnt += 1

    print(cnt)
    sim.append(cnt)

print(sum(sim)/nb_sim)

'''


class Simulation:
    def __init__(self, nb_sim, M, N, money_each):
        self.nb_sim = nb_sim
        self.M = M
        self.N = N
        self.money_each = money_each


    #問１
    def problem1(self): 
        import random
        sim = []
        for j in range(self.nb_sim):
            all = [self.money_each for i in range(self.M)]
            cnt = 0
            for i in range(self.N):
                give = random.randint(0, self.M-1)
                while True:
                    get = random.randint(0, self.M-1)
                    if get != give:
                        break

                if all[give] >= 130:
                    all[give] -= 130
                    all[get] += 130
        
            for money in all:
                if money == 0:
                    cnt += 1

            sim.append(cnt)

        return sum(sim)/self.nb_sim

    #問２
    def problem2(self): 
        import random
        sim = []
        for j in range(self.nb_sim):
            all = [self.money_each for i in range(self.M)]
            cnt = 0
            for i in range(self.N):
                give = random.randint(0, self.M-1)
                while True:
                    get = random.randint(0, self.M-1)
                    if get != give:
                        break

                if all[give] > 200000:
                    continue
                if all[give] <= 200000 and all[give] > 150000:
                    all[give] -= 1300
                    all[get] += 1300
                else:
                    all[give] -= 130
                    all[get] += 130
        
            for money in all:
                if money == 0:
                    cnt += 1

            sim.append(cnt)

        return sum(sim)/self.nb_sim

if __name__ == '__main__':
    s = Simulation(50, 100, 10000, 100000)
    print(s.problem1())
    print(s.problem2())


