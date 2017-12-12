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
#include <vector>

def RunVisualizationThread(self):
def WaitForVisualizationThread(self):
def RunVisualizationOnly(self):
void RunVisualization( std.vector<cv.Point3d>& pointcloud,
					   std.vector<cv.Vec3b>pointcloud_RGB = std.vector<cv.Vec3b>(),
					   std.vector<cv.Point3d>pointcloud1 = std.vector<cv.Point3d>(),
					   std.vector<cv.Vec3b>pointcloud1_RGB = std.vector<cv.Vec3b>())
void ShowClouds( std.vector<cv.Point3d>& pointcloud,
				 std.vector<cv.Vec3b>pointcloud_RGB = std.vector<cv.Vec3b>(),
				 std.vector<cv.Point3d>pointcloud1 = std.vector<cv.Point3d>(),
				 std.vector<cv.Vec3b>pointcloud1_RGB = std.vector<cv.Vec3b>())
void ShowCloud( std.vector<cv.Point3d>& pointcloud,
				 std.vector<cv.Vec3b>& pointcloud_RGB, 
				 std.string& name)

def visualizerShowCamera(self, R[9], t[3], r, g, b):
def visualizerShowCamera(self, R, t, r, g, b, s, name = ""):
