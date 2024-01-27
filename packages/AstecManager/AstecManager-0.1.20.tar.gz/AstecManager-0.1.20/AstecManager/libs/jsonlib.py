import json
import os
import re
from os.path import isdir, join, isfile,getctime
from datetime import datetime,date
from colorama import Fore,Style
metadata_file = "metadata.json"
logFolderName = "LOGS"
def printColor(color,text):
    print(color + str(text))
    print(Style.RESET_ALL)
def printRed(text):
    printColor(Fore.RED,str(text))
def printYellow(text):
    printColor(Fore.YELLOW,str(text))
def printMagenta(text):
    printColor(Fore.MAGENTA, str(text))
def printCyan(text):
    printColor(Fore.CYAN, str(text))
def printGreen(text):
    printColor(Fore.GREEN,str(text))

def printParameters(jsonParams):
    print("Parameters : " + "\n")
    params = str(jsonParams)
    params = params.replace("'","").replace('"','').replace("{","").replace("}","")
    paramslines = params.split(",")
    for line in paramslines:
        print(line.strip()+"\n")
def printCurrentStep(jsonDict):
    step = jsonDict["step"]
    warnings = []
    outputstr = ""
    print("----------------------------")
    print("\n")
    if "embryo_name" in jsonDict:
        outputstr += "Embryo " + str(jsonDict["embryo_name"])
    else :
        warnings.append("Embryo name not found in metadata")
    if step == "fusion":
        outputstr += " was fused"
        if "EXP_FUSE" in jsonDict:
            outputstr += " in folder FUSE_"+jsonDict["EXP_FUSE"]
        else :
            warnings.append("EXP_FUSE not found !")
        if "user" in jsonDict:
            outputstr += " by user "+str(jsonDict["user"])
        else :
            warnings.append("user not found !")
        if "begin" in jsonDict:
            outputstr += " from time "+str(jsonDict["begin"])
        else :
            warnings.append("begin time of fusion not found !")
        if "end" in jsonDict:
            outputstr += " to time "+str(jsonDict["end"])
        else :
            warnings.append("end time of fusion not found !")
        if "date" in jsonDict:
            outputstr += " the "+str(jsonDict["date"])
        else :
            warnings.append("processing date of fusion not found !")
        if "omero_config_file" in jsonDict:
            if jsonDict["omero_config_file"] is not None:
                outputstr += " and has been upload on OMERO "
        else:
            warnings.append("No information on OMERO upload ")
        outputstr += "\n"
        print(outputstr)
        printParameters(jsonDict)
    elif step == "intraregistration":
        outputstr += " intraregistration was done"
        if "EXP_INTRAREG" in jsonDict:
            outputstr += " in folder INTRAREG_"+str(jsonDict["EXP_INTRAREG"])
        else :
            warnings.append("EXP_INTRAREG not found !")
        if "EXP_FUSE" in jsonDict:
            outputstr += " on fusion FUSE_"+str(jsonDict["EXP_FUSE"])
        if "EXP_SEG" in jsonDict:
            outputstr += " on segmentation SEG_"+str(jsonDict["EXP_SEG"])
        if "EXP_POST" in jsonDict:
            outputstr += " on postcorrection POST_"+str(jsonDict["EXP_POST"])
        if "user" in jsonDict:
            outputstr += " by user "+str(jsonDict["user"])
        else :
            warnings.append("user not found !")
        if "begin" in jsonDict:
            outputstr += " from time "+str(jsonDict["begin"])
        else :
            warnings.append("begin time of intrareg not found !")
        if "end" in jsonDict:
            outputstr += " to time "+str(jsonDict["end"])
        else :
            warnings.append("end time of intrareg not found !")
        if "date" in jsonDict:
            outputstr += " the "+str(jsonDict["date"])
        else :
            warnings.append("processing date of intrareg not found !")
        if "omero_config_file" in jsonDict:
            if jsonDict["omero_config_file"] is not None:
                outputstr += " and has been upload on OMERO "
        else:
            warnings.append("No information on OMERO upload ")
        outputstr += "\n"
        print(outputstr)
        print("\n")
    elif step == "intrareg_movie":
        outputstr += " intraregistration movie was done"
        if "EXP_INTRAREG" in jsonDict:
            outputstr += " in folder INTRAREG_" + str(jsonDict["EXP_INTRAREG"])
        else:
            warnings.append("EXP_INTRAREG not found !")
        if "EXP_FUSE" in jsonDict:
            outputstr += " on fusion FUSE_" + str(jsonDict["EXP_FUSE"])
        else:
            warnings.append("EXP_FUSE not found !")
        if "user" in jsonDict:
            outputstr += " by user " + str(jsonDict["user"])
        else:
            warnings.append("user not found !")
        if "begin" in jsonDict:
            outputstr += " from time " + str(jsonDict["begin"])
        else:
            warnings.append("begin time of intrareg not found !")
        if "end" in jsonDict:
            outputstr += " to time " + str(jsonDict["end"])
        else:
            warnings.append("end time of intrareg not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of intrareg not found !")
        if "omero_config_file" in jsonDict:
            if jsonDict["omero_config_file"] is not None:
                outputstr += " and has been upload on OMERO "
        else:
            warnings.append("No information on OMERO upload ")
        outputstr += "\n"
        print(outputstr)
        print("\n")
    elif step == "rawdata_intensities_plot":
        #print("Embryo "+str(jsonDict["embryo_name"])+" raw data intensities plot was done by user "+str(jsonDict["user"])+" from time "+str(jsonDict["begin"])+" to time "+str(jsonDict["end"])+" the "+str(jsonDict["date"])+"\n")
        outputstr += " raw data intensities computed"
        if "user" in jsonDict:
            outputstr += " by user " + str(jsonDict["user"])
        else:
            warnings.append("user not found !")
        if "begin" in jsonDict:
            outputstr += " from time " + str(jsonDict["begin"])
        else:
            warnings.append("begin time of intrareg not found !")
        if "end" in jsonDict:
            outputstr += " to time " + str(jsonDict["end"])
        else:
            warnings.append("end time of intrareg not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of intrareg not found !")
        outputstr += "\n"
        print(outputstr)
        print("\n")
    elif step == "compute_contour":
        outputstr += " intraregistration movie was done"
        if "contour_folder" in jsonDict:
            outputstr += " in folder CONTOUR_" + str(jsonDict["contour_folder"])
        else:
            warnings.append("contour_folder not found !")
        if "EXP_BACKGROUND" in jsonDict:
            outputstr += " on background BACKGROUND_" + str(jsonDict["EXP_BACKGROUND"])
        else:
            warnings.append("EXP_BACKGROUND not found !")
        if "user" in jsonDict:
            outputstr += " by user " + str(jsonDict["user"])
        else:
            warnings.append("user not found !")
        if "resolution" in jsonDict:
            outputstr += " with resolution " + str(jsonDict["resolution"])
        else:
            warnings.append("resolution not found !")
        if "normalisation" in jsonDict:
            outputstr += " with normalisation " + str(jsonDict["normalisation"])
        else:
            warnings.append("normalisation not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of intrareg not found !")
        outputstr += "\n"
        print(outputstr)
        print("\n")
    elif step == "mars":
        outputstr += " first time point was computed"
        if "EXP_SEG" in jsonDict:
            outputstr += " in folder SEG_" + jsonDict["EXP_SEG"]
        else:
            warnings.append("EXP_SEG not found !")
        if "EXP_FUSE" in jsonDict:
            outputstr += " using fusion FUSE_" + jsonDict["EXP_FUSE"]
        else:
            warnings.append("EXP_FUSE not found !")
        if "user" in jsonDict:
            outputstr += " by user " + str(jsonDict["user"])
        else:
            warnings.append("user not found !")
        if "begin" in jsonDict:
            outputstr += " on time " + str(jsonDict["begin"])
        else:
            warnings.append("mars time point not found !")
        if "resolution" in jsonDict:
            outputstr += " with resolution " + str(jsonDict["resolution"])
        else:
            warnings.append("resolution not found !")
        if "normalisation" in jsonDict:
            outputstr += " with normalisation " + str(jsonDict["normalisation"])
        else:
            warnings.append("normalisation not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of mars not found !")
        if "use_contour" in jsonDict:
            if jsonDict["use_contour"] is not None and jsonDict["use_contour"]:
                outputstr += " using contour "
        else:
            warnings.append("No information on contour used ")
        if "EXP_CONTOUR" in jsonDict:
            outputstr += " with contour from folder CONTOUR_"+str(jsonDict["EXP_CONTOUR"])
        else:
            warnings.append("No information on contour folder used ")
        if "omero_config_file" in jsonDict:
            if jsonDict["uploaded_on_omero"] is not None and jsonDict["uploaded_on_omero"]:
                outputstr += " and has been upload on OMERO "
        else:
            warnings.append("No information on OMERO upload ")
        outputstr += "\n"
        print(outputstr)
        printParameters(jsonDict)
    elif step == "segmentation":
        outputstr += " segmentation was computed"
        if "EXP_SEG" in jsonDict:
            outputstr += " in folder SEG_" + jsonDict["EXP_SEG"]
        else:
            warnings.append("EXP_SEG not found !")
        if "EXP_FUSE" in jsonDict:
            outputstr += " using fusion FUSE_" + jsonDict["EXP_FUSE"]
        else:
            warnings.append("EXP_FUSE not found !")
        if "user" in jsonDict:
            outputstr += " by user " + str(jsonDict["user"])
        else:
            warnings.append("user not found !")
        if "mars_path" in jsonDict:
            outputstr += " using mars " + str(jsonDict["mars_path"])
        else:
            warnings.append("mars_path not found !")
        if "begin" in jsonDict:
            outputstr += " from time " + str(jsonDict["begin"])
        else:
            warnings.append("segmentation first time point not found !")
        if "end" in jsonDict:
            outputstr += " to time " + str(jsonDict["end"])
        else:
            warnings.append("segmentation end point not found !")
        if "resolution" in jsonDict:
            outputstr += " with resolution " + str(jsonDict["resolution"])
        else:
            warnings.append("resolution not found !")
        if "normalisation" in jsonDict:
            outputstr += " with normalisation " + str(jsonDict["normalisation"])
        else:
            warnings.append("normalisation not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of segmentation not found !")
        if "use_contour" in jsonDict:
            if jsonDict["use_contour"] is not None and jsonDict["use_contour"]:
                outputstr += " using contour "
        else:
            warnings.append("No information on contour used ")
        if "EXP_CONTOUR" in jsonDict:
            outputstr += " with contour from folder CONTOUR_"+str(jsonDict["EXP_CONTOUR"])
        else:
            warnings.append("No information on contour folder used ")
        if "omero_config_file" in jsonDict:
            if jsonDict["uploaded_on_omero"] is not None and jsonDict["uploaded_on_omero"]:
                outputstr += " and has been upload on OMERO "
        else:
            warnings.append("No information on OMERO upload ")
        outputstr += "\n"
        print(outputstr)
        printParameters(jsonDict)
    elif step == "segmentation_test":
        outputstr += " segmentation test was computed"
        if "EXP_SEG" in jsonDict:
            outputstr += " in folder SEG_" + jsonDict["EXP_SEG"]
        else:
            warnings.append("EXP_SEG not found !")
        if "EXP_FUSE" in jsonDict:
            outputstr += " using fusion FUSE_" + jsonDict["EXP_FUSE"]
        else:
            warnings.append("EXP_FUSE not found !")
        if "user" in jsonDict:
            outputstr += " by user " + str(jsonDict["user"])
        else:
            warnings.append("user not found !")
        if "mars_path" in jsonDict:
            outputstr += " using mars " + str(jsonDict["mars_path"])
        else:
            warnings.append("mars_path not found !")
        if "begin" in jsonDict:
            outputstr += " from time " + str(jsonDict["begin"])
        else:
            warnings.append("segmentation first time point not found !")
        if "end" in jsonDict:
            outputstr += " to time " + str(jsonDict["end"])
        else:
            warnings.append("segmentation end point not found !")
        if "resolution" in jsonDict:
            outputstr += " with resolution " + str(jsonDict["resolution"])
        else:
            warnings.append("resolution not found !")
        if "normalisation" in jsonDict:
            outputstr += " with normalisation " + str(jsonDict["normalisation"])
        else:
            warnings.append("normalisation not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of segmentation not found !")
        if "use_contour" in jsonDict:
            if jsonDict["use_contour"] is not None and jsonDict["use_contour"]:
                outputstr += " using contour "
        else:
            warnings.append("No information on contour used ")
        if "EXP_CONTOUR" in jsonDict:
            outputstr += " with contour from folder CONTOUR_" + str(jsonDict["EXP_CONTOUR"])
        else:
            warnings.append("No information on contour folder used ")
        if "omero_config_file" in jsonDict:
            if jsonDict["uploaded_on_omero"] is not None and jsonDict["uploaded_on_omero"]:
                outputstr += " and has been upload on OMERO "
        else:
            warnings.append("No information on OMERO upload ")
        outputstr += "\n"
        print(outputstr)
        printParameters(jsonDict)
    elif step == "post_correction":
        outputstr += " post correction was computed"
        if "EXP_POST" in jsonDict:
            outputstr += " in folder POST_" + jsonDict["EXP_POST"]
        else:
            warnings.append("EXP_POST not found !")
        if "EXP_SEG" in jsonDict:
            outputstr += " using segmentation SEG_" + jsonDict["EXP_SEG"]
        else:
            warnings.append("EXP_SEG not found !")
        if "user" in jsonDict:
            outputstr += " by user " + str(jsonDict["user"])
        else:
            warnings.append("user not found !")
        if "begin" in jsonDict:
            outputstr += " from time " + str(jsonDict["begin"])
        else:
            warnings.append("post correction first time point not found !")
        if "end" in jsonDict:
            outputstr += " to time " + str(jsonDict["end"])
        else:
            warnings.append("post correction end point not found !")
        if "resolution" in jsonDict:
            outputstr += " with resolution " + str(jsonDict["resolution"])
        else:
            warnings.append("resolution not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of post correction not found !")
        if "omero_config_file" in jsonDict:
            if jsonDict["uploaded_on_omero"] is not None and jsonDict["uploaded_on_omero"]:
                outputstr += " and has been upload on OMERO "
        else:
            warnings.append("No information on OMERO upload ")
        outputstr += "\n"
        #printYellow("Embryo "+str(jsonDict["embryo_name"])+" post correction generated in folder POST_"+str(jsonDict["EXP_POST"])+" from SEG_"+str(jsonDict["EXP_SEG"])+" by user "+str(jsonDict["user"])+" from time "+str(jsonDict["begin"])+"to time "+str(jsonDict["end"])+" the "+str(jsonDict["date"])+" in resolution "+str(jsonDict["resolution"])+(" uploaded on OMERO " if jsonDict["uploaded_on_omero"] else "")+"\n")
        print(outputstr)
        printParameters(jsonDict)
    elif step == "post_correction_test":
        outputstr += " post correction test was computed"
        if "EXP_POST" in jsonDict:
            outputstr += " in folder POST_" + jsonDict["EXP_POST"]
        else:
            warnings.append("EXP_POST not found !")
        if "EXP_SEG" in jsonDict:
            outputstr += " using segmentation SEG_" + jsonDict["EXP_SEG"]
        else:
            warnings.append("EXP_SEG not found !")
        if "user" in jsonDict:
            outputstr += " by user " + str(jsonDict["user"])
        else:
            warnings.append("user not found !")
        if "begin" in jsonDict:
            outputstr += " from time " + str(jsonDict["begin"])
        else:
            warnings.append("post correction first time point not found !")
        if "end" in jsonDict:
            outputstr += " to time " + str(jsonDict["end"])
        else:
            warnings.append("post correction end point not found !")
        if "resolution" in jsonDict:
            outputstr += " with resolution " + str(jsonDict["resolution"])
        else:
            warnings.append("resolution not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of postcorrection not found !")
        if "omero_config_file" in jsonDict:
            if jsonDict["uploaded_on_omero"] is not None and jsonDict["uploaded_on_omero"]:
                outputstr += " and has been upload on OMERO "
        else:
            warnings.append("No information on OMERO upload ")
        outputstr += "\n"
        # printYellow("Embryo "+str(jsonDict["embryo_name"])+" post correction generated in folder POST_"+str(jsonDict["EXP_POST"])+" from SEG_"+str(jsonDict["EXP_SEG"])+" by user "+str(jsonDict["user"])+" from time "+str(jsonDict["begin"])+"to time "+str(jsonDict["end"])+" the "+str(jsonDict["date"])+" in resolution "+str(jsonDict["resolution"])+(" uploaded on OMERO " if jsonDict["uploaded_on_omero"] else "")+"\n")
        print(outputstr)
        printParameters(jsonDict)
    elif step == "embryo_properties":
        outputstr += " properties computed"
        if "EXP_INTRAREG" in jsonDict:
            outputstr += " on intraregistration INTRAREG_" + jsonDict["EXP_INTRAREG"]
        else:
            warnings.append("EXP_INTRAREG not found !")
        if "EXP_POST" in jsonDict:
            outputstr += " on postcorection POST_" + jsonDict["EXP_POST"]
        else:
            warnings.append("EXP_POST not found !")
        if "user" in jsonDict:
            outputstr += " by user " + str(jsonDict["user"])
        else:
            warnings.append("user not found !")
        if "begin" in jsonDict:
            outputstr += " from time " + str(jsonDict["begin"])
        else:
            warnings.append("properties first time point not found !")
        if "end" in jsonDict:
            outputstr += " to time " + str(jsonDict["end"])
        else:
            warnings.append("properties end point not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of properties not found !")
        outputstr += "\n"
        #printCyan("Embryo "+str(jsonDict["embryo_name"])+" properties generated on folder INTRAREG_"+str(jsonDict["EXP_INTRAREG"])+"  by user "+str(jsonDict["user"])+" from time "+str(jsonDict["begin"])+"to time "+str(jsonDict["end"])+" the "+str(jsonDict["date"])+"\n")
        print(outputstr)
        printParameters(jsonDict)
    elif step == "upload_on_omero":
        outputstr += " upload of folder done "
        if "input_folder" in jsonDict:
            outputstr += " on folder " + jsonDict["input_folder"]
        else:
            warnings.append("input_folder not found !")
        if "user" in jsonDict:
            outputstr += " by user " + str(jsonDict["user"])
        else:
            warnings.append("user not found !")
        if "omero_project" in jsonDict:
            outputstr += " in omero project " + str(jsonDict["omero_project"])
        else:
            warnings.append("omero project not found !")
        if "omero_dataset" in jsonDict:
            outputstr += " in omero dataset " + str(jsonDict["omero_dataset"])
        else:
            warnings.append("omero dataset not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of uppload not found !")
        outputstr += "\n"
        print(outputstr)
        print("\n")
    elif step == "name_embryo":
        outputstr += " automatic naming computed"
        if "EXP_INTRAREG" in jsonDict:
            outputstr += " on intraregistration INTRAREG_" + jsonDict["EXP_INTRAREG"]
        else:
            warnings.append("EXP_INTRAREG not found !")
        if "EXP_POST" in jsonDict:
            outputstr += " on postcorection POST_" + jsonDict["EXP_POST"]
        else:
            warnings.append("EXP_POST not found !")
        if "user" in jsonDict:
            outputstr += " by user " + str(jsonDict["user"])
        else:
            warnings.append("user not found !")
        if "begin" in jsonDict:
            outputstr += " from time " + str(jsonDict["begin"])
        else:
            warnings.append("naming first time point not found !")
        if "end" in jsonDict:
            outputstr += " to time " + str(jsonDict["end"])
        else:
            warnings.append("naming end point not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of naming not found !")
        outputstr += "\n"
        #printCyan("Embryo "+str(jsonDict["embryo_name"])+" named automatically on folder INTRAREG_"+str(jsonDict["EXP_INTRAREG"])+"and post POST_"+str(jsonDict["EXP_POST"])+" by user "+str(jsonDict["user"])+" the "+str(jsonDict["date"])+"\n")
        print(outputstr)
        printParameters(jsonDict)
    elif step == "copy_rawdata":
        outputstr += " RAW DATA copied"
        if "input_folder" in jsonDict:
            outputstr += " from folder" + jsonDict["input_folder"]
        else:
            warnings.append("input_folder not found !")
        outputstr += "\n"
        # printCyan("Embryo "+str(jsonDict["embryo_name"])+" named automatically on folder INTRAREG_"+str(jsonDict["EXP_INTRAREG"])+"and post POST_"+str(jsonDict["EXP_POST"])+" by user "+str(jsonDict["user"])+" the "+str(jsonDict["date"])+"\n")
        print(outputstr)
        #print("Embryo "+str(jsonDict["embryo_name"])+" RAWDATA were copied from folder "+str(jsonDict["input_folder"])+"\n")
        print("\n")
    elif step == "background":
        outputstr += " Backgrounds generated"
        if "EXP_FUSE" in jsonDict:
            outputstr += " on fusion" + jsonDict["EXP_FUSE"]
        else:
            warnings.append("EXP_FUSE not found !")
        if "begin" in jsonDict:
            outputstr += " from time " + str(jsonDict["begin"])
        else:
            warnings.append("background first time point not found !")
        if "end" in jsonDict:
            outputstr += " to time " + str(jsonDict["end"])
        else:
            warnings.append("background end point not found !")
        if "date" in jsonDict:
            outputstr += " the " + str(jsonDict["date"])
        else:
            warnings.append("processing date of background not found !")
        outputstr += "\n"
        # printCyan("Embryo "+str(jsonDict["embryo_name"])+" named automatically on folder INTRAREG_"+str(jsonDict["EXP_INTRAREG"])+"and post POST_"+str(jsonDict["EXP_POST"])+" by user "+str(jsonDict["user"])+" the "+str(jsonDict["date"])+"\n")
        print(outputstr)
        #print("Embryo "+str(jsonDict["embryo_name"])+" RAWDATA were copied from folder "+str(jsonDict["input_folder"])+"\n")
        print("\n")
    elif step == "downscale_mars":
        outputstr += " First time point downscaled "
        if "mars_file" in jsonDict:
            outputstr += " from source" + jsonDict["mars_file"]
        else:
            warnings.append("source not found !")
        if "output_folder" in jsonDict:
            outputstr += " to folder" + jsonDict["output_folder"]
        else:
            warnings.append("output_folder not found !")
        if "template_file" in jsonDict:
            outputstr += " using template" + jsonDict["template_file"]
        else:
            warnings.append("template_file not found !")
        if "resolution" in jsonDict:
            outputstr += " to resolution" + jsonDict["resolution"]
        else:
            warnings.append("resolution not found !")
        outputstr += "\n"
        # printCyan("Embryo "+str(jsonDict["embryo_name"])+" named automatically on folder INTRAREG_"+str(jsonDict["EXP_INTRAREG"])+"and post POST_"+str(jsonDict["EXP_POST"])+" by user "+str(jsonDict["user"])+" the "+str(jsonDict["date"])+"\n")
        print(outputstr)
        #print("Embryo "+str(jsonDict["embryo_name"])+" MARS was donscaled from source "+str(jsonDict["mars_file"])+" to folder "+str(jsonDict["output_folder"])+" using template "+str(jsonDict["template_file"])+" to resolution "+str(jsonDict["resolution"])+"\n")
        print("\n")
    else:
        printRed("Step "+str(step)+" not recognized")
    if len(warnings) > 0:

        printRed("         Warnings           ")
        for warn in warnings:
            printRed("- "+warn+"\n")

