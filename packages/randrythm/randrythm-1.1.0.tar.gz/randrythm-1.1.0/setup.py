from setuptools import setup, find_packages


with open("README.md", 'r') as f:
    desc = f.read()


setup(
    name="randrythm",
    version='1.1.0',
    long_description=desc,
    long_description_content_type='text/markdown',
    author="Torrez",
    python_requires='>=3.10'
)
