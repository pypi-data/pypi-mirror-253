
import pip 
import os

def install_dependencies():
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    print(__location__)
    if hasattr(pip, 'main'):
        pip.main(['install',  "-r", __location__+ "/requirements.txt"])
    else:
        pip._internal.main(['install', "-r", __location__+ "/requirements.txt"])

if __name__ == '__main__':
    install_dependencies()