def printMetadata(embryoPath):
    jsonData = loadMetaData(embryoPath)
    if jsonData is None:
        print("No metadata was found for the embryo")
        return
    sortedByDateTEMP = sorted(jsonData, key=lambda x: x["date"])
    sortedByDate = list(sortedByDateTEMP)
    for itemJson in sortedByDate:
        printCurrentStep(itemJson)
        print("\n")

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def isFileImage(fileName):
    return fileName is not None and (fileName.endswith(".mha") or fileName.endswith(".mha.gz") or fileName.endswith(".nii") or fileName.endswith(".nii.gz") or fileName.endswith(".inr") or fileName.endswith(".inr.gz") or fileName.endswith(".tif") or fileName.endswith(".tif.gz") or fileName.endswith(".tiff") or fileName.endswith(".tiff.gz"))

def parseDateFromLogPath(log_path):
    match = re.search(r'\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}', log_path)
    if match is not None:
        found_date = datetime.strptime(match.group(), '%Y-%m-%d-%H-%M-%S').date()
        return found_date.strftime("%d/%m/%Y %H:%M:%S")
    else:
        match = re.search(r'\d{4}-\d{2}-\d{2}-\d{2}:\d{2}:\d{2}', log_path)
        if match is not None:
            found_date = datetime.strptime(match.group(), '%Y-%m-%d-%H-%M-%S').date()
            return found_date.strftime("%d/%m/%Y %H:%M:%S")
        else:
            found_date = date.fromtimestamp(getctime(log_path))
            return found_date.strftime("%d/%m/%Y %H:%M:%S")


