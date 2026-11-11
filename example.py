"""Convert two synthetic image landmarks to physical coordinates."""

from geometry import voxel_to_physical


def main() -> None:
    spacing_mm = (1.0, 2.0, 3.0)
    origin_mm = (10.0, 20.0, 30.0)
    landmarks = {
        "Origin landmark": (0, 0, 0),
        "Offset landmark": (2, 3, 4),
    }

    print(f"Image origin: {origin_mm} mm")
    print(f"Voxel spacing: {spacing_mm} mm per voxel")
    for name, index_xyz in landmarks.items():
        position_mm = voxel_to_physical(index_xyz, spacing_mm, origin_mm)
        print(f"{name}: voxel {index_xyz} -> {position_mm} mm")


if __name__ == "__main__":
    main()
