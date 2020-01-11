# współczynnik zmienności
# Średnie obciążenie , współczynnik zmienności  czasp racy do czasu całkowitego
# Rlang  wykorzystanie
# first come first serve  (50, 100) takei obiązenie, takie współczynnik zmienności schemat dostarczyć  o ile zdązył czy ile spóźniony
# Procesor schering - round robin

# zbudować symulator, i te 2 /\

from random import randrange, random

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

N = int(input('Ilość próbek: '))
delay = input('Opóźnienie: ')
input_task_time = input('Czas zadania: ')
min_task_time, max_time_task = input_task_time.split(',')
print(N, delay, min_task_time, max_time_task)

srednia_1, odchylenie_1 = 3, 1.5
srednia_2, odchylenie_2 = 8, 1.2

np.random.seed(1)
tasks = np.concatenate((np.random.normal(srednia_1, odchylenie_1, int(0.4 * N)),
                        np.random.normal(srednia_2, odchylenie_2, int(0.6 * N))))[:, np.newaxis]


groups_tasks = {}
for task in tasks:
    task = str(abs(task)).replace('[', '').replace(']', '')
    task_group, _ = str(task).split('.')
    if int(task_group) in groups_tasks:
        groups_tasks[int(task_group)] += 1
    else:
        groups_tasks[int(task_group)] = 1

tasks = []
for key, value in groups_tasks.items():
    for x in range(value):
        rand = random()
        tasks.append(key + round(rand,2))


with open('tasks_file.txt', 'w', encoding='utf-8') as file:
    for iter, task in enumerate(tasks):

        line = '{},{},{} \n'.format(str(iter),
                                       str(round(task,2)),
                                       str(randrange(int(min_task_time), int(max_time_task)+1))
                                       )
        file.write(line)
