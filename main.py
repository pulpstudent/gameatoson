# gameatoson / gameato_bot_

import requests

# update version 
update_version = "update3.0"
update_url = 'https://api.telegram.org/bot6140992753:AAHMGN0s0H1SLjIlt_or9S2Tu_dRGaaLqdQ/sendPhoto'
parameters = {
    "chat_id" : "-1001924808520" ,
    "photo" : "https://gameato.ir/wp-content/uploads/2023/10/Group-4055.png" ,
    "caption" :  update_version + "\n" + "\n" + "Changes : " + "\n" + "1- This is zoomg_bot " + "\n" + "\n" + "#ggdevs" 
}

resp_update = requests.get(update_url, data= parameters)
print(resp_update.text)



###

### define gameato_bot ###
def zoomg_bot(s1 , z_s2 , z_chat_id , z_point_id) : 
    from bs4 import BeautifulSoup as bs 
    import re 
    import time 
    import random


    # basics 

    general_sum = 0

        # zoomg_bot

    db_emoji_1 = { 0 : "📍" , 1 : "🖋️" , 2 : "📌" , 3 : "🧷" , 4 : "⭕️" , 5 : "🌀" , 6 : "🔷" , 7 : "🔶" , 8 : "🔔" , 9 : "💬" , 10 : "🟡" , 11 : "🔵" , 12 : "🟢"}
    db_emoji_2 = { 0 : "🔍" , 1 : "👨‍💻" , 2 : "🔥" , 3 : "🎯" , 4 : "💣" , 5 : "📌" , 6 : "🔰" , 7 : "🌀" , 8 : "🟣" , 9 : "⭕️" , 10 : "" , 11 : "" , 12 : ""}
    db_cta_z = { 0 : "💬نظر شما در این مورد چیه؟" , 1 : "💬نظرتو کامنت کن برامون" , 2 : "💬نظرتو کامنت کن" , 3 : "💬نظرتو چیه؟ کامنتش کن" , 4 : "" , 5 : "" , 6 : "" , 7 : "" , 8 : "" , 9 : "" , 10 : "" , 11 : "" , 12 : "" , 13 : "" , 14 : "" , 15 : "" , 16 : "" , 17 : ""}
    # db_gg = { 0 : "🤟بپا دوز گیم خونت نیوفته!" , 1 : "👋یه سر به سایتمون هم بزن" , 2 : "🤪نبینم ناراحت باشیا!" , 3 : "💪پاشو پاشو الکی ادا حال بدا رو در نیار" , 4 : "" , 5 : "" , 6 : "" , 7 : "" , 8 : "" , 9 : "" , 10 : "" , 11 : "" , 12 : "" , 13 : "" , 14 : "" , 15 : "" , 16 : "" , 17 : ""}
    title_list_z = []
    url_list_z = []
    counter_z = 0 


    # start gameato_bot_

    while True : 

        # sleep n1
        time.sleep(s1)

        # 1. START zoomg_bot from gameato_bot ----------------------------------------------------------- #

        general_sum += 1

        url_list_z = []

        r = requests.get("https://www.zoomg.ir")
        soup = bs(r.text , "html.parser")
        article_links = soup.find( "div" , class_="latestArticles").find_all("a")
        urls = [link["href"] for link in article_links]
        for iurl in urls :
            if iurl[21:30]=="game-news" : 
                if len(iurl)>31 :
                    url_list_z.append(iurl)

        for i in url_list_z: 
            if i in title_list_z : 
                print("same shit")
                print(counter_z)
                counter_z += 1 
            else: 
                title_list_z.append(i)
                r = requests.get(i)
                soup = bs(r.text , "html.parser")

                #extract title <span> 
                title = soup.h1.span.text


                #extract descreption <div> and some dogshits...
                description = soup.find("div" , class_="article-section").p.text
                gg_sum = 0
                gg_i = 0
                for i in description : 
                    if i == "." : 
                        gg_sum += 1 
                        gg_i += 1 
                    elif i != "." and gg_i <= z_point_id - 1 : 
                        gg_sum += 1 
                    elif i != "." and gg_i > z_point_id - 1  :
                        break
                description = description[0:gg_sum]

                #extract image url <img> 
                image = soup.find_all("img" , class_="img-responsive filterdark cover")
                for url in image : 
                    url = url['src']

                
                # run 
                emoji_1 = db_emoji_1[random.randint(0,12)]
                emoji_2 = db_emoji_2[random.randint(0,12)]
                cta_z = db_cta_z[random.randint(0,17)]
                #gg = db_gg[random.randint(0,17)]

                # test_bot = -1001924808520
                # gameato = -1001745459269
                # gameato | bot = -1001975079060

                
                base_url = 'https://api.telegram.org/bot6140992753:AAHMGN0s0H1SLjIlt_or9S2Tu_dRGaaLqdQ/sendPhoto'
                parameters = {
                    "chat_id" : str(z_chat_id) ,
                    "photo" : url ,
                    "caption" : emoji_1 + title + "\n" + "\n" + emoji_2 + description + "\n" + "\n" + cta_z + "\n" + "---------------" + "\n" + "🆔@gameato" + "\n" + "🌐gameato.ir" 
                }

                if general_sum > 1 : 
                    resp = requests.get(base_url, data= parameters)
                    print(resp.text)
                    print(counter_z)
                    counter_z += 1 
                else : 
                    counter_z += 1 
                    
                # sleep z_s2
                time.sleep(z_s2)

        # 1. END zoomg_bot from gameato_bot ----------------------------------------------------------- #



# print zoomg_bot

    # s1 , z_s2 , z_chat_id , z_point_id 
        # test_bot = -1001924808520
        # gameato = -1001745459269
        # gameato | bot = -1001975079060

print(zoomg_bot(10,360,-1001745459269,3))


