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
    hankaku = ["0","1","2","3","4","5","6","7","8","9"]
    zenkaku = ["０","１","２","３","４","５","６","７","８","９"] 
    columns = df.columns.values
    for i,j in zip(hankaku,zenkaku):
        for k in columns:
            df[k] = df[k].str.replace(j,i)
    return df


def size2g(df): #小、大さじのところだけ変更する
    df['size'] = df['size'].replace('大さじ(\d+).*',r'\1*15',regex=True)
    df['size'] = df['size'].replace('小さじ(\d+).*',r'\1*5',regex=True)
    df['size'] = df['size'].replace('(\d+)ｇ',r'\1',regex=True)
    df['size'] = df['size'].replace('(\d+)g',r'\1',regex=True)
    df['size'] = df['size'].replace('少々','0.5')
    df['size'] = df['size'].replace('(\d+)グラム',r'\1',regex=True)
    df['size'] = df['size'].replace('^0(\d+)',r'\1',regex=True)
    return df

def g2float(df):
    x = df[df['size'].str.match(r'^\d+\.*\**\d$')].copy()
    x['size'] = x['size'].apply(eval)
    return x


def clean_ingredient(df):
    df = df.fillna('適量')
    df = z2h(df)
    df = size2g(df)
    df = g2float(df)
    return df