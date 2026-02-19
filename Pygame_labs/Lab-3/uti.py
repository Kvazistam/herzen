import PyInstaller.__main__
import shutil

PyInstaller.__main__.run([
    'alien_invasions.py',
    '--onefile',
    '--noconsole',
], )

shutil.copytree('sounds/', '/soundss')
shutil.copytree('sprites/', '/spritess')
