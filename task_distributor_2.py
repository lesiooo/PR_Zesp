# współczynnik zmienności
# Średnie obciążenie , współczynnik zmienności  czasp racy do czasu całkowitego
# Rlang  wykorzystanie
# first come first serve  (50, 100) takei obiązenie, takie współczynnik zmienności schemat dostarczyć  o ile zdązył czy ile spóźniony
# Procesor schering - round robin

# zbudować symulator, i te 2 /\

from random import randrange

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

N = int(input('Ilość próbek: '))
delay = input('Opóźnienie: ')
input_task_time = input('Czas zadania: ')
min_task_time, max_time_task = input_task_time.split(',')
print(N, delay, min_task_time, max_time_task)

np.random.seed(1)
tasks = np.concatenate((np.random.normal(3, 1, int(0.3 * N)),
                        np.random.normal(8, 1, int(0.7 * N))))[:, np.newaxis]
tasks_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]

fig, ax = plt.subplots()

for kernel in ['tophat']:
    kde = KernelDensity(kernel=kernel, bandwidth=0.5).fit(tasks)
    log_dens = kde.score_samples(tasks_plot)
    ax.plot(tasks_plot[:, 0], np.exp(log_dens), '-',
            label="kernel = '{0}'".format(kernel))

ax.text(6, 0.38, "N={0} points".format(N))

ax.legend(loc='upper left')
ax.plot(tasks[:, 0], -0.005 - 0.01 * np.random.random(tasks.shape[0]), '+k')

ax.set_xlim(0, 15)
ax.set_ylim(-0.02, 0.4)
plt.show()

with open('tasks_file.txt', 'w', encoding='utf-8') as file:
    for iter, task in enumerate(tasks):

        line = '{},{},{},{} \n'.format(str(iter),
                                       str(abs(task)),
                                       str(abs(int(task * 10))),
                                       str(randrange(int(min_task_time), int(max_time_task)+1))
                                       )
        file.write(line)
