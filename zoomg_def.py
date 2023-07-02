# + gameatoson gameato_bot / zoomg_game

def zoomg_game( s1 , s2 , chat_id ) : 
    import requests
    from bs4 import BeautifulSoup as bs 
    import re 
    import time 
    import random

    # basics 
    db_emoji = { 0 : "🔍" , 1 : "👨‍💻" , 2 : "🔥" , 3 : "🎯" , 4 : "💣" , 5 : "📌" , 6 : "🔰" , 7 : "🌀" , 8 : "🟣" , 9 : "⭕️" , 10 : "" , 11 : "" , 12 : ""}
    db_cta = { 0 : "💬نظر شما در این مورد چیه؟" , 1 : "💬نظرتو کامنت کن برامون" , 2 : "💬نظرتو کامنت کن" , 3 : "💬نظرتو چیه؟ کامنتش کن" , 4 : "" , 5 : "" , 6 : "" , 7 : "" , 8 : "" , 9 : "" , 10 : "" , 11 : "" , 12 : "" , 13 : "" , 14 : "" , 15 : "" , 16 : "" , 17 : ""}
    db_gg = { 0 : "🤟بپا دوز گیم خونت نیوفته!" , 1 : "👋یه سر به سایتمون هم بزن" , 2 : "🤪نبینم ناراحت باشیا!" , 3 : "💪پاشو پاشو الکی ادا حال بدا رو در نیار" , 4 : "" , 5 : "" , 6 : "" , 7 : "" , 8 : "" , 9 : "" , 10 : "" , 11 : "" , 12 : "" , 13 : "" , 14 : "" , 15 : "" , 16 : "" , 17 : ""}
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
                title = soup.find("span" , class_="row").text


                #extract descreption <div> and some dogshits...
                description = soup.find("div" , class_="article-section").p.text
                gg_sum = 1
                for i in description : 
                    if i=="." : 
                        break
                    else:
                        gg_sum+=1
                description = description[0 : gg_sum]
            
            
                #extract image url <img> 
                image = soup.find_all("img" , class_="img-responsive filterdark cover")
                for url in image : 
                    url = url['src']

                
                # run 
                emoji = db_emoji[random.randint(0,12)]
                cta = db_cta[random.randint(0,17)]
                gg = db_gg[random.randint(0,17)]

                # test_bot = -1001924808520

                base_url = 'https://api.telegram.org/bot6140992753:AAHMGN0s0H1SLjIlt_or9S2Tu_dRGaaLqdQ/sendPhoto'
                parameters = {
                    "chat_id" : str(chat_id) ,
                    "photo" : url ,
                    "caption" : emoji + description + "\n" + cta + "\n" + "---------------" + "\n" + "🆔@gameato" + "\n" + "🌐gameato.ir" + "\n" + gg + "\n"
                }

                resp = requests.get(base_url, data= parameters)
                print(resp.text)
                print(counter)
                counter += 1 

                # sleep n2
                time.sleep(s2)

