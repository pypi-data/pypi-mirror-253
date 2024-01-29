import re
from datetime import datetime
import pandas as pd

class CIMB:
  def __init__(self):
    self.monthData = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]

  def extract(self,df):
    return self.CIMB_table_spliting(df)

  def deleteCIMBdetail(self,x):
    try:
      data = x.index("PT Bank CIMB Niaga")
      return x[:data]
    except:
      return x

  def CIMB_table_spliting(self,df):
    df = df[1]
    dtlist = {
        "INDEX":[],
        "BULAN_TAHUN":[],
        "TANGGAL":[],
        "KETERANGAN":[],
        "STATUS":[],
        "AMMOUNT":[],
        "SALDO":[]
    }
    index = 0
    for er in df:
        data = re.findall(r"(\d\d\d\d\-\d\d\-\d\d)\s+(.*)",er[0])[0]
        tahun,bulan = data[0].split('-')[:2]
        bulan = self.monthData[int(bulan)-1]

        dtlist['INDEX'].append(index)
        dtlist['TANGGAL'].append(data[0])
        dtlist['BULAN_TAHUN'].append(bulan+' '+tahun)
        dtlist['KETERANGAN'].append(data[1])

        data = er[1].strip().split(' ')
        if len(data[0])>1:
            if '-' in data[0]:
                data = ['-']+[data[0].replace('-','')]+[data[1]]
            else:
                data = ['+']+[data[0].replace('+','')]+[data[1]]

        if data[0]=='-':
            dtlist['STATUS'].append('CREDIT')
            dtlist['AMMOUNT'].append(data[1].replace(',','').strip())
        else:
            dtlist['STATUS'].append('DEBIT')
            dtlist['AMMOUNT'].append(data[1].replace(',','').strip())
        dtlist['SALDO'].append(data[2].replace(',','').strip())

        index+=1

    df = pd.DataFrame.from_dict(dtlist)
    df['AMMOUNT'] = df['AMMOUNT'].astype(float)
    df['SALDO']   = df['SALDO'].astype(float)

    df['KETERANGAN'] = df['KETERANGAN'].apply(self.deleteCIMBdetail)

    return df
  
class CIMB_Credit:
  def __init__(self):
    self.monthData = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]

  def extract(self,df):
    return self.CIMB_Credit_table_spliting(df)

  def CIMB_Credit_table_spliting(self,df):
    tahun = re.findall('\d{2}\s+[A-Z]{3}\s+(\d\d\d\d)',df[0].replace("_CREDIT",""))[0]

    df = df[1]
    dtlist = []

    lastSaldo = 0
    for index,er in enumerate(df):
      tanggal    = None
      keterangan = None
      ammount    = None
      saldo      = None
      status     = None

      tanggal     = re.findall('\d\d\/\d\d',er[0])[0]
      keterangan  = er[0].replace(tanggal,'').strip()

      tanggal     = tanggal.replace('/','')

      uang_kas    = er[1].replace(",","").replace(".","").strip().split(' ')
      try:
        uang_kas.remove('')
      except:
        pass

      if "_CREDIT" in uang_kas[0]:
        status       = 'CREDIT'
        uang_kas[0]  = uang_kas[0].replace('_CREDIT','')
      else:
        status = 'DEBIT'

      print(uang_kas)
      ammount = float(uang_kas[0])/100
      saldo   = float(uang_kas[1].replace('_CREDIT',''))/100

      bulan_tahun   = f"{self.monthData[int(tanggal[2:])-1]} {tahun}"
      tanggal       = f"{tahun}-{tanggal[2:]}-{tanggal[:2]}"

      dtlist.append({
        'INDEX' :index,
        'BULAN_TAHUN':bulan_tahun,
        'TANGGAL' : tanggal,
        'KETERANGAN' : keterangan,
        'STATUS' : status,
        'AMMOUNT' : ammount,
        'SALDO' : saldo,
      })

    df = pd.DataFrame.from_dict(dtlist)
    return df