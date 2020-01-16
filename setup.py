from setuptools import setup, find_packages

setup(
    name='django-model-auditor',
    version='',
    packages=['migrations'],
    url='',
    license='',
    author='vishalagrawal',
    install_requires=[
        "Django>=3.0",
        "dictdiffer>=0.8.1"
    ],
    python_requires='>=3.8',
    author_email='',
    description='An extension to the Django web framework that provides version control for model instances.'
)