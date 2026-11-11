# Biomedical Image Geometry

A small Python research-software project for exploring and testing
coordinate transformations in 3D imaging using synthetic data.

## Research problem

Image voxels are indexed by integers, while spatial measurements are
usually expressed in physical units such as millimetres. Correctly
handling image spacing, orientation and transformations is essential
when relating image data to 3D landmarks.

## Run the example

From the repository root, run `python example.py`. The example uses the
Python standard library and two synthetic landmarks. For each axis, it
multiplies the zero-based voxel index by the spacing in millimetres and
adds the physical origin.

```text
Image origin: (10.0, 20.0, 30.0) mm
Voxel spacing: (1.0, 2.0, 3.0) mm per voxel
Origin landmark: voxel (0, 0, 0) -> (10.0, 20.0, 30.0) mm
Offset landmark: voxel (2, 3, 4) -> (12.0, 26.0, 42.0) mm
```

Run `python -m unittest -v` to check the conversion and spacing validation.

## Planned example

1. Generate a synthetic 3D volume and landmarks.
2. Convert voxel coordinates to physical coordinates.
3. Apply a rigid transformation.
4. Visualise image slices and landmarks.
5. Save the parameters needed to reproduce the example.

## Development goals

- Small, reusable Python modules.
- Tests with known expected results.
- Reproducible installation and examples.
- Clear documentation for users and contributors.

## Status

Early development. The current version converts landmarks for images whose
axes align with the physical coordinate axes.

## Scope and data

This is an independent portfolio demonstration using synthetic data.
It contains no patient data or code from restricted research projects.
It is intended for learning and software demonstration.

## Author

Ghazaleh Tanhaei
