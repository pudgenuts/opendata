import pandas as pd
import array as arr
import sys 
import time
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('--year')
parser.add_argument('--data')
args = parser.parse_args()


def format(x):
        return "${:.1f}K".format(x/1000)


# Index(['FY', 'Name', 'JobTitle', 'AgencyID', 'Agency', 'HireDate', 'AnnualSalary', 'GrossPay', 'OT', 'OTratio'], dtype='object')
data = pd.read_csv(args.data, delimiter='\t')

data['OT'] =  (data.GrossPay - data.AnnualSalary)
data['OTratio'] =  data.OT / data.AnnualSalary
data['baseRetirement'] = (data.AnnualSalary * 0.025)
data['retirementBonus'] = (data.GrossPay * 0.025) - (data.AnnualSalary * 0.025)

# data.style.format({"AnnualSalary": "${:20,.0f}", "GrossPay": "${:20,.0f}"})

# print(data.head(10))
data.columns 
print(data.columns)
#

print(data.describe())
TopEarners = [];

years = arr.array('i',[ 2011,2012,2013,2014,2015,2016,2017,2018,2019])
for currentYear in years: 
        print(currentYear)
        file = args.data + currentYear + ".tsv"
        data = pd.read_csv(file, delimiter='\t')
        
        data['OT'] =  (data.GrossPay - data.AnnualSalary)
        data['OTratio'] =  data.OT / data.AnnualSalary
        data['baseRetirement'] = (data.AnnualSalary * 0.025)
        data['retirementBonus'] = (data.GrossPay * 0.025) - (data.AnnualSalary * 0.025)
        
        extract =  data.loc[(data['FY'] == currentYear) & (data['OT'] > 0 ) ]
        largest = extract.nlargest(20,'OTratio')
        for index, row in largest.iterrows():
                TopEarners.append(row['Name'])
 

        sorted = largest.sort_values(['GrossPay'])
        extract.GrossPay.format('${0:..2f}')
        print(extract.describe())
        largest.style.format({"AnnualSalary": "${:20,.0f}", "GrossPay": "${:20,.0f}"})
        print(sorted.to_string())
        print(extract['OT'].sum())
 
# 
# extract.sort_values('GrossPay')
# largest = extract.nlargest(10,'OTratio')
# 
# uniqueEarners = list(dict.fromkeys(TopEarners))
# print(uniqueEarners)
# for name in uniqueEarners: 
#         nameExtract = data.loc[data['Name'] == name] 
#         print(nameExtract)
# 
# 
# 
# print(data.AgencyID.unique())
# Agencies = data.AgencyID.unique()
# for ID in Agencies: 
#         print(ID)
#         for currentYear in years:
#                 agencyExtract = data.loc[(data['FY'] == currentYear) & (data['AgencyID'] == ID)]
#                 formatted_float = "${:,.2f}".format(agencyExtract['GrossPay'].sum())
#                 print(" %s: %s" %(currentYear, formatted_float))
# 
# 
# #for row in extract.rows():
         #print(row)