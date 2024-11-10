from setuptools import setup, find_packages
from pathlib import Path

__version__ = '0.0.0'
AUTHOR_NAME = 'Nida-16'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'nidashaikh1602@gmail.com'
REPO_NAME = 'CNN-Kidney-Disease-Classification'
SHORT_DESC = 'CNN based Kidney Disease Classification Project'
LONG_DESC = Path("README.md").read_text(encoding="utf-8")
KEYWORDS = "cnn, classifier, classification"

setup(
    name=SRC_REPO,  # Required
    version=__version__,  # Required
    author=AUTHOR_NAME,  # Optional
    author_email=AUTHOR_EMAIL,  # Optional
    description=SHORT_DESC,  # Optional
    long_description=LONG_DESC,  # Optional
    long_description_content_type='text/markdown',
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",  # Optional
    project_urls={  # Optional
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
        # "Say Thanks!": "http://saythanks.io/to/example"
    },
    package_dir={"": "src"},  # Optional
    packages=find_packages(where="src"),  # Required
    entry_points={"console_scripts": [
        f"{SRC_REPO}={SRC_REPO}:main"]},  # Optional
    classifiers=["Development Status :: 1 - Planning",
                 "Intended Audience :: Developers",
                 "Topic :: Scientific/Engineering :: Medical Science Apps.",
                 "License :: OSI Approved :: MIT License",],
    keywords=KEYWORDS,  # Optional
    python_requires=">=3.10, <4"
)
