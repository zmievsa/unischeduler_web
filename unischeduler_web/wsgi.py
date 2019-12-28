try:
    from unischeduler_web import app
except ModuleNotFoundError:
    from .unischeduler_web import app

if __name__ == "__main__":
    app.run()