import numpy as np
import unittest

from dummy_algorithm import DummyAlgorithm


class TestAlgorithm(unittest.TestCase):
    """Unit tests for the Algorithm class and its implementations."""

    def setUp(self):
        """Set up test data before each test."""
        self.image_data = np.random.randint(
            0, 256, (100, 100, 3), dtype=np.uint8
        )  # Random image
        self.audio_data = np.random.rand(44100)  # Simulated 1-second audio signal
        self.numerical_data = [1, 2, 3, 4, 5]  # Simple numerical sequence
        self.params = {"quality": "high"}  # Example parameters
        self.algorithm = DummyAlgorithm()

    def test_compress_not_implemented(self):
        """Ensure Algorithm class raises NotImplementedError for compress()."""
        with self.assertRaises(NotImplementedError):
            Algorithm.compress(self.image_data, self.params)

    def test_decompress_not_implemented(self):
        """Ensure Algorithm class raises NotImplementedError for decompress()."""
        with self.assertRaises(NotImplementedError):
            Algorithm.decompress(self.image_data, self.params)

    def test_dummy_compress(self):
        """Test that DummyAlgorithm's compress method returns the same data."""
        compressed = self.algorithm.compress(self.image_data, self.params)
        self.assertTrue(np.array_equal(compressed, self.image_data))

    def test_dummy_decompress(self):
        """Test that DummyAlgorithm's decompress method returns the same data."""
        decompressed = self.algorithm.decompress(self.image_data, self.params)
        self.assertTrue(np.array_equal(decompressed, self.image_data))

    def test_compress_different_data_types(self):
        """Test that compress works for different data types."""
        for data in [self.image_data, self.audio_data, self.numerical_data]:
            compressed = self.algorithm.compress(data, self.params)
            self.assertEqual(type(compressed), type(data))

    def test_decompress_different_data_types(self):
        """Test that decompress works for different data types."""
        for data in [self.image_data, self.audio_data, self.numerical_data]:
            decompressed = self.algorithm.decompress(data, self.params)
            self.assertEqual(type(decompressed), type(data))


if __name__ == "__main__":
    unittest.main()
