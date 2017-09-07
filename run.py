from subprocess import call

call(["pip", "install", "-e", "."])
call(["pserve", "development.ini"])
