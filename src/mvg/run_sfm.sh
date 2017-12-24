!bin/bash

rm video.mp4
ffmpeg -i http://192.168.10.48:8080/video -c copy -flags +global_header video.mp4
rm -rf frames
mkdir frames
cd output
rm -rf disparity
rm -rf keypoints
rm -rf rectified
mkdir disparity
mkdir keypoints
mkdir rectified
cd ..

ffmpeg -i "video.mp4" frames/image-%3d.jpg
python2 structure_from_motion.py