"# NETS213FinalProject" 
1. Content Aggregation: go through YouTube and get links for top 50 pop songs and timing clips for what we want crowd to sing. We also need to find a platform that the crowd can record their hums into (1)
2. Quality Control Module 1: Go through all the songs and make sure they have a viable chorus (can users mimic the tune of the chorus?) (1)
3. Aggregation Module: Once finalize the content, we upload these video links and timing clips onto MTurk along with the voice recording link (Vocaroo) and wait for responses. (2)
  
  **Milestone: First round of responses from MTurk**
4. Downloading: We are going to web scrape the HTML content of each audio file link, automating the download of all the audio files. (2)
5. Quality Control Module 2: Once we get our data, we will upload all of these crowd-sourced audio files onto a new MTurk HIT. This HIT will ask workers to verify if the hums resemble the source song clip (i.e. we will ask if the hum matches the song link). This will be the second quality control step to ensure that each hum somewhat resembles the song (eliminating audio files with extreme background noise, 1-second audio clips, etc.). This step also includes a control verification. Similar to HW7, we will have “gold-standard” humming verifications where, in one instance, an amateur hum is mimicking the intended song clip, and in another, the hum is not mimicking the intended song clip. If the worker gets both of these right, we will take their answer, so we don’t have to manually go through 2500 audio files. (2)
6. Feature Extraction Component: For each audio file of the good data that we have, we’re going to run our feature extraction algorithm (4)
7. ML Training: Create a training data set, of audio being the data and song being the label. (2)
8. Final Product: When someone uses our app, they will provide their own rendition of the song, and we will standardize, normalize, and feature extract the data and we will use k-nearest neighbors to figure out the predictive label.(4)
