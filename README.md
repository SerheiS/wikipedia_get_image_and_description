#Get URL of image and its description from Wikipedia's page
Hi! I created this script to get Picture of Today from Wikipedia and its description. You can try it for any Wiki's page to get these data. If you have a questions or would like to discuss something feel free to contact me:
Telegram: @petrolhds
Email: chih.sereza.s@gmail.com

# Please, read text below before trying 🫣!
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
 - BeautifulSoup (for getting clear description from page's HTML source file)
 
You can create virtual environment (VENV) or install it directly on your machine. It is up to you

type ```pip install -r requirements.txt``` in your terminal window

2. To get today's Picture of The Day from Wikipedia data type ```python main.py```

3. IN terminal you will get URL of source image and it's description

# Notes (if you have some issues or some time to read):

Speaking about PODT from Wikipedia it can be not only an image, but also GIF or Video. So sometimes it can cause break of this script.

If you are trying to get data from another page pay attention to TARGET_PAGE. You must set the page that contains not only media file but also its escription. In other way it will brake.

But are free to use parts of this code for your progects. Just get any separate function from it to get necessary data!

P.S. I will be glad to communicate about it if you wish. See my contacts at the top 😉


