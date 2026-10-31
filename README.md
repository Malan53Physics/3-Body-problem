# 3-Body-problem
The three-body problem is a famous physics and mathematics puzzle about predicting the motion of three celestial bodies (such as planets, stars, or moons) as they interact with each other through Newton's law of universal gravitation.


## Why this problem?

The three-body problem has no general closed-form solution, and most starting conditions are chaotic: a tiny change in the initial positions or velocities leads to a completely different path. A few special cases are stable, such as the figure-eight orbit found by Chenciner and Montgomery in 2000, where all three bodies chase each other along one figure-eight curve.

## Features
- Seven starting setups:
 - Random positions and velocities
 - Lagrange-style triangle
 - Figure-eight orbit
 - Binary pair with a satellite
 - Cinematic collision (weaker gravity, longer trails)
 - Predefined binary
 - User-defined (you type in positions and velocities)
- Choice of window size (HD, 4K, 8K)
- Colored bodies with trails
- Softening term (1e-4) to avoid division by zero when two bodies get very close

## How it works

Each body feels the gravitational pull of the other two. For body i, the acceleration is:

```
a_i = sum over j != i of  G * (r_j - r_i) / |r_j - r_i|^3

```

(All masses are set to 1.) Every frame, the program updates the velocities from the accelerations, then updates the positions from the new velocities. This is the semi-implicit (symplectic) Euler method, with time step dt = 0.008.

## Requirements
- Python 3.8+
- NumPy
- Matplotlib
```
pip install numpy matplotlib
```

## Running it
```
python Three_Body_Problem_version1.py
```

## Credits and process

Started from a basic simulation built with help from my CS teacher, YouTube tutorials, Google, and AI tools. I used them to learn the physics and code structure.
