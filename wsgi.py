from unischeduler_web.main import app
import sys


app.config['DEBUG'] = False

if __name__ == "__main__":
    app.run(port=5000 if len(sys.argv) < 2 else int(sys.argv[1]))