def loadJsonForContour(postPath, postFolderName):# CODE DUPLICATE TODO LATER

    jsonObjects = []
    fuseEXP = postFolderName.replace("CONTOUR_", "")
    # read with image and name
    jsonObject = {}
    jsonObject["step"] = "compute_contour"
    files = [f for f in os.listdir(postPath) if os.path.isfile(join(postPath, f)) and isFileImage(f)]
    begin = 1000000
    end = -1000000
    embryoName = ""
    fuseDate = None
    firstTimeFile = None
    for file in files:
        if embryoName == "":
            embryoName = file.split("_contour_")[0]
        fileTimeSplit = file.split("_t")
        if len(fileTimeSplit) > 0:
            time = int(fileTimeSplit[1].split(".")[0])
            if time > end:
                end = time
            if time < begin:
                firstTimeFile=join(postPath, file)
                begin = time
    if firstTimeFile is not None:
        fuseDate = date.fromtimestamp(getctime(firstTimeFile)).strftime("%d/%m/%Y %H:%M:%S")
        jsonObject["date"] = fuseDate
    jsonObject["begin"] = begin
    jsonObject["end"] = end
    jsonObject["embryo_name"] = embryoName
    try :
        floatval = float("0."+fuseEXP.split("_")[-1])
        jsonObject["resolution"] = floatval
    except:
        print("No resolution found")
    jsonObject["EXP_CONTOUR"] = fuseEXP
    jsonObjects.append(jsonObject)
    return jsonObjects
