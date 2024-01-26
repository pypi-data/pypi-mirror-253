from setuptools import setup, find_packages

setup(
    name='ft_package_jtaravel',
    version='0.0.1',
    author='Julien Taravella',
    author_email='jtaravel@42paris.fr',
    description='My first package w/ 1 counting function :)',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)