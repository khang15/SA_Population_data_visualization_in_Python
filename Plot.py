import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from Preprocess import *


def LocationAgeFixed(type, sex) :
    plt.figure(figsize=(32,32))
    location = input('Chọn quốc gia : ')
    age = input('Chọn tuối : ')
    data = df[df['Location'] == location]
    if sex == False :
        data = data[data['Sex'] == 'Both']
        if type == 'bar-v' :
            sns.barplot(x=data.index, y=data[age], ci=None)
        if type == 'bar-h' :
            sns.barplot(x=data[age], y=data.index, orient = "h", ci=None)
        if type == 'line' :
            sns.lineplot(x=data.index, y=data[age])
        if type == 'point' :
            plt.stem(data.index, data[age])     
    if sex == True :
        data1 = data[data['Sex'] == 'Male']
        data2 = data[data['Sex'] == 'Female']
        bars1 = data1['0-4']
        bars2 = data2['0-4']
        if type == 'bar' :
            plt.bar(bars1.index, bars1, color='#7f6d5f', edgecolor='white', width=2)
            plt.bar(bars2.index, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=2)
        if type == 'line' :
            plt.stackplot(bars1.index, bars1, bars2)
        plt.xticks(bars1.index)
        plt.legend(['Male','Female'])

    plt.title('Dân số ' + location + ' ở độ tuổi ' + age)
    plt.ylabel('Dân số ( nghìn )')
    plt.xticks(rotation=45)
    plt.show()

def LocationYearFixed(type, sex) :
    plt.figure(figsize=(32,32))
    location = input('Chọn quốc gia : ')
    year = int(input('Chọn năm : '))
    data = df.loc[year,:]
    if sex == False :
        data = data[data['Sex'] == 'Both']
        bar = np.array(data.iloc[0,3:], dtype = float)
        if type == 'bar-v' :
            sns.barplot(x=data.columns[3:], y=bar)
        if type == 'bar-h' :
            sns.barplot(x=data.columns[3:], y=bar, orient="h")
        if type == 'line' :
            sns.lineplot(x=data.columns[3:], y=bar, sort=False)

    if sex == True :
        data1 = data[data['Sex'] == 'Male']
        data2 = data[data['Sex'] == 'Female']
        bars1 = np.array(data1.iloc[0,3:], dtype = float)
        bars2 = np.array(data1.iloc[0,3:], dtype = float)

        if type == 'bar' :
            plt.bar(data.columns[3:], bars1, color='#7f6d5f', edgecolor='white', width=1)
            plt.bar(data.columns[3:], bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=1)
        if type == 'line' :
            plt.stackplot(data.columns[3:], bars1, bars2)

        plt.legend(['Male','Female'])

    plt.title('Dân số ' + location + ' tại năm ' + str(year))
    plt.xlabel('Độ tuổi')
    plt.ylabel('Dân số ( nghìn )')
    plt.xticks(rotation=45)
    plt.show()

def YearAgeFixed(type) :
    year = int(input('Chọn năm : '))
    age = input('Chọn độ tuổi : ')
    data = df.loc[year,:]
    data = data[data['Sex'] == 'Both']
    data.set_index('Location', inplace=True)
    data = pd.DataFrame(data[age], index = data.index)
    if type == 'pie' :
        data.plot(kind='pie', subplots=True, figsize=(32,32), labels )
    if type =='donut' :
        data.plot(kind='pie', subplots=True, figsize=(32,32))
        my_circle=plt.Circle( (0,0), 0.6, color='white')
        p=plt.gcf()
        p.gca().add_artist(my_circle)

    plt.title('Tỉ lệ dân số giữa các nước theo độ tuổi ' + age +' tại năm ' + str(year) )
    plt.show()
    
def AgeFixed(type) :
    plt.figure(figsize=(32,32))
    age = input('Chọn độ tuổi : ')
    data = df[df['Sex'] == 'Both']
    if type == 'line' :
        sns.lineplot(data.index, data[age], hue = data['Location'])
    if type == 'scatter' :
         sns.scatterplot(data.index, data[age], hue = data['Location'])
    
    plt.title('Dân số ở độ tuổi ' + age)
    plt.ylabel('Dân số ( nghìn )')
    plt.xticks(data.index, rotation=45)
    plt.show()

def YearFixed(type) :
    year = int(input('Chọn năm : '))
    data = df[df['Sex'] == 'Both']
    data = data.loc[year,:]
    data.set_index('Location',inplace=True)
    data_x = []
    data_y = []
    hue = []
    for location in data.index :
        for col in data.columns[2:] :
            data_x.append(col)
            data_y.append(data.loc[location,col])
            hue.append(location)
    
    if type == 'line' :
        sns.lineplot(x=data_x, y=data_y, hue =hue, sort=False)
    if type == 'scatter' :
        sns.scatterplot(x=data_x, y=data_y, hue =hue)

    plt.title('Dân số của các nước tại năm ' + str(year))      
    plt.ylabel('Population ( thousand )')
    plt.xticks(rotation=45)
    plt.show()
