import csv

filenames = ['data/turnstile_110507.txt', 'data/turnstile_110508.txt', 'data/turnstile_110509.txt']
output_file = 'data/output_file.txt'
def create_master_turnstile_file(filenames, output_file):
    '''
    Write a function that takes the files in the list filenames, which all have the
    columns 'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn', and consolidates
    them into one file located at output_file.  There should be ONE row with the column
    headers, located at the top of the file. The input files do not have column header
    rows of their own.

    For example, if file_1 has:
    line 1 ...
    line 2 ...

    and another file, file_2 has:
    line 3 ...
    line 4 ...
    line 5 ...

    We need to combine file_1 and file_2 into a master_file like below:
     'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    line 3 ...
    line 4 ...
    line 5 ...
    '''
    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')


        for filename in filenames:

            f_in = open(filename, 'r')
            reader = csv.reader(f_in, delimiter=',')
            writer = csv.writer(master_file, delimiter=',', lineterminator='\n')
            for row in reader:
                if len(row) / 8. == 1:
                    writer.writerow(row)
                else:
                    writer.writerow(row[:8])
                    for i in range((len(row) - 8) / 5):
                        writer.writerow(row[:3] + row[8 + i * 5:8 + i * 5 + 5])

            f_in.close()
    master_file.close()

    # your code here
