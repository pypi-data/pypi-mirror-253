"""
Activation class represents a DerivableFunction
"""
import numpy as np
from abc import ABC, abstractmethod
from math import exp

from ...DerivableFunction import DerivableFunction
from .ActivationTypes import ActivationTypes

EPSILON = 10E-8
MAX_EXPONENT = 1E2

class Activation(DerivableFunction):

	"""
	Base class for all activations.
	Derived classes must implement:

	__call__(X_in, X_out), where X_in is the input to this function,
						   and output is what the function produced.
	"""

	def __init__(self, function):

		super().__init__(function)
		self.activationType = None

	@abstractmethod
	def __call__(self, X_in: np.array, X_out: np.array):
		pass

class Sigmoid(Activation):

	def sigmoid(x):

		if (x > 0):
			x = min(x, MAX_EXPONENT)
		else:
			x = max(x, -MAX_EXPONENT)

		return (1)/(1+exp(-x))

	def __init__(self):


		sigmoid = np.vectorize(Sigmoid.sigmoid)

		super().__init__(sigmoid)

		self.activationType = ActivationTypes.SIGMOID

	def derivative(self):

		if (self._order == 0):

			back = Sigmoid()
			sigmoid_d = np.vectorize(lambda x: x*(1-x))
			back.set_function(sigmoid_d) #setting derivative function
			back._order += 1 #increasing order to 1
			
			return back
	
		else:
			return None #no further derivative needed

	def __call__(self, X_in: np.array, X_out: np.array=None):

		if (self._function is None):
			return None

		#depending on what order this function is, it uses a different matrix
		if (self._order == 0):
			return self._function(X_in)
		elif (self._order == 1):
			return self._function(X_out)


	def __str__(self):
		return "Sigmoid" + "'"*self._order

class ReLU(Activation):

	def __init__(self):

		relu = np.vectorize(lambda x: (x if x > 0 else 0))
		super().__init__(relu)

		self.activationType = ActivationTypes.RELU

	def derivative(self):

		if (self._order == 0):

			back = ReLU()
			relu_d = np.vectorize(lambda x: (1 if x > 0 else 0))
			back.set_function(relu_d)
			back._order += 1

			return back

		else:
			return None

	def __call__(self, X_in: np.array, X_out: np.array=None):

		if(self._function is None):
			return None

		return self._function(X_in)

	def __str__(self):

		return "ReLU" + "'"*self._order

class Sign(Activation):

	def __init__(self):

		sign = np.vectorize(lambda x: (-1 if x < 0 else 1))
		super().__init__(sign)
		self.activationType = ActivationTypes.SIGN

	def derivative(self):

		if (self._order == 0):

			back = Sign()
			sign_d = np.vectorize(lambda x: 0)
			back.set_function(sign_d)
			back._order += 1

			return back

		else:
			return None

	def __call__(self, X_in: np.array, X_out: np.array=None):

		if(self._function is None):
			return None

		return self._function(X_in)

	def __str__(self):

		return "Sign"  + "'"*self._order

class Tanh(Activation):

	def tanh(x: float):

		if (x > 0):
			x = min(x, MAX_EXPONENT)
		else:
			x = max(x, -MAX_EXPONENT)

		ep = exp(x)
		em = exp(-x)

		return ((ep-em)/(ep+em + EPSILON))

	def __init__(self):

		super().__init__(np.vectorize(Tanh.tanh))
		self.activationType = ActivationTypes.TANH

	def derivative(self):

		if (self._order == 0):

			back = Tanh()
			tanh_d = np.vectorize(lambda x: (1-x*x))
			back.set_function(tanh_d)
			back._order += 1

			return back

		else:
			return None

	def __call__(self, X_in: np.array, X_out: np.array=None):

		if(self._function is None):
			return None

		if (self._order == 0):

			return self._function(X_in)

		elif (self._order == 1):

			return self._function(X_out)


	def __str__(self):

		return "Tanh" + "'"*self._order

class Linear(Activation):

	def __init__(self):

		super().__init__(np.vectorize(lambda x: x))
		self.activationType = ActivationTypes.LINEAR

	def derivative(self):

		if (self._order == 0):

			back = Linear()
			linear_d = np.vectorize(lambda x: 1)
			back.set_function(linear_d)
			back._order += 1

			return back

		else:
			return None

	def __call__(self, X_in: np.array, X_out: np.array=None):

		if(self._function is None):
			return None

		if (self._order == 0):

			return X_in

		elif (self._order == 1):

			return self._function(X_in)


	def __str__(self):

		return "Linear"  + "'"*self._order

class Softmax(Activation):

	def softmax(X):

		X = np.exp(X- np.max(X, axis=0, keepdims=True))

		return X / np.sum(X, axis=0, keepdims=True)


	def __init__(self):

		super().__init__(Softmax.softmax)
		self.activationType = ActivationTypes.SOFTMAX

	def derivative(self):

		return None #don't even want to bother

	def __call__(self, X_in: np.array, X_out: np.array=None):

		if(self._function is None):
			return None

		return self._function(X_in)


	def __str__(self):

		return "Softmax" + "'"*self._order


#final map
ActivationMap: dict = 	{
						ActivationTypes.SIGMOID : Sigmoid,
						ActivationTypes.RELU: ReLU,
						ActivationTypes.SIGN: Sign,
						ActivationTypes.SOFTMAX: Softmax,
						ActivationTypes.LINEAR: Linear,
						ActivationTypes.TANH: Tanh, 
					}