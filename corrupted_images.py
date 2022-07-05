import argparse
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

parser = argparse.ArgumentParser(description="Filter corrupted images in dataset")
parser.add_argument('path', type=str, help="path to folder")

args = vars(parser.parse_args())
folder = args["path"]


def print_notation():
    print("[ 0 ] - Ignore all corrupted files")
    print("[ 1 ] - Move them to another directory")
    print("Enter command number:")


def check_subdir(name):
    print(f"Checking /{name}")

    corrupted_count = 0
    corrupted_files = []
    total_count = len(os.listdir(f"{folder}/{name}"))

    for file in os.listdir(f"{folder}/{name}"):
        image_open = open(f"{folder}/{name}/{file}", 'rb')
        data = image_open.read()

        try:
            tf.io.decode_jpeg(data)
        except:
            corrupted_files.append(file)
            corrupted_count += 1

    print(f"Filtering /{name} finished! Corrupted images count: {corrupted_count} | {corrupted_count/total_count*100:.0f}")

    if corrupted_count > 0:
        while True:
            print_notation()
            command = int(input())

            if command == 0:
                print("All corrupted files are ignored")
                break
            elif command == 1:
                if not os.path.isdir(f"{folder}/Corrupted/"):
                    os.mkdir(f"{folder}/Corrupted/")

                for file in corrupted_files:
                    os.rename(f"{folder}/{name}/{file}", f"{folder}/Corrupted/{file}")

                print("Movement finished")

                break

    print()


for sub_folder in os.listdir(folder):
    check_flag = False

    while True:
        print(f"Do you want to check /{sub_folder}? [ y/n ]")
        output = str(input()).upper()

        if output == "Y":
            check_flag = True
            break
        elif output == "N":
            break
        else:
            print("Unknown answer!")

    if check_flag:
        check_subdir(sub_folder)
