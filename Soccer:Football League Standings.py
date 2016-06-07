#Soccer/Football League Standings
from lxml import html
import requests
from termcolor import colored, cprint
import sys


#gets the correct text
def EPL():
    page = requests.get('http://www.livescore.com/soccer/england/premier-league/')
    tree = html.fromstring(page.content)

    number_1 = tree.xpath('(//html/body/div[2]/div[5]/div[16]/div[2]//text())[position()>3 and not(position()=5)and not(position()=6)'
                       'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
                       'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
                       'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_2 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[3]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_3 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[4]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_4 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[5]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_5 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[6]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_6 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[7]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_7 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[8]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_8 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[9]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_9 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[10]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_10 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[11]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_11 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[12]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_12 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[13]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_13 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[14]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_14 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[15]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_15 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[16]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_16 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[17]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_17 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[18]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_18 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[19]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=23)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_19 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[20]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=23)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_20 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[16]/div[21]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=23)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')

    #print in good format
    cprint("RANK    Pts  Played      Team            ",'red',attrs=['underline'])
    cprint('  ' + number_1[0] + '.' + '    ' + number_1[4] + '    ' + number_1[2] + '     ' + number_1[1],'green')
    cprint('  ' + number_2[0] + '.' + '    ' + number_2[4] + '    ' + number_2[2] + '     ' + number_2[1],'green')
    cprint('  ' + number_3[0] + '.' + '    ' + number_3[4] + '    ' + number_3[2] + '     ' + number_3[1],'green')
    cprint('  ' + number_4[0] + '.' + '    ' + number_4[4] + '    ' + number_4[2] + '     ' + number_4[1],'green')
    cprint('  ' + number_5[0] + '.' + '    ' + number_5[4] + '    ' + number_5[2] + '     ' + number_5[1],'yellow')
    cprint('  ' + number_6[0] + '.' + '    ' + number_6[4] + '    ' + number_6[2] + '     ' + number_6[1],'yellow')
    print('  ' + number_7[0] + '.' + '    ' + number_7[4] + '    ' + number_7[2] + '     ' + number_7[1])
    print('  ' + number_8[0] + '.' + '    ' + number_8[4] + '    ' + number_8[2] + '     ' + number_8[1])
    print('  ' + number_9[0] + '.' + '    ' + number_9[4] + '    ' + number_9[2] + '     ' + number_9[1])
    print('  ' + number_10[0] + '.' + '   ' + number_10[4] + '    ' + number_10[2] + '     ' + number_10[1])
    print('  ' + number_11[0] + '.' + '   ' + number_11[4] + '    ' + number_11[2] + '     ' + number_11[1])
    print('  ' + number_12[0] + '.' + '   ' + number_12[4] + '    ' + number_12[2] + '     ' + number_12[1])
    print('  ' + number_13[0] + '.' + '   ' + number_13[4] + '    ' + number_13[2] + '     ' + number_13[1])
    print('  ' + number_14[0] + '.' + '   ' + number_14[4] + '    ' + number_14[2] + '     ' + number_14[1])
    print('  ' + number_15[0] + '.' + '   ' + number_15[4] + '    ' + number_15[2] + '     ' + number_15[1])
    print('  ' + number_16[0] + '.' + '   ' + number_16[4] + '    ' + number_16[2] + '     ' + number_16[1])
    print('  ' + number_17[0] + '.' + '   ' + number_17[4] + '    ' + number_17[2] + '     ' + number_17[1])
    cprint('  ' + number_18[0] + '.' + '   ' + number_18[4] + '    ' + number_18[2] + '     ' + number_18[1],'red')
    cprint('  ' + number_19[0] + '.' + '   ' + number_19[4] + '    ' + number_19[2] + '     ' + number_19[1],'red')
    cprint('  ' + number_20[0] + '.' + '   ' + number_20[4] + '    ' + number_20[2] + '     ' + number_20[1],'red')
    print("\n")


