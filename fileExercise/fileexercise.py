import os.path
import json
import logging

def fileErrorMessage(Exception):
    "wrong file selected"
def createFile(filename):
    try:
       data= {1:"Windows",2:"Linux",3:"Mac",4:"Other"}
       with open(filename, "w") as file:
        file.write(json.dumps(data))
    except fileErrorMessage as e:
             logging.error(e)
             print(e)


def ask_servernames(filename):
    try:
        with open(filename,"r") as inFile:
            for line in inFile:
                line = line.split()
                logging.info(line)
                print(line)
    except IOError as e:
            logging.error(e)
            print(e)

def print_names_from_file(filename):
    try:
        with open(filename, "r") as inFile:
            for line in inFile:
                print(line)
    except IOError as e:
        print(e)

def main():
    try:

        filename = "C:\\Users\\MU59BM\\source\\repos\\PythonTraining\\fileExercise\\data.txt"
        logFile = "C:\\Users\\MU59BM\\source\\repos\\PythonTraining\\fileExercise\\data.log"
        logging.basicConfig(
            filename='my_log_file.log',  # Specify the file name
            filemode='a',  # Append mode (use 'w' for overwrite)
            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
            datefmt='%H:%M:%S',
            level=logging.DEBUG
        )

        createFile(filename)
        ask_servernames(filename)
        print_names_from_file(filename)
    except Exception as e:
        print("Something went wrong...")
        print(e)

if __name__ == "__main__":
    main()