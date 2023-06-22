# CSV to JSON conversion
import csv
import json

dict1 = {}

try:
    def csv_dict():
        with open('oscar_age_female.csv', 'r') as read_file:
            #convert csv into dict
            reader_file = csv.DictReader(read_file)
            for rows in reader_file:
                key = rows["Index"]
                dict1[key] = rows

    def dict_json():
        # file convert from csv to json and store in variable json_converted
        json_converted = json.dumps(dict1, indent=4)
        print(json_converted)
        with open('oscar_age_female_json.json', 'w') as new_file:
            new_file.write(json_converted)


except FileNotFoundError:
    print('No such file found')
except Exception as e:
    print(e)
finally:
    print('Process done')


csv_dict()
dict_json()