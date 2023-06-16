from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("Video", validators=[InputRequired()])
    submit = SubmitField("Hochladen")

@app.route('/', methods=['GET',"POST"])
@app.route('/<name>', methods=['GET',"POST"])
def home(name):
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        return render_template('bedanken.html')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
