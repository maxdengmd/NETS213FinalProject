README description of code running and analysis

We decided to host our crowd-sourced hum data collection on Mechanical Turk Sandbox which runs as follows:
- It is a form layout that contains:
  - 1 link directs to an example of closed mouth humming
  - 1 link directs to an example of open mouth humming which we want
  - 1 link directs to the song we want the user to hum (which is uploaded as a spreadsheet .csv onto MTurk)
  - 1 link directs to Vocaroo, the platform we are using to collect audio data
  - 1 input form allows users to copy and paste their recording
  - 1 submit button for the form

We plan to do the following analysis based on .mp3 files that are acceptable after our quality control step:
  - Do feature extraction and identification using librosa
  - Normalize and save these extracted feature ids
  - Use this as a database to train our ML model using Keras
  - Use this to predict a user-inputed song