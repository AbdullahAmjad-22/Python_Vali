#This method allows PyTorch to access Vali's GPU image memory directly. It avoids copying the image data into another GPU allocation.

# Convert the processed Surface into a tensor
tensor = torch.from_dlpack(surf_float)

print("Shape:", tensor.shape)
print("Data type:", tensor.dtype)
print("Device:", tensor.device)