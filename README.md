# Python Vali – Video Processing

## About the Project

This project explores **Python Vali**, a Python library used for GPU-accelerated video processing.

The goal is to understand how Vali handles video decoding, frame processing, GPU memory, and integration with PyTorch.

The project contains separate Python files, each demonstrating a different Vali method or concept.

## Concepts Covered

- Video decoding using `PyDecoder`
- Creating and managing Vali Surfaces
- Decoding individual video frames
- Seeking video frames using timestamps
- Converting pixel formats
- Resizing video frames
- Sharing GPU memory with PyTorch using DLPack
- Transferring frames from GPU to CPU using NumPy

## Project Structure

| File | Description |
|---|---|
| `01_install.py` | Installing Vali and checking GPU availability. |
| `02_decoder.py` | Creating a video decoder and accessing video information. |
| `03_surface.py` | Creating a Surface to store video frame data in GPU memory. |
| `04_decodeSurface.py` | Decoding video frames into a Vali Surface. |
| `05_SeekContext_TS.py` | Seeking to a specific video position using timestamps. |
| `06_SurfaceConvertor.py` | Converting video frames from one pixel format to another. |
| `07_SurfaceResizer.py` | Resizing video frames using GPU processing. |
| `08_dlPack.py` | Sharing Vali GPU memory with PyTorch tensors using DLPack. |
| `09_SurfaceDownloader.py` | Downloading frames from GPU memory into NumPy arrays. |

## Technologies Used

- Python
- Python Vali
- PyTorch
- NumPy
- NVIDIA CUDA
- NVIDIA GPU

## Requirements

- Python
- NVIDIA GPU
- Compatible NVIDIA drivers and CUDA environment
- Python Vali
- PyTorch
- NumPy

## Purpose

This is a learning and practice project focused on understanding Python Vali and its role in GPU-accelerated video processing.

Each file demonstrates a specific method or functionality, making it easier to understand and experiment with individual concepts.