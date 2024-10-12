# filevisualizer/file_utils.py

import csv

def read_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data
