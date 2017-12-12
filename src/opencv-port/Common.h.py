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

#pragma warning(disable: 4244 18 4996 4800)

#include <opencv2/core/core.hpp>
#include <opencv2/features2d/features2d.hpp>
#include <vector>
#include <iostream>
#include <list>
#include <set>

struct CloudPoint	cv.Point3d pt
	std.vector<int> imgpt_for_img
	double reprojection_error


def FlipMatches(self, matches):
def KeyPointsToPoints(self, kps, ps):
def PointsToKeyPoints(self, ps, kps):

def CloudPointsToPoints(self, cpts):

void GetAlignedPointsFromMatch( std.vector<cv.KeyPoint>& imgpts1,
							    std.vector<cv.KeyPoint>& imgpts2,
							    std.vector<cv.DMatch>& matches,
							   std.vector<cv.KeyPoint>& pt_set1,
							   std.vector<cv.KeyPoint>& pt_set2)

void drawArrows(cv.Mat& frame, prevPts, nextPts, status, verror, line_color = cv.Scalar(0, 0, 255))

#ifdef USE_PROFILING
#define CV_PROFILE(msg,code)	{\
	std.cout << msg << " ";\
	__time_in_ticks = (double)cv.getTickCount();\
	{ code }\
	std.cout << "DONE " << ((double)cv.getTickCount() - __time_in_ticks)/cv.getTickFrequency() << "s" << std.endl;\

#else:
#define CV_PROFILE(msg,code) code
#endif

def open_imgs_dir(self, dir_name, images, images_names, downscale_factor):
def imshow_250x250(self, name_, patch):
