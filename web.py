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
def worldcup():
    return render_template("world3.html")




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


 





