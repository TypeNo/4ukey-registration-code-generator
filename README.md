# AIROST-INTERN-21-22-IOT-SMART-PARKING-SYSTEM
COVER PAGE



Project Title
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 



Prepared by: 
1.Team Member 1
2.Team Member 2
3.Team Member 3
 





Project Report

Team Leader 	Your Name...
Team Member 1 	Your Name...
Team Member 2 	Your Name...
Team Member 3 	Your Name...


Project Task Delegation
Features 	Description	Person In Charge	Outcome (Did you manage to build it? If no, why?)
Sign In/Sign Up			
Video Making			
Booking			
			
			
Simple Object detection(back-end)	A feature that can used to detect that whether the car parking slot is available or not available.	Yeo Chun Teck	Yes
Simple 2D map(back-end) 	A feature that can display the location of available and unavailable car parking slots.This feature is along with navigation that can show the route to the available car parking slot which is closest to the entrance	Yeo Chun Teck	Yes
Automatic execution of back-end application	The application will be executed when the user scan the QR code	Yeo Chun Teck	No.Haven’t find a way to connect the back-end application to the server or the database.
QR code scanner	A feature that allow the user to scan QR code to claim the information which is encoded into QR code 	Yeo Chun Teck	Yes
QR code scanner result page	A page that will display the information about the username,location,date and time when scanning.There is a button connect to 2D map(front-end).If the QR code scanned didn’t contain the certain information,the page will display ‘invalid’	Yeo Chun Teck	Not.Still working on running python script in flutter app.Also considering that this page may be unnecessary because thinking this page could be skipped after scanning the QR code.The result of the QR code could be display in the 2D map platform to show that whether the QR code the user scanned is valid because it will not received any coordinates from the database
2D map(front-end)	A feature that user can display the 2d map in their app	Yeo Chun Teck	Not.Haven’t find a way to run  python script in flutter app
			
			


Environment Set Up
1.Is there anything we need to be informed/take precautions about before setting up the environment?
2.What software do we need to install?
3.What should we do after finish installing the software?
4.Is there any alternative way to set up an environment (If yes, repeat Step 1 to 

1.)
I.The program of object detection and 2d map will need the below python libraries to launch:
cv2
os
csv
Numpy
statistics
II.Install the python libraries by typing”pip install “package name” in the command prompt of VScode.The below is the example

III.The version of installed Python is recommend to be 3.x version
IV.If VS code ask about whether you want to  get the flutter package,just click yes to get the packages.
V.For the object detection part,the parking lot is limited to the type of opened parking lot that has only one entry and one exit.The route is one way only.The type of parking lot which is available:

2.)
I.Please install VScode:https://code.visualstudio.com/
II.Please install Python extension in VS code(you can find it in the ‘extension’ session in the VScode)
III.Please install Python 3.x version
IV.Adding the Python into the Path
V.Please install Dart extension and Flutter extension in VS code(you can find it in the ‘extension session in the VScode)
VI.Please install Android Studio
VII.Please install IP webcam in your phone

3.)For the object detection and 2d map part(front end)
I.Download the whole zip file of the code
II.Then unzipped the code to the file location you want
III.Open VS code to open the folder
IV.Choose the Python you installed as interpreter by clicking the ‘python 3.6.0 64-bit’ at the left bottom of the window
V.Go to Selector.py for some modification on configuration setting:
a)In line 17,url =”the IPv4 address of  the IP webcam which is installed in your phone ”

VI.Pointing the linked phone camera to the parking lot you targeted from above
VII.Run “Selector.py” 
VIII.Select every parking slots by clicking left button of mouse and click enter everytime you select the slot to save the data
IX.Click c to cancel and ecs to quit


X.Launch the ‘run.py’ to launch multiple python files

For flutter app part:
I.Open Android studio to set up what kind of emulator devices you want to display the app
II.You can launch the qrcodescannerpage.dart in the VScode by selecting the device you just set up in android studio as the emulator device





Project Installation
In this part, you need to show us how to install/deploy/run your software after setting up the environment. You may combine this part together with the previous part

1.Attach a GitHub Repo URL Link which has your code inside
2.Explain to us what should we do to run your software
a.What file location should we put your code in
b.How to run the code? (is there any command?)
c.Etc etc



Project Resources

Resources	URL Link
Presentation Video	
GitHub Repo	
Others 	


Individual Progress Update
Think of it as documentation of your own project development

1.Feature/Task You are responsible for.
2.Week1, Week2, Week3, Week4 Detail update

Week 1 (10 - 13 NOV)	What have you done in the past 4 weeks? What have you learnt? Try to explain it in as detail as possible. So we can understand better your progress
Week 2 (14 - 20 NOV)	
Week 3 (21 - 28 NOV)	
Week 4 (29 NOV - 2 DEV)	

3.Video Link if you have any
Week 1 (10 - 13 NOV)	Considering about the projects that I intend to start.
Collecting information about the projects and technologies that I ‘m interested
Finding the team that has launched the project that can apply the technologies I ‘m interested in
Discussing with the group mates about every part of the projects
Deciding the path of project development and allocating the task to do
Deciding the feature which should be included in the project
Learn to certain what kind of things I seek for and do more detailed and more further planning for development
Learning to figure out every possibilities that could be added to enhance the quality of the project
Week 2 (14 - 20 NOV)	Learning some basic of dart language and python language
Learning to setting up the environment for application
Learning about the libraries or packages of python language and dart language
Seeking help from senior for installing package or libraries and environment setup
Building up a QR code scanner page with a feature that can claim data hidden in QR code
Searching project related to object detection to get some inspiration 
Building up a simple python program for detecting whether car parking slot is available  
Thinking about what kind of 2d map could I display based on the knowledge I learned
Searching through similar project to know what kind of technologies I could use
Building up simple python 2d map program which is dependable on the information collected from detector part
Learning that starting without any foundation of different programming language is impossible
Learning to arrange time for researching and implementation
Finding ways of learning by researching the excellent project by other people
Learning that there are many technologies that I couldn’t understand with my low knowledge and I couldn’t research completely in a short time
Having more clear image to the programming
Week 3 (21 - 28 NOV)	Continuing the 2d map part which I faced some problem in transforming data collected into csv file in last week
Finding the point where causes the problem to occur by browsing Internet
Seeking some advice from senior on helping me to solve the problem and research the project from other person
Building up a simple navigation feature in 2d map which can show the user the route from entrance to the closest available parking slot.
Thinking about the algorithm that I could use for the navigation features
Revealing the current working outcome to the group mates and seeking for their feedback
Seeking some opinions on running python script in flutter app
Sharing some ideas about the later project and discuss the things we should do afterward
Learning that there is need for using different software to build software
Learning that database is very important in software programming
Week 4 (29 NOV - 2 DEV)	Working on running python script in flutter app
Researching about QR code to know what information should be encoded in it 
Researching about the purpose of the use of QR code
Researching about how the app send the information collected from qr code scanner to the database
Preparing documentation of project and weekly progress report
Recording project presentation video
Making some modification on the objection detection part and 2d map part
Adding the feature to link the application to the phone camera
Adding comments in the script
Building up experimental sample for demo
Learning that there are so many places need to be improved
Figuring out there are some limit to the application created 
Figuring out that I did mistakes and using wrong concept in 2d map part in making this project
