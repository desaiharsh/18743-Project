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
    area_line = 144
    area_eff_line = 147
    read_lat = 149
    write_lat = 160
    read_dyn = 170
    write_dyn = 180
    leakage = 188
elif memtype == "MRAM" or memtype == "SOT":
    area_line = 155
    area_eff_line = 158
    read_lat = 160
    write_lat = 171
    read_dyn = 183
    write_dyn = 193
    leakage = 202


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
 
        
