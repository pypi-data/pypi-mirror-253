from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='EventEmitterPy',
    version='0.3.0',
    description="A super fast, memory effcient events system for Python",
    author="Ahmed Rakan",
    author_email="ar.aldhafeeri11@gmail.com",
    packages=['EventEmitterPy'],
    install_requires=[
        # Add any dependencies here
    ],
    test_suite='tests',
    long_description=long_description,
    long_description_content_type="text/markdown",
)