//
// Created by mh on 2019/9/11.
//

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <cv_bridge/cv_bridge.h>
#include <iostream>
#include <cmath>
#include <opencv2/calib3d/calib3d.hpp>

#include <opencv2/core/core.hpp>
#include <opencv2/aruco.hpp>

#include <opencv2/calib3d.hpp>


#include <tf2/LinearMath/Quaternion.h>
#include <tf2_ros/transform_broadcaster.h>
#include <geometry_msgs/TransformStamped.h>

#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/PointStamped.h>
#include <aruco_msg/aruco_tf_id.h>
ros::Publisher pose_pub,aruco_tf_id_pub;
image_transport::Publisher img_pub;
void publishPose(ros::Publisher &pose_pub,ros::Publisher &pointStp_pub, tf2_ros::TransformBroadcaster &br,cv::Vec3f tvec,double q[], int markerID);
void getQuaternion(cv::Mat R, double Q[]);
double q[4];
cv::Mat cameraMatrixKinect =(cv::Mat_<double >(3,3) << 614.2276611328125, 0.0, 327.88189697265625, 0.0, 613.449462890625, 239.263671875, 0.0, 0.0, 1.0);
cv::Mat distCoeffs = (cv::Mat_<double >(1,5) << 0.0, 0.0, 0.0, 0.0, 0.0);
void arucoCallback(const sensor_msgs::ImageConstPtr& msg)
{
    try
    {
        cv::Mat img ,imgOutput;
        cv_bridge::toCvShare(msg, "bgr8")->image.copyTo(img);
//        double second = msg->header.stamp.toSec();
        img.copyTo(imgOutput);
        std::vector<int> markerIds;
        std::vector<std::vector<cv::Point2f>> markerCorners, rejectedCandidates;
        cv::Ptr<cv::aruco::DetectorParameters> parameters;
        cv::Ptr<cv::aruco::Dictionary> dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_4X4_250);
        cv::aruco::detectMarkers(img, dictionary, markerCorners, markerIds);
        if(markerIds.size() > 0){
            cv::aruco::drawDetectedMarkers(imgOutput, markerCorners, markerIds);

            std::vector<cv::Vec3d> rvecs, tvecs;//rvecs and tvecs must be double
            static tf2_ros::TransformBroadcaster br;
            cv::aruco::estimatePoseSingleMarkers(markerCorners,0.043, cameraMatrixKinect, distCoeffs, rvecs, tvecs);
            for(int i=0; i<markerIds.size(); i++) {
                cv::Mat R = cv::Mat::zeros(3, 3, CV_64FC1);
                cv::Rodrigues(rvecs[i], R);
                getQuaternion(R, q);
                if(markerIds[i] == 0 ) {
                    publishPose(pose_pub,aruco_tf_id_pub, br, tvecs[i], q, markerIds[i]);
                    cv::aruco::drawAxis(imgOutput, cameraMatrixKinect, distCoeffs, rvecs[i], tvecs[i], 0.1);
                }
            }
        }
        cv::imshow("Image Arm1",imgOutput);
        sensor_msgs::ImagePtr msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", imgOutput).toImageMsg();
        img_pub.publish(msg);
	    cv::waitKey(10);
    }
    catch (cv_bridge::Exception& e)
    {
        ROS_ERROR("Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
    }
}

int main(int argc, char **argv){
    std::vector<cv::Point> worldPoint;
    ros::init(argc, argv, "image_listener");
    ros::NodeHandle nh("~");
    cv::startWindowThread();
    image_transport::ImageTransport it(nh);
    pose_pub = nh.advertise<geometry_msgs::TransformStamped>("/camera/target1_pose3d", 10);
    aruco_tf_id_pub = nh.advertise<aruco_msg::aruco_tf_id>("/camera/aruco_tf_id/arm1", 10);
//    pointStp_pub = nh.advertise<geometry_msgs::PointStamped>("/camera/pointStamp", 10);
    img_pub = it.advertise("/camera/image_with_coordination", 10);
    image_transport::Subscriber sub = it.subscribe("/camera/color/image_raw", 1, arucoCallback);
    ros::spin();
}


void publishPose(ros::Publisher &pose_pub,ros::Publisher &pointStp_pub, tf2_ros::TransformBroadcaster &br,cv::Vec3f tvec,double q[],int markerID){

    geometry_msgs::TransformStamped transformStamped;
//    geometry_msgs::PointStamped pointStamped;
    aruco_msg::aruco_tf_id arutfid;
    transformStamped.header.stamp = ros::Time::now();
    transformStamped.header.frame_id = "camera_rgb_optical_frame";//should be camera
    transformStamped.child_frame_id = std::to_string(markerID);
    transformStamped.transform.translation.x = tvec(0);
    transformStamped.transform.translation.y = tvec(1);
    transformStamped.transform.translation.z = tvec(2);

    transformStamped.transform.rotation.x = q[0];
    transformStamped.transform.rotation.y = q[1];
    transformStamped.transform.rotation.z = q[2];
    transformStamped.transform.rotation.w = q[3];
    br.sendTransform(transformStamped);

    pose_pub.publish(transformStamped);
    arutfid.id = markerID;
    arutfid.tf.header.stamp = ros::Time::now();
    arutfid.tf.header.frame_id = "camera_rgb_optical_frame";
    arutfid.tf.child_frame_id = std::to_string(markerID);
    arutfid.tf.transform.translation.x = tvec(0);
    arutfid.tf.transform.translation.y = tvec(1);
    arutfid.tf.transform.translation.z = tvec(2);

    arutfid.tf.transform.rotation.x = q[0];
    arutfid.tf.transform.rotation.y = q[1];
    arutfid.tf.transform.rotation.z = q[2];
    arutfid.tf.transform.rotation.w = q[3];
    aruco_tf_id_pub.publish(arutfid);
//    pointStamped.point.x = tvec(0);
//    pointStamped.point.y = tvec(1);
//    pointStamped.point.z = tvec(2);
//    pointStp_pub.publish(pointStamped);
}

