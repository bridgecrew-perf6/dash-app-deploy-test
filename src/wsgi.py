from app import app as dash_app

application = dash_app.server

if __name__ == "__main__":
    application.run()
