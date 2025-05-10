def spytai_rozmir_yalynky () :
     r = int(input("Введи розмір ялинки"))
     return r;
def maliu_bagato_probiliv (skik_probiliv):
    pr = "";

    if skik_probiliv == 0 :
        return " ";

    pr = " " + maliu_bagato_probiliv(skik_probiliv - 1);

    return pr

def malui_bagato_zirochok (skik_stars) :
    star = "";

    if skik_stars == 0 :
        return "";
    star = "*" + malui_bagato_zirochok(skik_stars - 1);

    return star;

def namalui_shapku_yalunky (rozmir, m = 1) :
    if m > rozmir :
        return "";

    print(str(maliu_bagato_probiliv(rozmir - m)) + str(malui_bagato_zirochok(m * 2 - 1)));
    namalui_shapku_yalunky(rozmir, m + 1)

def namalui_nijku_yalunky (rozmir):
    print(maliu_bagato_probiliv(rozmir - 1) + "*");
def namalui_yalunky (rozmir) :
    namalui_shapku_yalunky(rozmir);
    namalui_nijku_yalunky(rozmir);
def main () :
    rozmir = spytai_rozmir_yalynky();

    print("Розмір ялинки: " + str(rozmir))

    namalui_yalunky(rozmir);

main();