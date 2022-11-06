import dep.generateLinks as glink
import dep.spec as spec


def makeLinks(name):
    hulp = glink.completed(name)
    print("de html tekst is ook terug te vinden in html.txt")
    return hulp


bool = True
k = open("html.txt", "w")
k.write("")
k.close()

while bool:
    hulp = ""
    name = input("wetenschappenlijke naam: ")
    if "spec." in name:
        hulp = spec.makeHTML(name)
    else:
        hulp = makeLinks(name)
    print(hulp)
    k = open("html.txt", "a")
    k.write(hulp + "\n\n")
    k.close()
    if input("sluiten? (y of n): ") == "y":
        bool = False