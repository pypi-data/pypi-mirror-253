from setuptools import setup, find_packages

setup(
    name='gepeto',
    version='0.0.4',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here.
        # For example: 'requests >= 2.25.1'
    ],
    author='Uzair',
    author_email='uzair@hellogepeto.com',
    description='pip install gepeto',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourgithub/gepeto',
)
