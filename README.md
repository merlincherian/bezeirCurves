# Arbitrary-degree Bezier Curves

This program, evaluates a 3D arbitrary-degree Bezier curve and approximates it with a polyline. THe program will read in an arbitrary number of 3D points and will fit an arbitrary-degree Bezier curve to them. The curve's u parameter will be incremented by du during evaluation.

# Specifications

  - The u increment (a real number between 0 and 1) is specified by the -u du argument. Default value: 0.05
  - The radius of the spheres is specified by the -r radius argument. Default value: 0.1
  - Each Bezier curve is parameterized from 0 to 1, and will have degree N - 1.
