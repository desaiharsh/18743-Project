import sys
import glob
import os

print "Number of arguments: ", len(sys.argv)
print "The memory type is: ", str(sys.argv[1])
print "The word width is: ", str(sys.argv[2])
#print "The filename is: ", str(sys.argv[3])

memtype = str(sys.argv[1])
wordwidth = str(sys.argv[2])
#filename = str(sys.argv[3])

outputfile = open("output-"+memtype+"-ww"+wordwidth+".txt", "w")

if memtype == "SRAM":
    area_line = 45
    area_eff_line = 48
    read_lat = 50
    write_lat = 60
    read_dyn = 70
    write_dyn = 80
    leakage = 88
elif memtype == "MRAM" or memtype == "SOT":
    area_line = 53
    area_eff_line = 56
    read_lat = 58
    write_lat = 68
    read_dyn = 79
    write_dyn = 90
    leakage = 99


#filepath = str("op_"+memtype+"_ww"+wordwidth+"/"+*.

outputfile.write("Area AreaEfficiency ReadLatency WriteLatency ReadDynEnergy WriteDynEnergy LeakageEnergy \n")

for filename in glob.glob('op_'+memtype+'_ww'+wordwidth+'/'+'*.txt'):
    print "File name:", str(filename)
    outputfile.write(filename+"\n")
    inputfile =  open(filename, "r")
    for i,line in enumerate(inputfile):
        if i == area_line:
            test_line = line.split()
            print "Area = " + test_line[8][:-4]
            outputfile.write(test_line[8]+" ")
        elif i == area_eff_line:
            test_line = line.split()
            print "Area Efficiency = " + test_line[4][:-1]
            outputfile.write(test_line[4]+" ")
        elif i == read_lat:
            test_line = line.split()
            print "Read Latency = " + test_line[4][:-2]
            outputfile.write(test_line[4]+" ")
        elif i == write_lat:
            test_line = line.split()
            print "Write Latency = " + test_line[4][:-2]
            outputfile.write(test_line[4]+" ")
        elif i == read_dyn:
            test_line = line.split()
            print "Read Dynamic Energy = " + test_line[5][:-2]
            outputfile.write(test_line[5]+" ")
        elif i == write_dyn:
            test_line = line.split()
            print "Write Dynamic Energy = " + test_line[5][:-2]
            outputfile.write(test_line[5]+" ")
        elif i == leakage:
            test_line = line.split()
            print "Leakage Power = " + test_line[4][:-2]
            outputfile.write(test_line[4]+"\n")
 
        
