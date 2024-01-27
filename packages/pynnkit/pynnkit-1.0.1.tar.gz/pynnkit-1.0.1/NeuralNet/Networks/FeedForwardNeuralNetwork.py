"""
Standard Feed Forward Neural Network
"""
import numpy as np
import pickle
import os

from ..Layers.WeightLayer import WeightLayer
from ..Layers.ActivationLayer import ActivationLayer, SoftmaxActivationLayer
from ..Layers.LossLayer import LossLayer
from ..Layers.Activation.Activation import *
from ..Layers.Loss.Loss import *
from ..Layers.Initializers.Initializers import *

from ..Layers.Construct import *
from ..Layers.Activation.ActivationTypes import ActivationTypes
from ..Layers.Initializers.InitializerTypes import InitializerTypes
from ..Layers.Loss.LossTypes import LossTypes
from ..Layers.WeightLayerTypes import WeightLayerTypes



class FeedForwardNeuralNetwork:

	"""
	Implementation of a FeedForwardNeuralNetwork.

	IMPORTANT:

	!!!

	Input matrices and label matrices have to be of shape: (inputsize, batchsize)

	!!!

	Attributes:

	public:
	protected:

	layers: list of all the layers inside the network
	compiled: indicator if this NeuralNetwork is already built, i.e. the last layer was added.

	private:

	Methods:

	@static from_format(list[dict]) -> FeedForwardNeuralNetwork		: builds a NeuralNetwork from a specific format, which can be acquired 
																	: by calling the format method in this class
	format() -> list[dict]											: returns the format with all informations about this NeuralNetwork

	@static load(str) -> FeedForwardNeuralNetwork					: Loads a NeuralNetwork from a file, in which one was previously save by the save method

	save(str, bool override=False)									: Saves this NeuralNetwork into the path given.
																	: If a file with the same name already exists, and override is False, this method will do nothing.

	copy() -> FeedForwardNeuralNetwork								: Returns an identical shallow copy of the NeuralNetwork

	predict(np.array) -> np.array									: Returns the prediction for the given input of shape (inputsize, batchsize)

	train(	X: np.array, Y: np.array, 								: Trains the NeuralNetwork with input matrix X of shape (inputsize, batchsize)
			batchsize: int, epochs: int,							: and label matrix Y of shape (outputsize, batchsize).
			print_after_n_batches: int=None,						: epochs defines how many times the network will train on the data.
			TEST_X: np.array=None, TEST_Y: np.array=None, 			: batchsize states the size of the individual batches the training data willbe divided into.
			print_accuracy=True										: If batchsize is not given, SGD, i.e. batchsize = 1 will be chosen.
		)															: If print_after_n_batches is not None, the method train will print out the progress onto sys.stdout.
																	: What will be printed is the loss and, if print_accuracy=True, the accuracy.
																	: The training progress in terms of loss and accuracy will be drawn from X and Y if
																	: TEST_X and TEST_Y are None, else they will be drawn from TEST_X and TEST_Y

	loss(X: np.array, Y: np.array) -> float							: Returns the loss occurring when predicting the input data X and expecting the label Y
	
	_construct_layer(size, type, hyperparams)						: actual building process after first defining the input layer. This method is protected.

	add_layer(	size: int 											: Adds a WeightLayer and a ActivationLayer corresponding to the type_.
				type_: Types.TYPE, hyperparams: dict				: type_ must be from ActivationTypes, hyperparams include WeightLayerTypes instances.
																	: If the added layer is a softmax layer, the networks compiles by itself.

	add_custom_layer(	layer: BaseLayer							: Adds a custom layer, which has to be an instantiated Class derived from 
					)												: NeuralNet.Layers.BaseLayer.BaseLayer.

	add_loss(..Types.LossType)										: Adds the loss and finally compiles the network. The loss must be a specified type from LossTypes.
	
	add_custom_loss(Loss: Loss)										: Adds a custom Loss derived from: NeuralNet.Layers.Loss.Loss

	accuracy(X: np.array, Y: np.array) -> float						: Gives back the accuracy as a probability [0, 1] on input X with labels Y.

	_train_batch(self, batch: np.array, label: np.array)			: Trains the network on an indivdual batch. Protected, since this should only be used by the training method.

	_print_training_status(self, X, Y, batches_processed, 
							current_epoch, TEST_X=None, 
							TEST_Y=None, print_accuracy=False)		: Prints the training status out onto sys.stdout 	

	"""

	def __init__(self):

		#container for all the layers
		self._layers = []
		#if the network is compiled, it means all layers are added, and it is ready to start training or predicting
		self._compiled = False
		#memorizing previous layersize, layer construction by calling add_layer with just the size parameter
		self._prev_layersize = -1

	@staticmethod
	def from_format(used_format: list):
		
		back = FeedForwardNeuralNetwork()
		#build_from_format is defined in Format builder, since the function is very complex
		back._layers = build_from_format(used_format)
		
		#If the network has a loss layer, it is already compiled
		if (used_format[-1]["type"] == "LossLayer"):
			back._compiled = True

		return back

	def format(self):
		
		back = []
		#looping over all layers and getting their format
		for layer in self._layers:
			back.append(layer.format())

		return back

	@staticmethod
	def load(path: str):

		#in the path there is a list of formats of layers in order
		
		try:

			loaded_format = None
			with open(path, "rb") as f:
				loaded_format = pickle.load(f)

			return FeedForwardNeuralNetwork.from_format(loaded_format)

		except FileNotFoundError:

			print("unable to load from: " + path)

	def save(self, path: str, override=False):

		if os.path.isfile(path) and not override: #won't override already existing file
			print("Won't override", path, "!")
			return

		own_format = self.format()

		with open(path, "wb") as f:
			pickle.dump(own_format, f)

	def copy(self):

		return FeedForwardNeuralNetwork.from_format(self.format())

	def predict(self, X: np.array):
		
		#prediction can occur without being compiled

		x = X.copy()

		for layer in self._layers[:-1]:

			x = layer.forward(x)

		return x

	def _train_batch(self, batch: np.array, label: np.array):

		xin = batch

		#saving inputs and outputs for backpropagation
		xinouts = []

		#forward pass
		for el in self._layers[:-1]:

			xout = el.forward(xin)
			xinouts.append((xin, xout))
			xin = xout

		#now xinouts contains the tuple (Input, Output) for every layer

		#backward pass
		#first at the loss layer

		#for storing gradients
		error, grad = self._layers[-1].backward(xin, label)
		#grad does not have to be used to train, since we're checking a loss layer
		#now backward pass over all layers
		for i in range(len(self._layers)-2, -1, -1):

			xin, xout = xinouts[i][0], xinouts[i][1]

			#retreiving error and gradient
			error, grad = self._layers[i].backward(error, xin, xout)

			#if the gradient was not None, this was a Learnable Layer.
			if (grad is not None):

				self._layers[i].update(grad)

	def _print_training_status(self, X, Y, batches_processed, current_epoch, TEST_X=None, TEST_Y=None, print_accuracy=False):

		#data to store the last loss and the last accuracy
		last_loss = 0.0
		last_accuracy = 0.0

		if (TEST_X is None):

			last_loss = self.loss(X, Y)
			
		else:

			last_loss = self.loss(TEST_X, TEST_Y)

		if (print_accuracy):

			if (TEST_Y is not None):

				last_accuracy = self.accuracy(TEST_X, TEST_Y)

			else:

				last_accuracy = self.accuracy(X, Y)

		print("=== Training on batch", batches_processed, "with loss", last_loss, "in epoch", (current_epoch+1), "", end="")
		if (print_accuracy):
			print("and accuracy", last_accuracy, "", end="")
		print("===")



	def train	(self, 	X: np.array, Y: np.array, batchsize: int = 1, #X is the input, Y the labels
						epochs: int = 1, print_after_n_batches: int = None, #if print_after_n_batches = None, nothing will be printed
						TEST_X = None, TEST_Y = None,
						print_accuracy=False,
				):

		if (not self._compiled):

			raise RuntimeError("Tried training on an uncompiled Network!")

		if (len(X.shape) != 2):

			print("Your input array(X) shape is", X.shape, "contrary to (?, ?)")
			return

		if (len(Y.shape) != 2):

			print("Your label array(Y) shape is", Y.shape, "contrary to (?, ?)")
			return

		if (TEST_X is not None and len(TEST_X.shape) != 2):

			print("Your test array(TEST_X) shape is", TEST_X.shape, "contrary to (?, ?)")
			return

		if (TEST_Y is not None and len(TEST_Y.shape) != 2):

			print("Your label arrays shape is", TEST_Y.shape, "contrary to (?, ?)")
			return

		#keeping track of the epoch
		current_epoch = 0

		#divding into batches
		sample_size = X.shape[1]

		#dividing the input X into batches of similiar size, and one batch of leftover training samples
		batches = []
		ybatches = []
		restbatch = None
		restbatchsize = sample_size % batchsize #what's left over
		batches_size = int(sample_size / batchsize) #number of batches of size sample_size

		laststart = 0 #for saving where batches was last indexed

		for i in range(batches_size):

			batches.append(X[:, i*(batchsize):(i+1)*(batchsize)])
			ybatches.append(Y[:, i*(batchsize):(i+1)*(batchsize)])

			laststart = (i+1)*batchsize



		restbatch = X[:, laststart:X.shape[1]]
		restybatch = Y[:, laststart:Y.shape[1]]
		#now all batches and restbatch secured

		#for knowing how many batches have already been processed
		batches_processed = 0

		while current_epoch < epochs:

			#iterating over epochs

			#counter for determining the current batch
			counter = 0 
			#now training with every batch
			for batch in batches:

				self._train_batch(batch, ybatches[counter])
				#increasing counter
				counter += 1

				batches_processed += 1

				#now, if it is time to print
				if (print_after_n_batches is not None and not (batches_processed % print_after_n_batches)):

					self._print_training_status(X, Y, batches_processed, current_epoch, TEST_X, TEST_Y, print_accuracy)

			#training with restbatch

			if (restbatch.shape[1] != 0):

				self._train_batch(restbatch, restybatch)

				batches_processed += 1

				#now, if it is time to print
				if (print_after_n_batches is not None and not (batches_processed % print_after_n_batches)):

					self._print_training_status(X, Y, batches_processed, current_epoch, TEST_X, TEST_Y, print_accuracy)


			#training completed for this epoch


			current_epoch += 1

	def loss(self, X: np.array, Y: np.array) -> float:
		
		x = X.copy()

		for layer in self._layers[:-1]:

			x = layer.forward(x)

		return self._layers[-1].forward(x, Y)

	def _construct_layer(self, size, type_, hyperparams):


		#construction methods from NeuralNet.Layers.Construct
		weightlayer = construct_weightlayer(self._prev_layersize, size, hyperparams)
		activationlayer = construct_activationlayer(type_)

		self._layers.append(weightlayer)
		self._layers.append(activationlayer)

	def add_layer(self, size: int, type_: str=None, hyperparams: dict = {}):

		"""
		Hyperparams can include:

		learning_rate: -
		regularization_lambda: -
		weightinitializer: Instantiated Initializer
		biasinitializer: Instantiated Initializer
		"""

		#checking if trying to add a layer to an already compiled network
		if (self._compiled):

			print("Networks is already compiled!")
			raise RuntimeError("Tried adding a layer to a compiled FeedForwardNeuralNetwork")

		#if self._prev_layersize == -1, this is the first call, i.e. the specification of the input size
		if(self._prev_layersize == -1):
			#setting size for input layer
			self._prev_layersize = size
			return

		#if no activation type was given
		if (self._prev_layersize != -1 and type_ is None):
			print("Unspecified layer")
			raise RuntimeError("Tried adding a layer without specifications")

		if (type_ not in ActivationMap): #ActivationMap from NeuralNet.Layers.Activation.Activation

			print("Your activation type does not seem to be recognized...")
			raise RuntimeError("Incorrect activation type used")
		
		#now constructing
		self._construct_layer(size, type_, hyperparams)

		#if the type was softmax, there needs to be added a final kind of layer
		if (type_ == ActivationTypes.SOFTMAX):

			#adding last layer

			self._layers.append(LossLayer(Softmax_Categorical_Cross_Entropy_Loss()))
			self._compiled = True

		self._prev_layersize = size


	def add_custom_layer(self, layer, output_size):#output_size of your neural network for storing purposes
		
		if (self._compiled):

			print("Networks is already compiled!")
			raise RuntimeError("Tried adding a layer to a compiled FeedForwardNeuralNetwork")

		self._layers.append(layer)
		self._prev_layersize = output_size

	def add_loss(self, losstype):
		
		if (self._compiled):

			print("Networks is already compiled!")
			raise RuntimeError("Tried adding a layer to a compiled FeedForwardNeuralNetwork")

		if (losstype not in LossMap): #lossMap from NeuralNet.Layers.Loss.Loss

			print("Your loss type does not seem to be recognized...")
			raise RuntimeError("Incorrect loss type used")

		self._layers.append(construct_losslayer(losstype))
		self._compiled = True #finished building



	def add_custom_loss(self, losslayer):
		
		if (self._compiled):

			print("Networks is already compiled!")
			raise RuntimeError("Tried adding a layer to a compiled FeedForwardNeuralNetwork")

		self._layers.append(losslayer)
		self._compiled = True

	def __str__(self):
		
		back: str = ""
		for layer in self._layers[:-1]:

			back += str(layer)+ " -> "
		back += str(self._layers[-1])
		return back

	def accuracy(self, X: np.array, Y: np.array) -> float:
		
		#only reasonable for classification tasks

		P = self.predict(X)
		PT = P.T
		YT = Y.T

		rows = YT.shape[0]

		hits = 0
		for i in range(YT.shape[0]):

			if (np.argmax(PT[i]) == np.argmax(YT[i])):
				hits += 1

		acc = hits/rows

		return acc