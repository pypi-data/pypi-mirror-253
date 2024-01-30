from setuptools import setup, find_packages

setup(
    name="qeapp-xps",
    version="0.1.0",
    packages=find_packages(),
    description="A plugin for calculating X-ray Photoelectron Spectroscopy (XPS) spectra.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Xing Wang",
    author_email="xingwang1991@gmail.com",
    url="https://github.com/superstar54/qeapp-xps",
    install_requires=[
        "anywidget",
        "ipywidgets",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    include_package_data=True,  # This tells setuptools to check MANIFEST.in for additional files
    entry_points={
        "aiidalab_qe.properties": [
            "xps = qeapp_xps:xps",
        ],
    },
    
)
