from src.compression.algorithm import Algorithm


class DummyAlgorithm(Algorithm):
    """
    Dummy implementation of the Algorithm class for testing purposes.
    This implementation simply returns the data unchanged.
    """

    @staticmethod
    def compress(data, params: dict[str, str]):
        """Mock compression: Returns the data unchanged."""
        return data

    @staticmethod
    def decompress(data, params: dict[str, str]):
        """Mock decompression: Returns the data unchanged."""
        return data
