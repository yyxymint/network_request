RX72PERTOJZ7XBQI

def call_ranking():
    for _ in range(15):
        print()
    for i in range(-1,-11,-1):
        print(str(-i)+'등 : ',end=" ")
        print(article_by_nickname[i][1]+ ' ('+str(article_by_nickname[i][0])+'글)')

def date_over():
    return now_month=='05'

def gall_wa():

    start_flag = True
    search_pos = -1981888

    no_add_signal = False

    global_dictionary = {}

    while True:    
        search_page = 1
        now_url='https://gall.dcinside.com/mgallery/board/lists/?id=fromis9real&page='+str(search_page)+'&search_pos='+str(search_pos)+'&s_type=search_subject_memo&s_keyword=%EC%99%80%7E'

        soup=get_soup(now_url)
        article_list=soup.find_all('div',{'class':'bottom_paging_box'})

        page_num = len(article_list[0].find_all('a')) - int(not(start_flag))
        start_flag = False

        for now_page in range(1,page_num+1):
            now_url='https://gall.dcinside.com/mgallery/board/lists/?id=fromis9real&page='+str(now_page)+'&search_pos='+str(search_pos)+'&s_type=search_subject_memo&s_keyword=%EC%99%80%7E'
            soup=get_soup(now_url)
            article_list=soup.find_all('tr',{'class':'ub-content us-post'})

            for article_num in range(len(article_list)):
                article_title = article_list[article_num].find('a').text
                writer = article_list[article_num].find('td',{'class':'gall_writer ub-writer'}).find('span',{'class':'nickname in'}).text
                article_order = article_list[article_num].find('td',{'class':'gall_num'}).text

                now_date = article_list[article_num].find('td',{'class':'gall_date'}).text

                now_month = article_list[article_num].find('td',{'class':'gall_date'}).text.split('.')[0]


                if now_month=='05':
                    no_add_signal= True

                article_title = article_list[article_num].find('a').text
                writer = article_list[article_num].find('td',{'class':'gall_writer ub-writer'}).find('span',{'class':'nickname in'}).text
                article_order = article_list[article_num].find('td',{'class':'gall_num'}).text

                now_date = article_list[article_num].find('td',{'class':'gall_date'}).text

                now_month = article_list[article_num].find('td',{'class':'gall_date'}).text.split('.')[0]
                    
                try:
                    global_dictionary[writer]
                except KeyError:
                    global_dictionary[writer] = set()

                if not no_add_signal:
                    print(article_title+'\t'+writer+'\t'+now_date)
                    global_dictionary[writer].add(article_title+' !@# '+article_order+' !@# '+now_date)

        if no_add_signal:
            break
        search_pos+=10000


    all_nickname = global_dictionary.keys()
    article_by_nickname = []

    for nick in all_nickname:
        article_by_nickname.append([len(global_dictionary[nick]),nick])
    article_by_nickname.sort()
    
    call_ranking()
