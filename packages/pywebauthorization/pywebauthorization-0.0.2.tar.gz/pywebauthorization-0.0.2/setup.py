from setuptools import setup, find_packages

setup(
    name='pywebauthorization',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author="Loren Hayden",
    author_email="lorenhayden@hotmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)