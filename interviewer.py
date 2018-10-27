import scipy.io.wavfile as wavefile
import sounddevice as sd
import numpy as np
import threading
from get_feature import get_features
from keras.models import model_from_json
import os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model_path=os.getcwd()
model = 'modell.json'
weight = 'model3.h5'

with open(os.path.join(model_path,model), 'r') as f:
	loaded_model_json = f.read()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(os.path.join(model_path,weight))
loaded_model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])


sample_rate = 256000
recording_time = 3
full_audio = None
choice = 0


def predict(feature):
	feature=feature.reshape(1,11,11,1)
	y_pred=loaded_model.predict_classes(feature)
	return y_pred

def record_audio():
	while choice != 0:
		audio_data = sd.rec(frames = sample_rate*recording_time, samplerate = sample_rate,channels = 1,dtype = 'int16',blocking = True)
		global full_audio
		if full_audio is None:
			full_audio = audio_data
		else:
			full_audio = np.vstack((full_audio, audio_data))
	return None


def record_response():
	input("\nEnter to record your response!")
	global choice
	choice = 1
	recorder = threading.Thread(target = record_audio, args = ())
	recorder.start()
	print('Recording...')
	choice = int(input("Enter 0 to stop!"))
	recorder.join()
	print('Recording saved sucessfully!\n')
	return None

def execute_interview(participant_name, json_path):
	"""
	execute_interview(json_path , file_path = None)
	
	Usage:
	Executes an Interview using the provided json file path and records response to
	filepath if provided and returns filepath of audio file.
	"""
	global full_audio
	full_audio = None
	import time,json
	data = json.load(open(json_path,'rb'))
	for dialogue in data:
		if dialogue == '-1':
			record_response()
		else:
			print(dialogue)
		time.sleep(2.5)
	print('Interview Finished')
	import os
	dir_path = './Responses'
	if not os.path.exists(dir_path):
		os.mkdir(dir_path)
	file_path = os.path.join(dir_path, participant_name + '.wav')
	wavefile.write(file_path ,sample_rate, full_audio)
	return file_path

if __name__ == '__main__':
	participant = input("Enter Participant Name: ")
	file_path = execute_interview(participant, './ellie.json')
	print('Generating report! Please wait...')
	feature = get_features(file_path)
	result = predict(feature[:,:121])
	if result == 0:
		condition = 'not Depressed'
	else:
		condition = 'Depressed'
	print('According to the report,you are %s\n'%condition)
	
	
	
