#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


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


def z2h(df):
    hankaku = ["0","1","2","3","4","5","6","7","8","9","/"]
    zenkaku = ["０","１","２","３","４","５","６","７","８","９","／"] 
    columns = df.columns.values
    for i,j in zip(hankaku,zenkaku):
        for k in columns:
            df[k] = df[k].str.replace(j,i)
    return df


def size2g(df): #小、大さじのところだけ変更する
    df['size'] = df['size'].replace('大さじ(\d+).*',r'\1*15',regex=True)
    df['size'] = df['size'].replace('小さじ(\d+).*',r'\1*5',regex=True)
    df['size'] = df['size'].replace('小さじ(\d/\d).*',r'5*\1',regex=True)
    df['size'] = df['size'].replace('(\d+)ｇ',r'\1',regex=True)
    df['size'] = df['size'].replace('(\d+)g',r'\1',regex=True)
    df['size'] = df['size'].replace('少々','0.5')
    df['size'] = df['size'].replace('(\d+)グラム',r'\1',regex=True)
    df['size'] = df['size'].replace('^0(\d+)',r'\1',regex=True)
    return df
    

def g2float(df):
    x = df[df['size'].str.match(r'^\d+\.*\**\d*$')].copy()
    x['size'] = x['size'].apply(eval)
    return x


def clean_ingredient(df):
    df = df.fillna('適量')
    df = rmkigou(df)
    df = z2h(df)
    df = size2g(df)
    df = g2float(df)

    return df

def report_popularity(df):
    df = df["recipeID"].value_counts()
    df = df.reset_index()
    df = df.rename(columns={"index":"recipeID","recipeID":"count"})
    return df


def rmkigou(df):
    kigoulist = ["●","☆","◎","※","▲","◯","★"]
    for kigou in kigoulist:
        df["ingredient"] = df["ingredient"].str.replace(kigou,"")
    return df


def sum_seasoning(df):
    df["ingredient"] = df["ingredient"].replace("グラニュー糖","砂糖")
    df["ingredient"] = df["ingredient"].replace("無塩バター","バター")
    df["ingredient"] = df["ingredient"].replace("マーガリン","バター")
    df["ingredient"] = df["ingredient"].replace("しょうゆ","醤油")
    peppers = ["こしょう","胡椒","塩・胡椒","塩・コショウ","塩、こしょう","ブラックペッパー","塩コショウ","塩・塩こしょう","塩,塩こしょう","塩・こしょう","塩胡椒","コショウ"]
    for pepper in peppers:
        df["ingredient"] = df["ingredient"].replace(pepper,"塩こしょう") 
    return df

def mk_vector(df):
    vec = pd.DataFrame(columns = ["recipeID","sugar","salt","butter","pepper","soysource"],index=[])
    vec_dic = {"砂糖":"sugar","塩":"salt","バター":"butter","塩こしょう":"pepper","醤油":"soysource"}

    vec["recipeID"] = df["recipeID"]

    for row in df.itertuples():
        vec.loc[vec["recipeID"]==row.recipeID,vec_dic[row.ingredient]] = row.size
        
    vec = vec.fillna(0)
    return vec


def extract_something(df,sth):
    x=df[df["recipe_name"].str.contains(sth,na=False)]
    y=df[df["details"].str.contains(sth,na=False)]
    z=x.append(y)
    a=set(z["recipeID"])
    return df[df["recipeID"].isin(a)]


'''
df_report = t1.read_report(2000)
repo_num = df_report["recipeID"].value_counts()
for row in df_repo_num.itertuples():
    repo_vec.loc[repo_vec["recipeID"]==row.recipeID,"repo_num"] = row.repo_num

ざっとしたプロットの方法
from pandas import plotting 
plotting.scatter_matrix(vec.iloc[:, 1:], figsize=(8, 8), alpha=0.5)
plt.show()
'''
