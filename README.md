# MyBlog
*** Currently in development ***

MyBlog web app created with Python and Flask. 

## Contents
* [Libraries](#lib)
    * [Flask-WTF](#flask-wtf)
    * [Flask-SQLAlchemy](#sql-alc)
    * [Flask-Migrate](#flask-mig)
    * [Werkzeug](#werk)
    * [Flask-Login](#flask-log)


---

## <a name="lib"></a>Libraries
   - Used to handle web forms in the app
   - Forms for app are held in the app/forms.py file

   #### <a name='sql-alc'></a>Flask-SQLAlchemy
   - Used as a flask wrapper to sqlalchemy package
   - Allows management of databases using classes, objects and methods
   - Database models are held in app/models.py

   #### <a name='flask-mig'></a>Flask-Migrate
   - Flask wrapper for Alembic package
   - Used to work with database migrations, to allow easier change and modification of databases

   #### <a name='werk'></a>Werkzeug
   - Used for generating/verifying password hashs (with salt) as well as parsing urls

   #### <a name='flask-log'></a>Flask-Login
   - Manages user logged in state


