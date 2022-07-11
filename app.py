from logging import PlaceHolder
from pywebio import *
from pywebio.output import *
from pywebio.input import *
import pandas as pd 
from datetime import datetime
from dateutil.relativedelta import relativedelta



def main():
    put_image(src = 'https://bobtutor.org/storage/logos/1613204243-1612810280-1602097956-logo.png')
    put_markdown('======================').style('color:green')
    put_markdown('\n' + 'Welcome to Presidential Awards Calculator for Bobtutor').style('font-size: 30px')
    toast("For gold, silver, and bronze metals this year, you may only enter hours that were between August 1, 2021 to July 31, 2022.", position='right',color='info', duration=10)
    put_markdown('The main function of this tool is to quickly find out how many hours you have and what award you are able to get.')
    put_markdown('You can also find out how many hours you need for a certain award; even the all mightiest lifetime achievement!').style('color:gray')
    put_markdown('Made for students in middle school and high school').style('color:red')
    put_markdown('Please input your date of birth and we will get started')
    put_text('======================').style('color:green')
    toast("The application dead line is August 7th (2022)", position='right',color='info', duration=4)
    
    def repeat():
        try:
            DOB = input("", placeholder = "Your Birth Date(dd/mm/yyyy)", required=True)
            dateObject = datetime.strptime(DOB, '%d/%m/%Y')
            put_text("Your bithday is: ", dateObject).style('color:orange')
            new_date = dateObject + relativedelta(years=16)
            put_text("Your 16th birthday is: " + str(new_date)).style('color:orange')
            POB = "07/1/2022"
            dateObject = datetime.strptime(POB, '%d/%m/%Y')
            t = 0
            if (new_date > dateObject):
                put_text("You are in the teen category!").style('color:red')
                put_text('======================').style('color:green')
                t += 1
            else:
                put_text("You are in the young adults category!").style('color:red')
                put_text('======================').style('color:green')
            if t > 0:
                repeat.getCategory = "teen"
            else:
                repeat.getCategory = "young adults"
            
            
        except ValueError:
            ping = "Please enter a valid birthday!"
            popup("Error", content=ping) 
            repeat()    
    
    repeat()
    put_text("Please make sure you have selected the (All) category in dates and downloaded the CSV files for teaching and training").style("color:red")
    put_image('https://cdn.discordapp.com/attachments/689663355874443278/995492928380227676/Screen_Shot_2022-07-09_at_5.53.23_PM.png')
    put_image('https://cdn.discordapp.com/attachments/689663355874443278/995508559146131477/Screen_Shot_2022-07-09_at_6.55.26_PM.png')
    

    def repeat1():
        try:
            userfile = file_upload("Select your TEACHING csv file: ", accept="text/csv", multiple=False)
            userfile1 = file_upload("Select your TRAINING csv file: ", accept="text/csv", multiple=False)
            open(userfile['filename'], 'wb').write(userfile['content'])
            open(userfile1['filename'], 'wb').write(userfile1['content'])
            df = pd.read_csv(userfile['filename'])
            df1 = pd.read_csv(userfile1['filename'])
            earliest = "08/01/2021"
            latest = "07/31/2022"
            earliest1 = datetime.strptime(earliest, '%m/%d/%Y')
            latest1 = datetime.strptime(latest, '%m/%d/%Y')

            tT = df['Teaching Time']
            pT = df['Prep time']
            teachingTime = []
            prepTime = []
            teachingTimeMAX = []
            prepTimeMAX = []
            i = -1 
            for item in df['Start At']:
                i += 1 
                teachingTimeMAX.append(int(tT[i]))
                prepTimeMAX.append(int(pT[i]))
                dateObject = datetime.strptime(item, '%Y-%m-%d %H:%M:%S')
                if earliest1 < dateObject < latest1:
                    teachingTime.append(int(tT[i]))
                    prepTime.append(int(pT[i]))
        
            trainingTime = []
            trainingTimeMax = []
            tTT = df1['Duration']
            k = -1
            for item in df1['Training Date']:
                k += 1
                trainingTimeMax.append(int(tTT[k]))
                dateObject1 = datetime.strptime(item, '%Y-%m-%d')
                if earliest1 < dateObject1 < latest1:
                    trainingTime.append(int(tTT[k]))

            put_markdown('======================').style('color:green')
            totalTime = sum(teachingTime) + sum(prepTime) + sum(trainingTime)
            repeat1.getTotalTime = totalTime 
            repeat1.getTotalTimeMAX = sum(teachingTimeMAX) + sum(prepTimeMAX) + sum(trainingTimeMax)
            
            
        except KeyError:
            ping = "Please make sure you have selected the right CSV files"
            popup("Error", content=ping) 
            scroll_to('middle')
            repeat1() 
            
        
    repeat1()
    bob = (repeat1.getTotalTime / 60)
    bobb = repeat1.getTotalTime 
    bobbb = (repeat1.getTotalTimeMAX / 60)
    clear(None)
    scroll_to('top')
    put_text("Total number of minutes this semester: " + str(bobb) + " || Total number of hours: " + str(bob)).style('color:orange; font-size: 20px')
    put_text("Net total of minutes (life time): " + str(bobbb) + " || Total number of hours: " + str(bobb)).style('color:orange; font-size: 20px')
    put_text("You are in the category of " + str(repeat.getCategory)).style('color:orange; font-size: 20px')
    
    
    eligi = 0 
    if bobbb >= 4000:
            eligi +=1
    lifetime = 4000
    lifetimePercentage = bobbb / 4000 
    if repeat.getCategory == "young adults":
        if bob >= 100:
            eligi += 1
        if bob >= 175:
            eligi += 1
        if bob >= 250:
            eligi += 1
        bronzePercentage = bob / 100 
        bronze = 100
        silverPercentage = bob / 175
        silver = 175
        goldPercentage = bob / 250
        gold = 250
    else:
        if bob >= 50:
            eligi += 1
        if bob >= 75:
            eligi += 1
        if bob >= 100:
            eligi += 1   
        bronzePercentage = bob / 50
        bronze = 50
        silverPercentage = bob / 75
        silver = 75
        goldPercentage = bob / 100
        gold = 100
    
    put_text('======================').style('color:green')
    if eligi == 4:
        put_text("You are a legend! You are able to get all of the awards!").style('color:orange; font-size: 20px')
    if eligi == 3:
        put_text("Congrats, you are able to get  3 of the awards!").style('color:orange; font-size: 20px')
    if eligi == 2:
        put_text("Congrats, you are able to get 2 of the awards!").style('color:orange; font-size: 20px')
    if eligi == 1:
        put_text("Congrats, you are able to get 1 of the awards!").style('color:orange; font-size: 20px')
    if eligi == 0:
        put_text("You are unable to get any of the awards and that's completely ok! You still made our community a better place!").style('color:red; font-size: 20px')
    put_text('======================').style('color:green')
    
    put_text("Following awards and eligibility: ").style('color:red')
    
    def achieved():
        put_text("You have achieved this metal").style('color:green; font-size: 18')
    def unachieved(pop, shop):
        put_text("You are unable to achive this award").style('color:red; font-size: 18')
        i = 0 
        progressBarz = ""
        progressBarzz = ""
        for x in range(50):
            if i < (pop * 50):
                i += 1
                progressBarzz += "█"
            else:
                progressBarz += "▒"
        put_text(progressBarzz + progressBarz)
        if shop == 1:
            int = (1 - pop) * bronze
        if shop == 2:
            int = (1 - pop) * silver
        if shop == 3:
            int = (1 - pop) * gold
        if shop == 4:
            int = (1 - pop) * lifetime

        put_text("You need " + str(round(int, 2)) + " more hours").style('color:red')
        put_text("You are " + str(round((pop * 100), 2)) + " percent of the way there!")
        
    
    put_image('https://cdn.discordapp.com/attachments/689663355874443278/995568369522724865/Screen_Shot_2022-07-09_at_10.53.11_PM.png')
    if eligi == 1:
        achieved()
    else:
        x = 1
        unachieved(bronzePercentage, x)
    put_text('======================').style('color:green')
    put_image('https://cdn.discordapp.com/attachments/689663355874443278/995569145309560913/Screen_Shot_2022-07-09_at_10.56.17_PM.png')
    if eligi == 2:
        achieved()
    else:
        x = 2
        unachieved(silverPercentage, x)   
    put_text('======================').style('color:green')
    put_image('https://cdn.discordapp.com/attachments/689663355874443278/995569296119955586/Screen_Shot_2022-07-09_at_10.56.51_PM.png')    
    if eligi == 3:
        achieved()
    else:
        x = 3
        unachieved(goldPercentage, x) 
    put_text('======================').style('color:green')  
    put_image('https://cdn.discordapp.com/attachments/689663355874443278/995885672881729586/unknown.png')
    if eligi == 4:
        achieved()
    else:
        x = 4
        unachieved(lifetimePercentage, x)        
    put_text('======================').style('color:green')
    
if __name__ == '__main__':
    start_server(main, port=8888, debug=True)
