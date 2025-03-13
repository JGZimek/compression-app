from algorithm import Algorithm
from PIL import Image
import io

class PngCompressionAlgorithm(Algorithm):
    @staticmethod
    def compress(data, params: dict[str, str]):

        compression_level = int(params.get('compression_level', 6))
        filter_method = params.get('filter_method', 'NONE')

        output = io.BytesIO()

        data.save(output, format="PNG", compress_level=compression_level, optimize=True, filter=filter_method)

        return output.getvalue()

    @staticmethod
    def decompress(data, params: dict[str, str]):

        img = Image.open(io.BytesIO(data))

        return img
