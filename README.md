Some quick experiments on current (2020) face detection algorithms (Haar Cascade and Facenet) with museum images. 

## Installation

It is very easy to end up with mismatched dependecies with python modules and therefore I strongly suggest to use virtualenv or [Anaconda](https://www.anaconda.com/products/individual). 

Setting up python 3.6 environment with conda (which comes with Ananconda):

	conda create --name tensorflow_env python=3.6
	conda activate tensorflow_env

Install python modules for machine learning environment:

	pip install mtcnn
	pip install tensorflow

Clone this repository:

## Running samples

**markup_faces_facenet.py** loops through all jpg images in images -directory and writes images to **results** directory with faces marked with rectangles.

**extract_faces_facenet.py** loops through all jpg images in images directory and wcrops detected faces as separate images to **faces** directory.

## Image source

Sample images are freely licensed (CC-BY 4.0) images from collections of Helsinki City Museum: https://hkm.finna.fi/

Some examples:

https://hkm.finna.fi/Record/hkm.HKMS000005:km00326o

https://hkm.finna.fi/Record/hkm.HKMS000005:km0000lpj4

https://hkm.finna.fi/Record/hkm.HKMS000005:00000wzq









