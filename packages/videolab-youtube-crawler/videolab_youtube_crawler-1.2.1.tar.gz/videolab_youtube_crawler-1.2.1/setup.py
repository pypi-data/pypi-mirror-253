# update version number (here and in __init__.py)
# python setup.py sdist bdist_wheel
# twine upload --repository pypi dist/*
# username: shuoniu

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="videolab_youtube_crawler",                     # This is the name of the package
    version="1.2.1",                        # The initial release version
    author="Shuo Niu",                     # Full name of the author
    author_email="ShNiu@clarku.edu",
    description="Clark University, Package for YouTube crawler and cleaning data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shuoniu89/VIDEOLab-youtube-analysis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    dependency_links=['https://pypi.org/project/google-api-python-client/'],
    install_requires=[
        'configparser',
        'datetime',
        'pytz',
        'pandas',
        'isodate',
        'xlrd',
        'youtube_transcript_api',
        'google-api-python-client'
    ],
    include_package_data=True,
    package_data={"videolab_youtube_crawler": ["CATEGORY_US.json"]},
    python_requires='>=3.8',
)