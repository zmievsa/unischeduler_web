from unischeduler_web.main import app
import sys

if len(sys.argv) > 1:
    port = int(sys.argv[1])
    if len(sys.argv) > 2:
        debug = sys.argv[2].lower() == "debug"
    else:
        debug = False
else:
    port = 5000
    debug = False

app.config['DEBUG'] = debug

if __name__ == "__main__":
    app.run(port=port)
