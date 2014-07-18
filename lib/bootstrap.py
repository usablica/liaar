import argparse


# to print the tool manual and other messages
def greeting():
    print """
 _      _
| |    (_)
| |     _  __ _  __ _ _ __
| |    | |/ _` |/ _` | '__|
| |____| | (_| | (_| | |
|______|_|\__,_|\__,_|_|
"""


def intro():
    # show greeting message
    greeting()

    # config arguments
    parser = argparse.ArgumentParser(description='Liaar creates a fake REST API using JSON files')

    parser.add_argument('app_name', action="store",
                        help="Application name to run")

    return parser.parse_args()
