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

#include "Visualization.h"

#include <pcl/common/common.h>
#include <pcl/visualization/cloud_viewer.h>
#include <pcl/visualization/pcl_visualizer.h>
#include <pcl/io/io.h>
#include <pcl/io/file_io.h>
#include <pcl/io/pcd_io.h>
#include <pcl/ModelCoefficients.h>
#include <pcl/point_types.h>
#include <pcl/sample_consensus/ransac.h>
#include <pcl/sample_consensus/sac_model_plane.h>
#include <pcl/filters/extract_indices.h>
#include <pcl/filters/statistical_outlier_removal.h>
#include <pcl/filters/voxel_grid.h>

#include <boost/thread.hpp>

#include <opencv2/core/core.hpp>

#include <Eigen/Eigen>

using namespace std
using namespace Eigen
 
void PopulatePCLPointCloud( pcl.PointCloud<pcl.PointXYZRGB>.Ptr& mycloud,
						    vector<cv.Point3d>& pointcloud, 
						    std.vector<cv.Vec3b>& pointcloud_RGB,
						   write_to_file = False
						   )

#define pclp3(eigenv3f) pcl.PointXYZ(eigenv3f.x(),eigenv3f.y(),eigenv3f.z())

pcl.PointCloud<pcl.PointXYZRGB>.Ptr cloud,cloud1,cloud_no_floor,orig_cloud
cloud_to_show_name = ""
show_cloud = False
sor_applied = False
show_cloud_A = True

