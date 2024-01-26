import cloudscraper, re, time, pandas
from bs4 import BeautifulSoup

def get_html(url:str):
    scraper = cloudscraper.CloudScraper()
    headers = {'Accept': 'text/html'}
    html = scraper.get(url,headers=headers)
    time.sleep(1)
    html = html.text
    return html

def existing_category(soup : BeautifulSoup):
    #return list of the broker industry
    value = []
    categories = soup.find_all("option")
    for category in categories:
        str = category.text 
        str = str[:-5]
        if str == 'Trave':
            str = 'Travel'
        value.append(str)
    return value

def all_profile(url:str):
    html = get_html(url)
    soup = BeautifulSoup(html,"html.parser")
    all_profiles = find_profiles(soup)
    return all_profiles

def pair_profile_category(main_url:str):
    all_profile_urls = all_profile(main_url)
    profile_category = dict()
    html = get_html(main_url)
    soup = BeautifulSoup(html,"html.parser")
    categories = existing_category(soup)
    categories.pop(0) #remove invalid result
    for category in categories:
        category_for_link = category.replace(" & ","+%26+").replace(" ","+").replace(" ","+")
        url = f"{main_url}?wpv-wpcf-specialty={category_for_link}&wpv_aux_current_post_id=460514&wpv_aux_parent_post_id=460514&wpv_view_count=477752"
        html = get_html(url)
        soup = BeautifulSoup(html,"html.parser")
        url_profiles = find_profiles(soup)
        for urls in url_profiles:
            if urls in profile_category:
                profile_category[urls].append(category)
            else:
                profile_category[urls] = [category]
    
    #there are profile url that doesnt have any category
    profile_uncategorized = list(set(all_profile_urls)-set(profile_category.keys()))
    for profile in profile_uncategorized:
        profile_category[profile] = ["Unknown"]
    return profile_category    

def find_profiles(soup : BeautifulSoup):
    #return list of profile urls for every category/industry
    profile_urls = []
    columns = soup.find_all("div","su-column su-column-size-4-5")
    for column in columns:
        inner_column = column.find("div","su-column-inner su-u-clearfix su-u-trim")
        url = inner_column.find("a")["href"]
        profile_urls.append(url)
    return profile_urls

def get_details(soup:BeautifulSoup):
    details = dict()
    main_content = soup.find("section",id="main_content")
    name = main_content.find("h3","blogpost_title").text
    details["Name"] = name
    p = main_content.find_all("p")[:4]
    find_for = ["Work phone","Work fax","Cell phone","Email"]
    for i in p:
        key = key_contact(i.text)
        value = value_contact(i.text)
        if key in find_for:
            if key == "Email":
                value = i.find("a")["href"].replace("mailto:","")                
            details[key] = value  
    return details

def key_contact(text:str):
    match = re.search(r"((\w+)\s*)+",text)
    if match:
        match = match.group(0)
    return match

def value_contact(text:str):
    try:
        subs = re.sub(r'\D',"",text)
    except TypeError:
        subs = None
    return subs   

def save_excel(result:list):
    df = pandas.DataFrame(result)
    df.to_excel("georgia_broker.xlsx")
    print("saved to excel")


if __name__=="__main__":
    result = []
    main_url = "https://gabb.org/gabb-business-brokers/"
    
    profile_category = pair_profile_category(main_url)
    
    #main program
    for profile in profile_category:
        try:
            url = profile
            html = get_html(url)
            soup = BeautifulSoup(html,"html.parser")
            detail = get_details(soup)
            list_category = profile_category.get(profile)
            detail["Industry"]=";".join(list_category)
            detail["URL"]=url
            result.append(detail)
        except Exception as e:
            print(f"{e} on {url}")
         
    save_excel(result)