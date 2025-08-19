Papertrail is a full-stack note-taking web app built with Flask, MySQL, and JavaScript.
It features a sticky-note UI and a RESTful backend for creating, retrieving, updating, and deleting notes.

## Features
- Add, view, edit, and delete notes
- MySQL database for note storage
- Color-coded sticky note layout

## Setup
1. Clone the repo: git clone https://github.com/rumaiyza/papertrail.git
2. Set up a virtual environment: python -m venv venv
                               source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies: pip install flask pymysql
4. Configure MySQL: CREATE DATABASE papertrail;
                    USE papertrail;

                    CREATE TABLE archive (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      title VARCHAR(255),
                      content TEXT
                    );

   Update MySQL credentials in app.py: db = pymysql.connect(host="localhost",user="your_username",password="your_password",database="papertrail")
6. Run app.py

## Potential Enhancements
- Export notes as PDF
- Enable search feature