################# Show Camera ##################
std.deque<std.pair<std.string,pcl.PolygonMesh> >					cam_meshes
std.deque<std.pair<std.string,std.vector<Matrix<float,6,1> > > >	linesToShow
#TODO define mutex
bool							bShowCam
iCamCounter = 0
iLineCounter = 0
int								ipolygon[18] = {0,1,2,  0,3,1,  0,4,3,  0,2,4,  3,1,4,   2,4,1

inline pcl.PointXYZ Eigen2PointXYZ(Eigen.Vector3f v) { return pcl.PointXYZ(v[0],v[1],v[2]);
inline pcl.PointXYZRGB Eigen2PointXYZRGB(Eigen.Vector3f v, rgb) { pcl.PointXYZRGB p(rgb[0],rgb[1],rgb[2]); p.x = v[0]; p.y = v[1]; p.z = v[2]; return p;
inline pcl.PointNormal Eigen2PointNormal(Eigen.Vector3f v, n) { pcl.PointNormal p; p.x=v[0];p.y=v[1];p.z=v[2];p.normal_x=n[0];p.normal_y=n[1];p.normal_z=n[2]; return p;
inline float* Eigen2float6(Eigen.Vector3f v, rgb) { static float buf[6]; buf[0]=v[0];buf[1]=v[1];buf[2]=v[2];buf[3]=rgb[0];buf[4]=rgb[1];buf[5]=rgb[2]; return buf;
inline Matrix<float,6, Eigen2Eigen(Vector3f v, rgb) { return (Matrix<float,6,1>() << v[0],v[1],v[2],rgb[0],rgb[1],rgb[2]).finished();
inline std.vector<Matrix<float,6,1> > AsVector( Matrix<float,6, p1,  Matrix<float,6, p2) { 	std.vector<Matrix<float,6,1> > v(2); v[0] = p1; v[1] = p2; return v;

def visualizerShowCamera(self, R, _t, r, g, b, s = 0.01 '''downscale factor''', name = ""):	name_ = name,line_name = name + "line"
	if name.length() <= 0:		stringstream ss; ss<<"camera"<<iCamCounter++
		name_ = ss.str()
		ss << "line"
		line_name = ss.str()

	
	t = -R.transpose() * _t

	vright = R.row(0).normalized() * s
	vup = -R.row(1).normalized() * s
	vforward = R.row(2).normalized() * s

	Vector3f rgb(r,g,b)

	pcl.PointCloud<pcl.PointXYZRGB> mesh_cld
	mesh_cld.push_back(Eigen2PointXYZRGB(t,rgb))
	mesh_cld.push_back(Eigen2PointXYZRGB(t + vforward + vright/2.0 + vup/2.0,rgb))
	mesh_cld.push_back(Eigen2PointXYZRGB(t + vforward + vright/2.0 - vup/2.0,rgb))
	mesh_cld.push_back(Eigen2PointXYZRGB(t + vforward - vright/2.0 + vup/2.0,rgb))
	mesh_cld.push_back(Eigen2PointXYZRGB(t + vforward - vright/2.0 - vup/2.0,rgb))

	#TODO Mutex acquire
	pcl.PolygonMesh pm
	pm.polygons.resize(6); 
	for(int i=0;i<6;i++)
		for(int _v=0;_v<3;_v++)
			pm.polygons[i].vertices.push_back(ipolygon[i*3 + _v])
	pcl.toROSMsg(mesh_cld,pm.cloud)
	bShowCam = True
	cam_meshes.push_back(std.make_pair(name_,pm))
	#TODO mutex release

	linesToShow.push_back(std.make_pair(line_name,
		AsVector(Eigen2Eigen(t,rgb),Eigen2Eigen(t + vforward*3.0,rgb))
		))

def visualizerShowCamera(self, R[9], t[3], r, g, b):	visualizerShowCamera(Matrix3f(R).transpose(),Vector3f(t),r,g,b)

def visualizerShowCamera(self, R[9], t[3], r, g, b, s):	visualizerShowCamera(Matrix3f(R).transpose(),Vector3f(t),r,g,b,s)

def visualizerShowCamera(self, R, t, r, g, b, s, name):	visualizerShowCamera(Matrix<float,3,3,RowMajor>(R.val),Vector3f(t.val),r,g,b,s,name)

########################################/

void viewerOneOff (pcl.visualization.PCLVisualizer& viewer)
#	viewer.setBackgroundColor(255,255,255); #white background
#	viewer.removeCoordinateSystem();	#remove the axes


def SORFilter(self):	
	pcl.PointCloud<pcl.PointXYZRGB>.Ptr cloud_filtered (new pcl.PointCloud<pcl.PointXYZRGB>)
	
	std.cerr << "Cloud before SOR filtering: " << cloud.width * cloud.height << " data points" << std.endl
	

	# Create the filtering object
	pcl.StatisticalOutlierRemoval<pcl.PointXYZRGB> sor
	sor.setInputCloud (cloud)
	sor.setMeanK (50)
	sor.setStddevMulThresh (1.0)
	sor.filter (*cloud_filtered)
	
	std.cerr << "Cloud after SOR filtering: " << cloud_filtered.width * cloud_filtered.height << " data points " << std.endl
	
	copyPointCloud(*cloud_filtered,*cloud)
	copyPointCloud(*cloud,*orig_cloud)
	
#	std.cerr << "PointCloud before VoxelGrid filtering: " << cloud.width * cloud.height << " data points (" << pcl.getFieldsList (*cloud) << ")."<<std.endl
#	
#	cloud_filtered.reset(new pcl.PointCloud<pcl.PointXYZRGB>)
#	
#	# Create the filtering object
#	pcl.VoxelGrid<pcl.PointXYZRGB> vgrid
#	vgrid.setInputCloud (cloud)
#	vgrid.setLeafSize (0.1f, 0.1f, 0.1f)
#	vgrid.filter (*cloud_filtered)
#	
#	std.cerr << "PointCloud after VoxelGrid filtering: " << cloud_filtered.width * cloud_filtered.height << " data points (" << pcl.getFieldsList (*cloud_filtered) << ")."<<std.endl;	
#	
#	copyPointCloud(*cloud_filtered,*cloud)
}	


void keyboardEventOccurred ( pcl.visualization.KeyboardEvent& event_,
                            void* viewer_void)
	viewer = static_cast<pcl.visualization.CloudViewer *> (viewer_void)
#	cout << "event_.getKeySym () = " << event_.getKeySym () << " event_.keyDown () " << event_.keyDown () << endl
	if (event_.getKeySym () == "s" or event_.getKeySym () == "S") and event_.keyDown ():
		cout << "s clicked" << endl
		
		cloud.clear()
		copyPointCloud(*orig_cloud,*cloud)
		if not sor_applied:			SORFilter()
			sor_applied = True
		} else:
			sor_applied = False


		show_cloud = True

	if (event_.getKeySym ().compare("1") == 0:
#ifndef WIN32
		and event_.keyDown ()
#endif
		) 
		show_cloud_A = True
		show_cloud = True

	if (event_.getKeySym ().compare("2") == 0:
#ifndef WIN32
		and event_.keyDown ()
#endif
		) 
		show_cloud_A = False
		show_cloud = True




void RunVisualization( vector<cv.Point3d>& pointcloud,
					   vector<cv.Vec3b>& pointcloud_RGB,
					   vector<cv.Point3d>& pointcloud1,
					   vector<cv.Vec3b>& pointcloud1_RGB) 
{	
	ShowClouds(pointcloud,pointcloud_RGB,pointcloud1,pointcloud1_RGB)
	RunVisualizationOnly();	


void ShowClouds( vector<cv.Point3d>& pointcloud,
				 vector<cv.Vec3b>& pointcloud_RGB,
				 vector<cv.Point3d>& pointcloud1,
				 vector<cv.Vec3b>& pointcloud1_RGB) 
	cloud.reset(new pcl.PointCloud<pcl.PointXYZRGB>)
	cloud1.reset(new pcl.PointCloud<pcl.PointXYZRGB>)
	orig_cloud.reset(new pcl.PointCloud<pcl.PointXYZRGB>)
    
	PopulatePCLPointCloud(cloud,pointcloud,pointcloud_RGB)
	PopulatePCLPointCloud(cloud1,pointcloud1,pointcloud1_RGB)
	copyPointCloud(*cloud,*orig_cloud)
	cloud_to_show_name = ""
	show_cloud = True
	show_cloud_A = True


void ShowCloud(pcl.PointCloud<pcl.PointXYZRGB>.Ptr _cloud, name) { 
	cloud.reset(new pcl.PointCloud<pcl.PointXYZRGB>)
	pcl.copyPointCloud(*_cloud,*cloud)
	cloud_to_show_name = name
	show_cloud = True
	show_cloud_A = True


void ShowCloud( vector<cv.Point3d>& pointcloud,
				 vector<cv.Vec3b>& pointcloud_RGB, 
				 std.string& name)	pcl.PointCloud<pcl.PointXYZRGB>.Ptr newcloud(new pcl.PointCloud<pcl.PointXYZRGB>)
	PopulatePCLPointCloud(newcloud,pointcloud,pointcloud_RGB)
	ShowCloud(newcloud,name)


def RunVisualizationOnly(self):	pcl.visualization.PCLVisualizer viewer("SfMToyLibrary Viewe")
    	
	viewer.registerKeyboardCallback (keyboardEventOccurred, (void*)&viewer)
	
    while (not viewer.wasStopped ())
		if show_cloud:			cout << "Show cloud: "
			if cloud_to_show_name != "":				cout << "show named cloud " << cloud_to_show_name << endl
				viewer.removePointCloud(cloud_to_show_name)
				viewer.addPointCloud(cloud,cloud_to_show_name)
			} else:
				if show_cloud_A:					cout << "show cloud A" << endl
					viewer.removePointCloud("orig")
					viewer.addPointCloud(cloud,"orig")
				} else:
					cout << "show cloud B" << endl
					viewer.removePointCloud("orig")
					viewer.addPointCloud(cloud1,"orig")


			show_cloud = False

		if cam_meshes.size() > 0:			num_cams = cam_meshes.size()
			cout << "showing " << num_cams << " cameras" << endl
			while(cam_meshes.size()>0)				viewer.removeShape(cam_meshes.front().first)
				viewer.addPolygonMesh(cam_meshes.front().second,cam_meshes.front().first)
				cam_meshes.pop_front()


		if linesToShow.size() > 0:			cout << "showing " << linesToShow.size() << " lines" << endl
			while(linesToShow.size()>0)				vector<Matrix<float,6,1> > oneline = linesToShow.front().second
				pcl.PointXYZRGB	A(oneline[0][3],oneline[0][4],oneline[0][5]),
									B(oneline[1][3],oneline[1][4],oneline[1][5])
				for(int j=0;j<3;j++) {A.data[j] = oneline[0][j]; B.data[j] = oneline[1][j];
				viewer.removeShape(linesToShow.front().first)
				viewer.addLine<pcl.PointXYZRGB,pcl.PointXYZRGB>(A,B,linesToShow.front().first)
				linesToShow.pop_front()
			} 
			linesToShow.clear()

		viewer.spinOnce()

}	

_t = NULL
def RunVisualizationThread(self):	_t = boost.thread(RunVisualizationOnly)

def WaitForVisualizationThread(self):	_t.join()



void PopulatePCLPointCloud( pcl.PointCloud<pcl.PointXYZRGB>.Ptr& mycloud,
						    vector<cv.Point3d>& pointcloud, 
						    std.vector<cv.Vec3b>& pointcloud_RGB,
						   bool write_to_file
						   )
	#Populate point cloud
	cout << "Creating point cloud..."
	t = cv.getTickCount()

	for (unsigned int i=0; i<pointcloud.size(); i++)		# get the RGB color value for the point
		cv.Vec3b rgbv(255,255,255)
		if pointcloud_RGB.size() > i:			rgbv = pointcloud_RGB[i]


		# check for erroneous coordinates (NaN, Inf, etc.)
		if (pointcloud[i].x != pointcloud[i].x or 
			pointcloud[i].y != pointcloud[i].y or 
			pointcloud[i].z != pointcloud[i].z or 
#ifndef WIN32
			isnan(pointcloud[i].x) or
			isnan(pointcloud[i].y) or 
			isnan(pointcloud[i].z) or
#else:
			_isnan(pointcloud[i].x) or
			_isnan(pointcloud[i].y) or 
			_isnan(pointcloud[i].z) or
#endif
			#fabsf(pointcloud[i].x) > 10.0 or 
			#fabsf(pointcloud[i].y) > 10.0 or 
			#fabsf(pointcloud[i].z) > 10.0
			False
			) 
			continue

		
		pcl.PointXYZRGB pclp
		
		# 3D coordinates
		pclp.x = pointcloud[i].x
		pclp.y = pointcloud[i].y
		pclp.z = pointcloud[i].z
		
		# RGB color, to be represented as an integer
		rgb = ((uint32_t)rgbv[2] << 16 | (uint32_t)rgbv[1] << 8 | (uint32_t)rgbv[0])
		pclp.rgb = *reinterpret_cast<float*>(&rgb)
		
		mycloud.push_back(pclp)

	
	mycloud.width = (uint32_t) mycloud.points.size(); # number of points
	mycloud.height = 1;								# a list, row of data
	
	t = ((double)cv.getTickCount() - t)/cv.getTickFrequency()
	cout << "Done. (" << t <<"s)"<< endl
	
	# write to file
	if write_to_file:		#pcl.PLYWriter pw
		#pw.write("pointcloud.ply",*mycloud)
		pcl.PCDWriter pw
		pw.write("pointcloud.pcd",*mycloud)


