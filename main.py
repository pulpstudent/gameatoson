# + gameatoson gameato_bot / zoomg_game

import requests

# update version 
update_version = "update1.1test"
update_url = 'https://api.telegram.org/bot6140992753:AAHMGN0s0H1SLjIlt_or9S2Tu_dRGaaLqdQ/sendPhoto'
parameters = {
    "chat_id" : "-1001924808520" ,
    "photo" : "https://gameato.ir/wp-content/uploads/2022/11/مگ.png" ,
    "caption" :  update_version + "\n" + "\n" + "Changes : " + "\n" + "1- added update_tag" + "\n" + "2- added title to every post" + "\n" + "3- added point_id to control Text length of posts" + "\n" + "\n" + "#ggdevs"
}

resp_update = requests.get(update_url, data= parameters)
print(resp_update.text)
###

# define zoomg_bot
def zoomg_game( s1 , s2 , chat_id , point_id ) : 
    from bs4 import BeautifulSoup as bs 
    import re 
    import time 
    import random

    # basics 

    db_emoji_1 = { 0 : "📍" , 1 : "🖋️" , 2 : "📌" , 3 : "🧷" , 4 : "⭕️" , 5 : "🌀" , 6 : "🔷" , 7 : "🔶" , 8 : "🔔" , 9 : "💬" , 10 : "🟡" , 11 : "🔵" , 12 : "🟢"}
    db_emoji_2 = { 0 : "🔍" , 1 : "👨‍💻" , 2 : "🔥" , 3 : "🎯" , 4 : "💣" , 5 : "📌" , 6 : "🔰" , 7 : "🌀" , 8 : "🟣" , 9 : "⭕️" , 10 : "" , 11 : "" , 12 : ""}
    db_cta = { 0 : "💬نظر شما در این مورد چیه؟" , 1 : "💬نظرتو کامنت کن برامون" , 2 : "💬نظرتو کامنت کن" , 3 : "💬نظرتو چیه؟ کامنتش کن" , 4 : "" , 5 : "" , 6 : "" , 7 : "" , 8 : "" , 9 : "" , 10 : "" , 11 : "" , 12 : "" , 13 : "" , 14 : "" , 15 : "" , 16 : "" , 17 : ""}
    # db_gg = { 0 : "🤟بپا دوز گیم خونت نیوفته!" , 1 : "👋یه سر به سایتمون هم بزن" , 2 : "🤪نبینم ناراحت باشیا!" , 3 : "💪پاشو پاشو الکی ادا حال بدا رو در نیار" , 4 : "" , 5 : "" , 6 : "" , 7 : "" , 8 : "" , 9 : "" , 10 : "" , 11 : "" , 12 : "" , 13 : "" , 14 : "" , 15 : "" , 16 : "" , 17 : ""}
    url_dic = {}
    title_list = []
    url_list = []
    run_sum = 0
    counter = 0 

    # start

    while True : 

        # sleep n1
        time.sleep(s1)

        url_list = []

        r = requests.get("https://www.zoomg.ir")
        soup = bs(r.text , "html.parser")
        article_links = soup.find( "div" , class_="latestArticles").find_all("a")
        urls = [link["href"] for link in article_links]
        for iurl in urls :
            if iurl[21:30]=="game-news" : 
                if len(iurl)>31 :
                    url_list.append(iurl)

        for i in url_list: 
            if i in title_list : 
                print("same shit")
                print(counter)
                counter += 1 
            else: 
                title_list.append(i)
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
                    elif i != "." and gg_i <= point_id - 1 : 
                        gg_sum += 1 
                    elif i != "." and gg_i > point_id - 1  :
                        break
                description = description[0:gg_sum]

                #extract image url <img> 
                image = soup.find_all("img" , class_="img-responsive filterdark cover")
                for url in image : 
                    url = url['src']

                
                # run 
                emoji_1 = db_emoji_1[random.randint(0,12)]
                emoji_2 = db_emoji_2[random.randint(0,12)]
                cta = db_cta[random.randint(0,17)]
                #gg = db_gg[random.randint(0,17)]

                # test_bot = -1001924808520

                base_url = 'https://api.telegram.org/bot6140992753:AAHMGN0s0H1SLjIlt_or9S2Tu_dRGaaLqdQ/sendPhoto'
                parameters = {
                    "chat_id" : str(chat_id) ,
                    "photo" : url ,
                    "caption" : emoji_1 + title + "\n" + "\n" + emoji_2 + description + "\n" + "\n" + cta + "\n" + "---------------" + "\n" + "🆔@gameato" + "\n" + "🌐gameato.ir" + "\n" + update_version
                }

                resp = requests.get(base_url, data= parameters)
                print(resp.text)
                print(counter)
                counter += 1 

                # sleep n2
                time.sleep(s2)


# print zoomg_bot
print(zoomg_game(7200,420,-1001924808520,2))

