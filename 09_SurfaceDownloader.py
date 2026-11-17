# This method copies image data from GPU memory into a NumPy array in CPU memory.
# It is useful when you want to display or inspect frames using OpenCV or Matplotlib.

# Create downloader
downloader = vali.PySurfaceDownloader(gpu_id)

# Allocate CPU memory
frame = np.empty(
    surf_rgb.HostSize,
    dtype=np.uint8
)

# Download the frame
ok, info = downloader.Run(surf_rgb, frame)

# Convert the flat array into an image
image = frame.reshape(
    surf_rgb.Height,
    surf_rgb.Width,
    3
)

print("Image shape:", image.shape)