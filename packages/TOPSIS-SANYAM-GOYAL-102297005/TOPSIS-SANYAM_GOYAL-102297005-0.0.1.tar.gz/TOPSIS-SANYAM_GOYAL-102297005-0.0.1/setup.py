from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README
setup(
    name = "TOPSIS-SANYAM_GOYAL-102297005",
    version = "0.0.1",
    license = "MIT",
    description = "A Python package to find TOPSIS for multi-criteria decision analysis method",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    author = "Sanyam Goyal",
    author_email = "sanyamgoyal2859@gmail.com",
    url = "https://www.github.com/sanyamgoyal401",
    keywords = ['topsis', 'UCS654', 'TIET', 'data', 'science', 'Prashant Singh Rana'],
    packages = ["topsis_python"],
    include_package_data = True,
    install_requires = ['pandas', 'tabulate'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3' 
    ],
     entry_points={
        "console_scripts": [
            "topsis=topsis_python.topsis:main",
        ]
     }
)