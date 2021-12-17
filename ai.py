import math
import numpy as np
from globals import *

class AI:
	def __init__(self, inputs_num, hidden_layers_num, hidden_layers_neurons_num, outputs_num):
		self.first_hw = list(list(np.random.randint(AI_MIN_WEIGHT, AI_MAX_WEIGHT) for i in range(inputs_num)) for i in range(hidden_layers_neurons_num))
		self.hw = list(list(list(np.random.randint(AI_MIN_WEIGHT, AI_MAX_WEIGHT) for i in range(hidden_layers_neurons_num)) for i in range(hidden_layers_neurons_num)) for i in range(hidden_layers_num-1))
		self.ow = list(list(np.random.randint(AI_MIN_WEIGHT, AI_MAX_WEIGHT) for i in range(hidden_layers_neurons_num)) for i in range(outputs_num))
		self.inputs_num = inputs_num
		self.hidden_layers_num = hidden_layers_num
		self.hidden_layers_neurons_num = hidden_layers_neurons_num
		self.outputs_num = outputs_num

	def run(self, inputs): # consertar isso aqui
		result = np.copy(np.matmul(self.first_hw, inputs)) # input layer to first hidden layer

		for matrix in self.hw: # get all the hidden layers
			result = np.copy(np.matmul(matrix, result)) # multiply hidden layer with last multiplication

		result = np.copy(np.matmul(self.ow, result)) # last hidden layer to output

		result = list(map(lambda x: self.activation(x), result)) # activation function
		return result

	def export_weights(self):
		first_hw = list()
		for row in self.first_hw:
			for i in row:
				first_hw.append(i)
		hw = list()
		for hidden in self.hw:
			for row in hidden:
				for i in row:
					hw.append(i)
		ow = list()
		for row in self.ow:
			for i in row:
				ow.append(i)
		return [first_hw, hw, ow]

	def set_weights(self, w):
		matrix_fw = list()
		for i in range(self.hidden_layers_neurons_num):
			matrix_fw.append(list())
			for j in range(self.inputs_num):
				matrix_fw[i].append(w[0][j+(self.inputs_num*i)])
		
		matrix_hw = list()
		for k in range(self.hidden_layers_num-1):
			matrix_hw.append(list())
			for i in range(self.hidden_layers_neurons_num):
				matrix_hw[k].append(list())
				for j in range(self.hidden_layers_neurons_num):
					matrix_hw[k][i].append(w[1][j+(self.hidden_layers_neurons_num*i)+((self.hidden_layers_neurons_num**2)*k)])

		matrix_ow = list()
		for i in range(self.outputs_num):
			matrix_ow.append(list())
			for j in range(self.hidden_layers_neurons_num):
				matrix_ow[i].append(w[2][j+(self.hidden_layers_neurons_num*i)])
		
		self.first_hw = matrix_fw
		self.hw = matrix_hw
		self.ow = matrix_ow

	def activation(self, x): # using relu
		if x > 10000: return 10000
		elif x < 0: return 0
		else: return x

ai = AI(2, 2, 3, 4)
test_inputs = [[1], [5]]
print("result:\n",ai.run(test_inputs))
#print(ai.ow)
#print(ai.export_weights())
#ai.set_weights(ai.export_weights())
# print(ai.export_weights())