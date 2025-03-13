from abc import ABC, abstractmethod


class Algorithm(ABC):
    """
    # TODO Add docstring
    ...
    """

    # TODO Add typing for data - how is the image stored (type()) and how is the audio signal stored?
    @staticmethod
    @abstractmethod
    def compress(data, params: dict[str, str]):
        """
        # TODO Fill docstring
        :param data:
        :param params:
        """
        raise NotImplementedError(
            "'Algorithm' is an abstract class, method 'compress' is not implemented."
        )

    # TODO Decompressed signal could be useful to compare the loss of the data when decompressing (an addition)
    # TODO Add typing for data
    @staticmethod
    @abstractmethod
    def decompress(data, params: dict[str, str]):
        """
        # TODO Fill docstring
        :param data:
        :param params:
        """
        raise NotImplementedError(
            "'Algorithm' is an abstract class, method 'decompress' is not implemented."
        )

