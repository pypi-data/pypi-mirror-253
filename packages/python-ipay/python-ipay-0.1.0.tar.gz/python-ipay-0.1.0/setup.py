from setuptools import setup, find_packages
import subprocess

with open('README.md', 'r') as f:
    long_description = f.read()

with open('LICENSE', 'r') as f:
    _license = f.read()

requirements = [
    i.strip() for i in open('requirements.txt', 'r').readlines() if not i.startswith("#")
]


def get_version_name():
    try:
        # Fetch the latest tag from git as th version name
        latest_tag = subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"]).strip().decode("utf-8")
        return latest_tag
    except subprocess.CalledProcessError:
        # Return default tags when no tags are available.
        return '0.1.0'


setup(
    name="python-ipay",
    description="A python library for ipay.",
    version=get_version_name(),
    author='Jamie Omondi',
    author_email='cruiseomondi90@gmail.com',
    url='https://github.com/Softech-Technologies/ipay',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_data={'': ['*.txt', '*.rst', '*.md']},
    license=_license
)
