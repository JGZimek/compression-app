import numpy as np

from algorithm import Algorithm


class CompressionReport:
    """
    A class that generates a report on data compression using a specified algorithm.
    This class applies a given compression algorithm to the provided data and
    stores relevant metrics.

    Attributes:
        data: The original data to be compressed.
        algorithm_class (Algorithm): The compression algorithm class to be used.
        params: Parameters for configuring the compression algorithm.
        mse_numerical: Mean squared error of the original data and compressed data as a number.
        mse_image: Mean squared error of the original data and compressed data for image signal.
        mse_audio: Mean squared error of the original data and compressed data for audio signal.
        data_after_decompression: The data after decompression, of the same type as `data`.
    """

    def __init__(
        self, data, algorithm_class: Algorithm, params
    ):  # TODO Add 'data' typing
        """
        Initializes the CompressionReport instance.

        :param data: The input data to be compressed.
        :param algorithm_class: An instance of the Algorithm class representing
                                the compression algorithm to be used.
        :param params: A dictionary containing parameters for the compression algorithm.
        """
        self.data = data  # TODO Add typing when it becomes clear
        self.algorithm_class: Algorithm = algorithm_class
        self.params: dict[str, str] = params
        self.compressed_data = None  # TODO Add typing when it becomes clear
        self.mse_numerical: float | None = None
        self.mse_image = None  # TODO Add typing when it becomes clear
        self.mse_audio = None  # TODO Add typing when it becomes clear # TODO RETHINK THESE TWO FIELDS
        self.data_after_decompression: type(data) | None = None

    def run(self):
        """
        Runs the compression algorithm on the given data.

        This method applies the compression process using the specified algorithm and parameters,
        and then creates an object that holds every necessary information about the compression process.
        """
        self.compressed_data = self.algorithm_class.compress(
            self.data, self.params
        )  # TODO Add typing
        self.calculate_measures()

    def calculate_measures(self) -> None:
        """
        Calculates the mean squared error (MSE) for different types of data.

        This method compares the original data and the decompressed data to measure
        the degradation introduced by compression.

        # TODO Fix Docstring, when the data and it's representation typing will be known
        - If the data is numerical (e.g., a NumPy array or list of numbers), it calculates `mse_numerical`.
        - If the data represents an image (NumPy array with shape (H, W) or (H, W, C)), it calculates `mse_image`.
        - If the data represents an audio signal (1D NumPy array), it calculates `mse_audio`.

        The results are stored in the corresponding class attributes.
        """
        if self.compressed_data is None:
            raise ValueError("Compressed data is not available.")

        def calculate_mse(original, compressed):
            """
            Calculates the Mean Squared Error (MSE) between the original and compressed data.

            :param original: The original uncompressed data.
            :param compressed: The compressed data.
            :return: The computed MSE value as a float.
            """
            return np.mean((np.array(original) - np.array(compressed)) ** 2)

        # TODO The code below could be refactored, when I will know the possible datatypes for data and compressed data
        if isinstance(self.data, np.ndarray):
            if len(self.data.shape) == 1:  # Likely numerical or audio data
                self.mse_audio = calculate_mse(self.data, self.compressed_data)
            elif len(self.data.shape) in [2, 3]:  # Likely an image
                self.mse_image = calculate_mse(self.data, self.compressed_data)
        elif isinstance(self.data, (list, tuple)) and all(
            isinstance(x, (int, float)) for x in self.data
        ):
            self.mse_numerical = calculate_mse(self.data, self.compressed_data)
