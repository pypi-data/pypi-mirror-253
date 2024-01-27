from setuptools import setup

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="uuid-v9",
    version="0.1.0",
    author="JHunt",
    author_email="hello@jhunt.dev",
    description="The v9 UUID supports both time-based sequential and random non-sequential IDs with an optional prefix, an optional checksum, and sufficient randomness to avoid collisions.",
    long_description=readme,
    long_description_content_type="text/markdown",
    # url="https://uuid-v9.jhunt.dev",
    packages=["."],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.8",
    platforms="any",
)
