# Copyright 2020 Canonical Ltd.
# Licensed under the Apache License, Version 2.0; see LICENCE file for details.

from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import setuptools


def _get_version() -> str:
    """Get the version via k8s/version.py, without loading k8s/__init__.py"""
    spec = spec_from_file_location('k8s.version', 'k8s/version.py')
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    return module.version


with open("README.md", "rt", encoding='utf8') as fh:
    long_description = fh.read()

with open("requirements.txt", "rt", encoding='utf8') as fh:
    requirements = fh.read().split('\n')

version = _get_version()
version_path = Path("k8s/version.py")
version_backup = Path("k8s/version.py~")
version_path.rename(version_backup)
try:
    with version_path.open("wt", encoding="utf8") as fh:
        fh.write('''\
# this is a generated file

version = {!r}
'''.format(version))

    setuptools.setup(
        name="ops-lib-k8s",
        version=version,
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

finally:
    version_backup.rename(version_path)
