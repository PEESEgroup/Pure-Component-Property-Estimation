import numpy as np
import pickle
import pandas as pd
import numpy as np
from tqdm import tqdm
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

#Calculate MARE
def calc_MARE(ym, yp):
    RAE=[]
    pstd=np.std(ym)
    for i in range(0,len(ym)):
        if ym[i] <= 0.1 and ym[i] >= -0.1:
            RAE.append(abs(ym[i]-yp[i])/pstd*100)
        else:
            RAE.append(abs(ym[i]-yp[i])/abs(ym[i]+0.000001)*100)
    mare=np.median(RAE)
    return mare

models =['LogP', 'LD50', 'LogWs', 'AiT', 'Tm', 'Tb',
         'Omega', 'pKa', 'HSolP', 'Hf', 'Lmv', 'Delta_D', 'Delta_H',
         'Delta_P', 'Tc', 'Pc', 'Vc', 'Gf', 'Hfus', 'LC50(FM)',
        'PCO', 'BCF', 'Fp', 'Hv', 'OSHA-TWA']

xls = pd.ExcelFile('Full Results.xlsx')

name=[]; N=[]; v=[]; r2simple=[]; RMSEsimple=[]; r2ML_rep=[];r2ML_model=[];
MARE=[]; RMSEML_rep=[] ;RMSEML_model=[] ; MCL=[]

for i in range(0,len(models)):
    print(models[i])
    model = pickle.load(open('./models/' + models[i] + '.sav', 'rb'))
    df=pd.read_excel(xls, models[i])
    X_data=df.iloc[:,-424:]
    ymodel=model.predict(X_data)
    name.append(models[i])
    N.append(len(df))
    v.append(len(df)-(425-len(df.columns[(df == 0).all()])))
    #Calculate R2 for simple models
    r2simple.append(round(r2_score(df['Experimental'], df['GC-Simple Prediction']),3))
    #Calculate R2 for ML models
    r2ML_model.append(round(r2_score(df['Experimental'], ymodel),3))
    #Calculate RMSE for simple models
    RMSEsimple.append(mean_squared_error(df['Experimental'], df['GC-Simple Prediction'], squared=False))
    #Calculate RMSE for ML models
    RMSEML_model.append(mean_squared_error(df['Experimental'], ymodel, squared=False))
    #Calculate MCL for ML models
    MCL.append(np.median(1.960*(df['GC-ML Uncertainty']/np.sqrt(len(df)))))
    #Calculate MARE for ML models
    MARE.append(calc_MARE(df['Experimental'], ymodel))

evals = pd.DataFrame(list(zip(name, N,v,r2simple,RMSEsimple, r2ML_rep,r2ML_model , MARE, RMSEML_rep, RMSEML_model, MCL )),columns =['Name', 'M', 'v', 'R2-Simple', 'RMSE-Simple', 'R2-ML-results','R2-ML-model' , 'MARE', 'RMSE-ML-results', 'RMSE-ML-model','MCL'])
evals.to_csv('Evalutions.csv',index=False)