from waitress import serve

from bookstore.asgi import application

if __name__ == "__main__":
    serve(application, port="8000")
