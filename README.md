# Anime Face Generation with StyleGAN

After seeing a demo of StyleGAN at an AI@UCI workshop, I wondered if it could be applied to anime faces. Turns out someone else had the idea as well! This is my implementation using my own custom dataset.

### Goal:
<img src='img/reals.png'>

### Current Training:
<img src='img/training.gif'>

### Environment
OS: Windows 10
GPU: Nvidia GTX 2070
Conda environment packages:
 - python==3.6
 - tensorflow-gpu==1.12.0
 - cudatoolkit==9.0
 - cudnn==7.6.0
 - opencv, pillow, numpy, scipy, lmdb, requests

### Data Preparation 
StyleGAN is very particular about how it reads its data. The repo provides a *dataset_tool.py* file to help (and increase your dataset's disk space by a factor of ~19). My dataset creation workflow is as follows:
1. Download raw images using **Grabber**, an image board downloader.
2. Crop anime faces from raw images using **lbpcascade_animeface**.
3. Upscale resolutions with **waifu2x**.
4. Convert to JPG.
5. Scale images to 512x512.
6. Create StyleGAN dataset with *dataset_tool.py*.

### Resources:
- [Making Anime Faces With StyleGAN - GWERN](https://www.gwern.net/Faces)
- [StyleGAN](https://github.com/NVlabs/stylegan)
- [Grabber - Image Board Downloader](https://github.com/Bionus/imgbrd-grabber)
- [lbpcascade_animeface - Anime/Manga Face Detector](https://github.com/nagadomi/lbpcascade_animeface)
- [Waifu2x](https://github.com/nagadomi/waifu2x)