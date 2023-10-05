import time #寫入系統現在時間
import unittest  #單元測試
import csv  #編輯csv及寫入csv
import os   #os 開啟檢視檔案
#匯入需要的套件


class people: # 定義一個人物類別（people），用於處理個人資訊和相關操作

    
    #初始化副程式
    def __init__(self, name, age, height, weight, sex):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = sex
    #建立方法用於取得系統現在時間
    def test_gettimenow(self):
        return time.strftime("%Y-%m-%d %H:%M", time.localtime())
    #建立方法用於BMI計算、結果回傳
    def bmi(self):
        return self.weight / ((self.height / 100) * (self.height / 100))
    #建立方法用於寫入csv中
    def writercsv(self):
        if os.path.exists('健康管理表單.csv'): #判斷檔案是否存在
            print('文件已存在，寫入檔案中')   #存在則印出該行
        else:
            with open('健康管理表單.csv', 'a') as file:  #不存在則建立 'a' 是續寫 
                writer = csv.writer(file)     #建立一個變數用來當作csv編輯器
                writer.writerow(['姓名', '年齡', '身高', '體重', '性別', 'BMI', '時間']) #寫入標題
                print('創建成功')

        time_now = self.test_gettimenow() #把上面獲取時間的方法存到變數中以便等等寫入csv
        BMI = round(self.bmi(), 2)        #把上面獲取bmi的方法也同樣存到變數中以便寫入csv

        with open('健康管理表單.csv', 'a') as file:  #打開檔案 這邊的'a' 一樣是續寫  用'w' 則是覆蓋 會直接覆蓋掉之前所存入的資料 
            writer = csv.writer(file)      #同上面要建立一個變數來當作csv編輯器 (在if 迴圈外面吃不到==)
            writer.writerow([self.name, self.age, self.height, self.weight, self.sex, BMI, time_now]) #要寫入的變數
            print('寫入檔案完成')


if __name__ == "__main__":  #主程式的進入點
    #讓使用者輸入個人資訊
    name = input("請輸入姓名")
    age_input = input("請輸入年齡")
    height_input = input("請輸入身高")
    weight_input = input("請輸入體重")
    sex = input("請輸入性別")
    
    #BMI的計算不能用字串，所以下面轉成浮點數
    age = int(age_input)
    height = float(height_input)
    weight = float(weight_input)


    # 創建人物類別的實例
    peoples = people(name, age, height, weight, sex)

    # 呼叫寫入CSV檔案的方法
    peoples.writercsv()


    



        
    

    
    
    

# inputlist=[]

# name = input("請輸入姓名")
# age_input = input("請輸入年齡")
# height_input = input("請輸入身高")
# weight_input = input("請輸入體重")
# sex = input("請輸入性別")

# inputlist=[name,age_input,height_input,weight_input,sex]

# while inputlist != [] :
#     print("寫入檔案中")
#     inputlist.clear()



# age = int(age_input)
# height = float(height_input)
# weight = float(weight_input)


# peoples = people(name,age,height,weight,sex)
# time_now = peoples.test_gettimenow()
# BMI = round(peoples.bmi(),2)
# print(f'現在時間是:{time_now}')
# print(f'您的BMI為:{BMI}')



# if os.path.exists('健康管理表單.csv'):
#     print('文件已存在寫入檔案中')

# else:
#     with open ('健康管理表單.csv','a')as file:
#         writer = csv.writer(file)
#         writer.writerow(['姓名','年齡','身高','體重','性別','BMI','時間'])
#         print('創建成功')

# with open('健康管理表單.csv','a')as file:
#     writer = csv.writer(file)
#     writer.writerow([name,age,height,weight,sex,BMI,time_now])
#     print('寫入檔案完成')


