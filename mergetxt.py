import os

workpath = "/Users/gehui/work/gitproject/python/content/";
copypath = "/Users/gehui/work/gitproject/python/all.TXT";

fopen = open(copypath, 'w')

pathDir =  os.listdir(workpath)
for cdfile in pathDir:
    child = os.path.join('%s%s' % (workpath, cdfile));
    fopen.write('%s%s' % (cdfile, os.linesep));
    cdfileopen = open(child, 'r')
    for eachLine in cdfileopen:
        fopen.write('%s' % (eachLine));
    cdfileopen.close();
    fopen.write('%s%s%s%s' % (os.linesep, os.linesep, os.linesep, os.linesep));

fopen.close();
