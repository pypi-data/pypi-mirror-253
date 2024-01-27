from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-responsive-tables2',
    version='0.8.0',
    author='Tristan Balon',
    author_email='tristan.balon@outlook.com',
    description="django-tables2 with AJAX searching and pagination.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LegendaryFire/django-responsive-tables2",
    python_requires='>=3.8',
    install_requires=[
        'django >= 5.0.0',
        'django_tables2 >= 2.7.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 5.0',
        'License :: OSI Approved :: MIT License',
    ]
)