def Liga():
    page = requests.get('http://www.livescore.com/soccer/spain/primera-division/')
    tree = html.fromstring(page.content)


    number_1 = tree.xpath('(//html/body/div[2]/div[5]/div[17]/div[2]//text())[position()>3 and not(position()=5)and not(position()=6)'
                       'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
                       'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
                       'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_2 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[3]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_3 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[4]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_4 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[5]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_5 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[6]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_6 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[7]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_7 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[8]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_8 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[9]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_9 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[10]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_10 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[11]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_11 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[12]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_12 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[13]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_13 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[14]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_14 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[15]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_15 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[16]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_16 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[17]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_17 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[18]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_18 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[19]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=23)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_19 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[20]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=23)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_20 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[17]/div[21]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=23)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')

    #print in good format
    cprint("RANK    Pts  Played      Team            ",'red',attrs=['underline'])
    cprint('  ' + number_1[0] + '.' + '    ' + number_1[4] + '    ' + number_1[2] + '     ' + number_1[1],'green')
    cprint('  ' + number_2[0] + '.' + '    ' + number_2[4] + '    ' + number_2[2] + '     ' + number_2[1],'green')
    cprint('  ' + number_3[0] + '.' + '    ' + number_3[4] + '    ' + number_3[2] + '     ' + number_3[1],'green')
    cprint('  ' + number_4[0] + '.' + '    ' + number_4[4] + '    ' + number_4[2] + '     ' + number_4[1],'green')
    cprint('  ' + number_5[0] + '.' + '    ' + number_5[4] + '    ' + number_5[2] + '     ' + number_5[1],'yellow')
    print('  ' + number_6[0] + '.' + '    ' + number_6[4] + '    ' + number_6[2] + '     ' + number_6[1],'yellow')
    print('  ' + number_7[0] + '.' + '    ' + number_7[4] + '    ' + number_7[2] + '     ' + number_7[1])
    print('  ' + number_8[0] + '.' + '    ' + number_8[4] + '    ' + number_8[2] + '     ' + number_8[1])
    print('  ' + number_9[0] + '.' + '    ' + number_9[4] + '    ' + number_9[2] + '     ' + number_9[1])
    print('  ' + number_10[0] + '.' + '   ' + number_10[4] + '    ' + number_10[2] + '     ' + number_10[1])
    print('  ' + number_11[0] + '.' + '   ' + number_11[4] + '    ' + number_11[2] + '     ' + number_11[1])
    print('  ' + number_12[0] + '.' + '   ' + number_12[4] + '    ' + number_12[2] + '     ' + number_12[1])
    print('  ' + number_13[0] + '.' + '   ' + number_13[4] + '    ' + number_13[2] + '     ' + number_13[1])
    print('  ' + number_14[0] + '.' + '   ' + number_14[4] + '    ' + number_14[2] + '     ' + number_14[1])
    print('  ' + number_15[0] + '.' + '   ' + number_15[4] + '    ' + number_15[2] + '     ' + number_15[1])
    print('  ' + number_16[0] + '.' + '   ' + number_16[4] + '    ' + number_16[2] + '     ' + number_16[1])
    print('  ' + number_17[0] + '.' + '   ' + number_17[4] + '    ' + number_17[2] + '     ' + number_17[1])
    cprint('  ' + number_18[0] + '.' + '   ' + number_18[4] + '    ' + number_18[2] + '     ' + number_18[1],'red')
    cprint('  ' + number_19[0] + '.' + '   ' + number_19[4] + '    ' + number_19[2] + '     ' + number_19[1],'red')
    cprint('  ' + number_20[0] + '.' + '   ' + number_20[4] + '    ' + number_20[2] + '     ' + number_20[1],'red')
    print("\n")


