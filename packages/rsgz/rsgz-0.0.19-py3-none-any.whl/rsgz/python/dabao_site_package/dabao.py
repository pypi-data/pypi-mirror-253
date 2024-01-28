import os,sys
import pkg_resources
import wheel.bdist_wheel

# 获取 site-packages 路径
site_packages_path = next(p for p in sys.path if 'site-packages' in p)  # F:\python\lib\site-packages

# # 获取已安装的模块列表
installed_modules = [dist.key for dist in pkg_resources.working_set]  # ['zipp', 'yarl', 'yacs', 'xlwings', 'xlsx2csv', 'xlrd', 'wsproto', 'wmi', 'win32-setctime', 'widgetsnbextension', 'whichcraft', 'wheel', 'werkzeug', 'websockets', 'webencodings', 'wcwidth', 'virtualenvwrapper-win', 'virtualenv', 'uvicorn', 'urllib3', 'uc-micro-py', 'typing-extensions', 'typeguard', 'twine', 'trio', 'trio-websocket', 'transformers', 'traits', 'traitlets', 'tqdm', 'tornado', 'torchvision', 'torch', 'toolz', 'tomli', 'tokenizers', 'tinycss2', 'tifffile', 'terminado', 'taichi', 'starlette', 'speech', 'sourceinspect', 'soupsieve', 'sortedcontainers', 'sniffio', 'six', 'simplejson', 'setuptools', 'send2trash', 'semantic-version', 'selenium', 'scipy', 'scikit-image', 'safetensors', 'rsgz', 'rsa', 'rich', 'rfc3986', 'requests', 'requests-toolbelt', 'regex', 'readme-renderer', 'rdflib', 'rapidfuzz', 'qtpy', 'qtconsole', 'qt5-tools', 'qt5-applications', 'pyzmq', 'pyyaml', 'pyxnat', 'pywinpty', 'pywin32', 'pywin32-ctypes', 'pywavelets', 'pytz', 'pytweening', 'python-multipart', 'python-levenshtein', 'python-dotenv', 'python-dateutil', 'pytest', 'pysocks', 'pyscreeze', 'pyrsistent', 'pyrect', 'pyqt5', 'pyqt5-tools', 'pyqt5-sip', 'pyqt5-qt5', 'pyqt5-plugins', 'pypiwin32', 'pypinyin', 'pyperclip', 'pyparsing', 'pyopenssl', 'pyopengl', 'pyodbc', 'pynput', 'pymysql', 'pymupdf', 'pymsgbox', 'pyinstaller', 'pyinstaller-hooks-contrib', 'pyhook3', 'pyhook', 'pygments', 'pygls', 'pygetwindow', 'pygame', 'pydub', 'pydot', 'pydantic', 'pycparser', 'pyautogui', 'pyaudio', 'pyasn1', 'psutil', 'psd-tools', 'prov', 'prompt-toolkit', 'prometheus-client', 'proglog', 'prettytable', 'polars', 'pluggy', 'platformdirs', 'pkgutil-resolve-name', 'pkginfo', 'pip', 'pinyin2hanzi', 'pillow', 'piexif', 'pickleshare', 'photoshop-python-api', 'pep517', 'pefile', 'pathlib', 'parso', 'pandocfilters', 'pandas', 'pandas-datareader', 'packaging', 'outcome', 'orjson', 'openpyxl', 'openpyxl-image-loader', 'opencv-python', 'omegaconf', 'numpy', 'notebook', 'nipype', 'nibabel', 'networkx', 'nest-asyncio', 'nbformat', 'nbconvert', 'nbclient', 'multidict', 'moviepy', 'mouseinfo', 'more-itertools', 'money', 'mistune', 'mdurl', 'mdit-py-plugins', 'matplotlib', 'matplotlib-inline', 'markupsafe', 'markdown-it-py', 'lxml', 'lsprotocol', 'looseversion', 'loguru', 'linkify-it-py', 'levenshtein', 'lama-cleaner', 'kiwisolver', 'keyring', 'keyboard', 'jupyterlab-widgets', 'jupyterlab-pygments', 'jupyter', 'jupyter-core', 'jupyter-console', 'jupyter-client', 'jsonschema', 'jinja2', 'jedi', 'jedi-language-server', 'jaraco.classes', 'itsdangerous', 'isodate', 'ipywidgets', 'ipython', 'ipython-genutils', 'ipykernel', 'install', 'iniconfig', 'imutils', 'importlib-resources', 'importlib-metadata', 'imageio', 'imageio-ffmpeg', 'idna', 'idm', 'huggingface-hub', 'httpx', 'httplib2', 'httpcore', 'h11', 'gradio', 'gradio-client', 'future', 'fsspec', 'frozenlist', 'forex-python', 'fonttools', 'flaskwebgui', 'flask', 'flask-cors', 'fitz', 'filelock', 'ffmpy', 'fastjsonschema', 'fastapi', 'exceptiongroup', 'etelemetry', 'et-xmlfile', 'entrypoints', 'docutils', 'docstring-to-markdown', 'docopt', 'dnspython', 'distlib', 'dill', 'diffusers', 'defusedxml', 'decorator', 'debugpy', 'cycler', 'cssselect', 'cryptography', 'configparser', 'configobj', 'comtypes', 'commonmark', 'colorama', 'click', 'ci-info', 'chrhyme', 'charset-normalizer', 'cffi', 'certifi', 'cattrs', 'build', 'bs4', 'bleach', 'beautifulsoup4', 'baidupcsapi', 'backcall', 'attrs', 'asynctest', 'async-timeout', 'async-generator', 'astunparse', 'argparse', 'argon2-cffi', 'argon2-cffi-bindings', 'anyio', 'antlr4-python3-runtime', 'altgraph', 'altair', 'aiosignal', 'aiohttp', 'aiofiles', 'aggdraw', 'accelerate']

# 遍历每个模块，打包成 wheel 文件
for module_name in installed_modules:
    module_path = os.path.join(site_packages_path, module_name)  # F:\python\lib\site-packages\zipp
    if os.path.isdir(module_path):
        # 构建 wheel 文件的输出路径
        wheel_path = os.path.join(site_packages_path, f"{module_name}.whl")  # F:\python\lib\site-packages\yarl.whl
        # 创建 bdist_wheel 实例
        bdist_wheel = wheel.bdist_wheel.bdist_wheel

        # 设置输入和输出路径
        bdist_wheel.dist_dir = site_packages_path
        bdist_wheel.build_dir = module_path

        # 执行打包操作
        bdist_wheel.run()

        # 重命名生成的 wheel 文件
        os.rename(os.path.join(site_packages_path, "dist", f"{module_name}-none-any.whl"), wheel_path)

        # 清理临时文件
        os.remove(os.path.join(site_packages_path, "dist", "requires.txt"))
        os.rmdir(os.path.join(site_packages_path, "dist"))
        os.rmdir(os.path.join(site_packages_path, "build"))