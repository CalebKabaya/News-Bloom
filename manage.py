from app import create_app
from flask_script import Manager,Server

#app instance
app= create_app('development')

manager=Manager(app)
manager.add_command('serve',Server)

if __name__ == '__name__':
    manager.run()