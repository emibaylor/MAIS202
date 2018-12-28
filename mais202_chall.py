import csv
import matplotlib.pyplot as plt

str = input("Enter input file name.\nIf no input, default of 'data.csv' will be used.\n");

purpose_dict = {}
purpose_cntr = {}

try:
    # if no filename input, use default data.csv
    if (str == ""):
        fname = "data.csv"
    else:
        fname = str

    # open file as csv file
    with open(fname) as csv_file:
        # read file, input it into a dictionary
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # if have already encountered the current purpose, update the values
            key = row['purpose']
            if key in purpose_dict:
                purpose_dict[key] = (purpose_dict[key] + float(row['int_rate']))
                purpose_cntr[key] = (purpose_cntr[key] + 1)
            # if haven't encountered it, add it to the dictionaries of counts and avgs
            else:
                purpose_dict[key] = float(row['int_rate'])
                purpose_cntr[key] = 1

    # avg values storage dict
    avg_int = {}

    # for each purpose, get its avg (sum of rates / # of datapoints), store it
    for purpose in purpose_dict:
        avg_int[purpose] = (purpose_dict[purpose] / purpose_cntr[purpose])

    str = input("Enter output file name.\nIf no input, default of 'avg_interest.csv' will be used.\n")

    # if no filename input, use default avg_interest.csv
    if (str == ""):
        outname = "avg_interest.csv"
    else:
        outname = str

    # writes output file
    with open(outname, "w+") as csv_output:
        writer = csv.writer(csv_output, delimiter=',')

        # writes header row
        writer.writerow(['purpose', 'avg_int_rate'])

        # writes all purposes and avg interest rate pair into output file
        for purpose in avg_int:
            writer.writerow([purpose,avg_int[purpose]])

    # generates graph of output data
    leftcoords = range(1, len(avg_int)+1)
    avgs = []
    purposelist = []

    for purpose in avg_int:
        purposelist.append(purpose)
        avgs.append(avg_int[purpose])

    plt.bar(leftcoords, avgs, tick_label = purposelist, width = 0.75, color = ['turquoise', 'orange'])

    plt.xlabel('Purposes')
    plt.ylabel('Avg. Interest Rate')
    plt.title('Avg. Interest Rate for Given Purposes')
    plt.xticks(rotation = 'vertical', verticalalignment = 'bottom')

    str = input("Enter output file name.\nIf no input, default of 'avg_int_graph.png' will be used.\n")

    # if no filename input, use default avg_int_graph.png
    if (str == ""):
        graphfile = "avg_int_graph.png"
    else:
        graphfile = str

    # saves graph as .png file
    plt.savefig(graphfile)

# error handling
# catches IOErrors, including where data filename does not exist.
except IOError as e:
    print("IOError with file", str, ":\n", e)
# catches KeyError, including if one of the required headings is not present
except KeyError as e:
    print("KeyError: Error with file format:\n", e)
    print("Please check the file meets the specifications.")
# catches TypeError, including if one of the required datapoints is missing or in an incorrect format
except TypeError as e:
    print("TypeError:\n", e )
    print("Something is most likely wrong with the data in the file. Please check that it meets the specifications.")
except ValueError as e:
    print("ValueError:\n", e)
    print("Something is most likely wrong with the data in the file. Please check that it meets the specifications.")
except Exception as e:
    print("Sorry, something went wrong:\n", e)
