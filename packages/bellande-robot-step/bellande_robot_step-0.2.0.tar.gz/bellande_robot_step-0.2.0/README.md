# 📦 Bellande Step

### ✔️ confirmed versions
- `The step function efficiently computes the next step towards a target node within a specified distance limit.`

### Usage 2D Space

Suppose you have two nodes representing positions in a 2D space:
- `node0` at coordinates `(0, 0)`
- `node1` at coordinates `(5, 5)`

You want to compute the next step from `node0` towards `node1` while limiting the maximum distance to 3 units.

```python
# Define the nodes
node0 = Node(0, 0)
node1 = Node(5, 5)

# Compute the next step within a distance limit of 3 units
next_step = bellande_step_2d(node0, node1, limit=3)

# Output the coordinates of the next step
print("Next Step Coordinates:", next_step.coord) 
```

## Usage 3D Space

Suppose you have two nodes representing positions in a 3D space:
- `node0` at coordinates `(0, 0, 0)`
- `node1` at coordinates `(5, 5, 5)`

You want to compute the next step from `node0` towards `node1` while limiting the maximum distance to 3 units.

```python
# Define the nodes
node0 = Node(0, 0, 0)
node1 = Node(5, 5, 5)

# Compute the next step within a distance limit of 3 units
next_step = bellande_step_3d(node0, node1, limit=3)

# Output the coordinates of the next step
print("Next Step Coordinates:", next_step.coord)
```

### Avaliable
- 2D Space
- 3D Space
- 4D Space
- 5D Space
- 6D Space
- 7D Space
- 8D Space
- 9D Space
- 10D Space


## Website
- https://pypi.org/project/bellande_robot_step/

### Installation
- `$ pip install bellande_robot_step`

```
Name: bellande_robot_step
Version: 0.1.0
Summary: Computes the next step towards a target node
Home-page: github.com/RonaldsonBellande/bellande_robot_step
Author: Ronaldson Bellande
Author-email: ronaldsonbellande@gmail.com
License: GNU General Public License v3.0
Requires: numpy
Required-by:
```

### License
This Package is distributed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html), see [LICENSE](https://github.com/RonaldsonBellande/bellande_robot_step/blob/main/LICENSE) and [NOTICE](https://github.com/RonaldsonBellande/bellande_robot_step/blob/main/LICENSE) for more information.
