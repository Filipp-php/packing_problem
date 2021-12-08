import sys
from accessify import private
import traceback
import random
import pandas as pd
import math
import itertools

class Base_algorithm():
    items = []
    M = 0
    n = 0
    
    def __init__(self, items, M, n):
        self.items = []
        for i in range(len(items)):
            self.items.append([items[i], i])
        self.M = M
        self.n = n

class BFS_algorithm(Base_algorithm):
        
    @private
    def bubble_sort(self):
        def swap(i, j):
            self.items[i], self.items[j] = self.items[j], self.items[i]

        n = len(self.items)
        swapped = True
        
        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n-x):
                if self.items[i-1][0] > self.items[i][0]:
                    swap(i - 1, i)
                    swapped = True

    def BFS_alg(self):
        self.bubble_sort()
        containers = []
        nbmrs_in_cntrs = {}
        key = 0
        for item in self.items:
            if len(containers) == 0:
                containers.append(item[0])
                nbmrs_in_cntrs[key] = []
                nbmrs_in_cntrs[key].append(item[1])
                key = key + 1
            else:
                best_id = 0
                best_cntr = containers[0]
                for j in range(len(containers)):
                    if item[0] + containers[j] <= self.M and self.M - best_cntr < self.M - containers[j]:
                        best_id = j
                        best_cntr = containers[j]
                        
                if best_id == 0 and item[0] + containers[j] > self.M:
                    containers.append(item[0])
                    nbmrs_in_cntrs[key] = []
                    nbmrs_in_cntrs[key].append(item[1])
                    key = key + 1  
                else:
                    containers[best_id] = containers[best_id] + item[0]
                    nbmrs_in_cntrs[best_id].append(item[1])
        return nbmrs_in_cntrs

class Usual_algorithm(Base_algorithm):
    
    @private
    def permutation(self, s = None):
        if len(s) == 1:
            return [s]

        perm_list = [] 
        for a in s:
            remaining_elements = [x for x in s if x[1] != a[1]]
            z = self.permutation(remaining_elements)
        
            for t in z:
                perm_list.append([a] + t)

        return perm_list
    
    def usual_alg(self):
        
        prmtns = self.permutation(self.items)
        
        best_case = {}
        
        for prmtn in prmtns:
            containers = []
            nbmrs_in_cntrs = {}
            key = 0
            for item in prmtn:
                if len(containers) == 0:
                    containers.append(item[0])
                    nbmrs_in_cntrs[key] = []
                    nbmrs_in_cntrs[key].append(item[1])
                    key = key + 1
                else:
                    flag = False
                    for j in range(len(containers)):
                        if item[0] + containers[j] <= self.M:
                            containers[j] = containers[j] + item[0]
                            nbmrs_in_cntrs[j].append(item[1])
                            flag = True
                            break
                    if flag == False:
                        containers.append(item[0])
                        nbmrs_in_cntrs[key] = []
                        nbmrs_in_cntrs[key].append(item[1])
                        key = key + 1
            best_q = len(best_case)
            if best_q == 0:
                best_case = nbmrs_in_cntrs
            elif best_q != 0 and best_q > len(nbmrs_in_cntrs):
                best_case = nbmrs_in_cntrs
            
        return best_case
        
    
class FF_algorithm():
    items = []
    M = 0
    n = 0
    
    def __init__(self, items, M, n):
        self.items = items
        self.M = M
        self.n = n
        
    def FF_alg(self):
        containers = []
        nbmrs_in_cntrs = {}
        key = 0
        count = 1
        for item in self.items:
            if len(containers) == 0:
                containers.append(item)
                nbmrs_in_cntrs[key] = []
                nbmrs_in_cntrs[key].append(count)
                key = key + 1
            else:
                flag = False
                for j in range(len(containers)):
                    if item + containers[j] <= self.M:
                        containers[j] = containers[j] + item
                        nbmrs_in_cntrs[j].append(count)
                        flag = True
                        break
                if flag == False:
                    containers.append(item)
                    nbmrs_in_cntrs[key] = []
                    nbmrs_in_cntrs[key].append(count)
                    key = key + 1
            count = count + 1
        return nbmrs_in_cntrs
        


