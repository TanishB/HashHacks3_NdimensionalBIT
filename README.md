# HashHacks3_NdimensionalBIT
## Project Name: Automated Depression Detection (ADDE)
## Theme: Healthcare
<b>Automating the process of tackling Depression with the help of Machine Learning</b> <br>

# Abstract

Depression is a common mental disorder that causes people to experience <br>
->depressed mood<br>
->loss of interest or pleasure<br>
->feelings of guilt or low self-worth<br>
->disturbed sleep or appetite<br>
->low energy<br>
->poor concentration.<br>
There are many problems we are dealing with, today like terrorism, poverty, corruption. We can say these are the known enemies but depression is the unknown enemy of society and we all know that:<br>
"An Unknown Enemy is more dangerous than a Known one"<br>
 <b>BUT</b> <br>
There is a problem which is bigger than depression and that is its  <b>DETECTION</b> <br>
=>Studies have shown that most of the people who are suffering from depression don't even know that they are in the depression. That means they don't feel the need to visit a doctor<br>
=>And even if they consult a doctor, then also it is not necessary that the doctor will correctly diagnose it. i.e a doctor cannot perform this task accurately.<br>
So some <b>automatic</b> and reliable means of depression recognition is required.<br>
<b>BUT DON'T WORRY</b><br>
We are in an age of Machine Learning & Artificial Intelligence and we can assign this task to machines which will perform this task at much good accuracy than humans.<br>
As depressed people behave differently from normal people which can be detected in audio and visual recordings of the patient. Studies have shown that depressed people tend to avoid eye contact, engage less in verbal communication, speak anxiously in short phrases and monotonously.<br>
### OUR AIM<br>
Is to develop an ML model which will predict if a person is suffering from depression or not using audio, visual and text features.<br>
# Data <br>
## Description:<br>
For <b>Audio Analysis:</b><br>
Data has been taken from DAIC-WOZ database which contains 189 clinical interviews b/w the patient and virtual interviewer Ellie. <br>
For<b> Text Analysis:</b><br>
Twitter Sentiment Analysis Dataset has been taken.<br>

## Data Pre-processing <br>
->For fixing the corrupted files we used SOX [Sound Extension] through system programming<br>
->And then using the transcript file we removed the voice of virtual interviewer.<br>
Data preprocessing is done using <b>Automate_Trimming.ipynb</b> file.<br>

# Methodology<br>
## Audio Analysis<br>
128 audio features are extracted from each audio file using Librosa library.<br>
And using those features we made spectrograms of every audio file.<br>
Unfortunately the ground truth of every audio file was not available so we did pretraining to know the labels of those audio files.<br>
So finally we have spectrograms and labels of each audio file.<br>
Finally we pass these into the Convolution Neural Network.<br>

## Text Analysis:<br>
Twitter sentiment dataset is taken and with the help of the natural language processing the classification is done and the emotion of the speech is classified.

## Results:<br>
The accuracy of 81% has been achieved overall .
<b> Installation part</b> <br>
1.git clone the repository
2.run python install.py
3. run python interviewer.py
