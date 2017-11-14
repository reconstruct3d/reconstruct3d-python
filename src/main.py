from scipy.io import loadmat
import numpy as np 
import skimage.io as io 
import os 
import skimage as skimg
from utils import * 
import argparse

def main(opts):
	"""Performs the whole algorithm i.e given video frames, 
	performs its 3D reconstruction

	Args: 
	opts: command line arguments

	Returns: 
	None
	"""

	#loading images
	pathnames = [os.path.join(opts.dataDir, x) for x in sorted(os.listdir(opts.dataDir)) if x.split('.')[-1] in opts.ext]
	imgs = io.ImageCollection(pathnames)
	num_imgs = len(imgs)

	#hardcoded for now for testing purposes
	focal_length = 719.5459

	#if bigger image than our limit, reshaping image and adjusting 
	#camera intrinsics. 
	opts.maxSize = 1024
	imsize = imgs[0].shape
	if opts.maxSize < np.max(imsize): 
	    scale = opts.maxSize / np.max(imsize)
	    focal_length = focal_length * scale 
	    imsize = skimg.transform.resize(imgs[0], scale).shape 

	#constructing camera intrinsic matrix
	K = f2K(focal_length)

	essential_matrices = list()
	for index, img in enumerate(imgs[:len(imgs) - 1]):
		#sift feature matching (taking pre-computed points for now for testing purposes)
		feats = matFileToFeatures('./matlab_cache/sift-keypoints/point'+str(index+1)+'.mat', imgs[0].shape, imgs[1].shape)
		
		# #fundamental matrix estimation 
		# F = estimateFundamentalMatrixRANSAC()

		# Loading the fundamental matrix
		F = loadmat('./matlab_cache/fundamental-matrix/F_matrix' + str(index + 1))['f_matrix']
		
		#essential matrix estimation 
		E = estimateEssentialMatrix(K, F, False)
		essential_matrices.append(E)		
		#camera projection matrix 

		#triangulation 

		#bundle adjustment
		
	# Testing the essential matrices
	# loading orginal matrices
	
	# test_essential_matrices(, E)
	pass

def test_essential_matrices(E_original, E):
	pass

def set_arguments(parser):
    parser.add_argument('-dataDir',action='store', type=str, default='../data/', dest='dataDir')
    parser.add_argument('-ext', action='store',type=list, default=['png', 'jpg'], dest='ext')
    parser.add_argument('-maxSize',action='store', type=int, default=1024, dest='maxSize')

if __name__=='__main__': 
	#setting parser for command-line arguments 
	parser = argparse.ArgumentParser()
	set_arguments(parser)

	#parsing arguments now..
	opts = parser.parse_args()

	#running the complete algorithm now..
	main(opts)