from typing import *

import numpy as np

import base64

def bytes2string(bytes : bytes, encoding : str = "ascii") -> str:

    return base64.b64encode(bytes).decode(encoding)

def string2bytes(base64_string : str) -> bytes:

    return base64.b64decode(base64_string)

class OptimizableClass(object):

    DEBUG_MODE = True

    @classmethod
    def optimize(cls) -> None:

        # disable debug mode
        cls.DEBUG_MODE = False

class ComplexFunction(OptimizableClass):

    def __init__(self, function   : Optional[ Callable ] = None,
                       derivative : Optional[ Callable ] = None,
                       inference  : Optional[ Callable ] = None, *,
                       is_average : Optional[ bool ]     = False) -> None:

        if (self.DEBUG_MODE):

            assert ((function is None) or (callable(function)))

            assert ((derivative is None) or (callable(derivative)))

            assert ((inference is None) or (callable(inference)))

            assert ((isinstance(is_average, bool)) or (isinstance(is_average, int)))

        # whether to pass object reference on inference for activation function and its derivative

        self.__function_self_ref   = True

        self.__derivative_self_ref = True

        self.__inference_self_ref  = True

        self.__is_average          = is_average

        # save reference to activation function and its derivative

        self._function   = function

        self._derivative = derivative

        self._inference  = inference

        # setting the object reference flags to False if function specified

        if (self._function is not None):
            self.__function_self_ref = False

        if (self._derivative is not None):
            self.__derivative_self_ref = False

        if (self._inference is not None):
            self.__inference_self_ref = False

    def define_function(self, target_function : Callable) -> None:

        if (self.DEBUG_MODE):
            assert callable(target_function)

        self._function = target_function

    def define_derivative(self, target_function : Callable) -> None:

        if (self.DEBUG_MODE):
            assert callable(target_function)

        self._derivative = target_function

    def define_inference(self, target_function : Callable) -> None:

        if (self.DEBUG_MODE):
            assert callable(target_function)

        self._inference = target_function

    def call_function(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        if (self._function is None):
            raise NotImplementedError("The function has not been defined. Try calling `define_function`.")

        if (self.__function_self_ref):
            return self._function(self, x, *args, **kwargs)

        return self._function(x, *args, **kwargs)

    def call_derivative(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        if (self._derivative is None):
            raise NotImplementedError("The function has not been defined. Try calling `define_derivative`.")

        if (self.__derivative_self_ref):
            return self._derivative(self, x, *args, **kwargs)

        return self._derivative(x, *args, **kwargs)

    def call_inference(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        if (self._inference is None):
            raise NotImplementedError("The function has not been defined. Try calling `define_inference`.")

        if (self.__inference_self_ref):
            return self._inference(self, x, *args, **kwargs)

        return self._inference(x, *args, **kwargs)
    
    def merge_losses(self, losses        : Iterable[ Union[ float, int ] ], 
                           sample_counts : Iterable[ int ]
            
            ) -> Tuple[ float, int ]:

        if (self.DEBUG_MODE):

            assert ((isinstance(losses, list)) or (isinstance(losses, tuple)) or (isinstance(losses, np.ndarray)))

            assert ((isinstance(sample_counts, list)) or (isinstance(sample_counts, tuple)) or (isinstance(sample_counts, np.ndarray)))

            assert (len(losses) == len(sample_counts))

        total_samples = int(np.sum(sample_counts))

        if (self.__is_average):
            return (float(np.dot(losses, sample_counts) / total_samples), total_samples)
        
        return (float(np.sum(losses)), total_samples)

    def __call__(self, x : np.ndarray, *args, **kwargs) -> np.ndarray:

        if (self.DEBUG_MODE):
            assert isinstance(x, np.ndarray)

        return self.call_inference(x, *args, **kwargs)
    

class NetworkLayer(OptimizableClass):
    pass

class NeuralNetwork(OptimizableClass):

    NETWORK_LAYERS = {}

    @classmethod
    def register_layer(cls, layer_class : Type[ "NetworkLayer" ]) -> Type[ "NetworkLayer" ]:

        cls.NETWORK_LAYERS[layer_class.__name__] = layer_class

        return layer_class
    
def batch_one_hot_encode(indices : np.ndarray, num_classes : Optional[ int ] = 10) -> np.ndarray:

    batch_size : int = len(indices)

    encoded_matrix : np.ndarray = np.zeros((batch_size, num_classes))

    for i in range(batch_size):
        encoded_matrix[i, indices[i]] = 1

    return encoded_matrix

def catch_error(default_value : Optional[ Any ] = None, ignore : Optional[ List[ Exception ] ] = []) -> Callable:

    ignore_tuple : Exception = tuple([  KeyboardInterrupt, *ignore  ])

    def _catch_error(function : Callable) -> Callable:

        def __catch_error(*args, **kwargs) -> Any:

            try:
                return function(*args, **kwargs)

            except ignore_tuple:
                raise

            except Exception:
                return default_value
            
        return __catch_error
    
    return _catch_error

def initialize_weights(target_size : tuple, n_input_nodes : int) -> np.ndarray:
    return np.random.randn(*target_size).reshape(target_size) * np.sqrt(2.0 / n_input_nodes)

class NeoVisUtils(object):

    SAFE_MODE = True

    @classmethod
    def apply_filter_condition(cls, f_query_string : str, condition : Dict[ str, str ]) -> str:

        if (cls.SAFE_MODE):

            assert isinstance(f_query_string, str)

            assert isinstance(condition, dict)

        return f_query_string.format(f"""{{{  ",".join(map(lambda x : f"{x[0]}: {repr(x[1])}", condition.items()))  }}}""")

    @classmethod
    def create_node_query_string(cls, counter : int, query_data : List[ Dict[ str, str ] ]) -> str:

        if (cls.SAFE_MODE):

            assert isinstance(counter, int)

            assert isinstance(query_data, list)

        if (counter == 1):
            return f"p{counter} = (n{counter}: `{query_data[counter-1][0]}`{{}})"

        return f"p{counter} = (n{counter}) - [r{counter}] -> (n{counter}: `{query_data[counter-1][0]}`{{}})"

    @classmethod
    def format_query(cls, query_data : List[ Dict[ str, str ] ]) -> str:

        if (cls.SAFE_MODE):
            assert isinstance(query_data, list)

        query_string = cls.apply_filter_condition(f"MATCH {cls.create_node_query_string(1, query_data)}", query_data[0][1])

        for counter in range(2, len(query_data) + 1):
            query_string += cls.apply_filter_condition(f" OPTIONAL MATCH p{counter} = (n{counter-1}) - [r{counter-1}] -> (n{counter}: `{query_data[counter-1][0]}`{{}})", query_data[counter-1][1])

        query_string += " RETURN " + ", ".join(f"p{counter}" for counter in range(1, len(query_data) + 1))

        return query_string

epsilon = 1e-7

if (__name__ == "__main__"):

    @catch_error()
    def parse_int(string : str) -> int:
        return int(string)
    
    print(parse_int("123"))

    print(parse_int("2-3"))