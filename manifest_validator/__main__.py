"""
manifest_validator

Usage:
  manifest_validator validate <manifest>
"""
import toml
import json
from collections import frozenmap
from typing import Dict, Any
from docopt import docopt  # type: ignore
from manifest_validator import __version__
from manifest_validator.validator import validate


def main(args: Dict[str, Any]):
    with open(args["<manifest>"], "r") as f:
        manifest = toml.load(f)
        manifest = frozenmap(manifest)

    if args["validate"]:
        success, errors = validate(manifest)
        if not success:
            print(json.dumps(errors, indent=4))
            exit(1)


if __name__ == "__main__":
    args = docopt(__doc__, version=__version__)
    main(args)
