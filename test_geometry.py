"""Tests for the voxel coordinate conversion."""

import unittest

from geometry import voxel_to_physical


class TestVoxelToPhysical(unittest.TestCase):
    def test_anisotropic_spacing_and_nonzero_origin(self):
        position = voxel_to_physical((2, 3, 4), (1.0, 2.0, 3.0), (10.0, 20.0, 30.0))
        self.assertEqual(position, (12.0, 26.0, 42.0))

    def test_zero_index_maps_to_origin(self):
        position = voxel_to_physical((0, 0, 0), (0.5, 2.0, 3.0), (-10.0, 20.0, 30.0))
        self.assertEqual(position, (-10.0, 20.0, 30.0))

    def test_rejects_invalid_spacing(self):
        invalid_spacings = (
            (0.0, 2.0, 3.0),
            (1.0, -2.0, 3.0),
            (1.0, 2.0, float("nan")),
            (1.0, 2.0, float("inf")),
        )
        for spacing in invalid_spacings:
            with self.subTest(spacing=spacing):
                with self.assertRaisesRegex(ValueError, "finite and positive"):
                    voxel_to_physical((2, 3, 4), spacing, (10.0, 20.0, 30.0))


if __name__ == "__main__":
    unittest.main()
