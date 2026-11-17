#This method changes the resolution of a frame while keeping its pixel format the same. For example, it can resize a 1920 × 1080 frame to 640 × 360.

# Create a smaller RGB Surface
surf_small = vali.Surface.Make(
    vali.PixelFormat.RGB,
    640,
    360,
    gpu_id
)

# Create the resizer
resizer = vali.PySurfaceResizer(
    vali.PixelFormat.RGB,
    gpu_id
)

# Resize the frame
resizer.Run(surf_rgb, surf_small)

  ########  WE CAN USE PYSURFACEUD TO DO BOTH THE RESIZE AND CONVERT IN ONE STEP.  ########