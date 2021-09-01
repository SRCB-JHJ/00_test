# PanoSLAM

**Version: 0.0.1**

This repository version is just for Haijing to test, and I does not guarantee the normal operation of the system.

## Installation

To use this system there are a few dependencies. Most of them are Python-based, but there are a few binary package needed as well.

Firstly, you should install the Python dependencies. I recommend using a conda or virtualenv environment at the very least. All of this code expects Python3.6+ and PyTorch >
1.4.0. Once you have your environment activated, install the Python dependencies with:

```
pip install -r requirements.txt
```

### 1. Spherical Distortion Package

This package contains the backend code for [Mapped Convolutions](https://github.com/meder411/MappedConvolutions) and [Tangent Images](https://github.com/meder411/Tangent-Images). Is it installable as
Python package, and is built around PyTorch. The mapped convolution operations as well as the resampling operations for tangent images are written in a mix of C++ and CUDA and wrapped as PyTorch
modules.

This package requires 3 non-Python dependencies: [Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page), [CGAL](https://www.cgal.org/), and [OpenEXR](https://www.openexr.com/).

To manually install [Eigen-3.3.4](https://gitlab.com/libeigen/eigen/-/releases/3.3.4) from source, first navigate to the desired directory and then run the following commands:

#### Building

```
cd eigen 
mkdir build 
cd build 
cmake .. 
make install
```

CGAL and OpenEXR can be installed via aptitude:

```
cd  ./PanoSLAM/third-package/Spherical-Package-master
sudo apt install libcgal-dev libopenexr-dev
```

Once these packages are installed, you can should the Python dependencies.

```
pip install -r requirements.txt
```

Finally, install this package with the commands:

```
python setup.py build -j 4
python setup.py install
```

Note that you can adjust the number after  `-j`  according to the number of cores available to your machine. It parallelizes compilation.

### 2. g2opy

This is a python binding of graph optimization C++ framework g2o. The pybind11 is also required, but it's built in this repository, you don't need to install.

#### Building

```
cd ./PanoSLAM/third-package/g2opy_pano/g2opy-master
mkdir build
cd build
cmake ..
make -j8
cd ..
python setup.py install
```

### 3. Pangolin

Pangolin is a lightweight portable rapid development library for managing OpenGL display / interaction and abstracting video input. At its heart is a simple OpenGl viewport manager which can help to
modularise 3D visualisation without adding to its complexity, and offers an advanced but intuitive 3D navigation handler. Pangolin also provides a mechanism for manipulating program variables through
config files and ui integration, and has a flexible real-time plotter for visualising graphical data.

#### Required Dependencies

* C++11
* OpenGL (Desktop / ES / ES2) \
  `sudo apt install libgl1-mesa-dev`
* Glew\
  `sudo apt install libglew-dev`
* CMake (for build environment)  \  
  `sudo apt install cmake`
* FFMPEG (For video decoding and image rescaling) \
  `sudo apt install ffmpeg libavcodec-dev libavutil-dev libavformat-dev libswscale-dev libavdevice-dev`
* DC1394 (For firewire input)\
  `sudo apt install libdc1394-22-dev libraw1394-dev`
* libuvc (For cross-platform webcam video input via libusb) \
  `git://github.com/ktossell/libuvc.git`
* libjpeg, libpng, libtiff, libopenexr (For reading still-image sequences) \
  `sudo apt install libjpeg-dev libpng12-dev libtiff5-dev libopenexr-dev`

#### Building

Pangolin uses the CMake portable pre-build tool. To checkout and build pangolin in the directory 'build', execute the following at a shell (or the equivelent using a GUI):

```
cd ./PanoSLAM/initialize/pangolin
mkdir build
cd build
cmake ..
make -j8
cd ..
python setup.py install
```

## Run

### Configuration

Please manually modify the configuration in this file:

```
cd ./PanoSLAM/camera/params.py
```

### Execute

If you want to test the video, please run the following file:

```
python run_video_slam.py
```

### Output
The output format is [timestamp, tx, ty, tz, qw, qx, qy, qz].
```
cd  frame_trajectory.txt
```

## TODO

* Complete PanoPoint for equirectangular image.
* Retrain BoW dictionary.
* Implement Bug-Free system.



  
