from setuptools import setup,find_packages
setup(
    name='mp42uni',
    version='1.0.5',
    description='Use this to show a video in the terminal (Unicode art)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['opencv-python>=4.5.2.52', 'Pillow>=8.3.2', 'questionary>=1.10.0'],
    url='https://github.com/donno2048/mp42uni',
    packages=find_packages(),
    license='MIT',
    author='Elisha Hollander',
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'mp42uni=mp42uni:main' ] }
)
