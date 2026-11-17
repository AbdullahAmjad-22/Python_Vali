#PySurfaceConvertor is used to convert a surface from one pixel format to another. for example in this case from NV12 to RGB.

# Create an RGB destination Surface
surf_rgb = vali.Surface.Make(
    vali.PixelFormat.RGB,
    dec.Width,
    dec.Height,
    gpu_id
)

# Create the converter
cvt = vali.PySurfaceConverter(gpu_id)

# Convert the frame
ok, info = cvt.Run(surf, surf_rgb)

print("Conversion:", ok, info)

  ########  WE CAN USE PYSURFACEUD TO DO BOTH THE RESIZE AND CONVERT IN ONE STEP.  ########