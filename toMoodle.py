import glob
import sys
import os
try:
    path=sys.argv[1]
    files = glob.glob(path+"*")
    os.makedirs(path+"moodle/")
    for fle in files:
        origin=open(fle,'r');
        result=open(path+"moodle/"+os.path.basename(fle[:-4])+"_moodle.txt",'w+');
        for line in origin:
            if line.find("QQQ") != -1:
                result.write("// question:"+line[3:len(line)])
            elif line.find("SSS") != -1:
                result.write("name:"+line[3:len(line)])
            elif line.find("RRR ") != -1:
                result.write("::"+line[4:len(line)])
            elif line.find("RRR ") != -1:
                result.write("::"+line[4:len(line)])
            elif line.find("*---") != -1:
                result.write("{"+'\n')
            elif line.find("CCC ") != -1:
                result.write('\t'+"~[moodle]"+line[4:len(line)])
            elif line.find("CCC50 ") != -1:
                result.write('\t'+"~%50%[moodle]"+line[6:len(line)])
            elif line.find("TTT ") != -1:
                result.write('\t'+"=[moodle]"+line[4:len(line)])
            elif line.find("CCCM ") != -1:
                result.write('\t'+"~"+line[5:len(line)])
            elif line.find("TTTM ") != -1:
                result.write('\t'+"="+line[5:len(line)])
            elif line.find("---*") != -1:
                result.write("}"+'\n')
            else:
                result.write(line)
        result.close()
except:
    print "Argument missing: Please add the location of the directory with the files"
