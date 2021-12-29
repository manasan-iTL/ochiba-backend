from bs4 import BeautifulSoup as bs4

# 課題
# ・ファイルアップロードされたら、フォルダー選択画面にredirectする
# ・この時に、HTMLのパスを格納した変数を渡す（URLにパラメータとして渡す）
# ・渡されたHTMLから解析してフォルダー名をgetで返す
# ・次のVIEWで選択されたフォルダのURL、タイトルを取得し、Formを作成
# ・それを画面に表示する

# soup = bs4(open('../media/files/html/bookmarks_2021_11_10.html', encoding='utf-8'), 'html.parser')
### フォルダーの取得 ###
def find_folders(path):
    soup = bs4(open(f'media/{path}', encoding='utf-8'), 'html.parser')
    folders = [tag.text for tag in soup.find_all('h3')]
    return folders
# for folder in folders:
#     print(folder)


### 個別の記事 ###


# 階層の移動はfor文を回しまくればたどり着ける

###　フォルダ毎のaタグのテキストを取る
# allhref = [[href.text for href in folder.find_all('a')] for i, folder in enumerate(soup.find_all('dl')) if i >=1 ]
# print(allhref[0])



# for i, folder in enumerate(soup.find_all('dl')):
#     if i == 1:
#         for k, target in enumerate(folder.find_all('a')):
#             # print(target.get('href'))
#             href.append(target.get('href'))
#             # print(href)
#     print(i)
#     allhref.append(href)
#     print(allhref[0][0])

### フォルダ名でそのフォルダ内の情報を取得できる（改良）
def search_url_text(path, folder):
    contents = []
    soup = bs4(open(f'media/{path}', encoding='utf-8'), 'html.parser')
    current_folder = soup.find(name='h3', text=folder).parent
    target_folder = current_folder.find('dl').find_all('a')
    for target in target_folder:
        dict = {'title':target.text.replace('\n', ''), 'url':target['href']}
        contents.append(dict)
    # texts = [href.text.replace('\n','') for href in target_folder]
    # hrefs = [href['href'] for href in target_folder]
    # contents = {'texts':texts, 'hrefs':hrefs}
    return contents

'''
contents = []
for target in target_foler:
    dict = {'title':target.text.replace('\n', ''), 'url':target['href']}
    contents.append(dict)
'''

