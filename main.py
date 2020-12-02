# Import csv package
import csv

if __name__ == '__main__':

    #instantiate list of lists in the format [[year][number-of-sightings],[year2][number-of-sightings2], ...]
    yearList = []

    with open(r"C:\Users\Matthew\Documents\ufoSightings.csv", 'r') as file_in:
        with open(r"C:\Users\Matthew\Documents\ufoYearCountComplete.csv", 'w', newline='') as file_out:

            # Load csv file for output
            writer = csv.writer(file_out)

            # Step over first line in input file to get rid of headings
            next(file_in)

            for line in file_in:
                # Extract the year from each row of file_in as string
                start = line.find("/", 3) + 1
                end = start + 4
                year = line[start:end]

                # Check if year exists in yearList
                # Increment if true
                # Add to yearList if false
                exists = False
                for i in range(len(yearList)):
                    if(yearList[i][0] == year):
                        exists = True
                        yearList[i][1] += 1
                if exists is False:
                    yearList.append([year, 1])

            # Write to output file the sorted list
            writer.writerows(sorted(yearList))