def generation(q = 5): #q - кол-во тестов
    import time
    N = [3, 5, 7, 9]
    for_exel = { 
                  'Объем входных данных': [], 
                  'Название алгоритма': [],
                  'Время работы алгоритма' : [],
                  'Процент тестов...' : [],
                  'Среднее относительное отклонение' : [],
                }
    
    for n in N:
        for_exel['Объем входных данных'].append(n)
        for_exel['Объем входных данных'].append(n)
        for_exel['Объем входных данных'].append(n)
        for_exel['Название алгоритма'].append('Переборный')
        for_exel['Название алгоритма'].append('FF')
        for_exel['Название алгоритма'].append('BFS')
        us_alg = {
                    'Время': 0, 
                    'Совпадения': 0, 
                    'Отклонение': 0
                    }
        ff = {
                    'Время': 0, 
                    'Совпадения': 0, 
                    'Отклонение': 0
                    }
        bfs = {
                    'Время': 0, 
                    'Совпадения': 0, 
                    'Отклонение': 0
                    }
        print("\nНовая серия теста с объемом данных " + str(n))
        for i in range(q):
            M = random.randint(5, 10)
            items = []
            for j in range(n):
                items.append(random.randint(1, M))
                #items.append(M)
                #items.append(1)

            print("\n Test " + str(i+1))
            print("  M = " + str(M))
            print("  Items: ")
            print(items)
            
            
            
            start_time = time.time() * 1000
            alg = Usual_algorithm(items, M, n)
            container = alg.usual_alg()
            end = time.time() * 1000
            t = end - start_time
            best = len(container)
            print("  Best: " + str(best))
            print("  Containers: " + str(len(container)))
            print("  Time: " + str(t))
            print(container)
            us_alg['Время'] = us_alg['Время'] + t
            if len(container) == best:
                us_alg['Совпадения'] = us_alg['Совпадения'] + 1
            us_alg['Отклонение'] = us_alg['Отклонение'] + abs(len(container) - best) / best
           
            
            start_time = time.time() * 1000
            alg = FF_algorithm(items, M, n)
            container = alg.FF_alg()
            end = time.time()* 1000
            t = end - start_time
            print("  Containers: " + str(len(container)))
            print("  Time: " + str(t))
            print(container)
            ff['Время'] = ff['Время'] + t
            if len(container) == best:
                ff['Совпадения'] = ff['Совпадения'] + 1
            ff['Отклонение'] = ff['Отклонение'] + abs(len(container) - best) / best
            
            
            start_time = time.time() * 1000
            alg = BFS_algorithm(items, M, n)
            containers = alg.BFS_alg()
            end = time.time() * 1000
            t = end - start_time
            print("  Containers: " + str(len(container)))
            print("  Time: " + str(t))
            print(container)
            bfs['Время'] = bfs['Время'] + t
            if len(container) == best:
                bfs['Совпадения'] = bfs['Совпадения'] + 1
            bfs['Отклонение'] = bfs['Отклонение'] + abs(len(container) - best) / best
        
        #внесение данных в ексель
        for_exel['Время работы алгоритма'].append(us_alg['Время'] / q)
        for_exel['Процент тестов...'].append(us_alg['Совпадения'] / q * 100)
        for_exel['Среднее относительное отклонение'].append(us_alg['Отклонение'] / q)
        for_exel['Время работы алгоритма'].append(ff['Время'] / q)
        for_exel['Процент тестов...'].append(ff['Совпадения'] / q * 100)
        for_exel['Среднее относительное отклонение'].append(ff['Отклонение'] / q)
        for_exel['Время работы алгоритма'].append(bfs['Время'] / q)
        for_exel['Процент тестов...'].append(bfs['Совпадения'] / q * 100)
        for_exel['Среднее относительное отклонение'].append(bfs['Отклонение'] / q)
        
    df = pd.DataFrame(for_exel)
    df.to_excel('./exp.xlsx', sheet_name='FfF', index=False)


if __name__ == "__main__":
    try:
        generation()
        print('Результаты тестов записаны в эксель файл: exp.xlsx')

        n = int(input("Введите количество предметов: "))

        M = int(input("Введите вместимость контейнера: "))

        print("Введите массы предметов")
        items = []
        for i in range(n):
            items.append(int(input("Введите массу предмета номер " + str(i+1) + ": ")))
            
        print("\nРезультаты:")
        
        containers = []
        alg = Usual_algorithm(items, M, n)
        containers.append(alg.usual_alg())

        alg = FF_algorithm(items, M, n)
        containers.append(alg.FF_alg())

        alg = BFS_algorithm(items, M, n)
        containers.append(alg.BFS_alg())
        
        
        for container in containers:
            print("Контейнеров использовано " + str(len(container)))
            print("Контейнеры: ")
            print(container)
            print("\n///\n")
        input("Введите любую клавишу...")

    except Exception as e:
        print("Ошибка: ", sys.exc_info()[0], ", детали:")
        print(traceback.format_exc())
        input("Проверьте данные и попробуйте еще раз")
