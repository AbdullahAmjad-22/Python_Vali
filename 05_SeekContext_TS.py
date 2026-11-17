#Seek Context is used to seek the context at a specific timestamp. we can also use seek frame to seek the context of a specific frame.
# Seek to 2 seconds
seek = vali.SeekContext(seek_ts=2.0)

ok, info = dec.DecodeSingleSurface(surf, seek)

print("Seek result:", ok, info)