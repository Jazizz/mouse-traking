# utils/gps_handler.py

import pandas as pd

def synchronize_gps_data(gps_data, movement_data):
    """Synchronize GPS data with video frame data."""
    frame_rate = 30  # Assuming 30 frames per second
    gps_data['Frame'] = gps_data['Time'].apply(lambda t: int(t * frame_rate))

    synchronized_data = pd.merge(pd.DataFrame(movement_data), gps_data, how='inner', left_on='frame', right_on='Frame')
    return synchronized_data
