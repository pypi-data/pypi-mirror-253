
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis_Shivam_102116113",
    version="1.0.2",
    author="Shivam Dhiman",
    author_email="shivam4968@gmail.com",
    description="Calculates Topsis Score and Rank",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/shiivvvaam/Topsis_Shivam_102116113.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["Topsis_Shivam_102116113"],
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Shivam_102116022.topsis:main",
        ]
    },
)
