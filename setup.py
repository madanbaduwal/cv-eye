# !/usr/bin/env python
 
try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup
 
# Load packages from requirements.txt
with open(("requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]
    
setuptools.setup(
    install_requires=[required_packages],
    name="madan",
    version="0.0.1",
    author="Madan Baduwal",
    author_email="madanbaduwal100@gmail.com",
    description="Open source ai library",
    url="https://github.com/MadanBaduwal/ai_library",
    project_urls={
        "Bug Tracker": "https://github.com/MadanBaduwal/ai_library/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "madan"},
    packages=setuptools.find_packages(where="madan"),
    python_requires=">=3.6",
)
