from Application import Application
import sys
import os

app = Application()

if not os.path.exists('./ProjectManager'):
    os.mkdir('./ProjectManager')

if __name__ == "__main__":
    app.parse(sys.argv[1:])
