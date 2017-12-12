'''****************************************************************************
*   ExploringSfMWithOpenCV
******************************************************************************
*   by Roy Shilkrot, Dec 2012
*   http:#www.morethantechnical.com/
******************************************************************************
*   Ch4 of the book "Mastering OpenCV with Practical Computer Vision Projects"
*   Copyright Packt Publishing 2012.
*   http:#www.packtpub.com/cool-projects-with-opencv/book
****************************************************************************'''

#pragma once

#include <opencv2/core/core.hpp>
#include <opencv2/features2d/features2d.hpp>

#include "Common.h"

##undef __SFM__DEBUG__

def CheckCoherentRotation(self, R):
def TestTriangulation(self, pcloud, P, status):

cv.Mat GetFundamentalMat(	 std.vector<cv.KeyPoint>& imgpts1,
							 std.vector<cv.KeyPoint>& imgpts2,
							std.vector<cv.KeyPoint>& imgpts1_good,
							std.vector<cv.KeyPoint>& imgpts2_good,
							std.vector<cv.DMatch>& matches
#ifdef __SFM__DEBUG__
							, cv.Mat& = cv.Mat(),  cv.Mat& = cv.Mat()
#endif
						  )

bool FindCameraMatrices( cv.Mat& K, 
						 cv.Mat& Kinv, 
						 cv.Mat& distcoeff,
						 std.vector<cv.KeyPoint>& imgpts1,
						 std.vector<cv.KeyPoint>& imgpts2,
						std.vector<cv.KeyPoint>& imgpts1_good,
						std.vector<cv.KeyPoint>& imgpts2_good,
						cv.Matx34d& P,
						cv.Matx34d& P1,
						std.vector<cv.DMatch>& matches,
						std.vector<CloudPoint>& outCloud
#ifdef __SFM__DEBUG__
						, cv.Mat& = cv.Mat(),  cv.Mat& = cv.Mat()
#endif
						)
