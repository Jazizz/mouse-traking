# utils/video_processor.py

import cv2

def extract_frames(video_path):
    """Extract frames from a video file."""
    cap = cv2.VideoCapture(video_path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    print(f"Total frames extracted: {len(frames)}")
    return frames
