==============================
2020-09-30
=============================
���� Site : https://jeongwookie.github.io/2019/05/31/190531-naver-main-news-crawling/

1. !pip install bs4
2  !pip install selenium

���� �ѱ۱��� -> ���ͳ����� Ȯ��  bs_obj = BeautifulSoup(result.content.decode('euc-kr','replace'), "html.parser")

�α��ι��� : https://boysboy3.tistory.com/133
�� Chrom ���� : V 85.0.

//*[@id="log.login"]


https://cafe.naver.com/ArticleList.nhn?search.clubid=28326943&search.boardtype=L

//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a

https://cafe.naver.com/ArticleList.nhn?search.clubid=28326943&search.boardtype=L&search.totalCount=151&search.page=2
https://cafe.naver.com/ArticleList.nhn?search.clubid=28326943&search.boardtype=L&search.totalCount=151&search.page=1

https://cafe.naver.com/ArticleList.nhn?search.clubid=28326943&search.boardtype=L&search.page=1


for page_num in range(1,3):
    base_url = "https://cafe.naver.com/ArticleList.nhn?search.clubid=28326943&search.boardtype=L&search.page={0}".format(page_num)
    driver.get(base_url)

    # ������ ��ư 50�� Ŭ��
    driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
    # �ε� �ð��� �����Ƿ� Ÿ�̹� ���߱� ���� sleep(0.5)
    time.sleep(0.5)
# # href �Ӽ��� ã�� url�� ����Ʈ�� �����Ѵ�.
article_list = driver.find_elements_by_css_selector('li.board_box a.txt_area')
article_urls = [ i.get_attribute('href') for i in article_list ]
 
for link in article_urls:
    test_list.append(link)

/html/body/div[1]/div/div[4]/table/tbody/tr[1]/td[1]/div[1]/div/a

//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]

#main-area > div:nth-child(6) > table > tbody > tr:nth-child(1) > td.td_article > div.board-name > div > a
//*[@id="main-area"]

//*[@id="main-area"]/div[4]/table/tbody


    
    for script in bs(["script", "style"]):
        script.extract()    # rip it out
        
    # get text
    text = bs.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = ' '.join(chunk for chunk in chunks if chunk)


1. git/vscode ��ġ

2. git �������� �Է�
git config --global user.name pdm2017
git config --global user.email pdm96@hanmail.net


git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/pdm2017/naver_cafe.git
git push -u origin main