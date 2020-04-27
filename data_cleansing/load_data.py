import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

#データ読み込みの関数。nは年数で1998~2014。
def year_error(n):
    raise Exception("nは1998から2014を入力してください n = %d" % n)


def read_recipe(n): 
    columns = ['recipeID','UserID','recipe_name','details','servings',
              'advice','upbringing','date']
    loc = 'data/recipe/recipe' + str(n) + '.csv'
    df = pd.read_csv(loc,names=columns,index_col=None)
    return df


def read_report(n):
    columns = ['recipeID','UserID','message','reply','date']
    loc = 'data/report/report' + str(n) + '.csv'
    df = pd.read_csv(loc,names=columns)
    return df


def read_step(n):
    columns = ['recipeID','step_number','note']
    loc = 'data/step/step' + str(n) + '.csv'
    df = pd.read_csv(loc,names=columns)
    return df


def read_ingredient(n):
    columns = ['recipeID','ingredient','size']
    loc = 'data/ingredient/ingredient' + str(n) + '.csv'
    df = pd.read_csv(loc,names=columns)
    return df
