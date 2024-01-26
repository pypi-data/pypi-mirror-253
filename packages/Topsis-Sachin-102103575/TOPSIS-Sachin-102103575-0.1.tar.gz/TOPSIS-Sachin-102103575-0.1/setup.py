import pathlib
from setuptools import setup, find_packages

HERE=pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='TOPSIS-Sachin-102103575',
    version='0.1',
    description='It does a topsis analysis of a given csv file',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Liquidator420/Topsis-Sachin-102103575",
    author="Sachin Sushil Singh",
    author_email="sachinsushilsingh@gmail.com",
    license="MIT",
    packages=["analysis"],
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        "console_scripts": [
            "analysis=analysis.__main__:main",
        ]
    },
)