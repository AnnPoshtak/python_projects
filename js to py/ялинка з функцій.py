def spytai_rozmir_yalynky ():
    r = int(input("Введіть розмір ялинки"))
    return r
def maliu_bagato_probiliv(skik_probiliv):
    pr = ""
    i=0
    while i < skik_probiliv:
        pr+=" "
        i+=1
    return pr
def malui_bagato_zirochok (skik_stars):
    star=""
    i = 0
    while i <skik_stars:
        star+="*"
        i+=1
    return star
def namalui_shapku_yalunky (rozmir):
    m = 1
    while m<rozmir+1:
        print(maliu_bagato_probiliv((rozmir * 2 - 1) / 2 - m + 0.5),malui_bagato_zirochok(m * 2 - 1))
        m+=1
def namalui_nijku_yalunky (rozmir):
    pr1=""
    i=0
    while i <rozmir-1:
        pr1+=" "
        i+=1
    print(pr1,"*")
def namalui_yalunky (rozmir):
    namalui_shapku_yalunky(rozmir)
    namalui_nijku_yalunky(rozmir)
def main():
    rozmir=spytai_rozmir_yalynky()
    namalui_yalunky(rozmir)
main()