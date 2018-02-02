from flask_script import Manager
from app import app, db
from app.db import *
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
manage = Manager(app)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()