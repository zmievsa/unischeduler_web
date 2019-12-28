try:
    from main import app
except ModuleNotFoundError:
    from .main import app

if __name__ == "__main__":
    app.run()