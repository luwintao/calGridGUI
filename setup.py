from setuptools import setup
import sys

# 用于pyinstaller打包的配置
APP = ['calGridGUI.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'pyperclip'],
    'excludes': [],
    'iconfile': None,  # 可以添加图标文件路径
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)