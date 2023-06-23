# Silentup

This project consists of a web application developed to allow users to upload files to a server. The web application was specifically designed for a school class, enabling students to upload files and share them with teachers.

## Features

The File Transfer Website includes the following features:

- **File Upload**: Users can select and upload files from their local devices.
- **File Transfer**: After uploading, the server owner can easily access the files in a designated folder.
- **Security**: File uploads are handled over an encrypted connection to ensure the security of transmitted data.
- **User-Friendly Interface**: The website has a simple and user-friendly interface to facilitate the upload and download of files.

## Technologies Used

The File Transfer Website was developed using the following technologies:

- **Python**: The back-end logic of the web application was programmed in Python.
- **Flask**: Flask is a web framework for Python and was used to develop the web application.
- **Flask-WTF**: Flask-WTF was used to create and validate forms for file uploads.
- **Werkzeug**: Werkzeug is a Python library used for file handling and secure file name management.
- **HTML**: HTML was used to define the page structure of the website.
- **CSS**: CSS was used to style the appearance and layout of the website.
- **Bootstrap**: Bootstrap, a CSS framework, was used to enhance the design and responsiveness of the website.

## Installation and Execution

To run the File Transfer Website on your local system, you need to follow these steps:

1. Ensure that Python is installed on your system (preferably Python 3).
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required dependencies by running the following command:
   ```
   pip install flask flask-wtf
   ```
4. Start the web application by executing the following command:
   ```
   python main.py
   ```
5. Open your web browser and visit the URL `http://localhost:5000` to view the File Transfer Website.

## Customizing the Website

If you want to customize the website for your own school, you can follow these steps:

1. Change the logo: Replace the existing logo images in the `static/logos` folder with your own logos.
2. Customize the title: Modify the website title in the HTML files `index.html` and `thankyou.html`.
3. Adjust the design: Use CSS to customize the appearance of the website according to your preferences and requirements.
4. Scaling the website: If needed, you can extend the functionality of the website, such as adding user registration, authentication, etc.

## Notes

- Make sure that the `static/files` directory exists and has write permissions for the process running the web application.
- Be sure to update the secret key configuration (`SECRET_KEY`) in the `main.py` file to ensure application security.
- This web application was developed for demonstration purposes and should be thoroughly tested and adapted before use in a production environment.

## Authors

This project was developed by Karl Harrenga. If you have any questions or suggestions, you can contact me at karl.cornelius100@gmail.com.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code, as long as you comply with the license terms.
