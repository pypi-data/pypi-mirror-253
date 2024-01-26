import setuptools

PACKAGE_NAME = "group-profile-remote"
package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.21',  # https://pypi.org/project/group-profile-remote/
    author="Circles",
    author_email="info@circles.life",
    description="PyPI Package for Circles Group-Profile-Remote Python",
    long_description="This is a package for sharing common Group-Profile-Remote function used in different repositories",
    long_description_content_type="text/markdown",
    url=f"https://github.com/circles-zone/{PACKAGE_NAME}-python-package",
    ppackages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'python-dotenv>=1.0.0',
        'pytest>=7.4.0',
        'database-without-orm-local>=0.0.23',
        'logzio-python-handler>= 4.1.0',
        'user-context-remote>=0.0.23',
        'logger-local>=0.0.11',
        'url-local>=0.0.27',
    ],
)
