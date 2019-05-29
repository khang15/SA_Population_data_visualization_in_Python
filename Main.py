from Plot import * 

def Main() :
    print('1. Cố định độ tuổi và quốc gia')
    print('2. Cố định năm và quốc gia')
    print('3. Cố định độ tuổi và năm')
    print('4. Cố định độ tuối')
    print('5. Cố định năm')
    s = int(input())
    print('\x1bc')
    if s == 1 :
        LocationAgeFixed_Menu()
    if s == 2 :
        LocationYearFixed_Menu()
    if s == 3 :
        YearAgeFixed_Menu()
    if s == 4 :
        AgeFixed_Menu()
    if s == 5 :
        YearFixed_Menu()

def LocationAgeFixed_Menu() :
    print('1. Tất cả')
    print('2. Phân chia giới tính')
    v = int(input())
    print('\x1bc')
    if v == 1 :
        print('1. Biểu đồ cột đứng')
        print('2. Biểu đồ cột ngang')
        print('3. Biểu đồ đường')
        print('4. Biểu đồ điểm')
        s = int(input())
        print('\x1bc')
        if s == 1 :
            LocationAgeFixed('bar-v',False)
        if s == 2 :
            LocationAgeFixed('bar-h',False)
        if s == 3 :
            LocationAgeFixed('line',False)
        if s == 4 :
            LocationAgeFixed('point',False)
    if v == 2 :
        print('1. Biểu đồ cột')
        print('2. Biểu đồ đướng')
        s = int(input())
        print('\x1bc')
        if s == 1 :
            LocationAgeFixed('bar',True)
        if s == 2 :
            LocationAgeFixed('line',True)

def LocationYearFixed_Menu() :
    print('1. Tất cả')
    print('2. Phân chia giới tính')
    v = int(input())
    print('\x1bc')
    if v == 1 :
        print('1. Biểu đồ cột đứng')
        print('2. Biểu đồ cột ngang')
        print('3. Biểu đồ đường')
        s = int(input())
        print('\x1bc')
        if s == 1 :
            LocationYearFixed('bar-v',False)
        if s == 2 :
            LocationYearFixed('bar-h',False)
        if s == 3 :
            LocationYearFixed('line',False)
    if v == 2 :
        print('1. Biểu đồ cột')
        print('2. Biểu đồ đướng')
        s = int(input())
        print('\x1bc')
        if s == 1 :
            LocationYearFixed('bar',True)
        if s == 2 :
            LocationYearFixed('line',True)

def AgeFixed_Menu() :
    print('1. Biểu đồ đường')
    print('2. Biểu đồ điểm')
    s = int(input())
    print('\x1bc')
    if s == 1 :
        AgeFixed('line')
    if s == 2 :
        AgeFixed('scatter')

def YearFixed_Menu() :
    print('1. Biểu đồ đường')
    print('2. Biểu đồ điểm')
    s = int(input())
    print('\x1bc')
    if s == 1 :
        YearFixed('line')
    if s == 2 :
        YearFixed('scatter')

def YearAgeFixed_Menu() :
    print('1.Biểu đồ tròn')
    print('2. Biểu đồ vành khăn')
    s = int(input())
    print('\x1bc')
    if s == 1 :
        YearAgeFixed('pie')
    if s == 2 :
        YearAgeFixed('donut')

Main()