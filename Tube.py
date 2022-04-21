import pandas
import matplotlib.pyplot as plt
from inspect import getsourcefile
import os.path

directory = os.path.dirname(__file__)

lineConnections = pandas.read_csv(directory + '\\LinesStations.csv')
allLines = pandas.read_csv(directory + '\\TubeLines.csv')
allStations = pandas.read_csv(directory + '\\TubeStations.csv')
allStationIDs = []
allStationDict = {}
allConnections = {}

for stationID in allStations["id"]:
    allStationIDs.append(stationID)

for stationID in allStationIDs:
    allStationDict[stationID] = {}
    allStationDict[stationID]["name"] = allStations.loc[allStations['id'] == stationID]["name"].item()
    allStationDict[stationID]["latitude"] = allStations.loc[allStations['id'] == stationID]["latitude"].item()
    allStationDict[stationID]["longitude"] = allStations.loc[allStations['id'] == stationID]["longitude"].item()
    
for i in range(len(lineConnections["station1"])):
    allConnections[i] = {}
    allConnections[i]["station1"] = lineConnections["station1"][i]
    allConnections[i]["station2"] = lineConnections["station2"][i]
    allConnections[i]["line"] = lineConnections["line"][i]
    
for idVal, railSegment in allConnections.items():
    station1ID = railSegment["station1"]
    station2ID = railSegment["station2"]
    railSegmentLineID = railSegment["line"]
    colour = allLines.loc[allLines['line'] == railSegmentLineID]["colour"].item()
    station1X = allStations.loc[allStations['id'] == station1ID]["longitude"].item()
    station1Y = allStations.loc[allStations['id'] == station1ID]["latitude"].item()
    station2X = allStations.loc[allStations['id'] == station2ID]["longitude"].item()
    station2Y = allStations.loc[allStations['id'] == station2ID]["latitude"].item()
    lineX = [station1X, station2X]
    lineY = [station1Y, station2Y]
    plt.plot(lineX, lineY, colour)
    
plt.show()