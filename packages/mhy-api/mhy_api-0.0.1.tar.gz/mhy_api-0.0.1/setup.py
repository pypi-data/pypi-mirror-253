from setuptools import setup,find_packages

setup(
    name='mhy_api',
    version='0.0.1',
    description='简化mihoyo的api调用方式',
    author='yuchu',
    author_email='yuchus@foxmail.com',
    install_requires=[
        'requests>=2.18.1',
        'cryptography>=38.0.3',
        'rsa>=4.4.1',
        'lxml>=4.9.0',
        'pillow>=10.0.0'
    ],
    packages=find_packages(),
)