from flask import Flask,render_template,request,redirect,url_for
import matplotlib.pyplot as plt
import pandas as pd
import time
import platform
import random
from pyarrow import NullType, csv
from find import find_city

app = Flask(__name__)

def korea_total():
    df = csv.read_csv('static\data2\최종22.csv').to_pandas()
    return df

def cal(name,arr,dfarr):
    sum=0
    total=0
    for i in range (25):
        if(arr[i]==0):
            continue
        df=dfarr[i]
        sum+=float(df[name])*arr[i]
        total+=arr[i]
    
    return sum/total



@app.route('/w',methods = ['GET', 'POST'])
def test2():
    if request.method=='POST':
        try:
            arr=[]


            for i in range(25):
                a='tag'+str(i+1)
                arr.append(int(request.form[a])) #점수기록


            df=korea_total()

            df1 = df[df['시도'].str.contains('강남구')]
            df2 = df[df['시도'].str.contains('강동구')]
            df3 = df[df['시도'].str.contains('강북구')]
            df4 = df[df['시도'].str.contains('강서구')]

            df5 = df[df['시도'].str.contains('관악구')]
            df6 = df[df['시도'].str.contains('광진구')]
            df7 = df[df['시도'].str.contains('구로구')]
            df8 = df[df['시도'].str.contains('금천구')]

            df9 = df[df['시도'].str.contains('노원구')]
            df10 = df[df['시도'].str.contains('도봉구')]
            df11 = df[df['시도'].str.contains('동대문구')]
            df12 = df[df['시도'].str.contains('동작구')]

            df13 = df[df['시도'].str.contains('마포구')]
            df14 = df[df['시도'].str.contains('서대문구')]
            df15 = df[df['시도'].str.contains('서초구')]
            df16 = df[df['시도'].str.contains('성동구')]

            df17 = df[df['시도'].str.contains('성북구')]
            df18 = df[df['시도'].str.contains('송파구')]
            df19 = df[df['시도'].str.contains('양천구')]
            df20 = df[df['시도'].str.contains('영등포구')]

           
            df21 = df[df['시도'].str.contains('용산구')]
            df22 = df[df['시도'].str.contains('은평구')]
            df23 = df[df['시도'].str.contains('종로구')]
            df24 = df[df['시도'].str.contains('서울특별시 중구')]

            df25 = df[df['시도'].str.contains('중랑구')]


            dfarr=[df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22,df23,df24,df25]
           


            safe=cal('안전',arr,dfarr)
            health=cal('건강',arr,dfarr)
            eco=cal('환경',arr,dfarr)
            economy=cal('경제',arr,dfarr)
            edu=cal('교육',arr,dfarr)
            social=cal('사회',arr,dfarr)
            leisure=cal('여가',arr,dfarr)
            
            
            
            
            

            return render_template("mainpage2.html",score=[round(health,1)*100,round(edu,1)*100
            ,round(economy,1)*100,round(social,1)*100,round(safe,1)*100,round(leisure,1)*100,round(eco,1)*100])
            
            

        except:
            r1=int(request.form['ran1'])/100
            r2=int(request.form['ran2'])/100
            r3=int(request.form['ran3'])/100
            r4=int(request.form['ran4'])/100
            r5=int(request.form['ran5'])/100
            r6=int(request.form['ran6'])/100
            r7=int(request.form['ran7'])/100
        


            df=korea_total()
            
            df['종합'] = ''        
            df['종합']=(df['안전']*r1+df['건강']*r2+df['환경']*r3+df['경제']*r4+df['교육']*r5+df['사회']*r6+df['여가']*r7)/(r1+r2+r3+r4+r5+r6+r7)
            df['종합']=round(df['종합'],3)
            df['집값']=round(df['아파트매매가'])
            df3 = df.sort_values(by='종합',ascending=False)
            df3 = df3.reset_index(drop=True)

        
            return render_template("mainpage2.html",rank1=list(df3['시도']),rank2=list(df3['종합']),rank3=list(df3['집값']))
    
  
    return render_template("world2.html")



@app.route('/map',methods = ['GET', 'POST'])
def test():
    return render_template("Seoul_Population.html")





@app.route('/',methods = ['GET', 'POST'])
def search():
    if request.method=='POST':
        temp = request.form.get("recom_btn")
        if temp == "추천해줘":
            r1=int(request.form['ran1'])/100
            r2=int(request.form['ran2'])/100
            r3=int(request.form['ran3'])/100
            r4=int(request.form['ran4'])/100
            r5=int(request.form['ran5'])/100
            r6=int(request.form['ran6'])/100
            r7=int(request.form['ran7'])/100
            
            #df=seoul_total()
            df=korea_total()
        
            df['종합'] = ''        
            df['종합']=(df['안전']*r1+df['건강']*r2+df['환경']*r3+df['경제']*r4+df['교육']*r5+df['사회']*r6+df['여가']*r7)/(r1+r2+r3+r4+r5+r6+r7)
            df['종합']=round(df['종합'],3)
            df['집값']=round(df['아파트매매가'])
            df3 = df.sort_values(by='종합',ascending=False)
            df3 = df3.reset_index(drop=True)

        
            return render_template("mainpage2.html",rank1=list(df3['시도']),rank2=list(df3['종합']),rank3=list(df3['집값']))
        elif temp=="검색":
            name = request.form['search']
            tier1,tier2,tier3,tier1_price,tier2_price,tier3_price = find_city(name)
            return render_template("mainpage2.html",tier1=tier1,tier2=tier2,tier3=tier3,tier1_price=tier1_price,tier2_price=tier2_price,tier3_price=tier3_price,zip=zip)
    
       

    
    return render_template("mainpage2.html")

@app.route('/ajax',methods = ['GET'])
def ajax():
    data = korea_total()
    d1 = random.randrange(0, 229)
    while (True):
        d2 = random.randrange(0, 229)
        if data.iloc[d1]['군집'] == data.iloc[d2]['군집']:
            d2 = random.randrange(0, 229)
        else:
            break

    d = data.iloc[[d1,d2]].drop(['집값','군집','아파트매매가'], axis=1)
    d.loc[:, '안전':'행복역량지수'] = 5 * d.loc[:, '안전': '행복역량지수']
    d = d.to_json(orient='split')

    return d


@app.route('/ajaxtest')
def ajaxtest():
    return render_template("world3.html")


 





