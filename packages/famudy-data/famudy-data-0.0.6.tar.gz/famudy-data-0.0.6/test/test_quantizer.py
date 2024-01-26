from unittest import TestCase

import numpy as np

from famudy.util.quantization import Quantizer


class QuantizerTest(TestCase):
    def test_shapes(self):
        quantizer = Quantizer(np.array([-1, -2, -3, -4, -5]), 1, 16, mask_value=None)

        B = 1000
        D = 5
        coordinates = np.random.rand(B, D) * 2 - 1
        encoded_coordinates = quantizer.encode(coordinates)
        decoded_coordinates = quantizer.decode(encoded_coordinates)

        mean_error = np.linalg.norm(decoded_coordinates - coordinates, axis=-1).mean()
        self.assertLess(mean_error, 1e-4)