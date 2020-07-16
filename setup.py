import setuptools

with open("README.md", "rt", encoding='utf8') as fh:
    long_description = fh.read()

with open("requirements.txt", "rt", encoding='utf8') as fh:
    requirements = fh.read().split('\n')


setuptools.setup(
    name="ops-lib-k8s",
    version="0.1.0",
    author="The Charmcraft team at Canonical Ltd.",
    author_email="charmcraft@lists.launchpad.net",
    description="Kubernetes component for the Operator Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chipaca/ops-lib-k8s",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=requirements,
)
