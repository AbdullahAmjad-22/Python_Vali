# This method takes compressed video data and decodes one frame into the Surface. The resulting image is stored in GPU memory.
ok, info = dec.DecodeSingleSurface(surf)

print("Success:", ok)
print("Information:", info)



# This method decodes frames one after another instead of jumping to a particular frame. It is useful when you want to process or count frames in a video.
dec_frames = vali.PyDecoder(video_path, {}, gpu_id=gpu_id)

surf_frames = vali.Surface.Make(
    dec_frames.Format,
    dec_frames.Width,
    dec_frames.Height,
    gpu_id
)

# Decode the first 10 frames
for i in range(10):
    ok, info = dec_frames.DecodeSingleSurface(surf_frames)

    if not ok:
        print("Decoding stopped:", info)
        break

    print("Decoded frame:", i)