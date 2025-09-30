import subprocess

def run_django_server():
    subprocess.run(["python", "manage.py", "runserver"])

if __name__ == "__main__":
    run_django_server()