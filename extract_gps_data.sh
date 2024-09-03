# extract_gps_data.sh

#!/bin/bash

# Ensure the output directory exists
mkdir -p output

# Extract the metadata from the GoPro video using ffmpeg
ffmpeg -y -i data/video.mp4 -codec copy -map 0:3 -f rawvideo output/meta.bin

# Use exiftool to extract GPS data from the GoPro video to a CSV file
exiftool -ee -G3 -p "$gpsTimeStamp, $gpsLatitude, $gpsLongitude, $gpsAltitude" data/video.mp4 > output/gps_data_extracted.csv

echo "GPS data extraction complete. Saved to output/gps_data_extracted.csv"
