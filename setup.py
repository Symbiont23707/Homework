from setuptools import setup, find_packages

Version = "4.0"
Description = "Parser who parse rss sites"

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read()

setup(
    name="rss-reader",
    author="Bykov Evgeny",
    version=Version,
    description=Description,
    author_email="146iqmega1hp@gmail.com",
    packages=find_packages("rss_packaging"),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[],
    keywords=["python"],
    entry_points={
        "console_scripts": [
            "rss_reader = rss_reader:main",
        ]
    },
)


