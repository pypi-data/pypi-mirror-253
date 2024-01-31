from setuptools import find_packages, setup

setup(
    name="hf_video",
    version="0.0.1",
    description="A package for handling videos in Huggingface",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.8.13",
)
