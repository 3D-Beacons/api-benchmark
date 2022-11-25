import csv


class CSVReader:
    """"Read test data from CSV file"""
    
    def __init__(self, file) -> None:
        try:
            file = open(file, "r")
        except TypeError:
            pass  # "file" was already a pre-opened file-like object
        self.file = file
        self.reader = csv.reader(file)
    
    
    def __next__(self):
        try:
            return next(self.reader)
        except StopIteration:
            # reuse file on EOF
            self.file.seek(0, 0)
            return next(self.reader)
