import setuptools
# 若Discription.md中有中文 須加上 encoding="utf-8"
with open("README.md", "r") as f:
    long_description = f.read()
    
setuptools.setup(
    name = "ErrorType",
    version = "0.1.3",
    author = "YUKAILIAO",
    author_email="joe881003@gmail.com",
    description="Error type analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JOE881003/Error-type-analysis",                                         packages=setuptools.find_packages(),     
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
    )