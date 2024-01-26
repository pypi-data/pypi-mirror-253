from setuptools import setup, find_packages

setup(
    name='NomanBot',
    use_scm_version=True,
    description='A brief description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'g4f',
    ],
)



