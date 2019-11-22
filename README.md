# Huffman Encoding

This software system consists of a Python web application deployed using the python web micro-framework: Flask.
The application consists of a folder called ‘app’ which contains all the pertinent classes and files.
The ‘app’ folder consists of three classes  ‘__init__.py’, ‘routes.py’, and  ‘huffman.py’.
The first class ‘__init__.py’ imports all the required dependencies and creates instances of Flask and Bootstrap
that are needed for the rest of the application. The second class ‘routes.py’, describes the three different URI’s
(uniform resource identifies) related to the homepage (‘/index’), the compression page (‘/compress-data’), and the
final output page(‘/return-files’). The third class ‘huffman.py’ details the file parsing, creation of
the Huffman binary tree in the form of a min-heap and finally compressing the file input into a smaller 
size using the Huffman binary tree. The ‘app’ folder consists of three sub-folder called ‘outputs’, ‘templates’, uploads’.
The ‘outputs’ folder contains the output file from the compression algorithm. The ‘templates’ folder contains the HTML UI templates
for displaying the data on the index, compression, and output pages. The ‘uploads’ folder contains the input binary files uploaded
by the user for compression.

### Prerequisites

•	In order to run this application locally 
o	In terminal or command prompt run 
•	git clone https://github.com/vvempati/huffmanEncoding
o	Then after moving into the huffmanEncoding directory
•	Download the latest installer of Python3.8 from python.org/downloads
•	Make sure the command python3 returns the correct version of python 
•	If pip does not exist on the development machine being used to run this application, it can be installed by running the commands
•	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
•	python get-pip.py
•	Then install Flask by running 
•	pip install flask
•	Then install Flask-Bootstrap by running 
•	pip install flask-bootstrap

•	Now the development environment should be good to go, so the user may use terminal or the command prompt to go to the directory where the application was downloaded to and run the command:
o	flask run
•	The application should be up and running on a local port at URL such as 
o	http://127.0.0.1:5000


## Built With

* Python 3.8
* Flask 1.1.1
* Flask-Bootstrap 3.7.1.1

## Authors
Vasavi Vempati
