import setuptools

def readme():
    with open('README.md') as file:
        README = file.read()
    return README

setuptools.setup(
    name="TOPSIS-SuvidhaSrivastava-102103019",
    version="0.1.0",
    description="Python package for implementing TOPSIS technique.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Suvidha Srivastava",
    author_email="ssrivastava1_be21@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: 3.7"
    ],
    packages=["src"],
    include_package_data=True,
    install_requires=['scipy',
                      'tabulate',
                      'numpy',
                      'pandas',
     ],
     entry_points={
        "console_scripts": [
            "topsis=src.topsis:main",
        ]
     },
)
