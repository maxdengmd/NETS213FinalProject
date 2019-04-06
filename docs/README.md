"# NETS213FinalProject" 
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

Quality Control Module:
- In the src directory, you'll find a screenshot and text file of the template we will be using on Mechanical Turk.
- Similar to what we did in class, we have two controls, one negative and one positive.
- We will be using a weighted majority vote.
- To determine whether a worker is qualifiable or not, he or she must select "Yes" for the positive quality control and "No" for the negative quality control
- We justify this qualification because workers must be able to tell whether songs resemble the original or not to set up an accurate database
- Each recording will be listened to 3 times, and the good samples will be allowed to pass for aggregation
- Hopefully, this will give us at least 40 samples to use

