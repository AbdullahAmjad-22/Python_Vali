import python_vali as vali
import numpy as np
import torch

# Select GPU 0
gpu_id = 0

# Video file path
video_path = "video.mp4"

print("Available GPUs:", vali.GetNumGpus())