def Ligue1():
    page = requests.get('http://www.livescore.com/soccer/france/ligue-1/')
    tree = html.fromstring(page.content)


    number_1 = tree.xpath('(//html/body/div[2]/div[5]/div[15]/div[2]//text())[position()>3 and not(position()=5)and not(position()=6)'
                       'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
                       'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
                       'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_2 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[3]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_3 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[4]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_4 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[5]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_5 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[6]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_6 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[7]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_7 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[8]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=21)and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_8 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[9]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_9 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[10]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_10 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[11]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_11 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[12]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_12 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[13]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_13 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[14]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_14 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[15]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_15 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[16]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_16 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[17]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_17 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[18]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=8)and not(position()=11)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_18 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[19]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=23)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_19 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[20]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=23)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')
    number_20 = tree.xpath(
        '(//html/body/div[2]/div[5]/div[15]/div[21]//text())[position()>3 and not(position()=5)and not(position()=6)'
        'and not(position()=7)and not(position()=8)and not(position()=23)and not(position()=10)and not(position()=12)and not(position()=13)and not(position()=14)'
        'and not(position()=15)and not(position()=16)and not(position()=17)and not(position()=18)and not(position()=19)and not(position()=20)'
        'and not(position()=22)and not(position()=24)and not(position()=26)]')


    #print in good format
    cprint("RANK    Pts  Played      Team            ",'red',attrs=['underline'])
    cprint('  ' + number_1[0] + '.' + '    ' + number_1[4] + '    ' + number_1[2] + '     ' + number_1[1],'green')
    cprint('  ' + number_2[0] + '.' + '    ' + number_2[4] + '    ' + number_2[2] + '     ' + number_2[1],'green')
    cprint('  ' + number_3[0] + '.' + '    ' + number_3[4] + '    ' + number_3[2] + '     ' + number_3[1],'green')
    cprint('  ' + number_4[0] + '.' + '    ' + number_4[4] + '    ' + number_4[2] + '     ' + number_4[1],'yellow')
    cprint('  ' + number_5[0] + '.' + '    ' + number_5[4] + '    ' + number_5[2] + '     ' + number_5[1])
    print('  ' + number_6[0] + '.' + '    ' + number_6[4] + '    ' + number_6[2] + '     ' + number_6[1])
    print('  ' + number_7[0] + '.' + '    ' + number_7[4] + '    ' + number_7[2] + '     ' + number_7[1])
    print('  ' + number_8[0] + '.' + '    ' + number_8[4] + '    ' + number_8[2] + '     ' + number_8[1])
    print('  ' + number_9[0] + '.' + '    ' + number_9[4] + '    ' + number_9[2] + '     ' + number_9[1])
    print('  ' + number_10[0] + '.' + '   ' + number_10[4] + '    ' + number_10[2] + '     ' + number_10[1])
    print('  ' + number_11[0] + '.' + '   ' + number_11[4] + '    ' + number_11[2] + '     ' + number_11[1])
    print('  ' + number_12[0] + '.' + '   ' + number_12[4] + '    ' + number_12[2] + '     ' + number_12[1])
    print('  ' + number_13[0] + '.' + '   ' + number_13[4] + '    ' + number_13[2] + '     ' + number_13[1])
    print('  ' + number_14[0] + '.' + '   ' + number_14[4] + '    ' + number_14[2] + '     ' + number_14[1])
    print('  ' + number_15[0] + '.' + '   ' + number_15[4] + '    ' + number_15[2] + '     ' + number_15[1])
    print('  ' + number_16[0] + '.' + '   ' + number_16[4] + '    ' + number_16[2] + '     ' + number_16[1])
    print('  ' + number_17[0] + '.' + '   ' + number_17[4] + '    ' + number_17[2] + '     ' + number_17[1])
    cprint('  ' + number_18[0] + '.' + '   ' + number_18[4] + '    ' + number_18[2] + '     ' + number_18[1],'red')
    cprint('  ' + number_19[0] + '.' + '   ' + number_19[4] + '    ' + number_19[2] + '     ' + number_19[1],'red')
    cprint('  ' + number_20[0] + '.' + '   ' + number_20[4] + '    ' + number_20[2] + '     ' + number_20[1],'red')
    print("\n")

