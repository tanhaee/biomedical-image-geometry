"""Coordinate conversions for synthetic 3D images."""

from math import isfinite
from typing import Tuple


def voxel_to_physical(
    index_xyz: Tuple[int, int, int],
    spacing_mm: Tuple[float, float, float],
    origin_mm: Tuple[float, float, float],
) -> Tuple[float, float, float]:
    """Return the voxel centre in millimetres for identity orientation.

    All triples use (x, y, z) order. Indices are zero-based, spacing
    is in millimetres per voxel, and the origin is the physical centre
    of voxel (0, 0, 0). The image axes align with the physical axes.

    Raises:
        ValueError: A spacing value is nonfinite, zero or negative.
    """
    index_x, index_y, index_z = index_xyz
    spacing_x, spacing_y, spacing_z = spacing_mm
    origin_x, origin_y, origin_z = origin_mm

    if any(not isfinite(value) or value <= 0 for value in spacing_mm):
        raise ValueError("Voxel spacing must be finite and positive on all axes.")

    return (
        origin_x + index_x * spacing_x,
        origin_y + index_y * spacing_y,
        origin_z + index_z * spacing_z,
    )
