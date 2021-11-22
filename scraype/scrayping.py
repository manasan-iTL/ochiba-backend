from bs4 import BeautifulSoup as bs4

# 課題
# ・ファイルアップロードされたら、フォルダー選択画面にredirectする
# ・この時に、HTMLのパスを格納した変数を渡す（URLにパラメータとして渡す）
# ・渡されたHTMLから解析してフォルダー名をgetで返す
# ・次のVIEWで選択されたフォルダのURL、タイトルを取得し、Formを作成
# ・それを画面に表示する

soup = bs4(open('../media/files/html/bookmarks_2021_11_10.html', encoding='utf-8'), 'html.parser')

### フォルダーの取得 ###

# folders = [tag.text for tag in soup.find_all('h3')]

# for folder in folders:
#     print(folder)


### 個別の記事 ###

### 階層の移動はfor文を回しまくればたどり着ける

# select_folders = soup.find_all('dl')

for i, folder in enumerate(soup.find_all('dl')):
     if i >= 1:
         for k, target in enumerate(folder.find_all('a')):
             allhref = []
             print(target.get('href'))


# allhref = select_folder.find_next_sibling()

# parent_href = soup.select_folder.parent.next_sibling

# print(allhref)

