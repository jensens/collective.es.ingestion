# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="collective.elastic.ingest",
    version="1.0a1",
    description="Celery Queue Tasks for ElasticSearch integration with plone.restapi",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Plone ElasticSearch Celery",
    author="Jens W. Klein",
    author_email="jk@kleinundpartner.at",
    url="https://github.com/collective/collective.elastic.ingest",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/collective.elastic.ingest",
        "Source": "https://github.com/collective/collective.elastic.ingest",
        "Tracker": "https://github.com/collective/collective.elastic.ingest/issues",
        # 'Documentation': 'https://collective.elastic.ingest.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective", "collective.elastic"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[
        "CacheControl",
        "celery",
        "elasticsearch",
        "requests",
        "setuptools",
        "six",
    ],
)
