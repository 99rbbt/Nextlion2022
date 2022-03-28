def extract_info(toon_list):
    result = []
    for toon in toon_list:
        title = toon.find("dl").find("dt").find("a").string
        who = toon.find("dl").find("dd", {"class":"desc"}).find("a").string
        rate = toon.find("dl").find("div", {"class":"rating_type"}).find("strong").text


        toon_info ={
            'title' : title,
            'who' : who,
            'rate' : rate
        }
        result.append(toon_info)
        

    return result