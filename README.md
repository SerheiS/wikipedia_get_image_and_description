# Get URL of image and its description from Wikipedia's page 🤗
Hi! I created this script to get Picture of Today and its description from Wikipedia. You can try it for any Wiki's page to get these data. If you have a questions or would like to discuss something feel free to contact me:
Telegram: @petrolhds
Email: chih.sereza.s@gmail.com

# Please, read the text below before trying 🫣!
This script was created to get image URL for downloading. So this script will give you only this data:
 - URL of image from Wiki's page (it can be any page, not only PODT (picture of today))
 - image name (name under which it is stored on Wiki's servers)
 - description (it parsed from Wiki's page with the help of BeautifulSoup! So take it into account)

The result mostly depends on the content of page. If you will get some issues don't be scared of them! Try:
 - another page
 - fix an issue if you can
 - contact me (I'm available 24/7)

Again, only this data will be allowable to you. Next actions with it is up to you! 😉
 
# How to use
1. This script requires such additional packages to be installed:
 - BeautifullSoup (for getting clear description from page's HTML source file)
 - requests for making HTTP requests to Wikipedia
 
You can create virtual environment (VENV) or install it directly on your machine. It is up to you!

type ```pip install -r requirements.txt``` in your terminal window to install necessary packages.

2. To get today's Picture of The Day from Wikipedia data type ```python wiki_script.py```.

3. In terminal window you will get name and URL of source image, and it's description.
![image](https://user-images.githubusercontent.com/106083959/210172179-d9b335e3-9ab8-4933-9f7c-6e613a88bd78.png)


# Notes (if you have some issues or some time to read):

 - Speaking about PODT from Wikipedia it can be not only an image, but also GIF, Video, etc. So sometimes it can cause breaking of this script.

 - If you are trying to get data from another page pay attention to TARGET_PAGE. You must set the page that contains not only media file but also its escription. In other way it will brake.

- You are free to use parts of this code for your progects. Just take any separate function from it to get necessary data and don't forget about necessary packages!

P.S. I will be glad to communicate about it if you wish. See my contacts at the top 😉


