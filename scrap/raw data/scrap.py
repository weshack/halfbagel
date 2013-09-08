import urllib2
import simplejson as son
import re
from BeautifulSoup import BeautifulSoup
def scrap(link):
    json={}
    response = urllib2.urlopen(link)
    linkflag=link.split('/')
    dirc = "http://www.wesleyan.edu/reslife/housing/"+linkflag[5]+"/"
    page_source = response.read()
    soup = BeautifulSoup(page_source)
    ############################


    ############################
    plans = soup.findAll('li')
    floorplans=[]
    for plan in plans:
        floorplans.append(str(plan))
    

    floorplan=[]   
    x="href="

    for plan in floorplans:
        if x in plan:
            floorplan.append(plan)

    if floorplan==[]:
        planlinks ="False"

    else:
        planlinks=[]
        for plan in floorplan:
            planlink=dirc + str(plan).split('"')[1]
            planlinks.append(planlink)
    ########################   
    

    des2 = soup.find('div', {"id":"col2"})
    quiet2="False"
    quietflag=des2.findAll('b')
    for flag in quietflag:
        if "Quiet Floor" in flag:
            quiet2="True"

    des2 = re.sub(r'<br />',' ', str(des2))
    #print des2
    des2 = BeautifulSoup(des2)
    des2 = ''.join(des2.findAll(text=True))
    #print des2



    des = soup.find('div', {"id":"col2"})
    des = str(des)#[52:][:-6]
    #print des
    ###############################
    img = soup.findAll('img')[1]
    img=str(img)
    img=img.split('"')[-4]
    if img[:3] == "../":
        img = "http://www.wesleyan.edu/reslife/housing/" + img[3:]
    else:
        img = dirc + img
    #print img
    #############################
    name = soup.h1
    name=str(name)[4:][:-5]
    #print name
    ###############################
    h3= soup.h3
    h3=str(h3)[4:][:-5]
    h3=h3.split(",")

    num_of_units=len(h3)
    #print num_of_units
    #print h3
    h4=[]

    for unit in h3:
        if "(quiet street)" in unit:
            quiet = 'True'
        else:
            quiet = 'False'
        h4.append(unit.strip())
    if quiet == 'True'or quiet2 == 'True':
        quiet3 = 'True'
    else:
        quiet3 = 'False'
    #print h4
    #print quiet

    
##########################
    json["name"]=name
    #json["description"] = des2
    #json["img"] = img
#    json["num_of_units"]=num_of_units
#    json["floorplans"]=planlinks
#    json["quiet"]=quiet3
    #print json
    json = (son.dumps(json))
    return json
