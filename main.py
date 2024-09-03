# main.py

from utils.video_processor import extract_frames
from utils.optical_flow import compute_optical_flow
from utils.gps_handler import synchronize_gps_data
from utils.visual import plot_mouse_path
import pandas as pd

def main():
    # Paths to input files
    video_path = 'data/video.mp4'
    gps_data_path = 'output/gps_data_extracted.csv'  # Use the extracted GPS data file

    # Step 1: Extract frames from the video
    print("Extracting frames from video...")
    frames = extract_frames(video_path)
    
    # Step 2: Compute optical flow to track mouse movement
    print("Computing optical flow for movement tracking...")
    movement_data = compute_optical_flow(frames)
    
    # Step 3: Load the extracted GPS data
    print("Loading extracted GPS data...")
    gps_data = pd.read_csv(gps_data_path)
    
    # Step 4: Synchronize extracted GPS data with movement data
    print("Synchronizing GPS data with video frames...")
    synchronized_data = synchronize_gps_data(gps_data, movement_data)
    
    # Step 5: Visualize the results
    print("Visualizing the mouse path...")
    plot_mouse_path(synchronized_data)

    # Step 6: Save results
    print("Saving results to output/analysis_results.csv...")
    synchronized_data.to_csv('output/analysis_results.csv', index=False)
    
    print("Analysis complete!")

if __name__ == "__main__":
    main()
