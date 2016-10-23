import pandas as pd

b1=pd.read_csv("Editbenign3/benign_2013_2_1.csv")

b1['crmf']=(b1['crmf']/b1['totaledit'])*100
b1['crms']=(b1['crms']/b1['totaledit'])*100
b1['crmv']=(b1['crmv']/b1['totaledit'])*100
b1['crnf']=(b1['crnf']/b1['totaledit'])*100
b1['crns']=(b1['crns']/b1['totaledit'])*100
b1['crnv']=(b1['crnv']/b1['totaledit'])*100
b1['crf_crv']=(b1['crf_crv']/b1['totaledit'])*100
b1['ntus']=(b1['ntus']/b1['totaledit'])*100
b1['crm']=(b1['crm']/b1['totaledit'])*100
b1['crn']=(b1['crn']/b1['totaledit'])*100
b1['nts_nts']=(b1['nts_nts']/b1['totaledit'])*100
b1.to_csv('Editbenign4/benign_13_2_1.csv',index=False, encoding='utf-8')

b1=pd.read_csv("Editbenign3/vandal_2013_2.csv")
b1['crmf']=(b1['crmf']/b1['totaledit'])*100
b1['crms']=(b1['crms']/b1['totaledit'])*100
b1['crmv']=(b1['crmv']/b1['totaledit'])*100
b1['crnf']=(b1['crnf']/b1['totaledit'])*100
b1['crns']=(b1['crns']/b1['totaledit'])*100
b1['crnv']=(b1['crnv']/b1['totaledit'])*100
b1['crf_crv']=(b1['crf_crv']/b1['totaledit'])*100
b1['ntus']=(b1['ntus']/b1['totaledit'])*100
b1['crm']=(b1['crm']/b1['totaledit'])*100
b1['crn']=(b1['crn']/b1['totaledit'])*100
b1['nts_nts']=(b1['nts_nts']/b1['totaledit'])*100

b1.to_csv('Editbenign4/vandal_13_2_1.csv',index=False, encoding='utf-8')
