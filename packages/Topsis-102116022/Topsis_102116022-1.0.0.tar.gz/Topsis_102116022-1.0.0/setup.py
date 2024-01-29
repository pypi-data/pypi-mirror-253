
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis_102116022",
    version="1.0.0",
    author="Kunal Arora",
    author_email="arorakunal0930@gmail.com",
    description="Calculates Topsis Score and Rank",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/kunalarora0930/Topsis_Kunal_102116022",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["Topsis_Kunal_102116022"],
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Kunal_102116022.topsis:main",
        ]
    },
)
