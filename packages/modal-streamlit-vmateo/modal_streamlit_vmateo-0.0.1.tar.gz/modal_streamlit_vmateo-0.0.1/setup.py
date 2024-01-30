import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1' 
PACKAGE_NAME = 'modal_streamlit_vmateo' 
AUTHOR = 'Mateo Pulido'
AUTHOR_EMAIL = 'mateo010120@gmail.com'
URL = 'https://github.com/MateoPulido0120/modal-streamlit-mateo.git'

LICENSE = 'MIT'
DESCRIPTION = 'Es una libreria editada de ventana modal para streamlit para mi caso personal' 
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'streamlit',
      'Deprecated==1.2.14',
      'deprecation'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)