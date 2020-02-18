import requests
from bs4 import BeautifulSoup
import urllib.request
import mysql.connector
from sys import argv
import re

sayac=0
while True:
  #f=open('butuncihazlar.txt')
  #lines = f.readlines()
  #url = lines[sayac]
  headers = {'User-Agent': 'Mozilla/5.0'}
  url = "https://www.kimovil.com/en/where-to-buy-motorola-one-action"
  #sayac+=1
  url_oku = requests.get(url, headers=headers)
  html_content = url_oku.text
  soup = BeautifulSoup(html_content,'html.parser')
   
  for child in soup.find_all("a", {"class":"foward-link"}):
    child.decompose()
  for child in soup.find_all("a", {"class":"more-like"}):
    child.decompose()	
  for child in soup.find_all("ul"):
    child.decompose()
  for child in soup.find_all("li"):
    child.decompose()
  for child in soup.find_all("span", {"class":"mini-help"}):
   child.decompose()
  for child in soup.find_all("div", {"class":"color-circle"}):
   child.decompose()
  for child in soup.find_all("div", {"class":"row user-opinion-questions"}):
   child.decompose()   
  for child in soup.find_all("ul", {"class":"dd-device-list"}):
   child.decompose()   
  for child in soup.find_all("dd", {"class":"sep origami"}):
   child.decompose()    
  for child in soup.find_all("p", {"class":"help chide"}):
   child.decompose()  
  for child in soup.find_all("p", {"class":"chide help"}):
   child.decompose()  
  for child in soup.find_all("p", {"class":"help"}):
   child.decompose() 
  for child in soup.find_all("div", {"class":"thumb-list clear"}):
   child.decompose()
  for child in soup.find_all("div", {"class":"video-list clear"}):
   child.decompose()
  for child in soup.find_all("div", {"class":"dxomark-score"}):
   child.decompose() 
  for child in soup.find_all("section", {"id":"commonly-compared"}):
   child.decompose() 
  for child in soup.find_all("section", {"class":"section clear"}):
   child.decompose() 
  for child in soup.find_all("div", {"id":"error_report"}):
   child.decompose()   
  for child in soup.find_all("div", {"id":"price_report"}):
   child.decompose()     
  for child in soup.find_all("br"):
   child.string = child.text.strip()
   
  for child in soup.find_all("dt"):
   child.string = 'altsatirBBasliKK'+child.text.strip()+'altsatir' 
   
  for child in soup.find_all("h3"):
   child.string = 'altsatirBKiB'+child.text.strip()+'altsatir'    
   
  cihazyazilacak = soup.find('h1',{'class' : 'k-h1'}).text
  modelname = cihazyazilacak.replace("Price and specifications on ","")
   
  cihazyazilacak = soup.find_all(["dt", "h3", "dd"])
  cihazexport = open("cihaz1.txt", "wb")
  cihazexport.write(str(cihazyazilacak).encode('utf-8'))
  cihazexport.close()

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<dd>\n</dd>', '<dd>null</dd>')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)    
  
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</dt>, ', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)   

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</dd>, ', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)   

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</dt>, ', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)  	
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('[<dt>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata) 
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</dd>]', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)   

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<span class="item"> </span>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<span class="item">', '</br>')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</dt>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</dd>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)   
  
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<dd class="sep">', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)    

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<dt>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<dd>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata) 
 
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<dd class="column-dd sep">', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata) 

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<dt class="br">', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata) 

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<dt class="chide">', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata) 

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<dd class="chide column-dd sep">', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata) 

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('DxOMark Score', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata) 
	
  fh = open("cihaz1.txt", "r", encoding="utf-8")
  lines = fh.readlines()
  fh.close()
  lines = filter(lambda x: not x.isspace(), lines)
  fh = open("cihaz1.txt", "w", encoding="utf-8")
  fh.write("".join(lines).strip())
  fh.close()
 
  f=open('cihaz1.txt', encoding="utf-8")
  lines = f.readlines()
  k=0
  kk=1
  cihazexport = open("cihaz1.txt", "wb")
  
  try:
    for line in lines:
      with open('cihaz1.txt', 'r', encoding="utf-8") as file:
        filedata = file.read()
      linesk = lines[k].strip()
      lineskk = lines[kk].strip()
      filedata =  linesk + lineskk
      with open('cihaz1.txt', 'a', encoding="utf-8") as file:
       file.write(filedata.strip()) 
      k+=2
      kk+=2
  except:
    pass
 
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('altsatir', '\n')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip()) 
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('Predecessor', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)   
 
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('Successors', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)  
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('Origami', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata) 
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<span>, </span>', ', ')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata) 	

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('  ', ' ')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata) 

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<div class="sub">', ' ')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata) 

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = re.sub(r'<div class="color-sep .*?">', '', filedata)
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip())

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</div>', ',')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<div style="position: relative; margin-right: -25px;">', ',')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<p><small>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</small></p>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<br></br>', '<br />')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</br>', '<br />')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)	

  feat=0
  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  for line in lines:
       if line.strip() != "Others":
            mynewtext.append(line)
       else:
            mynewtext.append("Others"+str(feat)+"\n")
            feat+=1
  with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)

  feat=0
  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  for line in lines:
       if line.strip() != "BKiBOthers":
            mynewtext.append(line)
       else:
            mynewtext.append("BKiBOthers"+str(feat)+"\n")
            feat+=1
  with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)
			
  fh = open("cihaz1.txt", "r", encoding="utf-8")
  lines = fh.readlines()
  fh.close()
  lines = filter(lambda x: not x.isspace(), lines)
  fh = open("cihaz1.txt", "w", encoding="utf-8")
  fh.write("".join(lines).strip())
  fh.close()
 
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('[<h3 class="k-h4">', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</h3>,', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('<h3 class="k-h4">', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = re.sub(r'<h3 class="k-h4" id="sec-.*?">', '', filedata)
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata.strip())

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('</h3>', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('BKiBDescription', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('BKiBRelated', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('BKiBPhotos', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)

  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('BKiBSuccessors', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)
	
  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('--', 'null')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)
	
  fh = open("cihaz1.txt", "r", encoding="utf-8")
  lines = fh.readlines()
  fh.close()
  lines = filter(lambda x: not x.isspace(), lines)
  fh = open("cihaz1.txt", "w", encoding="utf-8")
  fh.write("".join(lines).strip())
  fh.close()
  
  k=0
  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  try:
    for line in lines:
      linestl = lines[k].strip()
      if (linestl[-1:] == ","):
         mynewtext.append(linestl[:-1]+"\n")		 
      else:
            mynewtext.append(line)
      k+=1
    with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)
  except:
    with open("cihaz1.txt","w", encoding="utf-8") as text:
      for i in mynewtext:
        text.write(i)
      text.write(linestl)
    pass

  k=0
  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  try:
    for line in lines:
      linestl = lines[k].strip()
      if (linestl[:6] == "<br />"):
         mynewtext.append(linestl[6:]+"\n")		 
      else:
            mynewtext.append(line)
      k+=1
    with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)
  except:
    with open("cihaz1.txt","w", encoding="utf-8") as text:
      for i in mynewtext:
        text.write(i)
      text.write(linestl)
    pass


  k=0
  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  try:
    for line in lines:
      linestl = lines[k].strip()
      if ("<span>" not in linestl):
         mynewtext.append(linestl.replace("</span>","")+"\n")		 
      else:
            mynewtext.append(line)
      k+=1
    with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)
  except:
    with open("cihaz1.txt","w", encoding="utf-8") as text:
      for i in mynewtext:
        text.write(i)
      text.write(linestl)
    pass

  fh = open("cihaz1.txt", "r", encoding="utf-8")
  lines = fh.readlines()
  fh.close()
  lines = filter(lambda x: not x.isspace(), lines)
  fh = open("cihaz1.txt", "w", encoding="utf-8")
  fh.write("".join(lines).strip())
  fh.close()

  k=0
  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  try:
    for line in lines:
      linestl = lines[k].strip()
      if (linestl == "BBasliKK"):
         pass
      else:
            mynewtext.append(line)
      k+=1
    with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)
  except:
    with open("cihaz1.txt","w", encoding="utf-8") as text:
      for i in mynewtext:
        text.write(i)
      text.write(linestl)
    pass 
	

  k=0
  kk=1
  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  try:
    for line in lines:
      linestl = lines[k].strip()
      linestlk = lines[kk].strip()
      if (linestl[:8] == "BBasliKK" and linestlk[:4] == "BKiB"):
         pass        
      else:
            mynewtext.append(line)
      k+=1
      kk+=1
    with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)
  except:
    with open("cihaz1.txt","w", encoding="utf-8") as text:
      for i in mynewtext:
        text.write(i)
      text.write(linestl)
    pass	
	
  k=0
  with open("cihaz1.txt", "r", encoding="utf-8") as text:
       lines=text.readlines()
  mynewtext=[]
  try:
    for line in lines:
      linestl = lines[k].strip()
      if (linestl[:4] == "BKiB"):
         baslik = linestl[4:]
      elif (linestl[:8] == "BBasliKK"):
        mynewtext.append(baslik.replace(" ","")+linestl[8:]+"\n")
      else:
            mynewtext.append(line)
      k+=1
    with open("cihaz1.txt","w", encoding="utf-8") as text:
       for i in mynewtext:
            text.write(i)
  except:
    with open("cihaz1.txt","w", encoding="utf-8") as text:
      for i in mynewtext:
        text.write(i)
      text.write(linestl)
    pass 


  with open('cihaz1.txt', 'r', encoding="utf-8") as file :
    filedata = file.read()
  filedata = filedata.replace('ScreenOthers', '')
  with open('cihaz1.txt', 'w', encoding="utf-8") as file:
    file.write(filedata)
	
  fh = open("cihaz1.txt", "r", encoding="utf-8")
  lines = fh.readlines()
  fh.close()
  lines = filter(lambda x: not x.isspace(), lines)
  fh = open("cihaz1.txt", "w", encoding="utf-8")
  fh.write("".join(lines).strip())
  fh.close()
	
  f=open('cihaz1.txt' , encoding="utf-8")
  lines = f.readlines()
  cnx = mysql.connector.connect(host='localhost',user='root',password='',database='phonedb', charset='utf8')
  cursor = cnx.cursor()
  eklemodel = (modelname.replace("'","").replace(":","").strip())
  modelname = eklemodel
  newmodelname = re.sub(r'.*?.\(', '', modelname)
  if(newmodelname == modelname):
    outmodelname = modelname.replace(" ","")
  else:
    newmodelname = newmodelname.replace(")","")
    try:
      if (int(newmodelname) >= 2010):
         outmodelname = modelname.replace("(","").replace(")","").replace(" ","")  
      else:
         outmodelname = modelname
         outmodelname = outmodelname.replace(" ","")	   
    except:
      outmodelname = modelname
      outmodelname = outmodelname.replace(" ","")     
  # try:
    # cursor.execute("INSERT INTO kimovil (Modelname) VALUES (%s)", (eklemodel, ))
  # except:
    # print("Bu cihaz zaten mevcut! Güncellendi!")
    # pass  
  cnx.commit()
  i=0
  j=1
  for line in lines:
    try:
      ekle = (lines[i].replace(" ","").replace("-","").replace("(","").replace(")","").replace("/","").replace("'","").replace(":","").replace(".","").replace(",","").strip())
    except:
      break
    ekle2 = (lines[j].replace("'","").strip())
    try:
      # cursor.execute("ALTER TABLE `kimovil` ADD `" + ekle + "` text")
      cursor.execute("UPDATE `yenicihaz` SET `"+ "K"+ekle.strip() +"` = RTRIM('" + ekle2.strip() + "') Where Outmodel = '"+ outmodelname.strip() +"'")
    except: 
        pass
    cnx.commit()
    i+=2
    j+=2
  print("Eklendi:" + eklemodel)
  if(url is None):
    break	
 
  break