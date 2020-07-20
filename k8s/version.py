# Copyright 2020 Canonical Ltd.
# Licensed under the Apache License, Version 2.0; see LICENCE file for details.

import subprocess
from pathlib import Path

__all__ = ("version",)

_FALLBACK = "0.0"  # this gets bumped after release


def _get_version():
    version = _FALLBACK + ".dev0+unknown"

    p = Path(__file__).parent
    if (p.parent / ".git").exists():
        try:
            proc = subprocess.run(
                ["git", "describe", "--tags", "--dirty"],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                cwd=p,
                check=True,
            )
        except Exception:
            pass
        else:
            version = proc.stdout.strip().decode("utf8")
            if "-" in version:
                # version will look like <tag>-<#commits>-g<hex>[-dirty]
                # in terms of PEP 440, the tag we'll make sure is a 'public version identifier';
                # everything after the first - needs to be a 'local version'
                public, local = version.split("-", 1)
                version = public + "+" + local.replace("-", ".")
                # version now <tag>+<#commits>.g<hex>[.dirty]
                # which is PEP440-compliant (as long as <tag> is :-)
    return version


version = _get_version()
