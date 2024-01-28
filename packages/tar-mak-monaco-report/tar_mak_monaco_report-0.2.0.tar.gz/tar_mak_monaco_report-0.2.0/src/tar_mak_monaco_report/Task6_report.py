from pathlib import Path
import os
from datetime import datetime, timedelta
import argparse


def read_from_file(filepath: Path) -> list:
    """
    Read file and return data in it as a string
    :param filepath: path to the file
    :return: data in file
    """
    with open(Path(filepath), "r", encoding="UTF-8") as fp:
        return fp.readlines()


def parse_abbr(abbr: Path) -> list:
    """
    Looks in the abbr file and translates the information in it into a list of dictionaries that contain information
    about racers, their abbreviation, car, and name.
    :param abbr:a file that contains racer's information
    :return: list with parsed info
    """
    data = read_from_file(abbr)
    racers_info = []
    for racer in data:
        racers_info.append({"abbr": racer.split("_")[0],
                            "name": racer.split("_")[1],
                            "car": racer.split("_")[2].strip()})
    return racers_info


def parse_log(start_log: Path, end_log: Path) -> dict:
    """
    The function takes information from the start_log and end_log files, determines the time of each of the racers,
     and filters out bad information.
    :param start_log: txt file with the initial times of the racers
    :param end_log: file with the final times of the riders
    :return: dict with raser abbr as a key, and lap time as value
    """
    start_time_dict = {}
    try:
        for racer in read_from_file(start_log):
            start_time_dict[racer[0:3]] = datetime.strptime(racer.strip()[-12:], '%H:%M:%S.%f')

    except ValueError:
        pass

    end_time_dict = {}
    for racer in read_from_file(end_log):
        end_time_dict[racer[0:3]] = datetime.strptime(racer.strip()[-12:], '%H:%M:%S.%f')

    personal_time_dict = {}
    for racer, time in end_time_dict.items():
        if time - start_time_dict.get(racer) > timedelta(seconds=0):
            personal_time_dict[racer] = (time - start_time_dict.get(racer))
    return personal_time_dict


def build_report(paths: list, order="asc") -> list:
    """
    Receiving the parameters paths and order, the function builds a dictionary with information about racers in the
    required order.
    of racers using the 'asc' parameter (by default). It determines the order from the fastest racer to the slowest
    and reverses it with the 'desc' parameter.
    :param paths: A list of absolute filepaths leading to the files abbreviations.txt, end.log, start.log.
    :param order: the order in which the list is built. 'asc' parameter (by default), determines the order from
    the fastest racer to the slowest and reversed with the 'desc' parameter.
    :return: a list of dictionaries containing information about each racer, place, name time, car, abbreviation
    """
    abbr, end_log, start_log = paths
    racers_data = []
    bad_time_data = []
    secondary_dict = parse_log(start_log, end_log)

    for racer in parse_abbr(abbr):
        try:
            racer['time'] = secondary_dict[racer['abbr']]
            racers_data.append(racer)
        except KeyError:
            racer['time'] = "Bad time data   "
            racer['place'] = "-"
            bad_time_data.append(racer)

    sorted_racers_data = sorted(racers_data, key=lambda s: s['time'])

    for index, racer in enumerate(sorted_racers_data, start=1):
        racer['place'] = str(index) + "."
    if order == "asc":
        return sorted_racers_data + bad_time_data
    elif order == "desc":
        sorted_racers_data.reverse()
        return bad_time_data + sorted_racers_data


def print_report(paths: list, racer_name=None, order="asc"):
    """
    Function that prints the necessary information about the racers, either one or all of them, depending on the need.
    :param racer_name: the name of the racer about whom you need to print information, default 'None'
    :param order: the order in which the list is built. 'asc' parameter (by default), determines the order from
    the fastest racer to the slowest and reversed with the 'desc' parameter.
    :param paths: A list of absolute filepaths leading to the files abbreviations.txt, end.log, start.log.
    :return: None
    """
    if racer_name:
        if racer_name not in [racer["name"] for racer in build_report(paths=paths)]:
            print("No such driver")
        else:
            for racer in build_report(paths=paths,
                                      order=order):
                if racer['name'] == racer_name:
                    print(f"{racer['place']} {racer['name']} | {racer['car']} | {str(racer['time'])[:-3]}")
    else:
        for racer in build_report(paths=paths,
                                  order=order):
            if order == "desc" and racer['place'] == "15.":
                print('-' * 60)

            print(f"{racer['place']} {racer['name']} | {racer['car']} | {str(racer['time'])[:-3]}")

            if order == "asc" and racer['place'] == "15.":
                print('-' * 60)

def main():
    """
    This function creates CLI for return_single_characters function

    """
    parser = argparse.ArgumentParser(description="This application returns sorted data about Monaco Racing")
    parser.add_argument('--files', '-f', help="enter your path to folder with data", default=None)
    parser.add_argument('--asc', action='store_true', help="sort in ascending order (default)")
    parser.add_argument('--desc', action='store_true', help="sort in descending order")
    parser.add_argument('--driver', '-d', type=str, help="enter driver name", default=None)
    args = parser.parse_args()
    if args.files is None:
        print("Enter path to folder with data files: abbreviations.txt, end.log, start.log ")

    file_pointers = []
    if args.files:
        try:
            for file_to_parse in ['abbreviations.txt', "end.log", "start.log"]:
                if file_to_parse not in os.listdir(args.files):
                    print(f"file {file_to_parse} not found")
                file_pointers.append(Path(os.path.join(args.files, file_to_parse)))
        except FileNotFoundError:
            print("No such folder")
        if args.desc:
            print_report(paths=file_pointers, order="desc")
        elif args.driver:
            print_report(paths=file_pointers, racer_name=args.driver)
        else:
            print_report(paths=file_pointers)


if __name__ == "__main__":
    main()
