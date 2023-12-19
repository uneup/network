from random import uniform
import numpy as np


x_sample = np.array([[-1, -1], [1, -1], [-1, 1], [1, 1]])
y_output = np.array([-1, -1, -1, 1])

weights = [uniform(0.0, 0.2) for _ in range(2)]
# weights = np.array([0, 0])
T = 0

def heaviside(NET):
	if NET > 0:
		return 1
	else:
		return -1


for epoch in range(1, 4):
	print('ЭПОХА', epoch, '#' * 80)
	for i in range(len(x_sample)):
		x_inputs = np.array([x_sample[i][0], x_sample[i][1]])
		x1, x2 = x_inputs
		w1, w2 = weights
		print(f'x1 = {x1}, x2 = {x2}')
		print(f'w1 = {w1}, w2 = {w2}')
		print(f'T = {T}')
		NET = np.dot(x_inputs, weights) - T
		print(f'Взвешенная сумма NET = {NET}')
		OUT = heaviside(NET)
		print(f'Выход нейрона OUT = {OUT}')
		print(f'Эталонное значение y1 = {y_output[i]}')
		if OUT != y_output[i]:
			print('ВЫХОД НЕ СООТВЕТСТВУЕТ ЭТАЛОННОМУ ЗНАЧЕНИЮ, МОДИФИКАЦИЯ КОЭФФИЦИЕНТОВ')
			weights = weights + x_inputs * y_output[i]
			weights[weights > 1] = 1
			T -= y_output[i]
		print()












# for i in range(4):
# 	for i in range(len(x_sample)):
# 		T -= y_output[i]
# 		weights = weights + x_sample[i] * y_output[i]
# 		# print(weights, 'loooool')
# 		#
# 		# print('Входные значения:', *x_sample[i])
# 		print('Веса:', *weights)
# 		print('T =', T)
# 		print('Выходное значение:', y_output[i])
# 		NET = sum(x_sample[i] * weights) - y_output[i] * T
# 		OUT = heaviside(NET)
# 		print('NET =', NET)
# 		print()
# 	print('#'*100)



