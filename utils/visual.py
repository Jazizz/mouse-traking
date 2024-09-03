# utils/visualizer.py

import matplotlib.pyplot as plt

def plot_mouse_path(data):
    """Plot the mouse path in 3D space."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(data['Longitude'], data['Latitude'], data['Altitude'], label='Mouse Path')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Altitude')
    plt.legend()
    plt.show()