void getQuaternion(cv::Mat R, double Q[])// convert opencv rotation matrix to quaternion
{
    double trace = R.at<double>(0,0) + R.at<double>(1,1) + R.at<double>(2,2);

    if (trace > 0.0)
    {
        double s = sqrt(trace + 1.0);
        Q[3] = (s * 0.5);
        s = 0.5 / s;
        Q[0] = ((R.at<double>(2,1) - R.at<double>(1,2)) * s);
        Q[1] = ((R.at<double>(0,2) - R.at<double>(2,0)) * s);
        Q[2] = ((R.at<double>(1,0) - R.at<double>(0,1)) * s);
    }

    else
    {
        int i = R.at<double>(0,0) < R.at<double>(1,1) ? (R.at<double>(1,1) < R.at<double>(2,2) ? 2 : 1) : (R.at<double>(0,0) < R.at<double>(2,2) ? 2 : 0);
        int j = (i + 1) % 3;
        int k = (i + 2) % 3;

        double s = sqrt(R.at<double>(i, i) - R.at<double>(j,j) - R.at<double>(k,k) + 1.0);
        Q[i] = s * 0.5;
        s = 0.5 / s;

        Q[3] = (R.at<double>(k,j) - R.at<double>(j,k)) * s;
        Q[j] = (R.at<double>(j,i) + R.at<double>(i,j)) * s;
        Q[k] = (R.at<double>(k,i) + R.at<double>(i,k)) * s;
    }
}


//rosrun camera_calibration cameracalibrator.py --size 11x11 --square 0.06 image:=/camera/color/image_raw
// realsense calibrated result
//[image]
//
//width
//640
//
//height
//480
//
//[narrow_stereo]
//
//camera matrix
//605.436409 0.000000 324.017932
//0.000000 606.522225 241.738229
//0.000000 0.000000 1.000000
//
//distortion
//0.099542 -0.214394 -0.001703 0.001842 0.000000
//
//rectification
//1.000000 0.000000 0.000000
//0.000000 1.000000 0.000000
//0.000000 0.000000 1.000000
//
//projection
//612.232727 0.000000 325.002133 0.000000
//0.000000 614.080505 241.196531 0.000000
//0.000000 0.000000 1.000000 0.000000
//('D = ', [0.09954198502295586, -0.21439394334275536, -0.001702890023334662, 0.0018417862696292924, 0.0])
//('K = ', [605.4364086628125, 0.0, 324.0179318463468, 0.0, 606.5222254460767, 241.73822915431185, 0.0, 0.0, 1.0])
//('R = ', [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0])
//('P = ', [612.2327270507812, 0.0, 325.0021333652003, 0.0, 0.0, 614.0805053710938, 241.19653142952302, 0.0, 0.0, 0.0, 1.0, 0.0])


//https://calib.io/pages/camera-calibration-pattern-generator
//rosrun camera_calibration cameracalibrator.py --size 11x7 --square 0.015 image:=/camera/color/image_raw

//[image]
//
//width
//640
//
//height
//480
//
//[narrow_stereo]
//
//camera matrix
//627.814560 0.000000 319.756785
//0.000000 626.309858 234.461047
//0.000000 0.000000 1.000000
//
//distortion
//0.137749 -0.272282 -0.003421 -0.001419 0.000000
//
//rectification
//1.000000 0.000000 0.000000
//0.000000 1.000000 0.000000
//0.000000 0.000000 1.000000
//
//projection
//639.362671 0.000000 319.051413 0.000000
//0.000000 637.677307 233.251712 0.000000
//0.000000 0.000000 1.000000 0.000000


//viper
//[image]
//
//width
//640
//
//height
//360
//
//[narrow_stereo]
//
//camera matrix
//486.521222 0.000000 326.412832
//0.000000 486.177731 187.786639
//0.000000 0.000000 1.000000
//
//distortion
//-0.164537 -0.025685 -0.001494 0.000642 0.000000
//
//rectification
//1.000000 0.000000 0.000000
//0.000000 1.000000 0.000000
//0.000000 0.000000 1.000000
//
//projection
//440.693085 0.000000 328.881965 0.000000
//0.000000 474.378815 187.872120 0.000000
//0.000000 0.000000 1.000000 0.000000
