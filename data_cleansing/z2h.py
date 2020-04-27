#半角数字にする関数

def z2h(df):
    hankaku = ["0","1","2","3","4","5","6","7","8","9"]
    zenkaku = ["０","１","２","３","４","５","６","７","８","９"] 
    
    columns = df.columns.values
    for i,j in zip(hankaku,zenkaku):
        for k in columns:
            df[k] = df[k].str.replace(j,i)
    return df
