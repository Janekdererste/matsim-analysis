# %%
import pandas
import matplotlib as plot


def mainModeValueCounts(dataFrame, seriesName):
    "This does things"
    counts = dataFrame['mainMode'].value_counts() * 100
    counts.name = seriesName  # rename doesn't seem to work, so just assign things here
    print(counts)
    return counts


def getRelative(dataFrame, changedColumns):
    "this also does things"
    result = dataFrame.copy()
    for name in changedColumns:
        result[name] = dataFrame[name] / dataFrame[name].sum()

    return result


dataPath = 'C:\\Users\\Janek\\Desktop\\nemo_analysis\\'

expectedModalShare = pandas.read_csv(
    dataPath + 'expected-modal-share.csv', index_col='mode')

baseCaseData = pandas.read_csv(dataPath + 'base-case.csv')
bikeHighways = pandas.read_csv(dataPath + 'bike-highways.csv')

print(expectedModalShare)
print(baseCaseData[:10])

# %%
numberOfTrips = baseCaseData.shape[0]
expectedNumberOfTrips = expectedModalShare['value'].aggregate(sum)
print('expected number of trips: ' + str(expectedNumberOfTrips))
print('baseCase number of trips: ' + str(numberOfTrips * 100))
print('highways number of trips: ' + str(bikeHighways.shape[0] * 100))


# %%
# ----------------------- Modal Share ----------------------
# the current example is a 1% sample, so we have to scale up by 100
modalShareSeries = mainModeValueCounts(baseCaseData, 'baseCase')
bikeHighwaysSeries = mainModeValueCounts(bikeHighways, 'bikeHighways')


# we can join on mode here, pandas just does the right thing with the counted series here
compare = pandas.concat([expectedModalShare, modalShareSeries, bikeHighwaysSeries],
                        axis=1, sort=False).rename(columns={'value': 'expected'})
compare.index.name = 'mode'
print(compare)

# plot absolute
compare.plot.bar()

# %%
# plot relative
relative = getRelative(compare, ['expected', 'baseCase', 'bikeHighways'])
relative.plot.bar()


# %%
