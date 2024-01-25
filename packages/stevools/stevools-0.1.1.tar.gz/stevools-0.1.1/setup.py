from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        requirements = f.readlines()
    return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]


setup(
    name='stevools',
    version='0.1.1',
    packages=find_packages(exclude=['test', 'test.*']),
    include_package_data=True,
    install_requires=read_requirements(),
    author='steveflyer',
    author_email='',
    description='',
    long_description=open('./README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'ls-py=stevools.scripts.ls_py:main'
        ]
    },
)

# To build:
# python setup.py sdist bdist_wheel
# To upload to pypi:
# twine upload dist/*
