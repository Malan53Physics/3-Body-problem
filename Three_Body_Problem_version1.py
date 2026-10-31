import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Resolution 
print("Choose resolution:")
print("1: HD (1800x1000)")
print("2: 4K (3840x2160)")
print("3: 8K (7680x4320)")
res = input("Enter choice (1-3): ")

res_map = {"1": (1800, 1000), "2": (3840, 2160), "3": (7680, 4320)}
WIDTH, HEIGHT = res_map.get(res, (1800, 1000))

presets = [
    "Random",
    "Lagrange",
    "Figure-eight",
    "Binary + satellite",
    "Cinematic collision",
    "Predefined binary",
    "User-defined",
]

print("\nChoose 3-body system:")
for i, name in enumerate(presets, 1):
    print(f"{i}: {name}")

choice = input("Enter choice (1-7): ")

if choice == "1":
    pos = np.random.uniform(-5, 5, (3, 2))
    vel = np.random.uniform(-0.4, 0.4, (3, 2))
    G = 1.0

elif choice == "2":
    pos = np.array([[0.0, 2.0], [-1.732, -1.0], [1.732, -1.0]])
    vel = np.array([[0.5, 0.0], [-0.25, 0.43], [-0.25, -0.43]])
    G = 1.0

elif choice == "3":
  
    p1 = [0.97000436, -0.24308753]
    v3 = [-0.93240737, -0.86473146]
    pos = np.array([p1, [-p1[0], -p1[1]], [0.0, 0.0]])
    vel = np.array([[-v3[0] / 2, -v3[1] / 2], [-v3[0] / 2, -v3[1] / 2], v3])
    G = 1.0

elif choice == "4":
    pos = np.array([[-2.0, 0.0], [2.0, 0.0], [0.0, 1.0]])
    vel = np.array([[0.0, 0.35], [0.0, -0.35], [-0.25, 0.0]])
    G = 1.0

elif choice == "5":
    pos = np.array([[-3.0, 0.0], [3.0, 0.0], [0.0, 2.2]])
    vel = np.array([[0.18, 0.22], [-0.18, -0.22], [0.00, -0.12]])
    G = 0.55

elif choice == "6":
    pos = np.array([[-3.0, 0.0], [3.0, 0.0], [0.0, 0.6]])
    vel = np.array([[0.0, 0.3], [0.0, -0.3], [0.15, 0.0]])
    G = 1.0

elif choice == "7":
    pos = np.zeros((3, 2))
    vel = np.zeros((3, 2))
    for i in range(3):
        pos[i] = [float(x) for x in input(f"Enter x y for body {i+1}: ").split()]
        vel[i] = [
            float(v) for v in input(f"Enter vx vy for body {i+1}: ").split()
        ]
    G = 1.0

else:
    raise SystemExit("Exiting: invalid choice.")

pos = pos.astype(float)
vel = vel.astype(float)

dt = 0.008
steps = 3500
trail_len = 180 if choice == "5" else 90
history = [[] for _ in range(3)]


def acceleration(p):
    a = np.zeros_like(p)
    for i in range(3):
        for j in range(3):
            if i != j:
                r = p[j] - p[i]
                d = np.linalg.norm(r) + 1e-4
                a[i] += G * r / (d**3)
    return a


fig, ax = plt.subplots(figsize=(WIDTH / 100, HEIGHT / 100))
ax.set_facecolor("black")
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)
ax.set_xticks([])
ax.set_yticks([])

colors = ["gold", "cyan", "magenta"]
stars = [ax.plot([], [], "o", markersize=8, color=colors[i])[0] for i in range(3)]
trails = [
    ax.plot([], [], lw=1, alpha=0.6, color=colors[i])[0] for i in range(3)
]


def update(frame):
    global pos, vel

    vel += acceleration(pos) * dt
    pos += vel * dt

    for i in range(3):
        history[i].append(pos[i].copy())
        if len(history[i]) > trail_len:
            history[i].pop(0)

        h = np.array(history[i])
        stars[i].set_data([pos[i, 0]], [pos[i, 1]])
        trails[i].set_data(h[:, 0], h[:, 1])

    return stars + trails

#pls run
ani = FuncAnimation(fig, update, frames=steps, interval=20, blit=False)
plt.show()


#with help of cs teacher and youtube and AIs + google for referance
