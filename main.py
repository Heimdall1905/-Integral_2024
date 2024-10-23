import matplotlib.pyplot as plt
import numpy as np

import ChM

a = 2.5
b = 3.3
alfa = 2/3
beta = 0

# таблица
columns = ['N', 'h', 'S', 'E', 'R', "S'", 'p', "p'", 'pr']
x = np.arange(-10, 2, 0.1)

ans = ChM.not_weight(a, b) # данные для таблицы, ответы
ans[0][0][4] = ans[1][0][4] = ans[2][0][4] = 0
ans[6].pop(0)
ans[3].pop(0)
ans[7].pop(0)
ans[4].pop(0)
ans[8].pop(0)
ans[5].pop(0)

plt.figure(1) # прямоугольник
plt.get_current_fig_manager().set_window_title("Метод прямоугольника")
plt.subplots_adjust(bottom=0.625, top=0.96, left=0.03, right=0.989)
table = plt.table(cellText=ans[0], cellLoc="center", colLabels=columns)
table.auto_set_font_size(False)
table.set_fontsize(10)
plt.plot([np.log10(i) for i in ans[6]], [np.log10(i) for i in ans[3]], 'r', x, 2*x, "k--")


plt.figure(2)  # трапеция
plt.get_current_fig_manager().set_window_title("Метод трапеции")
plt.subplots_adjust(bottom=0.8, top=0.96, left=0.03, right=0.989)
table = plt.table(cellText=ans[1], cellLoc="center", colLabels=columns)
table.auto_set_font_size(False)
table.set_fontsize(10)
plt.plot([np.log10(i) for i in ans[7]], [np.log10(i) for i in ans[4]], 'r', x, 2*x, "k--")

plt.figure(3)
plt.get_current_fig_manager().set_window_title("Метод Симпсона")
plt.subplots_adjust(bottom=0.625, top=0.96, left=0.03, right=0.989)
table = plt.table(cellText=ans[2], cellLoc="center", colLabels=columns)
table.auto_set_font_size(False)
table.set_fontsize(10)
plt.plot([np.log10(i) for i in ans[8]], [np.log10(i) for i in ans[5]], 'r', x, 4*x, "k--")



'''ans_with_weight = ChM.with_weight(a, b, alfa, beta)
ans_with_weight[0][0][4] = ans_with_weight[1][0][4] = 0
ans_with_weight[4].pop(0)
ans_with_weight[2].pop(0)
ans_with_weight[5].pop(0)
ans_with_weight[3].pop(0)


plt.figure(4)
plt.xlim([-4, 0])
plt.get_current_fig_manager().set_window_title("Метод Ньютона-Котса")
plt.subplots_adjust(bottom=0.625, top=0.96, left=0.03, right=0.989)
table = plt.table(cellText=ans_with_weight[0], cellLoc="center", colLabels=columns)
table.auto_set_font_size(False)
table.set_fontsize(10)
plt.plot([np.log10(i) for i in ans_with_weight[4]], [np.log10(i) for i in ans_with_weight[2]], 'y',
         x, 3*x, 'r--', x, 4*x, 'b--')

plt.figure(5)
plt.xlim([-2.5, 0])
plt.get_current_fig_manager().set_window_title("Метод Гаусса")
plt.subplots_adjust(bottom=0.625, top=0.96, left=0.03, right=0.989)
table = plt.table(cellText=ans_with_weight[1], cellLoc="center", colLabels=columns)
table.auto_set_font_size(False)
table.set_fontsize(10)
plt.plot([np.log10(i) for i in ans_with_weight[5]], [np.log10(i) for i in ans_with_weight[3]], 'y',
         x, 6*x, 'b--')'''

plt.show()














