# DolFile

DolFile makes it easy to keep files in one central location. Send files to it over an API for safe keeping and retrieve them later the same way.

This project is under active development, with more features planned to improve security and usability.

## Prerequisites

1. Python 3.9 or later
2. pip 22.0 or later

## Security: set your own credentials

DolFile creates its first admin user on startup from environment variables, and **it will not start until you provide them**. There is no built-in default login.

- Running from source: set `DOLFILE_USERNAME` and `DOLFILE_PASSWORD`.
- Running with Docker: set `USERNAME` and `PASSWORD` with `-e`, as shown below. (`DOLFILE_USERNAME` and `DOLFILE_PASSWORD` work too.)

Choose a strong password. The credentials are only used the first time, when the database has no users yet.

## Setup

### Option 1: Run from source

1. Clone the repository:
   ```bash
   git clone https://github.com/fpaitoo/DolFile.git
   cd DolFile
   ```
2. Install the dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
3. Set your credentials:
   ```bash
   export DOLFILE_USERNAME='your-username'
   export DOLFILE_PASSWORD='a-strong-password'
   ```
4. Start the server (change the port if you prefer):
   ```bash
   gunicorn --workers 1 --timeout 120 -b 0.0.0.0:8000 wsgi:gunicorn_app
   ```
5. Open `http://127.0.0.1:8000` in your browser (or your server's IP and port) and sign in with the credentials you set.

### Option 2: Docker

1. Pull the image:
   ```bash
   docker pull gpaitoo/dolfile
   ```
2. Run it with your own credentials:
   ```bash
   docker run --name dolfile -p 8000:8000 \
     -e USERNAME='your-username' \
     -e PASSWORD='a-strong-password' \
     gpaitoo/dolfile
   ```
3. Open `http://127.0.0.1:8000` (or your server's IP and port) and sign in with the credentials you set.

## License

Released under the [MIT License](LICENSE).
