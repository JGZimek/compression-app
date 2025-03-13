from abc import ABC, abstractmethod


class Algorithm(ABC):
    """
    Abstract base class for compression algorithms.

    This class defines a standard interface for implementing compression algorithms.
    Subclasses must implement the `compress` and 'decompress' methods.

    Methods:
        compress(data, params): Abstract method for compressing data.
        decompress(data, params): Abstract method for decompressing data.
    """

    # TODO Add typing for data - how is the image stored (type()) and how is the audio signal stored?
    @staticmethod
    @abstractmethod
    def compress(data, params: dict[str, str]):
        """
        Compresses the given data using the specified parameters.

        :param data: The input data to be compressed preferably as a NumPy array.
        :param params: A dictionary of compression parameters as key-value string pairs.
        :return: The compressed data in a proper format.
        :raises NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError(
            "'Algorithm' is an abstract class, method 'compress' is not implemented."
        )

    # TODO Add typing for data
    # TODO If I understand this whole compression thing well enough:
    #  DECOMPRESS IS probably NOT NEEDED / POSSIBLE TO DO IF IM NOT MISTAKEN - So don't try to implement it
    #  I will delete it after we agree on it.
    @staticmethod
    @abstractmethod
    def decompress(data, params: dict[str, str]):
        """
        Decompresses the given compressed data using the specified parameters.

        :param data: The compressed data.
        :param params: A dictionary of decompression parameters as key-value string pairs.
        :return: The decompressed data as a NumPy array.
        :raises NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError(
            "'Algorithm' is an abstract class, method 'decompress' is not implemented."
        )