def loadJsonForBackground(postPath, postFolderName):# CODE DUPLICATE TODO LATER
    from datetime import date
    jsonObjects = []
    fuseEXP = postFolderName.replace("BACKGROUND_", "").replace("Background_","")
    # read with image and name
    jsonObject = {}
    jsonObject["step"] = "background"
    files = [f for f in os.listdir(postPath) if os.path.isfile(join(postPath, f)) and isFileImage(f)]
    begin = 1000000
    end = -1000000
    embryoName = ""
    fuseDate = None
    firstTimeFile = None
    for file in files:
        if embryoName == "":
            embryoName = file.split("_background_")[0]
        fileTimeSplit = file.split("_t")
        if len(fileTimeSplit) > 0:
            time = int(fileTimeSplit[1].split(".")[0])
            if time > end:
                end = time
            if time < begin:
                firstTimeFile=join(postPath, file)
                begin = time
    if firstTimeFile is not None:
        fuseDate = date.fromtimestamp(getctime(firstTimeFile)).strftime("%d/%m/%Y %H:%M:%S")
        jsonObject["date"] = fuseDate
    jsonObject["begin"] = begin
    jsonObject["end"] = end
    jsonObject["embryo_name"] = embryoName
    jsonObject["EXP_FUSE"] = fuseEXP
    jsonObjects.append(jsonObject)
    return jsonObjects

