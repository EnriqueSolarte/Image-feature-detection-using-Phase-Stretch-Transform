from setuptools import setup, find_packages

setup(
    name='pst',
    version='0.1.0',
    packages=find_packages(include=['pst', '.']),
    author = "JalaliLabUCLA",
    description = ("Phase stretch transform - https://github.com/JalaliLabUCLA/Image-feature-detection-using-Phase-Stretch-Transform - https://en.wikipedia.org/wiki/Phase_stretch_transform")
)