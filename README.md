# Proximity
Proximity is a simple way for special education teachers to track the contact they have with their sudents during non-traditional instruction.

Currently, Proximity is a proof of concept project to validate that the speed and simplicity of a web app outperforms countless spreadsheets.

## What does it do?
* Simplifies the capture of contacts with students during non traditional instruction.
    * Maintain a list of all available students that ever user/teacher can select from
    * Select and maintain a sublist of those students per user/teacher
    * Group students into classes
    * Capture a contact for an individual student
    * Capture a contact for a group of students in a class
    * Maintain list of methods of contact
    * Maintain list of services offered to students

## Preview

![Proximity Preview](https://static.wixstatic.com/media/4cfec4_ef42c91cd56c4359a3aad27046772495~mv2.png)

## How do I run this locally?
* Clone the repo: `git clone https://github.com/KevinDryfuse/contact_tracker.git`
* Create virtual environment, install requirements, and initialize database:
```
python -m venv venv
. venv/Scripts/activate.ps1
pip install -r requirements.txt
flask db upgrade
```
* Run python and create a user:
```
your_email = '<YOUR EMAIL>'
your_first_name = '<YOUR FIRST NAME>'
your_last_name = '<YOUR LAST NAME>'
your_password = '<YOUR PASSWORD>'
from uuid import uuid4
from flask_web import db
from flask_web.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_web import create_app
app = create_app()
app.app_context().push()
your_hashed_password = generate_password_hash(your_password)
u = User(external_id=str(uuid4()), first_name=your_first_name, last_name=your_last_name, email=your_email, password_hash=your_hashed_password)
db.session.add(u)
db.session.commit()
```
* Run the app: flask run
* login and play

## TODO
* Creating a contact starting from a class should be in alphabetical order
* Ability to mark students as absent when creating a contact
* Print functionality
* Update / delete of contacts