def loadJsonForPost(postPath, postFolderName):# CODE DUPLICATE TODO LATER
    from datetime import date
    jsonObjects = []
    readImages = True
    fuseEXP = postFolderName.replace("POST_", "")
    logFolder = join(postPath, logFolderName)
    if isdir(logFolder):
        # read logs
        pyfiles = [join(logFolder,f) for f in os.listdir(logFolder) if os.path.isfile(join(logFolder,f)) and f.endswith(".py")] #all params files
        if len(pyfiles) > 0:
            pyfiles.sort(key=lambda x: getctime(x))
            readImages = False
            for lastParameterFile in pyfiles:
                jsonObject = {}
                jsonObject["step"] = "post_correction"
                jsonObject["date"] = parseDateFromLogPath(lastParameterFile)
                #jsonObject["date"] = date.fromtimestamp(getctime(lastParameterFile)).strftime("%d/%m/%Y %H:%M:%S")
                f = open (lastParameterFile,"r")
                linesfull = f.read()
                lines = linesfull.split("\n")
                f.close()
                for line in lines:
                    shortline = line.strip().replace("\n","").replace(" ","")
                    if not shortline.startswith("#"):
                        print(shortline)
                        keyval = shortline.split("=")
                        if keyval[0] in ["PATH_EMBRYO"] or len(keyval)<2: #We dont want this line
                            continue
                        if keyval[0] == "EN":
                            jsonObject["embryo_name"] = keyval[1]
                        elif keyval[1] == "True" or keyval[1] == "False": # If we find a bool
                            jsonObject[keyval[0]] = bool(keyval[1])
                        elif is_float(keyval[1]): # If we find a float
                            jsonObject[keyval[0]] = float(keyval[1])
                        elif is_integer(keyval[1]): # If we find a float
                            jsonObject[keyval[0]] = int(keyval[1])
                        else : # If its string
                            jsonObject[keyval[0]] = keyval[1].replace("'","").replace('"','')
                if not "EXP_POST" in jsonObject:
                    jsonObject["EXP_POST"] = fuseEXP
                jsonObjects.append(jsonObject)
    if not isdir(logFolder) or readImages:
        # read with image and name
        jsonObject = {}
        jsonObject["step"] = "post_correction"
        files = [f for f in os.listdir(postPath) if os.path.isfile(join(postPath, f)) and isFileImage(f)]
        begin = 1000000
        end = -1000000
        embryoName = ""
        fuseDate = None
        firstTimeFile = None
        for file in files:
            if embryoName == "":
                embryoName = file.split("_post_")[0]
            fileTimeSplit = file.split("_t")
            if len(fileTimeSplit) > 0:
                time = int(fileTimeSplit[1].split(".")[0])
                if time > end:
                    end = time
                if time < begin:
                    firstTimeFile=join(postPath, file)
                    begin = time
        if firstTimeFile is not None:
            fuseDate = date.fromtimestamp(getctime(firstTimeFile)).strftime("%d/%m/%Y %H:%M:%S")
            jsonObject["date"] = fuseDate
        jsonObject["begin"] = begin
        jsonObject["end"] = end
        jsonObject["embryo_name"] = embryoName
        jsonObject["EXP_POST"] = fuseEXP
        jsonObjects.append(jsonObject)
    return jsonObjects

