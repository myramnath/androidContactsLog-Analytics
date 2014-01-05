import android, os, csv, itertools, datetime

fileName = datetime.date.today().strftime("%I-%M%p %B %d %Y")
fileName = str(datetime.datetime.now())
print(fileName)

droid = android.Android()

HeaderFields = ["Name", "PhoneNum", "Duration", "type"] 
#outfile = open("./contact"+ fileName +".txt","w")
#outfile = open("./contact.txt","w")
outfile = open("/storage/sdcard0/sl4a/scripts/myscripts/crons/output/contact"+ fileName +".txt","w")

myconst = droid.getConstants("android.provider.CallLog$Calls").result 
calls=droid.queryContent(myconst["CONTENT_URI"],["name","number","duration","date","type"]).result 
for call in calls: 
    #print call
    outfile.write(str(call) + os.linesep)

outfile.close()
print("done")
