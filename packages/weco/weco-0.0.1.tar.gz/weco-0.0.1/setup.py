from setuptools import setup, find_packages

setup(
    name='weco',
    version='0.0.1',
    description='Weco AI Python package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yuxiang Wu',
    author_email='yuxiang@weco.ai',
    url='https://github.com/wecoai/weco-python',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ] ,
    python_requires='>=3.8',
)

