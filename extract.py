"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    neos = []

    with open(neo_csv_path) as f:
        csv_data = csv.DictReader(f)

        for item in csv_data:
            try:
                neo = NearEarthObject(
                    designation=item["pdes"],
                    name=item["name"],
                    diameter=item["diameter"] if item["diameter"] != "" else "nan",
                    hazardous=True if item["pha"] == "Y" else False
                )

            except Exception as e:
                print(e.__str__())

            else:
                neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    cas = []

    with open(cad_json_path) as f:
        json_data = json.load(f)
        json_data = [dict(zip(json_data["fields"], data)) for data in json_data["data"]]

        for item in json_data:
            try:
                ca = CloseApproach(
                    designation=item["des"],
                    dt=item["cd"],
                    distance=item["dist"],
                    velocity=item["v_rel"]
                )

            except Exception as e:
                print(e.__str__())
                continue

            else:
                cas.append(ca)

    return cas
