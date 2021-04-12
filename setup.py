from setuptools import setup,find_packages
setup(
    name='mp42uni',
    version='1.0.1',
    description='Use this to show a video in the terminal (Unicode art)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['opencv-python', 'Pillow'],
    url='https://github.com/donno2048/mp42uni',
    packages=find_packages(),
    license='MIT',
    author='Elisha Hollander',
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'mp42uni=mp42uni:main' ] }
)
