from setuptools import setup, find_packages

setup(
    name='traccar_api',
    version='0.3.0',
    description='Python client for interacting with Traccar GPS tracking API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='LiGuru',
    author_email='services.nvlahovski@gmail.com',
    url='https://github.com/LiGuru/traccar_api',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
