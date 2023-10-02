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
        file = form.file.data
        filename = file.filename
        filename = secure_filename(filename.rsplit('.', 1)[0])
        extension = file.filename.rsplit('.', 1)[1]
        new_filename = f"{name}.{extension}"
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(filename))) # Saves the file
        os.rename(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(filename)), os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(new_filename))) # Renames the file
        return render_template('thanks.html')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
