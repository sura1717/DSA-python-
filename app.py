# from flask import Flask

# we are created a dynamin web application

from flask import Flask

# initilize flask app

app = Flask("__name__")

# it create an iinstance of flask which will be your (WSGI) application.

if __name__ == "__main__":
    app.run()


