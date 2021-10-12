from flask import Flask,render_template,request,redirect,url_for
import matplotlib.pyplot as plt
import pandas as pd
import time
import platform 
from pyarrow import NullType, csv

app = Flask(__name__)

@app.route('/s',methods = ['GET', 'POST'])
def test3():
  
    return render_template("sulmoon.html")



@app.route('/wc',methods = ['GET', 'POST'])
def tes():
  
    return render_template("worldcup.html")



def cal(name,arr,dfarr):
    sum=0
    total=0
    for i in range (4):
        df=dfarr[i]
        sum+=float(df[name])*arr[i]
        total+=arr[i]
    
    return sum/total



@app.route('/w',methods = ['GET', 'POST'])
def test2():
    if request.method=='POST':
        try:
            arr=[]


            for i in range(16):
                a='tag'+str(i+1)
                arr.append(int(request.form[a]))


            df=seoul_total()

            df1 = df[df['구'].str.contains('강남구')]
            df2 = df[df['구'].str.contains('강동구')]
            df3 = df[df['구'].str.contains('강북구')]
            df4 = df[df['구'].str.contains('강서구')]


            dfarr=[df1,df2,df3,df4]

            #df1['건강']*arr[0]+df1['건강']*arr[1]+df1['건강']*arr[2]+df1['건강']*arr[3]

            health=cal('건강',arr,dfarr)
            edu=cal('교육',arr,dfarr)
            com=cal('상권',arr,dfarr)
            life=cal('생활',arr,dfarr)
            sport=cal('스포츠',arr,dfarr)
            safe=cal('안전',arr,dfarr)
            leisure=cal('여가',arr,dfarr)
            gym=cal('체육',arr,dfarr)
            eco=cal('환경',arr,dfarr)
            
            
            

            return render_template("mainpage2.html",score=[round(health,1),round(edu,1)
            ,round(com,1),round(life,1),round(sport,1),round(safe,1),round(leisure,1),round(gym,1),round(eco,1)])
            #return render_template("mainpage2.html",ran1=round(health,1), ran2=round(edu,1),
            #ran3=round(com,1),ran4=round(life,1),ran5=round(sport,1),ran6=round(safe,1),ran7=round(leisure,1),ran8=round(gym,1),ran9=round(eco,1))

        except:
            r1=int(request.form['ran1'])/100
            r2=int(request.form['ran2'])/100
            r3=int(request.form['ran3'])/100
            r4=int(request.form['ran4'])/100
            r5=int(request.form['ran5'])/100
            r6=int(request.form['ran6'])/100
            r7=int(request.form['ran7'])/100
            r8=int(request.form['ran8'])/100
            r9=int(request.form['ran9'])/100
            r10=int(request.form['ran10'])/100
                
            df=seoul_total()
            
            df['종합'] = ''        
            df['종합']=(df['건강']*r1+df['교육']*r2+df['상권']*r3+df['생활']*r4+df['스포츠']*r5+df['안전']*r6+df['여가']*r7+df['체육']*r8+df['환경']*r9+df['집값']*r10)/(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10)
            df['종합']=round(df['종합'],3)
            df3 = df.sort_values(by='종합',ascending=False)
            df3 = df3.reset_index(drop=True)

            
            return render_template("mainpage2.html",rank1=list(df3['구']),rank2=list(df3['종합']),dff=df3)
    
  
    return render_template("world2.html")



@app.route('/map',methods = ['GET', 'POST'])
def test():
  
    return render_template("Seoul_Population.html")





@app.route('/',methods = ['GET', 'POST'])
def search():
    if request.method=='POST':

       
        r1=int(request.form['ran1'])/100
        r2=int(request.form['ran2'])/100
        r3=int(request.form['ran3'])/100
        r4=int(request.form['ran4'])/100
        r5=int(request.form['ran5'])/100
        r6=int(request.form['ran6'])/100
        r7=int(request.form['ran7'])/100
        r8=int(request.form['ran8'])/100
        r9=int(request.form['ran9'])/100
        r10=int(request.form['ran10'])/100

               
        df=seoul_total()
        
        df['종합'] = ''        
        df['종합']=(df['건강']*r1+df['교육']*r2+df['상권']*r3+df['생활']*r4+df['스포츠']*r5+df['안전']*r6+df['여가']*r7+df['체육']*r8+df['환경']*r9+df['집값']*r10)/(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10)
        df['종합']=round(df['종합'],3)
        df3 = df.sort_values(by='종합',ascending=False)
        df3 = df3.reset_index(drop=True)

        
        return render_template("mainpage2.html",rank1=list(df3['구']),rank2=list(df3['종합']),dff=df3)

    
       

    
    return render_template("mainpage2.html")


@app.route('/ss',methods = ['GET', 'POST'])
def search2():
    
         
        r1=1
        r2=1
        r3=1
        r4=1
        r5=1
        r6=1
        r7=1
        r8=1
        r9=1

               
        df=seoul_total()
        
        df['종합'] = ''        
        df['종합']=(df['건강']*r1+df['교육']*r2+df['상권']*r3+df['생활']*r4+df['스포츠']*r5+df['안전']*r6+df['여가']*r7+df['체육']*r8+df['환경']*r9)/(r1+r2+r3+r4+r5+r6+r7+r8+r9)
        df3 = df.sort_values(by='종합',ascending=False)
        df3 = df3.reset_index(drop=True)

        dic = {'구':list(df3['구']), '종합':list(df3['종합'])}

        #return render_template("mainpage3.html",tables=df3.to_html())
        return render_template("mainpage3.html",rank1=list(df3['구']),rank2=list(df3['종합']),rank3=dic )  

    

def seoul_total():
    df = csv.read_csv('static\data\서울종합2.csv').to_pandas()
    return df