def loadJsonForSeg(segPath, segFolderName): # CODE DUPLICATE TODO LATER
    from datetime import date
    jsonObjects = []
    readImages = True
    fuseEXP = segFolderName.replace("SEG_", "")
    logFolder = join(segPath, logFolderName)
    if isdir(logFolder):
        # read logs
        pyfiles = [join(logFolder,f) for f in os.listdir(logFolder) if os.path.isfile(join(logFolder,f)) and f.endswith(".py")] #all params files
        if len(pyfiles) > 0:
            pyfiles.sort(key=lambda x: getctime(x))
            readImages = False
            for lastParameterFile in pyfiles:
                jsonObject = {}
                jsonObject["step"] = "segmentation"
                jsonObject["date"] = parseDateFromLogPath(lastParameterFile)
                #jsonObject["date"] = date.fromtimestamp(getctime(lastParameterFile)).strftime("%d/%m/%Y %H:%M:%S")
                f = open (lastParameterFile,"r")
                linesfull = f.read()
                lines = linesfull.split("\n")
                f.close()
                for line in lines:
                    shortline = line.strip().replace("\n","").replace(" ","")
                    if not shortline.startswith("#"):
                        keyval = shortline.split("=")
                        if keyval[0] in ["PATH_EMBRYO"] or len(keyval)<2: #We dont want this line
                            continue
                        if keyval[0] == "EN":
                            jsonObject["embryo_name"] = keyval[1]
                        elif keyval[1] == "True" or keyval[1] == "False": # If we find a bool
                            jsonObject[keyval[0]] = bool(keyval[1])
                        elif is_float(keyval[1]): # If we find a float
                            jsonObject[keyval[0]] = float(keyval[1])
                        elif is_integer(keyval[1]): # If we find a float
                            jsonObject[keyval[0]] = int(keyval[1])
                        else : # If its string
                            jsonObject[keyval[0]] = keyval[1].replace("'","").replace('"','')
                if not "EXP_SEG" in jsonObject:
                    jsonObject["EXP_SEG"] = fuseEXP
                jsonObjects.append(jsonObject)
    if not isdir(logFolder) or readImages:
        jsonObject = {}
        jsonObject["step"] = "segmentation"
        # read with image and name
        files = [f for f in os.listdir(segPath) if os.path.isfile(join(segPath, f)) and isFileImage(f)]
        begin = 1000000
        end = -1000000
        embryoName = ""
        fuseDate = None
        firstTimeFile = None
        for file in files:
            if embryoName == "":
                embryoName = file.split("_seg_")[0]
            fileTimeSplit = file.split("_t")
            if len(fileTimeSplit) > 0:
                time = int(fileTimeSplit[1].split(".")[0])
                if time > end:
                    end = time
                if time < begin:
                    firstTimeFile=join(segPath, file)
                    begin = time
        if firstTimeFile is not None:
            fuseDate = date.fromtimestamp(getctime(firstTimeFile)).strftime("%d/%m/%Y %H:%M:%S")
            jsonObject["date"] = fuseDate
        jsonObject["begin"] = begin
        jsonObject["end"] = end
        jsonObject["embryo_name"] = embryoName
        jsonObject["EXP_SEG"] = fuseEXP
        jsonObjects.append(jsonObject)
    return jsonObjects

