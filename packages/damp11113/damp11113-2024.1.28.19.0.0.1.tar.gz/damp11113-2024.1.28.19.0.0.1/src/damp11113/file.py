"""
damp11113-library - A Utils library and Easy to use. For more info visit https://github.com/damp11113/damp11113-library/wiki
Copyright (C) 2021-2023 damp11113 (MIT)

Visit https://github.com/damp11113/damp11113-library

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import shutil
import zipfile
import json
import natsort
import psutil
import configparser

#-----------------------------read---------------------------------------

def readfile(file, decode='utf-8'):
    with open(file, 'r', encoding=decode) as f:
        return f.read()

def readfileline(file, line):
    with open(file, 'r') as f:
        return f.readlines()[line]

def readjson(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def readini(filename, section_name, parameter_name):
    config = configparser.ConfigParser()
    config.read(filename)

    if section_name in config and parameter_name in config[section_name]:
        return config[section_name][parameter_name]
    else:
        print(f"Section '{section_name}' or parameter '{parameter_name}' not found in the INI file.")
        return None

#-----------------------------move---------------------------------------

def movefile(file, to):
    shutil.move(file, to)

def movefolder(folder, to):
    shutil.move(folder, to)

#-----------------------------copy---------------------------------------

def copyfile(file, to):
    shutil.copy(file, to)

def copyfolder(folder, to):
    shutil.copytree(folder, to)

#-----------------------------remove--------------------------------------

def removefile(file):
    os.remove(file)

def removefolder(folder):
    shutil.rmtree(folder)

#-----------------------------renamefile-----------------------------------

def renamefile(file, to):
    os.rename(file, to)

def renamefolder(folder, to):
    os.rename(folder, to)

#----------------------------------create-----------------------------------

def createfolder(folder):
    os.mkdir(folder)

def createfile(file):
    open(file, 'a').close()

#----------------------------------write------------------------------------

def writefile(file, data):
    with open(file, 'a') as f:
        f.write(data + '\n')
        f.close()

def writefile2(file, data, encode="utf-8"):
    with open(file, 'w', encoding=encode) as f:
        f.write(data)
        f.close()

def writefile3(file, data):
    with open(file, 'a') as f:
        f.write(data)
        f.close()

def writefileline(file, line, data):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines[line] = data
        with open(file, 'w') as f:
            f.writelines(lines)

def writejson(file, data):
    with open(f'{file}.json', 'w') as f:
        json.dump(data, f)


#----------------------------------append-----------------------------------

def appendfile(file, data):
    with open(file, 'a') as f:
        f.write(data)

def appendfileline(file, line, data):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines[line] = data
        with open(file, 'a') as f:
            f.writelines(lines)

#---------------------------------------open---------------------------------

def openfile(ide, file):
    os.system(f"{ide} {file}")

#---------------------------------------run---------------------------------

def runfile(file):
    os.system(f"start {file}")

def runpy(file):
    os.system(f"python {file}")

def runjs(file):
    os.system(f"node {file}")

def runjava(file):
    os.system(f"java {file}")

def runbash(file):
    os.system(f"bash {file}")

def runcpp(file):
    os.system(f"g++ {file}")

def runc(file):
    os.system(f"gcc {file}")

def runphp(file):
    os.system(f"php {file}")

def runruby(file):
    os.system(f"ruby {file}")

def rungo(file):
    os.system(f"go {file}")

def runperl(file):
    os.system(f"perl {file}")

def rundocker(file):
    os.system(f"docker {file}")

def runvim(file):
    os.system(f"vim {file}")

def runnano(file):
    os.system(f"nano {file}")

def rungedit(file):
    os.system(f"gedit {file}")

def runkate(file):
    os.system(f"kate {file}")

#--------------------------------------kill---------------------------------

def kill(file):
    os.system(f"taskkill /f /im {file}")

#--------------------------------------zip----------------------------------

def unzip(file, to):
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(to)

def comzip(file, to):
    with zipfile.ZipFile(file, 'w') as zip_ref:
        zip_ref.write(to)

#----------------------------------size------------------------------------

def sizefile(file):
    size = 0

    for path, dirs, files in os.walk(file):
        for f in files:
            size += os.path.getsize(os.path.join(path, f))

    return size / 1000000

def sizefolder(folder):
    size = 0

    for path, dirs, files in os.walk(folder):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

    return size / 1000000

def sizefolder2(folder):
    size = psutil.disk_usage(folder).used
    return size / 1000000

def sizefolder3(folder):
    size = 0

    for path, dirs, files in os.walk(folder):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)

    return size

#----------------------------------all-------------------------------------

def allfiles(folder):
    return os.listdir(folder)

#----------------------------------count-------------------------------------

def countline(file, decode='utf-8'):
    with open(file, 'r', encoding=decode) as f:
        line = sum(1 for _ in f)
    return line

#-------------------------------sort_files-------------------------

def sort_files(file_list ,reverse=False):
    flist = []
    for file in file_list:
        flist.append(file)
    return natsort.natsorted(flist, reverse=reverse)
