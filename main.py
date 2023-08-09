# gameatoson / gameato_bot_

import requests

# update version 
update_version = "update2.0"
update_url = 'https://api.telegram.org/bot6140992753:AAHMGN0s0H1SLjIlt_or9S2Tu_dRGaaLqdQ/sendPhoto'
parameters = {
    "chat_id" : "-1001924808520" ,
    "photo" : "https://gameato.ir/wp-content/uploads/2022/11/مگ.png" ,
    "caption" :  update_version + "\n" + "\n" + "Changes : " + "\n" + "1- pspro crawler just activated ->" + "\n" + "1.1- crawls all <new> pspro product every 89 loops (about every one week)" + "\n" + "1.2- prints <url>, <title>, <model> and <price> of each new product" + "\n" + "1.3- for gameato | bot" + "\n" + "2- market.gameato crawler just activated ->" + "\n" + "2.1 crawls all <new> ad every s1+s2 sleep time" + "\n" + "2.2 prints <title>, <pic>, <sit>, <seller_name>, <rregion> and <price> of each new product" + "\n" + "2.3- for gameato | bot and gameato" + "\n" + "\n" + "#ggdevs"
}

resp_update = requests.get(update_url, data= parameters)
print(resp_update.text)



###

### define gameato_bot ###
def gameato_bot(s1 , z_s2 , z_chat_id , z_point_id , s2 , mp_s2 , mp_chat_id) : 
    from bs4 import BeautifulSoup as bs 
    import re 
    import time 
    import random


    # basics 

        # zoomg_bot

    db_emoji_1 = { 0 : "📍" , 1 : "🖋️" , 2 : "📌" , 3 : "🧷" , 4 : "⭕️" , 5 : "🌀" , 6 : "🔷" , 7 : "🔶" , 8 : "🔔" , 9 : "💬" , 10 : "🟡" , 11 : "🔵" , 12 : "🟢"}
    db_emoji_2 = { 0 : "🔍" , 1 : "👨‍💻" , 2 : "🔥" , 3 : "🎯" , 4 : "💣" , 5 : "📌" , 6 : "🔰" , 7 : "🌀" , 8 : "🟣" , 9 : "⭕️" , 10 : "" , 11 : "" , 12 : ""}
    db_cta_z = { 0 : "💬نظر شما در این مورد چیه؟" , 1 : "💬نظرتو کامنت کن برامون" , 2 : "💬نظرتو کامنت کن" , 3 : "💬نظرتو چیه؟ کامنتش کن" , 4 : "" , 5 : "" , 6 : "" , 7 : "" , 8 : "" , 9 : "" , 10 : "" , 11 : "" , 12 : "" , 13 : "" , 14 : "" , 15 : "" , 16 : "" , 17 : ""}
    # db_gg = { 0 : "🤟بپا دوز گیم خونت نیوفته!" , 1 : "👋یه سر به سایتمون هم بزن" , 2 : "🤪نبینم ناراحت باشیا!" , 3 : "💪پاشو پاشو الکی ادا حال بدا رو در نیار" , 4 : "" , 5 : "" , 6 : "" , 7 : "" , 8 : "" , 9 : "" , 10 : "" , 11 : "" , 12 : "" , 13 : "" , 14 : "" , 15 : "" , 16 : "" , 17 : ""}
    title_list_z = []
    url_list_z = []
    counter_z = 0 

        # mpproduct_bot

    db_cta_mp = { 0 : "" , 1 : "🥹 بازیت رو طاقچه داره خاک میخوره؟ در گیماتو مارکت آگهیش کن و بفروشش 🥳" , 2 : "🥲 کنسولتو میخوای عوض کنی؟ کنسول قدیمیتو در گیماتو مارکت آگهیش کن و کنسول نو بخر 😇" , 3 : "🫠 تو گیماتو مارکت، اگه بعد ۷ روز آگیهت فروش نره، خود گیماتو ازت میخردش 🤩" , 4 : "" , 5 : "" , 6 : "" , 7 : "" , 8 : "" , 9 : "" , 10 : "" }
    title_list_mp = []
    url_list_mp = []
    counter_mp = 0 

        # pspro_bot

    pspr_bot_numb = 88
    title_list_pspro = []
    url_list_pspro = []

    # start gameato_bot_

    while True : 

        # sleep n1
        time.sleep(s1)

        # 1. START zoomg_bot from gameato_bot ----------------------------------------------------------- #

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

                resp = requests.get(base_url, data= parameters)
                print(resp.text)
                print(counter_z)
                counter_z += 1 

                # sleep z_s2
                time.sleep(z_s2)

        # 1. END zoomg_bot from gameato_bot ----------------------------------------------------------- #

        # sleep s2
        time.sleep(s2)

        # 2. START mpproduct_bot from gameato_bot ----------------------------------------------------- #

        url_list_mp = []

        r = requests.get("https://market.gameato.ir/products/index")
        soup = bs(r.text , "html.parser")
        product_links = soup.find( "div" , class_="products-grid").find_all("a")
        urls = [link["href"] for link in product_links]
        for iurl in urls :
            url_list_mp.append(iurl)

        for i in url_list_mp: 
            if i in title_list_mp : 
                print("same shit")
                print(counter_mp)
                counter_mp += 1 
            else: 
                title_list_mp.append(i)
                r_product = requests.get(i)
                soup_product = bs(r_product.text , "html.parser")

                # filter 
                filter = soup_product.find("span" , class_ = "pirsic-type").text
                if filter == "گیمر" : 
                    # title 
                    title = soup_product.find("h1" , class_="product-title").text

                    # url_pic
                    pic = soup_product.find("img" , attrs= {"id" : "main-pic" })
                    pic = str(pic)
                    url_pic = pic[31:-47]

                    # sit
                    sit = soup_product.find("span" , class_= "value").text

                    # seller_name 
                    seller_name = soup_product.find("span" , class_= "pirsic-name").text

                    # rregion 
                    rregion = soup_product.find("div" , class_="sc-loc").text

                    # price 
                    price = soup_product.find_all("span" , class_="value")
                    sum = 0 
                    for letter in price : 
                        sum += 1 
                        r_price = letter
                        if sum == 3 : 
                            break
                    price = str(r_price)
                    price = price[20:-7]

                    # run 

                    cta_mp = db_cta_mp[random.randint(0,10)]
                    # test_bot = -1001924808520
                    # gameato = -1001745459269
                    # gameato | bot = -1001975079060


                    base_url = 'https://api.telegram.org/bot6140992753:AAHMGN0s0H1SLjIlt_or9S2Tu_dRGaaLqdQ/sendPhoto'
                    parameters = {
                        "chat_id" : str(mp_chat_id) ,
                        "photo" : url_pic ,
                        "caption" : "🔰" + "خرید " + title + "\n" + "\n" + "🔹" + "فروشنده: " + seller_name + "\n" + "🔹" + "وضعیت کالا: " + sit + "\n" + "🔹" + "محله: " + rregion +  "\n" + "🔹" + "قیمت فروشنده: " + price + "\n" + "لینک مشاهده و خرید: " + "\n" + i + "\n" + "\n" + cta_mp + "\n" + "\n" + "---------------" + "\n" + "#آگهی_فروش" + "\n" + "🆔@gameato" + "\n" + "🌐market.gameato.ir"
                    }

                    # main resp 
                    resp = requests.get(base_url, data= parameters)
                    print(resp.text)
                    print(counter_mp)
                    counter_mp += 1 

                    # static resp -> 
                    base_url = 'https://api.telegram.org/bot6140992753:AAHMGN0s0H1SLjIlt_or9S2Tu_dRGaaLqdQ/sendPhoto'
                    parameters = {
                        "chat_id" : -1001975079060 ,
                        "photo" : url_pic ,
                        "caption" : "🔰" + "خرید " + title + "\n" + "\n" + "🔹" + "فروشنده: " + seller_name + "\n" + "🔹" + "وضعیت کالا: " + sit + "\n" + "🔹" + "محله: " + rregion +  "\n" + "🔹" + "قیمت فروشنده: " + price + "\n" + "لینک مشاهده و خرید: " + "\n" + i + "\n" + "\n" + cta_mp + "\n" + "\n" + "---------------" + "\n" + "#آگهی_فروش" + "\n" + "🆔@gameato" + "\n" + "🌐market.gameato.ir"
                    }
                    resp = requests.get(base_url, data= parameters)
                    print(resp.text)



                    # sleep mp_s2
                    time.sleep(mp_s2)

        # 2. END mpproduct_bot from gameato_bot ----------------------------------------------------- #

        pspr_bot_numb += 1

        # 3. START pspro_bot from gameato_bot ----------------------------------------------------- #

        if pspr_bot_numb % 89 == 0 : 
            r = requests.get("https://pspro.ir/index.php?route=product/search&search=&sort=p.date_available&order=DESC&limit=100")
            soup_pspro = bs(r.text ,"html.parser" )

            pspro_sum = 0

            ## get links 
            pspro_product_link = soup_pspro.find("div" , class_="row py-3 px-4").find_all("a")
            urls = [link["href"] for link in pspro_product_link]

            for url in urls : 
                url_list_pspro.append(url)

            for i in url_list_pspro : 
                if i in title_list_pspro : 
                    print("same pspro shit")

                else : 
                    title_list_pspro.append(i)
                    r = requests.get(i)
                    pspro_page_soup = bs(r.text ,"html.parser")

                    # url 
                    pspro_url = i

                    # title 
                    pspro_title = pspro_page_soup.find("h1" , class_="h3 font-latin-yekan").text

                    # model 
                    pspro_model = pspro_page_soup.find("h5" , class_="d-inline text-light").text

                    # price 
                    pspro_price = pspro_page_soup.find("div" , attrs={"style" : "max-width: 300px"}).find_all("meta")
                    pspro_price = str(pspro_price)
                    pspro_price = pspro_price[16:27]

                    # sum 
                    pspro_sum += 1 
                    pspro_sum_ = str(pspro_sum)

                    # run

                    # test_bot = -1001924808520
                    # gameato = -1001745459269
                    # gameato | bot = -1001975079060

                    base_url = 'https://api.telegram.org/bot6140992753:AAHMGN0s0H1SLjIlt_or9S2Tu_dRGaaLqdQ/sendPhoto'
                    parameters = {
                        "chat_id" : -1001975079060 ,
                        "photo" : "https://gameato.ir/wp-content/uploads/2022/06/gameato.jpg" , 
                        "caption" : pspro_sum_ + "-" + pspro_title + "\n" + "\n" + "🔹" + "مدل: " + pspro_model + "\n" + "🔹" + "قیمت: " + pspro_price + "\n" + "\n" + pspro_url + "\n" + "\n" + "#محصول_جدید"
                    }
                    resp = requests.get(base_url, data= parameters)
                    print(pspro_sum)
                    print(resp.text)

                    # sleep time
                    time.sleep(2)
        else : 
            print("not yet pspro")

        # 3. END pspro_bot from gameato_bot ----------------------------------------------------- #
                    


# print gameato_bot_

    # s1 , z_s2 , z_chat_id , z_point_id , s2 , mp_s2 , mp_chat_id
        # test_bot = -1001924808520
        # gameato = -1001745459269
        # gameato | bot = -1001975079060

print(gameato_bot(3600,180,-1001745459269,2,3600,60,-1001745459269))

