from error_type import load_data
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter
import os
import datetime
#import sys
#sys.path = ['/test'] + sys.path
#x = load_data('program', '2024-01-04')
plt.rc('font', family='Microsoft JhengHei')

def stat_data(data):#整理原始資料的mode成功率

    if type(data) == str:#避免原始資料為空出現error
        return 'N'
    lst_directfit = list(set(data['directfit']))#建立directfit的所有類別
    df = pd.DataFrame({'Mode':[], 'Total':[], 'Sum PASS':[], 'Sum NG':[], 'Fail RATE':[]})#建立資料框架
    for i in lst_directfit:#遍歷所有directfit類別
        tp_row = data[data.directfit == i]#為第i個directfit的資料
        total = len(tp_row)#總次數
        sum_PASS = len(tp_row[tp_row.errortype == 'success'])#總成功次數
        sum_NG = len(tp_row[(tp_row.errortype != 11) & (tp_row.errortype != 'success')])#總失敗次數
        rate_fail = round(sum_NG*100/total)#失敗率
        stat_dict = {'Mode':i, 'Total':total, 'Sum PASS':sum_PASS, 'Sum NG':sum_NG, 'Fail RATE':rate_fail}
        #df = df.append(stat_dict, ignore_index=True)
        df = pd.concat([df, pd.DataFrame([stat_dict])], ignore_index = True)
    
    return df


def plot_failrate(da, first_r = None, last_r = None):#失敗率作圖

    st_da = stat_data(da)#使用上述function統計資料
    st_da = (st_da.sort_values('Fail RATE', ascending = False))[first_r:last_r].sort_values('Fail RATE', ascending = True)#用失敗率由大到小排序，可給定範圍變數
    y = list(st_da['Fail RATE'])#失敗率取值
    x = list(st_da['Mode'])#mode類別
    plt.figure(figsize=(15, 10), dpi = 200)#設定畫框
    plt.barh(x, y, color='tab:red')#作水平長條圖
    plt.legend(['失敗率'])
    plt.title('Tool失敗率')
    for i, v in enumerate(y):#在每條上增加數據
        plt.text(v, i, str(v)+'%', color='blue', fontweight='bold')
        
    return plt

    
def plot_total(da, first_r = None, last_r = None):#使用總次數作圖

    st_da = stat_data(da)#使用上述function統計資料
    st_da = (st_da.sort_values('Total', ascending = False))[first_r:last_r].sort_values('Total', ascending = True)#用總次數由大到小排序，可給定範圍變數
    
    y = list(st_da['Total'])#總次數取值
    x = list(st_da['Mode'])#mode類別
    plt.figure(figsize=(15, 10), dpi = 200)#設定畫框
    plt.barh(x, y, color='b')#做水平長條圖
    plt.legend(['使用次數'])
    plt.title('Tool使用次數')

    for i, v in enumerate(y):#在每條上增加數據
        plt.text(v, i, str(v), color='blue', fontweight='bold')
    return plt
    
    
def plot_failrate_total(da, first_r = None, last_r = None):#tool使用次數長條圖與標記失敗率
    st_da = stat_data(da)
    st_da = (st_da.sort_values('Total', ascending = False))[first_r:last_r]
    y1 = list(st_da['Fail RATE'])
    y2 = list(st_da['Total'])
    x = list(st_da['Mode'])
    plt.figure(figsize=(15, 10), dpi = 200)
    bar1 = plt.bar(x,y2,color='b',width=0.4, align='edge')  # 第一組數據靠左邊緣對齊
    
    plt.xticks(rotation=90)
    plt.legend(['個數'])
    plt.title('Tool失敗率與個數')
    
    for rect1, rect2 in zip(bar1, y1):#在每一條長條圖上增加失敗率
        height = rect1.get_height()
        plt.text(rect1.get_x() + rect1.get_width() / 2.0, height, f'{rect2:.0f}'+'%', ha='center', va='bottom')
        
    return plt  
        

def plot_sum_error(da):#tool錯誤次數統計圖
    error_type = [y.split('-')[0] for y in [z for z in da['errortype']]]#抓出每個error type代碼的第一段
    error_type_key = Counter(error_type).keys()
    error_type_value = Counter(error_type).values()
    plt.figure(figsize=(25, 10), dpi = 200)
    bar1 = plt.bar(error_type_key, error_type_value)
    plt.title('Tool錯誤統計')
    plt.ylabel('數量')
    plt.xlabel('錯誤類別')
    
    for rect in bar1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2, height, f'{height:.0f}', ha = 'center', va = 'bottom')
    
    return plt

def plot_to_png(date = datetime.date.today().strftime('%Y-%m-%d'), end_date = ''):
    
    if os.path.isdir('統計圖表') == False:#如果資料夾不存在，創建
        os.makedirs('統計圖表/OG')
        os.makedirs('統計圖表/OG2')
        os.makedirs('統計圖表/OG3')
        os.makedirs('統計圖表/OGlite')
    if date == (datetime.date.today().strftime('%Y-%m-%d')):#如果沒有設定date，則以當日前一天為date
        day_time = (date.today() - datetime.timedelta(days = 1)).strftime('%Y-%m-%d')
    else:
        day_time = date
      
    OG = ['OG',
          'OG2', 
          'OG3', 
          'OGlite']
    if end_date == '':#單日輸出
        for og in OG:#遍例四個OG
            
            path = '統計圖表/{}/Chart {}'.format(og, day_time)#存檔位置
            if not os.path.isdir(path):#如無存檔位置，創建
                os.mkdir(path)
            da = load_data(data = 'program', date = day_time, OG = og)
            
            if type(da) == str:#如果當日無資料，也就是產出的錯誤分析資料型態非資料框架，跳過這次回圈，進入下次回圈
                continue
            
            plot_failrate(da).savefig('統計圖表/{}/Chart {}/{} Failrate chart.png'.format(og, day_time, day_time))
            plot_total(da).savefig('統計圖表/{}/Chart {}/{} Total chart.png'.format(og, day_time, day_time))
            plot_failrate_total(da).savefig('統計圖表/{}/Chart {}/{} Failrate and Total chart.png'.format(og, day_time, day_time))
            plot_sum_error(da).savefig('統計圖表/{}/Chart {}/{} Sum error chart.png'.format(og, day_time, day_time))
            
    elif end_date != '':#多日輸出
        for og in OG:#遍例四個OG
            
            path = '統計圖表/{}/Chart {} to {}'.format(og, day_time, end_date)#存檔位置
            if not os.path.isdir(path):#如無存檔位置，創建
                os.mkdir(path)
            da = load_data(data = 'program', date = day_time, end_date = end_date, OG = og)
            
            if type(da) == str:#如果當日無資料，也就是產出的錯誤分析資料型態非資料框架，跳過這次回圈，進入下次回圈
                continue
            
            plot_failrate(da).savefig('統計圖表/{}/Chart {} to {}/{} to {} Failrate chart.png'.format(og, day_time, end_date, day_time, end_date))
            plot_total(da).savefig('統計圖表/{}/Chart {} to {}/{} to {} Total chart.png'.format(og, day_time, end_date, day_time, end_date))
            plot_failrate_total(da).savefig('統計圖表/{}/Chart {} to {}/{} to {} Failrate and Total chart.png'.format(og, day_time, end_date, day_time, end_date))
            plot_sum_error(da).savefig('統計圖表/{}/Chart {} to {}/{} to {} Sum error chart.png'.format(og, day_time, end_date, day_time, end_date))

