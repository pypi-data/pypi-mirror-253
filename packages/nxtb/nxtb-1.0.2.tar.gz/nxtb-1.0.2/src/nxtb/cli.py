# SPDX-FileCopyrightText: 2024 S60W79 <ernetnakisuml@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-only

import argparse
from . import nxtb
import inspect
import sys
import json

allArgs = sys.argv


def main():
    parser = argparse.ArgumentParser(
        description="Free Nextbike Command line interface\nFor more information visit bikes.dvb.solutions.\nDo NOT use this cli from remote. In this case use the attached .py lib ore the .js lib.\nThis code is licensed under GNU GPL v3.",
        epilog="--apikey and --loginkey are optionally, global flags. \nTimes can be given as HH:MM, HH:MM/dd-mm-yyyy or the second time stamp.",
    )

    subparsers = parser.add_subparsers(dest="function_name", help="Arguments")
    subparsers.required = True  # Make sure a subparser is always provided

    # Dynamically create subparsers for each function in nxtb
    for func_name in dir(nxtb):
        func = getattr(nxtb, func_name)
        if callable(func):
            # Extract the function parameters
            params = inspect.signature(func).parameters
            func_parser = subparsers.add_parser(
                func_name, help=f"->" + ", ".join(params)
            )

            for param_name, param in params.items():
                # Skip 'self' or 'cls' if it's a method
                if param_name in ["self", "cls"]:
                    continue

                # Add argument to the parser based on parameter type
                if param.default != inspect.Parameter.empty:
                    if param.default is False:
                        # Boolean parameter, use action='store_true'
                        func_parser.add_argument(
                            f"--{param_name}",
                            action="store_true",
                            help=f"{param_name} flag for {func_name}",
                        )
                    else:
                        func_parser.add_argument(
                            f"--{param_name}",
                            type=type(param.default),
                            default=param.default,
                            help=f"{param_name} argument for {func_name}",
                        )
                else:
                    func_parser.add_argument(
                        f"--{param_name}",
                        type=str,
                        help=f"{param_name} argument for {func_name}",
                    )

    args, unknown_args = parser.parse_known_args()

    # Check if the function exists in the imported module
    if hasattr(nxtb, args.function_name) and callable(
        getattr(nxtb, args.function_name)
    ):
        # Call the function with the extracted arguments
        func_args = {k: v for k, v in vars(args).items() if k not in ["function_name"]}
        for arg in unknown_args:
            if arg.startswith("--"):
                key = arg[2:]
                value = allArgs[allArgs.index("--" + key) + 1]
                exec("nxtb." + key + " = '" + value + "'")
                continue
        print(
            json.dumps(
                json.loads(getattr(nxtb, args.function_name)(**func_args)), indent=2
            )
        )
    else:
        print(
            f"Error: Function '{args.function_name}' not found or not callable in nxtb module."
        )


if __name__ == "__main__":
    main()
