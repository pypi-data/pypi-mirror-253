from setuptools import setup, find_packages

setup(
    name='shellplus',
    version="0.0.005a",
    packages=find_packages(),
    install_requires=[
        'rich',  # Add any other dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Programming Language :: Python :: 3.11',
    ],
)
