# Vandalism-Detection-in-Wikipedia
This is a Vandalism Detection in Wikipedia Project.

Goal of the project: Analyzing editing behavior patterns and using the differences between users to flag potential vandal users.

Result: Improved the accuracy of Cluebot_NG (one of the vandalism bot used by wikipedia) from 71.4 % to 83.65 %

The folder DataSet1 contains following things:
1) EditHistory, UserNames and PageTitles database of Wikipedia
(Source: Database provided by VEWS (Srijan et al.), PAN 2010, PAN 2011 Dataset, and Data extracted from Wikipedia)
2) Python codes for analyzing the Database,to find various behavioral features
3) Individual database files(.csv) created for each feature after analyzing them
4) Python codes for training the system to learn the analyzed data using many machine learning algorithms
5) Models created from learning after applying various algorithms

The folder WikiVandalism contains:
1) C# files to create an interface for the detection tool.
2) C# files which shows the result of various algorithms on testing data.
3) Learned models.

I would specially like to thank Srijan et al. for guiding me whenever I was stuck in this project and for providing access to VEWS Database. 
