from app import app
from flask import render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from huffman import Huffman

UPLOAD_FOLDER = '/app/uploads'
OUTPUT_FOLDER = '/app/outputs'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route("/compress-data", methods=["GET", "POST"])
def compress_data():

    if request.method == "POST":

        if request.files:

            file = request.files["ecg_data"]  # pass file to huffman encoding class
            # print('test')
            print(file)

            filename = secure_filename(file.filename)
            print('uploaded filename:', filename)
            print('current directory:', os.getcwd())

            file.save(os.path.join(os.getcwd()+UPLOAD_FOLDER, filename))
            data_filepath = os.getcwd() + UPLOAD_FOLDER + '/' + filename

            input_file_size = os.stat(data_filepath).st_size

            text_object = Huffman(data_filepath)

            ratio = text_object.create_output()

    return render_template("compress_output.html", file_size=input_file_size, compression_ratio=ratio, final_file_size=(text_object.initial_byte_counter * 3), result=text_object.codes_dict)


@app.route('/return-files/')
def return_files():
    try:
        output_filename = 'output.bin'
        output_data_filepath = os.getcwd() + OUTPUT_FOLDER + '/' + output_filename

        return send_file(output_data_filepath, attachment_filename=output_filename)
    except Exception as e:
        return str(e)


