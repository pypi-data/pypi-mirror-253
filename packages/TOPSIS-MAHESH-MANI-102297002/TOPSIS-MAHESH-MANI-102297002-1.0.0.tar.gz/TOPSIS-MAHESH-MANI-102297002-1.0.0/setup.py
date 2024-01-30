from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README
setup(
    name = "TOPSIS-MAHESH-MANI-102297002",
    version = "1.0.0",
    license = "MIT",
    description = "A Python package to find TOPSIS for multi-criteria decision analysis method",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    author = "Mahesh Mani",
    author_email = "imaheshmani13@gmail.com",
    url = "https://www.github.com/maheshmani13",
    keywords = ['topsis', 'UCS654', 'TIET'],
    packages = ["topsis_python"],
    include_package_data = True,
    install_requires = ['pandas', 'numpy'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: MacOS :: MacOS X',  
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3' 
    ],
     entry_points={
        "console_scripts": [
            "topsis=topsis_python.Topsis:main",
        ]
     }
)