import matplotlib.pyplot as plt
import numpy as np

import ChM

a = 2.5
b = 3.3
alfa = 2/3
beta = 0

ans = ChM.not_weight(a, b) # данные для таблицы, ответы
ans[0][0][4] = ans[1][0][4] = ans[2][0][4] = 0
ans[0][0][5] = ans[1][0][5] = ans[2][0][5] = 0

# таблица
columns = ['N', 'h', 'S', 'E', 'R', "S'", 'p', "p'", 'pr']
plt.figure(1) # прямоугольник
plt.get_current_fig_manager().set_window_title("Метод прямоугольника")
plt.subplots_adjust(bottom=0.625, top=0.96, left=0.03, right=0.989)
table = plt.table(cellText=ans[0], cellLoc="center", colLabels=columns)
table.auto_set_font_size(False)
table.set_fontsize(10)
#plt.plot([np.log10(i) for i in ans[3]], [np.log10(i) for i in ans[6]], "b--")

plt.figure(2) #трапеция
plt.get_current_fig_manager().set_window_title("Метод трапеции")
plt.subplots_adjust(bottom=0.8, top=0.96, left=0.03, right=0.989)
table = plt.table(cellText=ans[1], cellLoc="center", colLabels=columns)
table.auto_set_font_size(False)
table.set_fontsize(10)

plt.figure(3)
plt.get_current_fig_manager().set_window_title("Метод Симпсона")
plt.subplots_adjust(bottom=0.625, top=0.96, left=0.03, right=0.989)
table = plt.table(cellText=ans[2], cellLoc="center", colLabels=columns)
table.auto_set_font_size(False)
table.set_fontsize(10)

plt.show()


'''for i in range(3):
    if i == 0:
        print("Метод прямоугольника")
    if i == 1:
        print("Метод трапеции")
    if i == 2:
        print("Метод Симпсона")
    for j in range(len(ans[i])):
        print(ans[i][j])'''













