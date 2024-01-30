from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'Library to extract information from Shlink'
LONG_DESCRIPTION = 'This library has been created to facilitate the extraction of information from Shlink in a simple manner. It also allows for the seamless addition of new functions to extract different types of information. Feel free to add or delete words to enhance the description.'

setup(
       
        name="PyShlink", 
        version=VERSION,
        author="Victor Díaz, Gonzalo Moyano",
        author_email="vmdcortes@gmail.com, gonzalomhenriquez13@gmail.com",
        description=DESCRIPTION,
        url="https://github.com/STIV-Cloud-Gaming-Hosting/PyShlink",
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
        'requests==2.31.0',
        'typing_extensions==4.8.0',
        ],
        python_requires='>=3.6',
        license_files=['LICENSE'],
        keywords=['python', 'shlink', 'api'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
        ]
)