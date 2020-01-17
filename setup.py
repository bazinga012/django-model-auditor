from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-model-auditor',
    version='0.0.4',
    url='https://github.com/bazinga012/django-model-auditor',
    license='MIT',
    author='vishalagrawal',
    install_requires=[
        "Django>=3.0",
        "dictdiffer>=0.8.1"
    ],
    python_requires='>=3.8',
    long_description_content_type='text/markdown',
    long_description=long_description,
    author_email='vishal18593@gmail.com',
    packages=find_packages(),
    description='An extension to the Django web framework that provides version control for model instances.'
)
