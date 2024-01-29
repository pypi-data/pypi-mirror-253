from setuptools import setup, find_packages

setup(
    name="s1_store",
    version="0.0.1",
    packages= find_packages(),
    author="CIA LABS",
    description="A package used to support the image storage and has the upload, retreive , Delete and update function",
    long_description= open("README.md").read(),
    long_description_content_type = "text/markdown"

)
