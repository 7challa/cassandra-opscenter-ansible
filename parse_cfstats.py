# Requirement: Capture reads and writes on Cassandra clusters by taking cfstats from few servers from Cassandra clusters. 
# Parse cfstats output to capture reads and writes.

with open('cfstats_output') as file:
    #file = open('cfstats.log')
    CF_NAME = ''
    ReadCount = ''
    WriteCount = ''
    cf_data = {}
    cf_data_value = []

    for line in file:
        line.lstrip()
        # print(line.lstrip())
        if line == '----------------\n':
            CF_NAME = ''
            ReadCount = ''
            WriteCount = ''

        if 'Keyspace' in line.lstrip().split(':'):
            Keyspace = line.lstrip().split(':')[1]
            print()
            print("KEYSPACE: {:>49} ".format(Keyspace.strip('\n')))
            CF_NAME = Keyspace
            ReadCount = ''
            WriteCount = ''

        if 'Column Family' in line.lstrip().split(':'):
            CF_NAME = line.lstrip().split(':')[1]
            #print('CF_NAME:' + CF_NAME)
        elif 'Read Count' in line.lstrip().split(':'):
            ReadCount = line.lstrip().split(':')[1]
            #print('ReadCount:' + ReadCount)
        elif 'Write Count' in line.lstrip().split(':'):
            WriteCount = line.lstrip().split(':')[1]

            # Conditional Print Start - Requirement is only to capture the tables where there is either read or write
            if int(WriteCount) == 0 and int(ReadCount) == 0:
                pass
            else:
                #Pring only if read and write counts are greater than 0
                print("CF_NAME: {:>50}    ReadCount: {:>10}    WriteCount: {:>10}".format(CF_NAME.strip('\n'),
                                                                                      ReadCount.strip('\n'),
                                                                                    WriteCount.strip('\n')))
            # Conditional Print End

           # print("CF_NAME: {:>50}    ReadCount: {:>10}    WriteCount: {:>10}".format(CF_NAME.strip('\n'), ReadCount.strip('\n'), WriteCount.strip('\n')))

