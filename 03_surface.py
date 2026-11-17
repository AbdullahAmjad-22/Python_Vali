# A Surface is Vali's container for storing image data in GPU memory.
surf = vali.Surface.Make(
    dec.Format,
    dec.Width,
    dec.Height,
    gpu_id
)