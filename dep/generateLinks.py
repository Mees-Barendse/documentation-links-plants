import pandas as pd
import time as time
import os
import dep.pykew.pykew.ipni as ipni


def alien1(name):
    uri = "https://alienplantsbelgium.myspecies.info/search/site/"

    split = name.split()
    path = os.getcwd() + '\\temp.txt'
    for i in split:
        uri += i + "%20"
    uri = uri.removesuffix("%20")
    os.system("curl " + uri + " > " + path)
    k = open("temp.txt", "r", encoding="utf-8")
    txt = str(k.read())
    list = txt.split("<")
    list2 = []
    try:
        for i in list:
            list2 += i.split(">")
        for i in list2:
            index = list2.index("Taxonomy term/Species list")
            out = list2[index - 5]
        out = out.removeprefix("a href=\"")
        out = out.removesuffix("\"")
    except:
        out = "null"
    return out


def Bio2(name):
    return "http://biodiversite.wallonie.be/fr/accueil.html?IDC=6"


def blumen3(name):
    try:
        df = pd.read_csv('link-csv\\linkDuits.csv', encoding="windows-1252")
        df = df[df.Name == name]
        link = df.iat[0, 2]
        return link

    except:
        return "null"


def eco4(name):
    url = "https://www.ecopedia.be/zoeken/"
    list = name.split()
    path = os.getcwd() + '\\temp.txt'
    for i in list:
        url += i + "%20"
    os.system("curl " + url + " > " + path)
    try:
        k = open("temp.txt", "r", encoding="utf-8")
        txt = str(k.read())
        list = txt.split("<h3 class=\"title\">\n    <a ")
        list2 = []
        for i in list:
            i = i.split("</a>  </h3>")
            list2 += i
        list = []
        for i in list2:
            if "h" == i[0]:
                i = i.removeprefix("href=\"")

                i = i.split(">")
                list += i
        list2 = []
        for i in list:
            i = i.split(" -")
            list2 += i
        list = []
        for i in list2:
            if i == name:
                return "https://www.ecopedia.be" + list2[list2.index(i) - 1].removesuffix("\"")
        return "null"
    except:
        return "null"


def world5(name):
    try:
        res = ipni.search(name)
        h = 0
        length = res.size()
        if length > 150:
            return "null"
        while h < length:
            string1 = str(next(res))
            h += 1
            if string1[0:len("{\'name\': \'" + name + "\'")] == "{\'name\': \'" + name + "\'":
                string = string1
                h = length
            if string1 == None:
                return "null"

        list = string.split(",")
        for i in list:
            if "\'family\':" in i:
                i = list.index(i)
                uri = list[i - 1]
                uri = uri.removesuffix("\'")
                uri = uri.removeprefix(" \'url\': \'/n/")
                uri = uri.removeprefix(" \'url\': \'/n/")
                return "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:" + uri
        return "null"
    except:
        return "null"


def soorten6(name):
    try:
        df = pd.read_csv('link-csv\\soortenbank.csv', encoding="windows-1252")
        df = df[df.Name == name]
        link = df.iat[0, 1]
        return link

    except:
        return "null"


def verspreiding7(name):
    try:
        df = pd.read_csv('link-csv\\versprijding.csv', encoding="windows-1252")
        df = df[df.NAME == name]
        link = df.iat[0, 0]
        link = format(link, '04d')
        return "https://www.verspreidingsatlas.nl/" + str(link)
    except:
        return "null"


def makeAll(name):
    list = []

    list.append(alien1(name))
    list.append(Bio2(name))
    list.append(blumen3(name))
    list.append(eco4(name))
    list.append(world5(name))
    list.append(soorten6(name))
    list.append(verspreiding7(name))
    while "null" in list:
        list.remove("null")
    return list


def testAll(name):
    print(alien1(name))
    print(Bio2(name))
    print(blumen3(name))
    print(eco4(name))
    print(world5(name))
    print(soorten6(name))
    print(verspreiding7(name))


def completed(name):
    html = ""
    list = makeAll(name)

    for k in list:
        site = k.split("/")[2].removeprefix("www.")
        site = site.capitalize()
        if site == "powo.science.kew.org":
            site = "Plantsoftheworldonline.org"
        html += "<p class=\"MsoNormal\" style=\"margin: 0cm 0cm 0pt;\"><a href=" + k + " target=\"_blank\">" + site + "</a></p>\n"
    return html


def makeLinks1(i):
    name = i
    links = ""
    if (alien1(name) != "null"):
        links += alien1(name) + " "
    if (Bio2(name) != "null"):
        links += Bio2(name) + " "
    if (eco4(name) != "null"):
        links += eco4(name) + " "

    if (blumen3(name) != "null"):
        links += blumen3(name) + " "

    if (world5(name) != "null"):
        links += world5(name) + " "

    if (soorten6(name) != "null"):
        links += soorten6(name) + " "

    if (verspreiding7(name) != "null"):
        links += verspreiding7(name) + " "

    print(links)










