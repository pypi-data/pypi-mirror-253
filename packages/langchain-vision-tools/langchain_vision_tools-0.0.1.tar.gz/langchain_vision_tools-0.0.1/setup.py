from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Vision tools for langchain'
LONG_DESCRIPTION = 'Includes a verity of vision based tools for langchain agents integration'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="langchain_vision_tools",
    version=VERSION,
    author="Lior Strugach",
    author_email="liliyanoffical@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['langchain', 'openai', 'deepdanbooru', 'tensorflow', 'clip-interrogator', 'numpy',
                      'python-dotenv'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'langchain', 'tools', 'agents', 'ai'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)