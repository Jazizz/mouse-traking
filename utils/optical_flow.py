# utils/optical_flow.py

import cv2
import numpy as np

def compute_optical_flow(frames):
    """Compute optical flow to track movement across frames."""
    gray_prev = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(gray_prev, mask=None, maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
    mask = np.zeros_like(frames[0])
    
    movement_data = []

    for i in range(1, len(frames)):
        gray_next = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
        p1, st, err = cv2.calcOpticalFlowPyrLK(gray_prev, gray_next, p0, None)

        good_new = p1[st == 1]
        good_old = p0[st == 1]

        for j, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (a, b), (c, d), (0, 255, 0), 2)
            frame = cv2.circle(frames[i], (a, b), 5, (0, 255, 0), -1)
        
        dx = np.mean(good_new[:, 0] - good_old[:, 0])
        dy = np.mean(good_new[:, 1] - good_old[:, 1])
        movement_data.append({'frame': i, 'dx': dx, 'dy': dy})

        gray_prev = gray_next.copy()
        p0 = good_new.reshape(-1, 1, 2)

    return movement_data
