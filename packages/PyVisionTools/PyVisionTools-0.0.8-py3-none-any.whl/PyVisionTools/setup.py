import setuptools


with open('PyVisionTools/README.md', 'r') as fhandle:
    long_description = fhandle.read()


setuptools.setup(
    name='PyVisionTools',
    version='0.0.8',
    author='varenikGD',
    author_email='arugula_baklava.0o@icloud.com',
    description='A collection of tools for image processing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Varenik2/PyVisionTools',
    classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
    python_requires='>=3.10.0',
)
