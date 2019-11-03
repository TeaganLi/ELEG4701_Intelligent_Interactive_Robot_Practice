this foloder is the code for OpenCV example in Lec8
including

   
    /launch
       /step1_image convert/convertandshow.launch      #convert the image between ROS and OpenCV
	   /step2_image_process/image_process.launch       #process the depth image from RealSense and publish the postion(x,y in pixel and z in mm) topic
       /step3_tran_position/tran_position.launch       #get the position topic and transform to x y z in m
	/manipulation_demo                             #the code in Lec7
	/src
		/check.py                                      #check the image topic
		/imageconvert.py                               #ROS and OpenCV
		/opencv_img_processing_V6.py                   #process the depyh image
		/position_process.py                           #get the position 
		
    
when you want to publish the postion topic to the manipulation_demo

1. make sure you can get depth and color image topic from RealSense
2. launch tran_position.launch
Then code will publish the pose topic
