from setuptools import setup, find_packages

setup(
    name="dsss_homework_math_quiz",
    version="0.1.0",
    description="A simple math quiz game for DSSS Homework 2.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/dsss_homework-2",
    packages=find_packages(include=["math_quiz", "math_quiz.*"]),
    install_requires=[
        # Specify dependencies here if there are any, e.g., "numpy>=1.19.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)