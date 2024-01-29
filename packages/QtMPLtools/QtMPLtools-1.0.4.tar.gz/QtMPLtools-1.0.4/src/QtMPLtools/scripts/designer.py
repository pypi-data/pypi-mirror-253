def main():
    import subprocess as sp
    import os
    from os.path import dirname, abspath

    os.environ["PYQTDESIGNERPATH"] = dirname(dirname(abspath(__file__)))
    sp.Popen("pyqt6-tools designer", shell=True, stdout=sp.DEVNULL)