def Bundesliga():
    #took each component as an array of 1 string, converted to a string then attach them back together in the right format
    page = requests.get('http://www.livescore.com/soccer/germany/bundesliga/')
    tree = html.fromstring(page.content)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[2]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[2]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[2]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[2]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint("RANK    Pts  Played   Team Name   ",'red', attrs=['underline'])
    cprint (" " + rank_1 +".     " + points_1 + "    " + played_1 +"      "+ name_1,'green')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[3]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[3]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[3]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[3]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1,'green')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[4]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[4]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[4]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[4]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint (" " + rank_1 +".     " + points_1 + "    " + played_1 +"      "+ name_1,'green')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[5]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[5]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[5]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[5]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint (" " + rank_1 +".     " + points_1 + "    " + played_1 +"      "+ name_1, 'green')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[6]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[6]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[6]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[6]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1,'yellow')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[7]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[7]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[7]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[7]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1,'yellow')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[8]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[8]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[8]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[8]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    print(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[9]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[9]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[9]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[9]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    print(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[10]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[10]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[10]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[10]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    print(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[11]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[11]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[11]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[11]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    print(" " + rank_1 + ".    " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[12]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[12]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[12]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[12]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    print(" " + rank_1 + ".    " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[13]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[13]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[13]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[13]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    print(" " + rank_1 + ".    " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[14]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[14]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[14]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[14]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    print(" " + rank_1 + ".    " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[15]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[15]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[15]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[15]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    print(" " + rank_1 + ".    " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[16]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[16]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[16]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[16]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    print(" " + rank_1 + ".    " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[17]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[17]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[17]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[17]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".    " + points_1 + "    " + played_1 + "      " + name_1,'red')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[18]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[1]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[18]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[18]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".    " + points_1 + "    " + played_1 + "      " + name_1,'red')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[19]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[14]/div[19]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[19]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[14]/div[19]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".    " + points_1 + "    " + played_1 + "      " + name_1,'red')
    print ("\n")

def SerieA():
    page = requests.get('http://www.livescore.com/soccer/italy/serie-a/')
    tree = html.fromstring(page.content)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[2]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[2]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[2]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[2]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint("RANK     Pts  Played   Team Name   ",'red', attrs=['underline'])
    cprint (" " + rank_1 +".      " + points_1 + "    " + played_1 +"      "+ name_1,'green')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[3]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[3]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[3]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[3]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint (" " + rank_1 +".      " + points_1 + "    " + played_1 +"      "+ name_1,'green')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[4]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[4]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[4]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[4]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint (" " + rank_1 +".      " + points_1 + "    " + played_1 +"      "+ name_1,'green')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[5]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[5]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[5]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[5]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint (" " + rank_1 +".      " + points_1 + "    " + played_1 +"      "+ name_1,'yellow')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[6]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[6]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[6]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[6]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint (" " + rank_1 +".      " + points_1 + "    " + played_1 +"      "+ name_1,'yellow')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[7]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[7]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[7]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[7]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint (" " + rank_1 +".      " + points_1 + "    " + played_1 +"      "+ name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[8]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[8]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[8]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[8]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".      " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[9]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[9]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[9]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[9]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".      " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[10]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[10]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[10]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[10]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".      " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[11]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[11]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[11]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[11]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[12]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[12]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[12]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[12]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[13]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[13]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[13]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[13]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[14]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[14]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[14]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[14]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[15]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[15]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[15]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[15]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1)

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[16]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[16]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[16]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[16]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1,'red')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[17]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[17]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[17]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[17]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1,'red')

    rank_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[18]/div[1]/span[2]//text()')
    name_1 = tree.xpath('//html/body/div[2]/div[5]/div[16]/div[18]/div[2]//text()')
    played_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[18]/div[3]//text()')
    points_1 = tree.xpath('/html/body/div[2]/div[5]/div[16]/div[18]/div[10]//text()')
    rank_1 = "".join(rank_1)
    name_1 = "".join(name_1)
    played_1 = "".join(played_1)
    points_1 = "".join(points_1)
    cprint(" " + rank_1 + ".     " + points_1 + "    " + played_1 + "      " + name_1,'red')
    print("\n")

def Choose_Menu():
    menu = colored("Which League?\nEPL 'epl', LigaBBVA 'liga', SerieA 'serie', Ligue1 'ligue', Bundesliga 'bundesliga'\n", 'red', attrs=['bold'])
    choose_menu = input(menu)
    while (choose_menu != "liga" and choose_menu != "serie" and choose_menu != "ligue" and choose_menu != "bundesliga" and
                   choose_menu != "epl" and choose_menu != "EPL" and choose_menu != "LIGA" and choose_menu != "SERIE"
           and choose_menu != "LIGUE" and choose_menu != "BUNDESLIGA" and choose_menu != "EPL" and choose_menu != "l"):
        choose_menu = input(menu)

    if (choose_menu == "liga" or choose_menu == "LIGA"):
        Liga()
        restart()
    if (choose_menu == "EPL" or choose_menu == "epl"):
        EPL()
        restart()
    if (choose_menu == "Serie" or choose_menu == "serie"):
        SerieA()
        restart()
    if (choose_menu == "bundesliga" or choose_menu == "BUNDESLIGA"):
        Bundesliga()
        restart()
    if (choose_menu == "ligue" or choose_menu == "LIGUE"):
        Ligue1()
        restart()
    if (choose_menu == "l"):
        print("Bye")
        sys.exit()

def restart():
    Choose_Menu()


#runs program
Choose_Menu()


