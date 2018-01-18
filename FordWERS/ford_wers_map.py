__author__ = 'shiyu'
import csv
from collections import defaultdict
from collections import OrderedDict #
import contextlib

def load_wers(file):
    reader = csv.reader(open(file, 'r'),delimiter='\t')
    d = {}
    for row in reader:
       k, v = row
       print k
       d[k.strip()] = v
    return d




def parse_chunked_code(fileB, dict, outputA, outputB):

    fh = initial_featureheaders()
    reader = csv.reader(open(fileB, 'r'),delimiter='\t')

    with open(outputA,'w') as out1, open(outputB, 'w') as out2:
        out1.write('OF0431_VIN_R'+','+','.join(fh.values())+'\n')
        out2.write('OF0431_VIN_R'+','+','.join(fh.values())+'\n')
        for row in reader:
            k, v = row
            output = match_wers(v,dict)
            print output["f"]
            print output["c"]
            out1.write(k+','+','.join(output["f"].values())+'\n')
            out2.write(k+','+','.join(map(str, output["c"].values()))+'\n')

    out1.close()
    out2.close()

def initial_featuredict():
    d = OrderedDict()
    for i in range(1,18,1):
        d[i]=''
    return d

def initial_featureheaders():
    d=OrderedDict()
    d[1]='Body Code'
    d[2]='Body Style'
    d[3]='Engine'
    d[4]='Transmission'
    d[5]='Drivetrain'
    d[6]='PEP/TPO'
    d[7]='Interior Trim'
    d[8]='Interior Trim Color'
    d[9]='Exterior Paint Color'
    d[10]='Version'
    d[11]='Moonroof/Sunroof'
    d[12]='Navigation'
    d[13]='Wheels'
    d[14]='Tech Package'
    d[15]='Handling Package'
    d[16]='Reverse Sensing'
    d[17]='Automated Parking System'
    return d

def initial_featurecount():
    d = OrderedDict()
    for i in range(1,18,1):
        d[i]=int(0)
    return d

def match_wers(codestr,dict):
    fd = initial_featuredict()
    fc = initial_featurecount()
    for item in str(codestr).split():
        print item
        for k,v in dict.items():
            if item==k:
            #if item.startswith(k):
                print item,k,v
                if len(fd[int(v)])==0:
                    fd[int(v)]=item
                else:
                    fd[int(v)]=fd[int(v)]+'|'+item
                fc[int(v)] += 1
    return {"f": fd, "c": fc}




if __name__ == '__main__':
    wers_dict = load_wers('/home/shiyu/ford/full_dict.csv')
    out1 = '/home/shiyu/ford/out1.csv'
    out2 = '/home/shiyu/ford/out2.csv'
    parse_chunked_code('/home/shiyu/ford/output.txt', wers_dict, out1,out2)
    #initial_featuredict()
    #test()