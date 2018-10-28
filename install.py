import os


dependencies = ['absl-py==0.5.0','altgraph==0.16.1','astor==0.7.1','backcall==0.1.0','bleach==3.0.2','certifi==2018.8.24','cffi==1.11.5','chardet==3.0.4','Click==7.0','colorama==0.4.0',
'decorator==4.3.0','defusedxml==0.5.0','entrypoints==0.2.3','Flask==1.0.2','future==0.17.0','gast==0.2.0','get==1.0.3','grpcio==1.15.0','h5py==2.8.0','idna==2.7','ipykernel==5.1.0','ipython==7.0.1',
'ipython-genutils==0.2.0','ipywidgets==7.4.2','itsdangerous==0.24','jedi==0.13.1','Jinja2==2.10','jsonschema==2.6.0','jupyter==1.0.0','jupyter-client==5.2.3','jupyter-console==6.0.0','jupyter-core==4.4.0',
'Keras==2.2.4','Keras-Applications==1.0.6','Keras-Preprocessing==1.0.5','macholib==1.11','Markdown==3.0.1','MarkupSafe==1.0','mistune==0.8.4','nbconvert==5.4.0','nbformat==4.4.0','notebook==5.7.0','numpy==1.15.2',
'pandas==0.23.4','pandocfilters==1.4.2','parso==0.3.1','pefile==2018.8.8','pickleshare==0.7.5','post==1.0.2','prometheus-client==0.4.1','prompt-toolkit==2.0.6','protobuf==3.6.1','public==1.0.3','pycparser==2.19','Pygments==2.2.0',
'PyInstaller==3.4','python-dateutil==2.7.3','pytz==2018.5','pywin32-ctypes==0.2.0','pywinpty==0.5.4','PyYAML==3.13','pyzmq==17.1.2','qtconsole==4.4.1','query-string==1.0.2','request==1.0.2','requests==2.19.1','scikit-learn==0.20.0',
'scipy==1.1.0','Send2Trash==1.5.0','simplegeneric==0.8.1','six==1.11.0','sklearn==0.0','sounddevice==0.3.12','tensorboard==1.11.0','tensorflow==1.11.0','termcolor==1.1.0','terminado==0.8.1','testpath==0.4.2','tornado==5.1.1',
'traitlets==4.3.2','urllib3==1.23','wcwidth==0.1.7','webencodings==0.5.1','Werkzeug==0.14.1','widgetsnbextension==3.4.2', 'librosa']
for depends in dependencies:
	os.system('pip install ' + depends)
