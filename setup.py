import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Django REST Client",
    version="1.0.0-alpha",
    author="Ty Mees",
    author_email="t.mees@randev.nl",
    description="A simple abstraction layer for JSON REST API's, "
                "modelled after Django's ORM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tymees/django-rest-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django :: 2.1",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    data_files=[("", ["LICENSE"])]
)