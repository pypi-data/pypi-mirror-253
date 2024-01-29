from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='topsis-yashas-102103726',
    packages=['topsis-yashas-102103726'],
    version='0.0.1',
    license='MIT',
    description='This is a Python Package implementing TOPSIS used for multi-criteria decision analysis method',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Yashas Kirnapure',
    author_email='yashas.kirnapure@gmail.com',
    url='https://github.com/Yashaskirnapure',
    keywords=['topsis', 'mcda', 'UCS654', 'TIET'],
    install_requires=[
        'numpy',
        'pandas',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
    ],
)