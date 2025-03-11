from algorithm import Algorithm


class CompressionReport:
    """
    # TODO Add docstring
    ...
    """

    def __init__(self, data, algorithm_class: Algorithm, params):
        """
        # TODO Fill docstring

        :param data:
        :param algorithm_class:
        :param params:
        """
        self.data = data
        self.algorithm_class: Algorithm = algorithm_class
        self.params = params
        self.mse_numerical = None
        self.mse_image = None
        self.mse_audio = None  # TODO RETHINK THESE TWO
        self.data_after_decompression: type(data) | None = None

    def run(self):
        """
        # TODO Fill docstring
        ...
        """
        self.algorithm_class.compress(self.data, self.params)
