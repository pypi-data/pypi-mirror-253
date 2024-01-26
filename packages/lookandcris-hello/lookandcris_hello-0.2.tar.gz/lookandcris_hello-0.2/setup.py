from setuptools import setup, find_packages

setup(
    name='lookandcris_hello',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
        # e.g. 'numpy>=1.11.1'
    ],
    author='LookAndCris',
    description='A small example package with some dependencies',
    license='MIT',
    entry_points={
        'console_scripts': [
            'lookandcris_hello = src:say_hello'
        ]
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
# prepare for distribution
# pip install setuptools wheel twine --upgrade

# first step: python setup.py sdist
# python3 setup.py sdist bdist_wheel

# second step: testing local
# pip install dist/lookandcris_hello-0.1-py3-none-any.whl

# Con el entry point, podemos ejecutar el comando lookandcris_hello

# third step: upload to pypi
# twine upload dist/*