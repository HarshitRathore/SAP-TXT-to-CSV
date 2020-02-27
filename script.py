import csv
import os

# print(" ============")
# print("//")
# print("\\\\")
# print(" ===========")
# print("            \\\\")
# print("            //")
# print(" ============")
print("SAP txt to csv Converter")
print()

# Code to check folder for txt files
for dirname, dirnames, filenames in os.walk('./'):
    txt_files = [filename for filename in filenames if ".txt" in filename.lower()]
    print(f'Found {len(txt_files)} txt files to convert:')
    print(txt_files)
    print()

    # Code to convert each file
    file_index = 1
    for file_ in txt_files:
        try:
            output_file = file_[:-4] + ".csv"
            print(f'#{file_index}: Converting {file_} to {output_file}')
            file_index += 1
            with open(file_, "r") as raw_file:
                file_data = raw_file.read().split('\n')
                original_length = len(file_data)

                # Below code is not required if manual removal is there
                # # Code to remove top summary table
                # index, count = 0, 0
                # for i in file_data:
                #     index += 1
                #     if "------" in i:
                #         count += 1
                #     if count == 3:
                #         break
                # file_data = file_data[index:]

                # Code to remove unnecessary lines
                file_data = [i for i in file_data if "------" not in i]

                # Code to remove empty lines
                file_data = [i for i in file_data if len(i) != 0]

                # Code to split table contents
                file_data = [i.split('|')[1:-1] for i in file_data]

                # Code to remove repetetive headers
                header = file_data[0]
                file_data = [i for i in file_data[1:] if i != header]

                # Code to add single header
                file_data.insert(0, header)

                # Code to refine the data
                refined_data = []
                for i in file_data:
                    refined_row = []
                    for j in i:
                        refined_row.append(j.strip())
                    refined_data.append(refined_row)

                # # Code to print table
                # for i in refined_data:
                #     print(i)

                # Code to write data to csv
                header_data = []
                row_data = []
                ## Adding headers
                header_data = refined_data[0]
                ## Adding rows
                row_data = refined_data[1:]
                ## Writing data
                with open(output_file, 'w', newline='') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(header_data)
                    csvwriter.writerows(row_data)
        except:
            print(f'Error while converting {file_}')

print()
print("Conversion Completed")
