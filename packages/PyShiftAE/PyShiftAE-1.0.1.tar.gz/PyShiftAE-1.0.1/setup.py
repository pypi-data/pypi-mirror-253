from setuptools import setup, find_packages

setup(
    name='PyShiftAE',
    version='1.0.1',
    description='Python for After Effects',
    author='Trenton Flanagan',
    packages=find_packages(),
    include_package_data=True,  # This line ensures that the data specified in MANIFEST.in is included
    install_requires=[
        # Dependencies listed here
    ],
    package_data={
        'PyShiftAE': ['*.pyd', '*.pyi', '*.aex'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.5',
)
