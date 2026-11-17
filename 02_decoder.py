#opens the video and prepares it for decoding
dec = vali.PyDecoder(video_path, {}, gpu_id=gpu_id)

#These properties tell us about the video before processing it. They include resolution, frame rate, duration and pixel format.
print("Width:", dec.Width)
print("Height:", dec.Height)
print("FPS:", dec.Framerate)
print("Average FPS:", dec.AvgFramerate)
print("Duration:", dec.Duration)
print("Total Frames:", dec.NumFrames)
print("Pixel Format:", dec.Format)
print("Variable Frame Rate:", dec.IsVFR)