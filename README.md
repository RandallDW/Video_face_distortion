# Video Face Distortion
## Introduction

## Author
	* Lu Chang
	* Yihan Pang
	* Dong Wang

## Environment Setup
	* Ubuntu 16.04
	* Python 2.7
	* Opencv 2.4.*
		- Under Ubuntu16.04, some Opencv3 functions may not work.
	* dlib
	* Pyqt5


### Package installation 
    Before running setup.sh, please make sure you have python-pip installed
	* $ bash setup.sh
	
### Install dlib
	* $ git clone https://github.com/davisking/dlib 
	* $ cd dlib
	* $ sudo python setup.py install 

[Reference](https://github.com/davisking/dlib)
#### Dlib related package
    * setuptools
        - $ pip install setuptools
    * cmake
        - $ sudo apt-get install cmake
    * openblas
        - $ git clone https://github.com/xianyi/OpenBLAS.git 
        - $ cd OPenBLAS
        - $ make; sudo make install
        - $ sudo apt-get install libopenblas-dev
    * boost
        - $ wget https://dl.bintray.com/boostorg/release/1.65.1/source/boost_1_65_1.tar.gz
          (Or go to boost.org manually download)
        - $ tar -xzf boost_1_65_1.tar.gz
        - $ cd boost_1_65_1
        - $ ./booststrap.sh --with-libraries=python
        - $ ./b2
        - $ sudo ./b2 install
        - $ sudo apt-get install libboost-all-dev

### Sample Code
	After installation, please run following files to make sure your opencv and
	dlib successfully installed.
	* face_detection_opencv.py
	* face_detection_dlib.py




