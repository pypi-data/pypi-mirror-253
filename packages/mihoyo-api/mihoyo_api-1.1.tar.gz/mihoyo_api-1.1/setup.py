from setuptools import setup,find_packages

setup(
    name='mihoyo_api',
    version='1.01',
    description='简化mihoyo的api调用方式',
    author='yuchu',
    author_email='yuchus@foxmail.com',
    install_requires=[
        'requests>=2.18.1',
        'cryptography>=38.0.3',
        'rsa>=4.4.1',
    ],
    packages=find_packages(),
)