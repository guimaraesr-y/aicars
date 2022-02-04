import random
import numpy as np

class Network(object):
	def __init__(self, sizes: list):
		"""A lista `sizes` contém o número de neurônios nas respectivas 
		camadas da rede. Por exemplo, se a lista for [2, 3, 1] então será 
		uma rede de três camadas, com o primeira camada contendo 2 neurônios, 
		a segunda camada 3 neurônios, e a terceira camada 1 neurônio. Os bias 
		e pesos para a rede são inicializados aleatoriamente, usando uma 
		distribuição Gaussiana com média 0 e variância 1. Note que a primeira 
		camada é assumida como uma camada de entrada, e por convenção nós não 
		definimos nenhum bias para esses neurônios, pois os bias são usados 
		na computação das saídas das camadas posteriores."""

		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
		self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
		print(self.biases)
		print('\n')
		print(self.weights)

	def feedforward(self, network_input):
		for b, w in zip(self.biases, self.weights):
			network_input = sigmoid(np.dot(w, network_input)+b)
		return network_input

	def get_weight_biases(self):
		return {'biases': self.biases, 'weights': self.weights}

	def set_weight_biases(self, data):
		self.biases = data['biases']
		self.weights = data['weights']

# Função de Ativação Sigmóide
def sigmoid(z):
	return 1.0/(1.0+np.exp(-z))

if __name__=='__main__':
	rede = Network([1,2,1])
	print(rede.feedforward(1))
	print(rede.feedforward(2))
	print(rede.feedforward(3))
	print(rede.feedforward(4))