def loadJsonFromIntraregLogs(fusePath, fuseFolderName):# CODE DUPLICATE TODO LATER
    from datetime import date
    jsonObjects = []
    readImages = True
    fuseEXP = fuseFolderName.replace("INTRAREG_","")
    logFolder = join(fusePath,logFolderName)
    if isdir(logFolder):
        # read logs
        pyfiles = [join(logFolder,f) for f in os.listdir(logFolder) if os.path.isfile(join(logFolder,f)) and f.endswith(".py")] #all params files
        if len(pyfiles) > 0:
            pyfiles.sort(key=lambda x: getctime(x))
            readImages = False # If we don't find param files , use images
            for lastParameterFile in pyfiles:
                jsonObject = {}
                jsonObject["step"]="intraregistration"
                #lastParameterFile = pyfiles[-1]
                jsonObject["date"] = parseDateFromLogPath(lastParameterFile)
                #jsonObject["date"] = date.fromtimestamp(getctime(lastParameterFile)).strftime("%d/%m/%Y %H:%M:%S")
                f = open (lastParameterFile,"r")
                linesfull = f.read()
                lines = linesfull.split("\n")
                f.close()
                for line in lines:
                    shortline = line.strip().replace("\n","").replace(" ","")
                    if not shortline.startswith("#"):
                        keyval = shortline.split("=")
                        if keyval[0] in ["PATH_EMBRYO"] or len(keyval)<2: #We dont want this line
                            continue
                        if keyval[0] == "EN":
                            jsonObject["embryo_name"] = keyval[1]
                        elif keyval[1] == "True" or keyval[1] == "False": # If we find a bool
                            jsonObject[keyval[0]] = bool(keyval[1])
                        elif is_float(keyval[1]): # If we find a float
                            jsonObject[keyval[0]] = float(keyval[1])
                        elif is_integer(keyval[1]): # If we find a float
                            jsonObject[keyval[0]] = int(keyval[1])
                        else : # If its string
                            jsonObject[keyval[0]] = keyval[1].replace("'","").replace('"','')
                if not "EXP_INTRAREG" in jsonObject:
                    jsonObject["EXP_INTRAREG"] = fuseEXP
                jsonObjects.append(jsonObject)
    return jsonObjects
def loadJsonForFuse(fusePath, fuseFolderName):# CODE DUPLICATE TODO LATER
    from datetime import date
    jsonObjects = []
    readImages = True
    fuseEXP = fuseFolderName.replace("FUSE_","")
    logFolder = join(fusePath,logFolderName)
    print(logFolder)
    if isdir(logFolder):
        # read logs
        pyfiles = [join(logFolder,f) for f in os.listdir(logFolder) if os.path.isfile(join(logFolder,f)) and f.endswith(".py")] #all params files
        print(pyfiles)
        if len(pyfiles) > 0:
            pyfiles.sort(key=lambda x: getctime(x))
            readImages = False # If we don't find param files , use images
            for lastParameterFile in pyfiles:
                jsonObject = {}
                jsonObject["step"]="fusion"
                #lastParameterFile = pyfiles[-1]
                jsonObject["date"] = parseDateFromLogPath(lastParameterFile)
                #jsonObject["date"] = date.fromtimestamp(getctime(lastParameterFile)).strftime("%d/%m/%Y %H:%M:%S")
                f = open (lastParameterFile,"r")
                linesfull = f.read()
                lines = linesfull.split("\n")
                f.close()
                for line in lines:
                    shortline = line.strip().replace("\n","").replace(" ","")
                    if not shortline.startswith("#"):
                        keyval = shortline.split("=")
                        if keyval[0] in ["PATH_EMBRYO"] or len(keyval)<2: #We dont want this line
                            continue
                        if keyval[0] == "EN":
                            jsonObject["embryo_name"] = keyval[1]
                        elif keyval[1] == "True" or keyval[1] == "False": # If we find a bool
                            jsonObject[keyval[0]] = bool(keyval[1])
                        elif is_float(keyval[1]): # If we find a float
                            jsonObject[keyval[0]] = float(keyval[1])
                        elif is_integer(keyval[1]): # If we find a float
                            jsonObject[keyval[0]] = int(keyval[1])
                        else : # If its string
                            jsonObject[keyval[0]] = keyval[1].replace("'","").replace('"','')
                if not "EXP_FUSE" in jsonObject:
                    jsonObject["EXP_FUSE"] = fuseEXP
                jsonObjects.append(jsonObject)
    if not isdir(logFolder) or readImages:
        jsonObject = {}
        jsonObject["step"] = "fusion"
        # read with image and name
        files = [f for f in os.listdir(fusePath) if os.path.isfile(join(fusePath,f)) and isFileImage(f)]
        begin = 1000000
        end = -1000000
        embryoName = ""
        fuseDate = None
        firstTimeFile = None
        for file in files:
            if embryoName == "":
                embryoName = file.split("_fuse_")[0]
            fileTimeSplit = file.split("_t")
            if len(fileTimeSplit) > 0:
                time = int(fileTimeSplit[1].split(".")[0])
                if time > end:
                    end = time
                if time < begin:
                    firstTimeFile=join(fusePath,file)
                    begin = time
        if firstTimeFile is not None:
            fuseDate = date.fromtimestamp(getctime(firstTimeFile)).strftime("%d/%m/%Y %H:%M:%S")
            jsonObject["date"] = fuseDate
        jsonObject["begin"] = begin
        jsonObject["end"] = end
        jsonObject["embryo_name"] = embryoName
        jsonObject["EXP_FUSE"] = fuseEXP
        jsonObjects.append(jsonObject)
    return jsonObjects

