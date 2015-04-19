import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
from flask import send_from_directory

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	print "Checking if file is allowed"
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
def readFile(filename):
	print "Opening the file..."
	f=open("uploads/%s"%filename,'r')
	print "Reading the file..."
	text=[]
	for line in f:
		text.append(line)
	print "Read the file! Let's show this bad boy now!"
	return render_template('display.html',filename=filename,content=text) 

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
    	print "Uploading file..."
        file = request.files['file']
        if file and allowed_file(file.filename):
        	print "File allowed and uploading..."
        	filename = secure_filename(file.filename)
        	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        	return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template('index.html') 
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form action="/" method=post enctype=multipart/form-data>
    #   <p><input type=file name=file>
    #      <input type=submit value=Upload>
    # </form>
    # '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	print "Awesome, it uploaded!"
	return readFile(filename)
	# return render_template('stolen.html',filename=filename) 
	print "It's rendering"

	# return send_from_directory(app.config['UPLOAD_FOLDER'],
 #                               filename)


if __name__ == '__main__':
    app.run()
