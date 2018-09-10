# Hello Tensorflow

## Getting Started

https://www.tensorflow.org/install/

Follow the above instructions for installing

**NOTE: VERSION NUMBERS ARE CRITICAL**

 - [CUDA Toolkit 9.0](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/) _1.5Gb_
     - Requires signup for free account
 - [cuDNN 7.2.1 for CUDA 9.0](https://developer.nvidia.com/cudnn) 
    - Follow these instructions on where to unzip
    - https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installwindows
 - [Python 3.6](https://www.python.org/downloads/release/python-366/)
 - Tensorflow-GPU 1.10

 ```bash
 # Set python virtual environment for this repo
 pipenv --python 3.6
 # Install specific version of TensorFlow
 pipenv install tensorflow-gpu==1.10
 # Other tooling
 pipenv install invoke pylint autopep8 pytest pytest-cov
 ```

## Resources

 - https://www.tensorflow.org/guides/