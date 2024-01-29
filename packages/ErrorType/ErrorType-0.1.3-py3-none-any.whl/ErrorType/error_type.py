import pandas as pd
import json
import requests
import datetime
import warnings
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter

warnings.filterwarnings('ignore')


def load_data(api, data, date = '', end_date = '', OG = 'OG2'):
    
    if OG == 'OG':
        OG = 'ogmemory.'
    if OG == 'OG2':
        OG = 'og2memory.'
    if OG == 'OG3':
        OG = 'og3memory.'
    if OG == 'OGlite':
        OG = 'oglitememory.'
        
    url = api

    if end_date == '':
        end_date = date
      
    if OG == 'oglitememory.':
        if data == 'program':
          payload = "SELECT make, year, model, id, directfit, serialnumber, errortype, account, number, time, inTire FROM {}transfermemory where time BETWEEN '{} 00:00:00' and '{} 23:59:59' AND account not in (SELECT Account FROM model_base.account_identification Where Identity != 'ATU') order by time asc;".format(OG, date, end_date)
        elif data == 'copy':
          payload = "SELECT make, model, id, directfit, errortype, account, number, time FROM {}copy_result where time BETWEEN '{} 00:00:00' and '{} 23:59:59'AND account not in (SELECT Account FROM model_base.account_identification Where Identity != 'ATU') order by time asc;".format(OG, date, end_date)
        elif data == 'trigger':
          payload = "SELECT make, sensorid, model, id, directfit, time, errortype, account FROM {}triggerinfo where time BETWEEN '{} 00:00:00' and '{} 23:59:59' AND account not in (SELECT Account FROM model_base.account_identification Where Identity != 'ATU') order by time asc;".format(OG, date, end_date)
    
    else:
        if data == 'program':
          payload = "SELECT make, year, model, id, directfit, serialnumber, errortype, account, number, time, inTire, final FROM {}transfermemory where time BETWEEN '{} 00:00:00' and '{} 23:59:59' and final = 1 AND account not in (SELECT Account FROM model_base.account_identification Where Identity != 'ATU') order by time asc;".format(OG, date, end_date)
        elif data == 'copy':
          payload = "SELECT make, model, id, directfit, errortype, account, number, time, final FROM {}copy_result where time BETWEEN '{} 00:00:00' and '{} 23:59:59' and final = 1 AND account not in (SELECT Account FROM model_base.account_identification Where Identity != 'ATU') order by time asc;".format(OG, date, end_date)
        elif data == 'trigger':
          payload = "SELECT make, sensorid, model, id, directfit, type, admin, time FROM {}triggerinfo where time BETWEEN '{} 00:00:00' and '{} 23:59:59' AND admin not in (SELECT Account FROM model_base.account_identification Where Identity != 'ATU') order by time asc;".format(OG, date, end_date)
    
    headers = {
      'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    x = json.loads(response.text)
    da = pd.json_normalize(x)
    
    if da.shape[0] == 0:
        return 'Empty'
    else:
        return da

def judge_error(temp_data_time):#錯誤判斷
    if ('13' in [y.split('-')[0] for y in [z for z in temp_data_time['errortype']]]):
        return 'quit undercharge'
    elif ('2_noResponse' in [x for x in temp_data_time['errortype']]):
        return 'entry fail'
    elif ('4_noResponse' in [x for x in temp_data_time['errortype']]):
        return 'prg.check fail'
    elif ('1' in [y.split('-')[0] for y in [z for z in temp_data_time['errortype']]]):
        return 'check ID fail'
    elif ('4' in [x for x in temp_data_time['errortype']]):
        return 'prg.check fail'
    elif ('2' in [y.split('-')[0] for y in [z for z in temp_data_time['errortype']]]):
        return 'entry fail'



def error_analysis(api, date, end_date = '', OG = 'OG2'):
    
    if end_date == '':#如果沒有輸入最終時間，則為單日搜尋
        end_date = date
    
    da_program = load_data(api, data = 'program', date = date, end_date = end_date, OG = OG)#讀取program資料
  
    if type(da_program) == str:
        return 'N'
  
    da_copy = load_data(api, data = 'copy', date = date, end_date = end_date, OG = OG)#讀取copy資料
    da_trigger = load_data(api, data = 'trigger', date = date, end_date = end_date, OG = OG)#讀取trigger資料
  
    da_program['inTire'] = da_program['inTire'].replace('0', 'false').replace('1', 'true')#將Intire轉換成True和false
    da_program['time'] = pd.to_datetime(da_program['time'])#將program資料的時間行轉為時間類型
    
    df = pd.DataFrame({'Account':[], 'Date':[], 'Serialnumber':[], 'Directfit':[], 'Errortype':[],
                    'Successe in the end':[], 'Use copyID':[], 'Trigger sensor ID':[], 'Number':[], 'InTire':[], 'Problem':[]})#建立資料框架
  
  
  
    if OG == 'OGlite':
        da_trigger = da_trigger.rename(columns={'account':'admin'})
        da_trigger = da_trigger.rename(columns={'errortype':'type'})
  
    lst_account = list(set(list(da_program['account'])))
    lst_account.sort(key = list(da_program['account']).index)#於時間date中所有的account類別(不重複)
  
  
      
    if type(da_copy) != str:#將copy資料的time轉為時間類型
        da_copy['time'] = pd.to_datetime(da_copy['time'])
    if type(da_trigger) != str:#將trigger資料的time轉為時間類型
        da_trigger['time'] = pd.to_datetime(da_trigger['time'])
  
  
  
  
  
    for account in lst_account:#使用for loop遍歷account
        temp_data = da_program[da_program.account == account]#暫時儲存account = lst_account其中一個類別的da_program資料
        while len(temp_data) != 0:
            temp_problem = []
            temp_data_idx = temp_data.index.copy()#製作temp_data
            time_forward_10min = temp_data['time'].iloc[0] + datetime.timedelta(minutes = 30)#第一筆資料時間往後30分鐘的時間
            time_backward_10min = temp_data['time'].iloc[0] - datetime.timedelta(minutes = 30)#第一筆資料時間往前30分鐘的時間
    
            row_1_make = temp_data['make'].iloc[0]
            row_1_year = temp_data['year'].iloc[0]
            row_1_model = temp_data['model'].iloc[0]
            row_1_directfit = temp_data['directfit'].iloc[0]
    
            temp_data_time = temp_data[(temp_data['time'] <= time_forward_10min) & (temp_data.make == row_1_make) & (temp_data.model == row_1_model) & (temp_data.year == row_1_year) & (temp_data.directfit == row_1_directfit)]#時間小於time_forward_10min的資料
            temp_data.drop(temp_data_idx[temp_data_idx.isin(temp_data_time.index)], inplace=True)#temp_data移除temp_data_time資料
    
            if (list(set(temp_data_time['errortype'])) == ['success'])|(list(set(temp_data_time['errortype'])) == ['11'])|(list(set(temp_data_time['errortype'])) == ['success', '11'])|(list(set(temp_data_time['errortype'])) == ['11', 'success']):
              continue#如果errortype中只有success或是11或是只有success跟11，就跳開迴圈往下一筆執行
              
            if  type(da_copy) == str:
                temp_copy = 'NO'
            else:
                #如果沒有copy則在Use copyID顯示NO
                temp_copy = 'No' if (len(da_copy[(da_copy.account == temp_data_time['account'].iloc[0]) & (da_copy.directfit == temp_data_time['directfit'].iloc[0]) & (da_copy['time'] < time_forward_10min) & (da_copy['time'] > time_backward_10min)])== 0) else 'Yes'
            if type(da_trigger) == str:
                temp_trigger = 'NO'
            else:
                #如果沒有trigger則在Trigger sensor ID 顯示NO
                temp_trigger = 'No' if (len(da_trigger[(da_trigger.directfit == temp_data_time['directfit'].iloc[0]) & (da_trigger.admin == temp_data_time['account'].iloc[0]) & (da_trigger.sensorid != 'NA') & (da_trigger['time'] < time_forward_10min) & (da_trigger['time'] > time_backward_10min)]) == 0) else repr([x for x in da_trigger.sensorid[(da_trigger.directfit == temp_data_time['directfit'].iloc[0]) & (da_trigger.admin == temp_data_time['account'].iloc[0]) & (da_trigger.sensorid != 'NA')]])
      
      
            add_row_dict = {
                'Account':account,
                'Date':'{}  to  {}'.format(temp_data_time['time'].iloc[0], temp_data_time['time'].iloc[-1]),
                'Serialnumber':temp_data_time['serialnumber'].iloc[0],
                'Directfit':temp_data_time['directfit'].iloc[0],
                'Errortype':repr([x for x in temp_data_time['errortype']]),
                'Successe in the end':'Yes' if 'success' in [x for x in temp_data_time['errortype']] else 'No',
                'Use copyID':temp_copy,
                'Trigger sensor ID': temp_trigger,
                'Number':repr([x for x in temp_data_time['number']]),
                'InTire':repr([x for x in temp_data_time['inTire']]),
            }#
      
      
      
            #如果error type裡沒有13
            if ('13' not in [y.split('-')[0] for y in [z for z in temp_data_time['errortype']]]):
              #如果error type裡沒有13且最後沒有成功
              if ('success' not in [x for x in temp_data_time['errortype']]):#succes = F
                if (add_row_dict['Trigger sensor ID'] == 'No'):#trigger = F
                  temp_problem.append('without sensor')#如果error type沒有13與success，沒有使用trigger，則判斷為without sensor
                elif (add_row_dict['Trigger sensor ID'] != 'No'):#trigger = T
                  temp_problem.append('not OEC')#如果error type沒有13與success，有使用trigger，則判斷為not OEC
              #如果error type裡沒有13且最後有成功
              elif('success' in [x for x in temp_data_time['errortype']]):#succes = T
                if ((temp_data_time[temp_data_time.errortype == 'success'].iloc[-1])['number']) == '1':#最後一次燒入為單顆燒入
                  if ((temp_data_time[temp_data_time.errortype == 'success'].iloc[-1])['inTire']) == 'true':#InTire = T
                    temp_problem.append('program in tire')#如果error type有succes，單顆燒入，有壓力，則判斷為program in tire
                  elif ((temp_data_time[temp_data_time.errortype == 'success'].iloc[-1])['inTire']) == 'false':#InTire = F
                    temp_problem.append(judge_error(temp_data_time))#如果error type有succes，單顆燒入，無壓力，則用judge_error判斷
                elif ((temp_data_time[temp_data_time.errortype == 'success'].iloc[-1])['number']) != '1':#最後一次燒入為多顆燒入
                  temp_problem.append(judge_error(temp_data_time))#如果error type有succes，多顆燒入，則用以上函式judge_error判斷
            #如果error type裡有13
            elif ('13' in [y.split('-')[0] for y in [z for z in temp_data_time['errortype']]]):
              #如果error type裡有13且最後有成功
              if ('success' in [x for x in temp_data_time['errortype']]):
                if (['13', 'true'] in [[i.split('-')[0], j] for i, j in zip(eval(add_row_dict['Errortype']), eval(add_row_dict['InTire']))]):
                  temp_problem.append('program in tire')#如果error type是13和Inetire = true同時出現，判斷為program in tire
                else:
                  temp_problem.append('quit undercharge')#如果error type是13和Inetire = true沒有同時出現，判斷為quit undercharge
              #如果error type裡有13且最後沒有成功    
              elif('success' not in [x for x in temp_data_time['errortype']]):
                temp_problem.append(judge_error(temp_data_time))#如果如果error type裡有13且最後沒有成功,使用judge_error判斷
      

            add_row_dict['Problem'] = temp_problem
      
            #df = df.append(add_row_dict, ignore_index=True)
            df = pd.concat([df, pd.DataFrame([add_row_dict])], ignore_index=True)#將problem加入資料框架
    return df

def error_analysis_to_csv(api, date = datetime.date.today().strftime('%Y-%m-%d'), end_date = ''):#如果沒有填入date，則date取當日日期

    if os.path.isdir('錯誤分析表格') == False:#如果資料夾不存在，創建
        os.makedirs('錯誤分析表格/OG')
        os.makedirs('錯誤分析表格/OG2')
        os.makedirs('錯誤分析表格/OG3')
        os.makedirs('錯誤分析表格/OGlite')
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
            
            path = '錯誤分析表格/{}/error {}'.format(og, day_time)#存檔位置
            if not os.path.isdir(path):#如無存檔位置，創建
                os.mkdir(path)
                
            df = error_analysis(api, date = day_time, end_date = end_date, OG = og)#使用error_analysis產出錯誤分析後資料框架
            if type(df) == str:#如果當日無資料，也就是產出的錯誤分析資料型態非資料框架，跳過這次回圈，進入下次回圈
                continue
            
            df.to_csv('錯誤分析表格/{}/error {}/error {} {}.csv'.format(og, day_time, og, day_time), index = False)#將錯誤資料分析的資料框架儲存到設定的位置
    
    elif end_date != '':#多日輸出
        for og in OG:
            
            path = '錯誤分析表格/{}/error {} to {}'.format(og, day_time, end_date)#存檔位置
            if not os.path.isdir(path):#如無存檔位置，創建
                os.mkdir(path)
                
            df = error_analysis(api, date = day_time, end_date = end_date, OG = og)#使用error_analysis產出錯誤分析後資料框架
            if type(df) == str:#如果當日無資料，也就是產出的錯誤分析資料型態非資料框架，跳過這次回圈，進入下次回圈
                continue
            
            df.to_csv('錯誤分析表格/{}/error {} to {}/error {} {} to {}.csv'.format(og, day_time, end_date, og, day_time, end_date), index = False)#將錯誤資料分析的資料框架儲存到設定的位置
    
    return df
##############################################################################################

plt.rc('font', family='Microsoft JhengHei')

def stat_data(data):#整理原始資料的mode成功率

    if type(data) == str:#避免原始資料為空出現error
        return 'N'
    lst_directfit = list(set(data['directfit']))#建立directfit的所有類別
    df = pd.DataFrame({'Mode':[], 'Total':[], 'Sum PASS':[], 'Sum NG':[], 'Success RATE':[], 'Fail RATE':[]})#建立資料框架
    for i in lst_directfit:#遍歷所有directfit類別
        tp_row = data[data.directfit == i]#為第i個directfit的資料
        total = len(tp_row)#總次數
        sum_PASS = len(tp_row[tp_row.errortype == 'success'])#總成功次數
        sum_NG = len(tp_row[(tp_row.errortype != 11) & (tp_row.errortype != 'success')])#
        rate_success = round(sum_PASS*100/total, 2)#成功率
        rate_fail = round(sum_NG*100/total, 2)#失敗率
        stat_dict = {'Mode':i, 'Total':total, 'Sum PASS':sum_PASS, 'Sum NG':sum_NG, 'Success RATE':rate_success, 'Fail RATE':rate_fail}
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

def plot_to_png(api, date = datetime.date.today().strftime('%Y-%m-%d'), end_date = ''):
    
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
            da = load_data(api, data = 'program', date = day_time, OG = og)
            
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
            da = load_data(api, data = 'program', date = day_time, end_date = end_date, OG = og)
            
            if type(da) == str:#如果當日無資料，也就是產出的錯誤分析資料型態非資料框架，跳過這次回圈，進入下次回圈
                continue
            
            plot_failrate(da).savefig('統計圖表/{}/Chart {} to {}/{} to {} Failrate chart.png'.format(og, day_time, end_date, day_time, end_date))
            plot_total(da).savefig('統計圖表/{}/Chart {} to {}/{} to {} Total chart.png'.format(og, day_time, end_date, day_time, end_date))
            plot_failrate_total(da).savefig('統計圖表/{}/Chart {} to {}/{} to {} Failrate and Total chart.png'.format(og, day_time, end_date, day_time, end_date))
            plot_sum_error(da).savefig('統計圖表/{}/Chart {} to {}/{} to {} Sum error chart.png'.format(og, day_time, end_date, day_time, end_date))
    
        
