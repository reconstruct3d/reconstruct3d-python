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

#include "Common.h"

#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>

#ifndef WIN32
#include <dirent.h>
#endif

using namespace std
using namespace cv

def FlipMatches(self, matches):	std.vector<cv.DMatch> flip
	for(int i=0;i<matches.size();i++)		flip.push_back(matches[i])
		swap(flip.back().queryIdx,flip.back().trainIdx)

	return flip


def CloudPointsToPoints(self, cpts):	std.vector<cv.Point3d> out
	for (unsigned int i=0; i<cpts.size(); i++)		out.push_back(cpts[i].pt)

	return out


void GetAlignedPointsFromMatch( std.vector<cv.KeyPoint>& imgpts1,
							    std.vector<cv.KeyPoint>& imgpts2,
							    std.vector<cv.DMatch>& matches,
							   std.vector<cv.KeyPoint>& pt_set1,
							   std.vector<cv.KeyPoint>& pt_set2) 
	for (unsigned int i=0; i<matches.size(); i++)#		cout << "matches[i].queryIdx " << matches[i].queryIdx << " matches[i].trainIdx " << matches[i].trainIdx << endl
		assert(matches[i].queryIdx < imgpts1.size())
		pt_set1.push_back(imgpts1[matches[i].queryIdx])
		assert(matches[i].trainIdx < imgpts2.size())
		pt_set2.push_back(imgpts2[matches[i].trainIdx])
	}	


def KeyPointsToPoints(self, kps, ps):	ps.clear()
	for (unsigned int i=0; i<kps.size(); i++) ps.push_back(kps[i].pt)


def PointsToKeyPoints(self, ps, kps):	kps.clear()
	for (unsigned int i=0; i<ps.size(); i++) kps.push_back(KeyPoint(ps[i],1.0f))


#define intrpmnmx(val,min,max) (max==min ? 0.0 : ((val)-min)/(max-min))

def drawArrows(self, frame, prevPts, nextPts, status, verror, _line_color):
	double minVal,maxVal; minMaxIdx(verror,&minVal,&maxVal,0,0,status)
	line_thickness = 1
	
    for (i = 0; i < prevPts.size(); ++i)
        if status[i]:
        {			
			alpha = intrpmnmx(verror[i],minVal,maxVal); alpha = 1.0 - alpha
			Scalar line_color(alpha*_line_color[0],
							  alpha*_line_color[1],
							  alpha*_line_color[2])

            p = prevPts[i]
            q = nextPts[i]
            
            angle = atan2((double) p.y - q.y, (double) p.x - q.x)
            
            hypotenuse = sqrt( (double)(p.y - q.y)*(p.y - q.y) + (double)(p.x - q.x)*(p.x - q.x) )
            
            if hypotenuse < 1.0:
                continue
            
            # Here we lengthen the arrow by a factor of three.
            q.x = (int) (p.x - 3 * hypotenuse * cos(angle))
            q.y = (int) (p.y - 3 * hypotenuse * sin(angle))
            
            # Now we draw the main line of the arrow.
            line(frame, p, q, line_color, line_thickness)
            
            # Now draw the tips of the arrow. I do some scaling so that the
            # tips look proportional to the main line of the arrow.
            
            p.x = (int) (q.x + 9 * cos(angle + CV_PI / 4))
            p.y = (int) (q.y + 9 * sin(angle + CV_PI / 4))
            line(frame, p, q, line_color, line_thickness)
            
            p.x = (int) (q.x + 9 * cos(angle - CV_PI / 4))
            p.y = (int) (q.y + 9 * sin(angle - CV_PI / 4))
            line(frame, p, q, line_color, line_thickness)




bool hasEnding (std.string  &fullString, &ending)
    if fullString.length() >= ending.length():        return (0 == fullString.compare (fullString.length() - ending.length(), ending.length(), ending))
    } else:
        return False



bool hasEndingLower (string  &fullString_, &_ending)
	fullstring = fullString_, ending = _ending
	transform(fullString_.begin(),fullString_.end(),fullstring.begin(),.tolower); # to lower
	return hasEnding(fullstring,ending)


def imshow_250x250(self, name_, patch):	Mat bigpatch; cv.resize(patch,bigpatch,Size(250,250))
	imshow(name_,bigpatch)


def open_imgs_dir(self, dir_name, images, images_names, downscale_factor):	if dir_name == NULL:		return


	dir_name_ = string(dir_name)
	vector<string> files_

#ifndef WIN32
#open a directory the POSIX way

	DIR *dp
	struct dirent *ep;     
	dp = opendir (dir_name)
	
	if dp != NULL:
		while (ep = readdir (dp))			if ep.d_name[0] != '.':
				files_.push_back(ep.d_name)

		
		(void) closedir (dp)

	else:
		cerr << ("Couldn't open the directory")
		return


#else:
#open a directory the WIN32 way
	hFind = INVALID_HANDLE_VALUE
	WIN32_FIND_DATA fdata

	if dir_name_[dir_name_.size()-1] == '\\' or dir_name_[dir_name_.size()-1] == '/':		dir_name_ = dir_name_.substr(0,dir_name_.size()-1)


	hFind = FindFirstFile(string(dir_name_).append("\\*").c_str(), &fdata);	
	if hFind != INVALID_HANDLE_VALUE:
		do
			if (strcmp(fdata.cFileName, ".") != 0 and
				strcmp(fdata.cFileName, "..") != 0)
				if fdata.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY:
					continue; # a diretory

				else:
					files_.push_back(fdata.cFileName)



		while (FindNextFile(hFind, &fdata) != 0)
	} else:
		cerr << "can't open directory\n"
		return


	if GetLastError() != ERROR_NO_MORE_FILES:
		FindClose(hFind)
		cerr << "some other error with opening directory: " << GetLastError() << endl
		return


	FindClose(hFind)
	hFind = INVALID_HANDLE_VALUE
#endif
	
	for (unsigned int i=0; i<files_.size(); i++)		if files_[i][0] == '.' or not (hasEndingLower(files_[i],"jpg")orhasEndingLower(files_[i],"png")):			continue

		m_ = cv.imread(string(dir_name_).append("/").append(files_[i]))
		if downscale_factor != 1.0:
			cv.resize(m_,m_,Size(),downscale_factor,downscale_factor)
		images_names.push_back(files_[i])
		images.push_back(m_)

		


