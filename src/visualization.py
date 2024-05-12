import matplotlib.pyplot as plt

def plot_network_traffic(data):
    """
    Plot network traffic data.

    Parameters:
    - data (list): List of tuples containing (timestamp, traffic_volume) data points.
    """
    timestamps = [point[0] for point in data]
    traffic_volume = [point[1] for point in data]

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, traffic_volume, color='blue')
    plt.title('Network Traffic Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Traffic Volume')
    plt.grid(True)
    plt.show()
