from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pynumerical',
    version='0.0.1',
    author='Anar Abdullayev',
    author_email='abdullaanar172@gmail.com',
    description='Numerical methods for differentiation and integration',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/abdanar/pynumerical',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    license="MIT",
    python_requires='>=3.10',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'numpy',
    ],
)
