"""
Function, that can give back it's derivative. Used for Loss Functions and Activation Functions
"""
import numpy as np
from abc import ABC, abstractmethod

class DerivableFunction(ABC):

	def __init__(self, function=None):
		"""
		Initializes this class with a given function.
		The given function will be used when this instance is called
		"""
		self._function = function
		self._order = 0

	@abstractmethod
	def __call__(self):
		"""
		Standard Function call
		"""
		pass

	@abstractmethod
	def derivative(self):
		"""
		Gives back the derivative based on the order
		"""
		pass

	@abstractmethod
	def __str__(self):
		"""
		Returns a unique string representation
		"""
		pass

	def set_function(self, function):
		"""
		Changes the given function
		"""
		self._function = function




