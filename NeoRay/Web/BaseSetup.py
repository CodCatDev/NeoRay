import os

def CreateConf():
    os.mkdir("web/")
    with open("web/index.html", "w") as f:
        f.write("<html><body>Welcome to NeoRay v0.2.04!</body></html>")

def CheckSetup():
    if not os.path.exists("web/"):
        CreateConf()