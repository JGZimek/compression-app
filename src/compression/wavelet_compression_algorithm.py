from algorithm import Algorithm
import pywt
import numpy as np

class WaveletCompressionAlgorithm(Algorithm):

    @staticmethod
    def compress(data: np.ndarray, params: dict[str, str]) -> np.ndarray:

        wavelet = params.get("wavelet", "db4")
        level = int(params.get("level", 4))
        mode = params.get("mode", "symmetric")

        coeffs = pywt.wavedec(data, wavelet=wavelet, level=level, mode=mode)

        return coeffs

    @staticmethod
    def decompress(data: np.ndarray, params: dict[str, str]) -> np.ndarray:

        wavelet = params.get("wavelet", "db4")

        reconstructed_signal = pywt.waverec(data, wavelet=wavelet)

        return reconstructed_signal
