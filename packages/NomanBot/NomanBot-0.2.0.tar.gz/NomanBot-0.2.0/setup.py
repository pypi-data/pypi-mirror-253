from setuptools import setup

setup(
    name='NomanBot',
    version='0.2.0', 
    use_scm_version=True,
    py_modules=['NomanBot'],
    description='A brief description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'g4f',  # add your dependencies here
    ],
)

