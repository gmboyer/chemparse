import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chemparse",
    version="0.1.3",
    author="Grayson Boyer",
    author_email="gmboyer@asu.edu",
    description="Chemical formula parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={},
    packages=['chemparse'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)