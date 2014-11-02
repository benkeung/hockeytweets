from models import Tweeter
import os
import csv
import sql_data

def load_accounts(csv_file):
    with open(csv_file, "rU") as csvfile:
        csv_reader = csv.reader(csvfile)

        # Read out the first line because it's just the header information
        csv_reader.next()

        tweeters = []
        for row in csv_reader:
            tweeter = tweeters.append(__create_tweeter(row))
        return tweeters

def __create_tweeter(csv_row):
    """
    Creates a tweeter data object from the csv row

    :param csv_row: A csv row representing a twitter handle
    """
    tweeter = Tweeter(
        csv_row[0],
        csv_row[1],
        csv_row[2],
        csv_row[3],
        csv_row[4])
    return tweeter

