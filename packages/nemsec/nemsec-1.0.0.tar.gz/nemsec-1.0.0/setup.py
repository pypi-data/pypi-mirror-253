from setuptools import setup, find_packages

setup(
    name='nemsec',
    version='1.0.0',
    author='Nemtyrev Aleksey',
    author_email='art.net82@gmail.com',
    description='NemSec - библиотека для обработки данных от устройств LoRaWAN',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/artnet82/NemSec',  # Update this with your GitHub repository URL
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'pyota',
        'numpy',
        'pandas'
    ],
)