def loadJsonFromSubFolder(inputFolder):
    finalJsonList = []
    subdirs = [f for f in os.listdir(inputFolder) if os.path.isdir(join(inputFolder, f))]
    for subdir in subdirs:
        if subdir == "FUSE":
            fusesubdirs = [f for f in os.listdir(join(inputFolder, subdir)) if
                           os.path.isdir(join(join(inputFolder, subdir), f))]
            for fusesubdir in fusesubdirs:
                if fusesubdir.startswith("FUSE_"):
                    jsonvals = loadJsonForFuse(join(join(inputFolder, subdir), fusesubdir), fusesubdir)
                    for jsoninstance in jsonvals:
                        finalJsonList.append(jsoninstance)
        if subdir == "SEG":
            fusesubdirs = [f for f in os.listdir(join(inputFolder, subdir)) if
                           os.path.isdir(join(join(inputFolder, subdir), f))]
            for fusesubdir in fusesubdirs:
                if fusesubdir.startswith("SEG_"):
                    jsonvals = loadJsonForSeg(join(join(inputFolder, subdir), fusesubdir), fusesubdir)
                    for jsoninstance in jsonvals:
                        finalJsonList.append(jsoninstance)
        if subdir == "POST":
            fusesubdirs = [f for f in os.listdir(join(inputFolder, subdir)) if
                           os.path.isdir(join(join(inputFolder, subdir), f))]
            for fusesubdir in fusesubdirs:
                if fusesubdir.startswith("POST_"):
                    jsonvals = loadJsonForPost(join(join(inputFolder, subdir), fusesubdir), fusesubdir)
                    for jsoninstance in jsonvals:
                        finalJsonList.append(jsoninstance)
        if subdir == "BACKGROUND":
            fusesubdirs = [f for f in os.listdir(join(inputFolder, subdir)) if
                           os.path.isdir(join(join(inputFolder, subdir), f))]
            for fusesubdir in fusesubdirs:
                if fusesubdir.startswith("BACKGROUND_") or fusesubdir.startswith(
                        "Background_"):  # the 2 exist , should use lower but keep the 2 tests for clarity
                    jsonvals = loadJsonForBackground(join(join(inputFolder, subdir), fusesubdir), fusesubdir)
                    for jsoninstance in jsonvals:
                        finalJsonList.append(jsoninstance)
        if subdir == "CONTOUR":
            fusesubdirs = [f for f in os.listdir(join(inputFolder, subdir)) if
                           os.path.isdir(join(join(inputFolder, subdir), f))]
            for fusesubdir in fusesubdirs:
                if fusesubdir.startswith("CONTOUR_"):
                    jsonvals = loadJsonForContour(join(join(inputFolder, subdir), fusesubdir), fusesubdir)
                    for jsoninstance in jsonvals:
                        finalJsonList.append(jsoninstance)
        if subdir == "INTRAREG":
            fusesubdirs = [f for f in os.listdir(join(inputFolder, subdir)) if
                           os.path.isdir(join(join(inputFolder, subdir), f))]
            for fusesubdir in fusesubdirs:
                if fusesubdir.startswith("INTRAREG_"):
                    jsonvals = loadJsonFromIntraregLogs(join(join(inputFolder, subdir), fusesubdir), fusesubdir)
                    for jsoninstance in jsonvals:
                        finalJsonList.append(jsoninstance)
                    #jsonvals = loadJsonFromSubFolder(join(join(inputFolder, subdir), fusesubdir))
                    #for jsoninstance in jsonvals:
                    #    finalJsonList.append(jsoninstance)
    return finalJsonList

def createMetadataFromFolder(embryoPath):
    finalJsonList = loadJsonFromSubFolder(embryoPath)
    with open(join(embryoPath,metadata_file), 'w+') as openJson:
        json.dump(finalJsonList, openJson)
def getMetaDataFile():
    """
    Return the used name for metadata files in AstecManager

    :returns: name of the file
    """
    return metadata_file


def loadMetaData(embryoPath):
    """
    Using an embryo path , this function load the metadata file corresponding to the embryo , and returns it

    :param embryoPath: string, path to the embryo folder
    :returns: list of dicts , the content of the json metadatas  , or None if it doesn't exist
    """
    if not isdir(embryoPath):
        print(" ! Embryo path not found !")
        return None

    jsonMetaData = join(embryoPath, getMetaDataFile())

    if not isfile(jsonMetaData):
        print(" ! Embryo metadata file not existing !")
        return None

    with open(jsonMetaData, 'r') as openJson:
        jsonObject = json.load(openJson)
    return jsonObject


def createMetaDataFile(embryoPath):
    if not isdir(embryoPath):
        os.makedirs(embryoPath)
    if not isfile(join(embryoPath, getMetaDataFile())):
        with open(join(embryoPath, getMetaDataFile()), "w+") as outfile:
            json.dump({}, outfile)
            return True
    return False


def writeMetaData(embryoPath, jsonDict):
    """
    Using an embryo path , this function write to the metadata file corresponding to the embryo the json dict

    :param embryoPath: string, path to the embryo folder
    :param jsonDict: dict, data to write (overwrite the content)
    """
    jsonMetaData = join(embryoPath, getMetaDataFile())
    if not isdir(embryoPath) or not isfile(jsonMetaData):
        createMetaDataFile(embryoPath)

    jsonMetaData = join(embryoPath, getMetaDataFile())

    with open(jsonMetaData, 'w') as openJson:
        json.dump(jsonDict, openJson)


def addDictToMetadata(embryoPath, jsonDict, addDate=True):
    """
    Add a dict to the json metadata file

    :param embryoPath: string, path to the embryo folder
    :param jsonDict: dict, dict to add to the metadata
    :param addDate: boolean,  if True, a new key is added to the dict , corresponding to now's date
    :returns: bool , True if the dict was added to the json metadata , False otherwise
    """
    if jsonDict is None:
        print("! Input json dict is None , can not add it to file")
        return False

    if type(jsonDict) is not dict:
        print(" ! input json is not a dictionary ! ")
        return False

    jsonMetadata = loadMetaData(embryoPath)
    if jsonMetadata is None:
        createMetaDataFile(embryoPath)

    if addDate:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        jsonDict["date"] = now
    jsonMetadata.append(jsonDict)
    writeMetaData(embryoPath, jsonMetadata)
