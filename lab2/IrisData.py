import pandas as pd 
import re 


class IrisData():
    missing_values = ["-", "--", "na", "NA", "n/a", "nan", "NaN", "null", "ng", "NG"]
    versicolor_pattern = r'[vV]ersicolo'
    versicolor_regex = re.compile(versicolor_pattern, re.IGNORECASE)
    setosa_pattern = r'[sS]etosa'
    setosa_regex = re.compile(setosa_pattern, re.IGNORECASE)
    virginica_pattern = r'[vV]irginica'
    virginica_regex = re.compile(virginica_pattern, re.IGNORECASE)

    def __init__(self: object) -> None:
        self.df = pd.read_csv("iris_with_errors.csv", na_values = self.missing_values)
        self.cleaned_df = pd.read_csv("iris_with_errors.csv", na_values = self.missing_values)
        self.na_df = self.df[self.df.isna().any(axis=1)]
    def clean_false_data(self: object) -> None:
        self.dropMissingDataRows()
        for index in self.cleaned_df.index: 
            name = self.cleaned_df.at[index, 'variety']

            virginica_match = self.virginica_regex.search(name) 
            setosa_match = self.setosa_regex.search(name) 
            versicolor_match = self.versicolor_regex.search(name)
            
            if versicolor_match: 
                self.cleaned_df.loc[index, 'variety'] = 'versicolor'
                self.df.loc[index, 'variety'] = 'versicolor'
            elif setosa_match:
                self.cleaned_df.loc[index, 'variety'] = 'setosa'
                self.df.loc[index, 'variety'] = 'setosa'
            elif virginica_match:
                self.cleaned_df.loc[index, 'variety'] = 'virginica'
                self.df.loc[index, 'variety'] = 'virginica'
            else: 
                self.cleaned_df.drop(index=index, inplace=True)
                continue

            val = self.cleaned_df.at[index, 'sepal.length']
            if ((not (0 < val <= 15))) or val == "nan":
                self.cleaned_df.drop(index=index, inplace=True)
                continue
            val = self.df.at[index, 'petal.length']
            if ((not (0 < val <= 15))) or val == "nan":
                self.cleaned_df.drop(index=index, inplace=True)
                continue
            val = self.cleaned_df.at[index, 'sepal.width']
            if ((not (0 < val <= 15))) or val == "nan":
                self.cleaned_df.drop(index=index, inplace=True)
                continue
            val = self.cleaned_df.at[index, 'petal.width']
            if ((not (0 < val <= 15))) or val == "nan":
                self.cleaned_df.drop(index=index, inplace=True)
                continue
        
    def clean_final_data(self: object) -> None:
        for index in self.df.index: 
            val = self.df.at[index, 'sepal.length']
            if ((not (0 < val <= 15))) or val == "nan":
                self.df.at[index, 'sepal.length'] = self.countCleanedMedian('sepal.length')
            val = self.df.at[index, 'petal.length']
            if ((not (0 < val <= 15))) or val == "nan":
                self.df.at[index, 'petal.length'] = self.countCleanedMedian('petal.length')
            val = self.df.at[index, 'sepal.width']
            if ((not (0 < val <= 15))) or val == "nan":
                self.df.at[index, 'sepal.width'] = self.countCleanedMedian('sepal.width')
            val = self.df.at[index, 'petal.width']
            if ((not (0 < val <= 15))) or val == "nan":
                self.df.at[index, 'petal.width'] = self.countCleanedMedian('petal.width')

    def dropMissingDataRows(self: object) -> None :
        self.cleaned_df.dropna(inplace=True)
    def countCleanedMedian(self: object, key: str) -> float:
        res = self.cleaned_df[key].median()
        return float(res)
