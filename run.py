from subprocess import call

call(["python", "setup.py", "-e", "."])
call(["pserve", "development.ini"])
