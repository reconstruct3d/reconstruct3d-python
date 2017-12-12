'''
 *  GPUSURFFeatureMatcher.h
 *  ExploringSfMWithOpenCV
 *
 *  Created by Roy Shilkrot on 6/13/12.
 *
 '''

#include "IFeatureMatcher.h"
#include <opencv2/gpu/gpu.hpp>

class GPUSURFFeatureMatcher : public IFeatureMatcherprivate:
	cv.Ptr<cv.gpu.SURF_GPU> extractor
	
	std.vector<cv.gpu.GpuMat> descriptors
	
	std.vector<cv.gpu.GpuMat> imgs; 
	std.vector<cv.gpu.GpuMat> imggpupts
	std.vector<std.vector<cv.KeyPoint> >& imgpts

	bool use_ratio_test
public:
	#c'tor
	GPUSURFFeatureMatcher(std.vector<cv.Mat>& imgs, 
					   std.vector<std.vector<cv.KeyPoint> >& imgpts)
	
	void MatchFeatures(int idx_i, idx_j, matches = NULL)
	
	std.vector<cv.KeyPoint> GetImagePoints(int idx) { return imgpts[idx];
