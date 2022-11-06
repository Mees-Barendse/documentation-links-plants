import dep.pykew.pykew.ipni as ipni
import pandas as pd
from dep.pykew.pykew.ipni_terms import Name
import os as os



def alien(name):
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


def world(name):
    try:
        query = {Name.genus: name}
        res = ipni.search(query)
        h = 0
        length = res.size()
        while h < length:
            string1 = str(next(res))
            h += 1
            if string1[0:len("{\'name\': \'" + name + "\'")] == "{\'name\': \'" + name + "\'":
                string = string1
                h = length
            if string1 == None:
                return "null"
        list2 = []
        list = string.split("[")
        for i in list:
            if "{" not in i or "}" not in i:
                list2 += i.split("]")
        list = []
        for i in list2:
            list += i.split(",")
        list2 = []
        if len(list) < 20:
            return "null"

        for i in list:
            if "\'id\': \'" in i:
                i = i.removeprefix(" \'id\': \'")
                i = i.removesuffix("\'")
                list2 += [i]
                uri = ""
        uri = list2[len(list2) - 1]
        return "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:" + uri
    except:
        return "null"


def makeHTML(name):
    out = ""
    alien1 = alien(name)
    powo = world(name)
    print(alien1.removesuffix("null") + "\n" + powo.removesuffix("null"))
    if alien1 != "null":
        out += "<p class=\"MsoNormal\" style=\"margin: 0cm 0cm 0pt;\"><a href=" + "Alienplantsbelgium.be" + " target=\"_blank\">" + "site" + "</a></p>\n"
    if powo != "null":
        out += "<p class=\"MsoNormal\" style=\"margin: 0cm 0cm 0pt;\"><a href=" + "Plantsoftheworldonline.org" + " target=\"_blank\">" + "site" + "</a></p>\n"
    return out



