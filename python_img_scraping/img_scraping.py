import requests
from bs4 import BeautifulSoup
import urllib
from pathlib import Path
import uuid

output_folder=Path("dog")
output_folder.mkdir(exist_ok=True)

url="https://www.pref.osaka.lg.jp/doaicenter/doaicenter/"
response=requests.get(url)
soup=BeautifulSoup(response.content,"html.parser")

content=soup.find("div",attrs={"class":"site_free site_free2"})
images=content.find_all("img")

for image in images:
    long_image_url=urllib.parse.urljoin(url,image["src"])
    image_data=requests.get(long_image_url)
    with open(str("./dog/")+str(uuid.uuid4())+str(".jpeg"),"wb") as file:
        file.write(image_data.content)
