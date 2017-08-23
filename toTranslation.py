import glob
import sys
import os
try:
    path=sys.argv[1]
    files = glob.glob(path+"*")
    os.makedirs(path+"result/")
    for fle in files:
        origin=open(fle,'r');
        formated=open("formated.txt",'w+');
        result=open(path+"result/"+os.path.basename(fle[:-4])+"_result.txt",'w+');
        for line in origin:
            if line.find("name:") != -1:
                formated.write(line[:line.find("name:")]+'\n')
                formated.write(line[line.find("name:"):])
            elif line.find("::[html]") != -1:
                formated.write(line[:line.find("::[html]")]+'\n')
                formated.write(line[line.find("::[html]"):len(line)-2]+'\n')
                formated.write("{"+'\n')
            elif line.find("::") != -1:
                index=line.find("::",line.find("::")+1)
                formated.write(line[:index]+'\n')
                formated.write(line[index:len(line)-2]+'\n')
                formated.write("{"+'\n')
            else:
                formated.write(line)
        formated.close()
        formatedRead=open("formated.txt",'r');
        for line in formatedRead:
            if line.find("// question:") != -1:
                result.write("QQQ"+line[12:len(line)])
            elif line.find("name:") != -1:
                result.write("SSS"+line[5:len(line)])
            elif line.find("::[html]") != -1:
                result.write("RRR "+line[8:len(line)])
            elif line.find("::") != -1:
                result.write("RRR "+line[2:len(line)])
            elif line.find("{") != -1:
                result.write("*---"+'\n')
            elif line.find("~[moodle]") != -1:
                result.write("CCC "+line[10:len(line)])
            elif line.find("~%50%[moodle]") != -1:
                result.write("CCC50 "+line[14:len(line)])
            elif line.find("=[moodle]") != -1:
                result.write("TTT "+line[10:len(line)])
            elif line.find("~") != -1:
                result.write("CCCM "+line[2:len(line)])
            elif line.find("=") != -1:
                result.write("TTTM "+line[2:len(line)])
            elif line.find("}") != -1:
                result.write("---*"+line[1:len(line)])
            else:
                result.write(line)
        result.close()
        os.remove("formated.txt")
except:
    print "Argument missing: Please add the location of the directory with the files"
