from setuptools import setup, find_packages

setup(
    name = "OCI_Inference_CustomModel",
    version = "0.1.0",
    packages = find_packages(),
    install_requires =  [ 'oci', 'json', 'requests', 'datetime', 'typing'],
    author = "Sakthivel Thangaraj",
    author_email = "sakthiveltvt.thangaraj@gmail.com",
    description =  'A packages for sending the inference request to LLM models custom hosted in OCI',
    url = '',
    classifiers = [ ' programming language:: python :: 3.12 ',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: Independent',
                    ],
    python_requires = '>=3.9',

)