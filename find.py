from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def manhattan_distance(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))

def find_city(name):
    arr = np.zeros(229)
    df1 = pd.read_csv('static/data2/최종22.csv',encoding='utf-8')

    lists_of_city = df1['시도'].tolist()
    lists_of_proce = df1['아파트매매가'].tolist()
    select_index=lists_of_city.index(name)

    df2=df1.drop(columns=['행복역량지수','시도','집값','군집','아파트매매가'], axis=1)

    for i in range(0,len(lists_of_city)):
        if i != select_index:
            temp1 = df2.iloc[select_index].tolist()
            temp2 = df2.iloc[i].tolist()
            simm=manhattan_distance(temp1,temp2)
            arr[i] = simm

        
    from_name_to_here=arr.tolist()

    df2['Manhatan_Distance']=from_name_to_here;
    df2['아파트매매가']=lists_of_proce;
    df2.insert(0,'시도',lists_of_city)
    df2=df2.sort_values(by=['Manhatan_Distance'],axis=0,ascending=True)

    df3 = df2.iloc[1:11]
    
    df3=df3.sort_values(by=['아파트매매가'],axis=0,ascending=True)

    df3['price_class']=pd.cut(df3['아파트매매가'], 3, labels=['tier1', 'tier2', 'tier3'])
    df3=df3.drop(columns=['안전','건강','환경','경제','교육','사회','여가','Manhatan_Distance'], axis=1)
    condition1 = df3['price_class'] == "tier1"
    condition2 = df3['price_class'] == "tier2"
    condition3 = df3['price_class'] == "tier3"
    df3=df3.drop(columns=['price_class'], axis=1)

    lists_of_tier1 = df3[condition1].시도.tolist();
    lists_of_tier2 = df3[condition2].시도.tolist();
    lists_of_tier3 = df3[condition3].시도.tolist();
    lists_of_tier1_price = df3[condition1].아파트매매가.tolist();
    lists_of_tier2_price = df3[condition2].아파트매매가.tolist();
    lists_of_tier3_price = df3[condition3].아파트매매가.tolist();
    return lists_of_tier1,lists_of_tier2,lists_of_tier3 ,lists_of_tier1_price ,lists_of_tier2_price , lists_of_tier3_price