"""
Pre-Implemented ActivationLayers:

ReLU
Sigmoid
Sign
Tanh
Linear
Softmax
"""
import numpy as np
from .BaseLayer import BaseLayer
from .Activation.Activation import *
from .Activation.ActivationTypes import ActivationTypes

class ActivationLayer(BaseLayer):


	def __init__(self, activation):

		"""
		Initializes this class with a given activation function.
		The given function function must be a subclass of DerivableFunction
		"""
		
		self._activation_function = activation
		self._activation_function_d = activation.derivative()

	def forward(self, X: np.array):

		"""
		Forward pass of the layer. Passes the given np.array of shape: (input_size, batch_size)
		into the activation function, and returns the result.
		"""
		
		return self._activation_function(X)

	def backward(self, Error: np.array, X_in: np.array, X_out: np.array):

		"""
		Backward pass of the layer.
		Returns a tuple with the Error multiplied with he first derivative of the activation function
		as the first parameter, None as the second since this layer does not have changable parameters.
		"""
		
		return (Error * self._activation_function_d(X_in, X_out), None)

	def format(self) -> dict:

		"""
		Returns a dict of form:

		{"type": "ActivationLayer", "function": self._activation_function}
		"""
		
		return {"type": "ActivationLayer", "function": self._activation_function}

	@staticmethod
	def from_format(form):

		"""
		Constructs and returns a ActivationLayer based off a format created via the format method.
		"""

		instantiated_function = form["function"]
		return ActivationLayer(instantiated_function)

	def copy(self):

		"""
		Returns a copy of this layer.
		"""
		
		return ActivationLayer(type(self._activation_function)())

	def __str__(self):
		"""
		Returns a string corresponding to the activation function inside this layer
		"""
		return "["+str(self._activation_function)+"]"

class SoftmaxActivationLayer(ActivationLayer):

	"""
	This class gets preinitialized with the softmax function.
	Other than that, the functions stay the same.
	"""

	def __init__(self, dummy=None):#dummy for format builder

		super().__init__(Softmax())

	def backward(self, Error: np.array, X_in: np.array, X_out: np.array):

		return (Error, None)

	def copy(self):

		return SoftmaxActivationLayer(type(self._activation_function)())

	def format(self) -> dict:
		
		return {"type": "SoftmaxActivationLayer", "function": self._activation_function}

	@staticmethod
	def from_format(form):

		return SoftmaxActivationLayer()
