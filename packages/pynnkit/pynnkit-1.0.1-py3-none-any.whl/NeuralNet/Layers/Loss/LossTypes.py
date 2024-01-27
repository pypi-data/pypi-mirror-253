#collection of all natively supported Loss Types

from enum import Enum, auto

class LossTypes(Enum):

	L1_LOSS = auto()
	L2_LOSS = auto()
	CATEGORICAL_CROSS_ENTROPY_LOSS = auto()
	BINARY_CROSS_ENTROPY_LOSS = auto()
	SOFTMAX_CROSS_ENTROPY_LOSS = auto()
	#HINGE_LOSS = auto()
	#PERCEPTRON_CRITERION = auto()