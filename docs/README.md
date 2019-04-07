# NETS213FinalProject
1. Content Aggregation: go through YouTube and get links for top 25 pop songs and timing clips for what we want crowd to sing. We also need to find a platform that the crowd can record their hums into (1)
2. Quality Control Module 1: Go through all the songs and make sure they have a viable chorus (can users mimic the tune of the chorus?) (1)
3. Aggregation Module: Once finalize the content, we upload these video links and timing clips onto MTurk along with the voice recording link (Vocaroo) and wait for responses. (2)
  **Milestone: First round of responses from MTurk**
4. Quality Control Module 2: Once we get our data, we will upload all of these crowd-sourced audio files onto a new MTurk HIT. This HIT will ask workers to verify if the hums resemble the source song clip (i.e. we will ask if the hum matches the song link). This will be the second quality control step to ensure that each hum somewhat resembles the song (eliminating audio files with extreme background noise, 1-second audio clips, etc.). This step also includes a control verification. Similar to HW7, we will have “gold-standard” humming verifications where, in one instance, an amateur hum is mimicking the intended song clip, and in another, the hum is not mimicking the intended song clip. If the worker gets both of these right, we will take their answer, so we don’t have to manually go through 2500 audio files. (2)
5. Downloading: We are going to web scrape the HTML content of each audio file link, automating the download of all the audio files. (2)
  **Milestone: Extraction of good humming files**
6. Feature Extraction Component: For each audio file of the good data that we have, we’re going to run our feature extraction algorithm (4)
  **Milestone: Finishing Feature Extraction**
7. ML Training: Create a training data set, of audio being the data and song being the label. (2)
8. Final Product: When someone uses our app, they will provide their own rendition of the song, and we will standardize, normalize, and feature extract the data and we will use k-nearest neighbors to figure out the predictive label.(4)
  **Milestone: Final Product**
  
----------------------------------------------------------------------------------------------------------------------------------------
  DATA:
  
  #input original data into HIT
  
0	1
0	TestSong1	https://www.youtube.com/watch?v=AgFeZr5ptV8
1	TestSong1	https://www.youtube.com/watch?v=WA4iX5D9Z64

 #output from worker HIT
 
 WorkerId	NameOfSong	RecordingLink
0	2	TestSong1	https://vocaroo.com/i/s1nPB5qtYeQI
1	1	TestSong1	https://vocaroo.com/i/s0ITpZOTVYmF
2	3	TestSong2	https://vocaroo.com/i/s1YhADhsJQD7
3	4	TestSong2	https://vocaroo.com/i/s1XDLqC9Gxvh

 #sort by song
 
 WorkerId	NameOfSong	RecordingLink
0	1	TestSong1	https://vocaroo.com/i/s0ITpZOTVYmF
1	2	TestSong1	https://vocaroo.com/i/s1nPB5qtYeQI
2	3	TestSong2	https://vocaroo.com/i/s1YhADhsJQD7
3	4	TestSong2	https://vocaroo.com/i/s1XDLqC9Gxvh

#aggregate data to create HITS for QC workers
#each HIT includes three of the links of a particular song and quality control

HIT	NameOfSong	RecordingLink1	RecordingLink2	RecordingLink3	Pos_Qual_Ctrl	Neg_Qual_Ctrl
0	1	TestSong1	https://vocaroo.com/i/s0ITpZOTVYmF	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI
1	2	TestSong2	https://vocaroo.com/i/s0ITpZOTVYmF	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI

#output from QC HIT

HIT	NameOfSong	Input.RecordingLink1	Input.RecordingLink2	Input.RecordingLink3	Input.Pos_Qual_Ctrl	Input.Neg_Qual_Ctrl	Answer.RecordingLink1	Answer.RecordingLink2	Answer.RecordingLink3	Answer.Pos_Qual_Ctrl	Answer.Neg_Qual_Ctrl
0	1	TestSong1	https://vocaroo.com/i/s0ITpZOTVYmF	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI	Yes	Yes	No	Yes	No
1	2	TestSong2	https://vocaroo.com/i/s0ITpZOTVYmF	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI	https://vocaroo.com/i/s1nPB5qtYeQI	Yes	Yes	No	Yes	No

#For each row, if the quality control questions pass (answer to pos_qual_ctrl==yes and answer to pos_qual_ctrl==no), then take the link, download the file and add it to the training dataset for our ML algorithm (song name is the label)

  
----------------------------------------------------------------------------------------------------------------------------------------
Quality Control Module for verifying crowdwork:
- In the src directory, you'll find a screenshot and text file of the QC template we will be using on Mechanical Turk
- Similar to what we did in class, we have two controls, one negative and one positive.
- We will be using a weighted majority vote.
- In the instance where we only have two workers that pass the qc control labels, and if their responses result in a tie between whether a sample resembles a song or not, we will denote it as "Yes" because we want as much data as possible.
- To determine whether a worker is qualifiable or not, he or she must select "Yes" for the positive quality control and "No" for the negative quality control
- We justify this qualification because workers must be able to tell whether songs resemble the original or not to set up an accurate database
- Each recording will be listened to 3 times, and the good samples will be allowed to pass for aggregation
- In the final project, we must ensure that the input .csv is properly configured with five columns, where there will be two columns of control and three columns of samples to be verified
- To make it better, the order of samples and control will be randomized on the HIT
- Hopefully, this will give us at least 40 samples to use

Aggregation Module:
- Following the preliminary data collection where crowdworkers are asked to hum back a song they have just heard, we will aggregate the data into an intermediate .csv file to feed into the quality control module
- This step will aggregate all the samples based on the song title
- There will also be positive and negative control data provided by us into the intermedia .csv file
