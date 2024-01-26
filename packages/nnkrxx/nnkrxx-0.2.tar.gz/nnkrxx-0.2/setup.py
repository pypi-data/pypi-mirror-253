from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name='nnkrxx',
    version='0.2',
    author='R. NAVEEN NITHYA KALYAN',
    author_email='naveennithyakalyan@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
     entry_points={
        'console_scripts': [
            'nnkrxx = nnkrxx.main:main',
        ],
     },
     classifiers=[
    
    "License :: OSI Approved :: MIT License",
    
],

    
)
