from setuptools import setup, find_packages

setup(
    name="NegsArchive",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here, e.g.
        # "numpy>=1.0",
        # "pandas>=1.0",
    ],
    entry_points={
        "console_scripts": [
            # If your project has command-line scripts, add their entry points here, e.g.
            # "my_script=my_package.my_module:main",
        ],
    },
    python_requires=">=3.6",
    # Add metadata about your project
    author="Sepehr Shahraeini",
    author_email="shahraeinisepehr@gmail.com",
    description="This is a python code that archive Negs channel content",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Sepehr-Shahraeini/NegsArchive.git",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)