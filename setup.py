from setuptools import setup, find_packages
import pathlib

project_dir = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (project_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="nextguild",
    version="1.0.0",
    description="Simplify interactions with the Guilded API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArjunSharda/nextguild",
    author="Arjun Sharda",
    author_email="sharda.aj17@gmail.com",
    classifiers=[  # Optional
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Communications :: Chat",
        
    ],



    package_dir={"": "nextguild"},
  
  
    packages=find_packages(where="src"),  # Required

    python_requires=">=3.7",

    install_requires=["requests", "asyncio", "websockets"],

    project_urls={
    "Homepage":"https://github.com/ArjunSharda/nextguild",
    "Bug Tracker":"https://github.com/ArjunSharda/nextguild/issues"
    },
)
