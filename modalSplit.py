# %%
import pandas
import matplotlib as plot
from pathlib import Path


def mainModeValueCounts(dataFrame, seriesName):
    "This does things"
    counts = dataFrame['mainMode'].value_counts() * 100
    counts.name = seriesName  # rename doesn't seem to work, so just assign things here
    return counts


def getRelative(dataFrame, changedColumns):
    "this also does things"
    result = dataFrame.copy()
    for name in changedColumns:
        result[name] = dataFrame[name] / dataFrame[name].sum()

    return result


def read_csv(listOfCsv):
    "This function reads supplied csvs and aggregates modal shares"
    modalSplits = []
    for file in listOfCsv:
        csv = pandas.read_csv(dataPath + file, usecols=['mainMode'])
        valueCounts = mainModeValueCounts(csv, Path(file).stem)
        modalSplits.append(valueCounts)
    return modalSplits


# %%
dataPath = 'C:\\Users\\Janek\\Desktop\\nemo_analysis\\'

expectedModalShare = pandas.read_csv(
    dataPath + 'expected-modal-share.csv', index_col='mode')

modalSplits = read_csv(['base-case.csv', 'bike-highways.csv'])
modalSplits.append(expectedModalShare)

modalShare = pandas.concat(modalSplits, axis=1, sort=False).rename(
    columns={'value': 'expected'})

print(modalShare)


# %%
numberOfTrips = modalShare.aggregate(sum)

print('number of trips by scenario')
print(numberOfTrips)

# %%
# plot absolute
modalShare.plot.bar()

# %%
# plot relative
# this should somehow work automagically
relative = getRelative(modalShare, ['expected', 'base-case', 'bike-highways'])
relative.plot.bar()
