from unischeduler_web.main import app
import sys
import os


# You can't rely on argv if an external process like gunicorn runs the server
# because the args are going to be from the call to gunicorn, not unischeduler.
# So don't be stupid and don't change this module without double-checking.

# 1 = True, Anything else = false
debug = os.environ.get('DEBUG', "1") == "1"
app.config['DEBUG'] = debug
if debug:
    if len(sys.argv) < 2:
        port = 8000
    else:
        port = int(sys.argv[1])
else:
    port = 5000
    debug = False

if __name__ == "__main__":
    app.run(port=port)
