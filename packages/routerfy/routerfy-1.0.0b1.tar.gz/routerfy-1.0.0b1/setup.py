from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

    
setup(
    name = 'routerfy',
    version = '1.0.0b1',
    author = 'Bruno Junqueira & Mateus Brazil',
    author_email = 'brunosdsj@gmail.com',
    license = 'MIT',
    description = 'O Routerfy tem uma sintaxe similar ao FastAPI. Feito para ser leve e de fácil uso para serviços AWS Serverless.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.pactual.net/bruno-s-junqueira/routerfy',
    py_modules = ['routerfy'],
    include_package_data=True,
    packages = find_packages(),
    extras_require ={
        "dev": ["click>=7.1.2", "fastapi==0.108.0", "uvicorn==0.25.0", "python-dotenv", "pyyaml"]
    },
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        routerfy=routerfy.cli:cli
    '''
)