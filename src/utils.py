from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import json

baseurl = "https://www.kompas.com/ramadhan/jadwal-imsakiyah"

def getdaerah() -> list:
    try:
        page = get("{}/kota-bogor".format(baseurl))
        soup = BeautifulSoup(page.text,"lxml")

        """
        <select class="js-imsak" name="state" onchange="load_jadwal_widget(this)" style="width: 100%">
        <option value="kab-aceh-barat">KAB. ACEH BARAT</option>
        """

        options = soup.find("select",{"name":"state"}).findAll("option")
        daerah = []
        for i in options:
            nama = i.text
            link = i["value"]
            
            daerah.append({
                "nama": nama,
                "daerah": link
            })
        return daerah
    except:
        return None

def getdata(daerah):
    try:
        df = pd.read_html("{}/{}".format(baseurl,daerah))
        df = df[0].to_json(orient="records")
        data = json.loads(df)
        return data
    except:
        return None
