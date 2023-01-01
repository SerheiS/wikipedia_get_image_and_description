import requests
import json
from bs4 import BeautifulSoup
from datetime import date

"""
Contact for discussing and more information:
telegram: @petrolhds
email: chih.sereza.s@gmail.com
---------------------------------------------

Modified script from official documentation which was 
supplemented with parsing of description from targe page.

Step 1
------
Request from Wiki name of the image that is POD

Step 2
------
Request from Wiki url fot that specified image

Step 3
------
Parse HTML from target (POD) page (see TARGET_TITLE for target URL)

Step 4
------
Cleaning of HTML to text + catching of necessary 
data (description of the picture and author)
"""

date_iso = date.today().isoformat()

URL = "https://en.wikipedia.org/w/api.php"
TARGET_PAGE = "Template:POTD protected/" + date_iso
"""
Actually you can paste any page from wikipedia that you want to process.
Script will try to catch image and description from it, if it is possible.
"""


def main():
    img_name = get_img_name(date_iso)
    img_url = get_img_url(img_name)
    description = parse_img_description(TARGET_PAGE)
    fetched_description = fetch_img_description(description)
    print(
        f"Image Name: {img_name}" +
        "\n--------------------------\n" +
        f"Image URL: {img_url}" +
        "\n--------------------------\n" +
        f"Description:\n\n" +
        f"{fetched_description}"
    )


def get_img_name(date_iso: str) -> str:
    """
    Get name of the image related to the current POTD (Pictute of Today).

    :param date_iso: :obj:`str` -> date for target POTD in ISO format 
    (year-month-day | xxxx-xx-xx).

    Note: all Wikipedia POTDs have the same page url, that looks like 
    'Template:POTD protected/<date>', where <date> is current date in 
    ISO format.

    :return: :obj: `str` -> name of image from the target page on the 
    Wikipedia server.

    Details: 
    --------
    function makes request to Wikipedia server with such 
    parameters (see `params` variable). Parameters are which properties 
    to get for the queried pages:
    • 'action': 'query' - fetch data from and about MediaWiki
    • 'format': 'json' - format of response from server
    • 'formatversion':'2' - use format=json with formatversion=2
    (According to the documentation)
    • 'prop': 'images' - returns all files contained on the given page(s)
    • 'titles': '<name of page>' - it contains name of target page

    (Source: https://www.mediawiki.org/w/api.php?action=help&modules=main)
    """

    params = {
        "action": "query",
        "format": "json",
        "formatversion": "2",
        "prop": "images",
        "titles": TARGET_PAGE
    }
    response = requests.get(url=URL, params=params)
    res_data = response.json()
    filename = res_data["query"]["pages"][0]["images"][0]["title"]
    return filename


def get_img_url(filename: str) -> str:
    """
    Get direct URL of the target image related to the current POTD 
    (Pictute of Today).

    :param filename: :obj:`str` -> name of the target image on 
    Wikipedia server

    :return image_url: :obj:`str` -> direct url of the target image

    Details: 
    --------
    function makes request to Wikipedia server with such 
    parameters (see `params` variable):
    • 'action': 'query' - 
    • 'format': 'json' - format of response from server
    • 'prop': 'imageinfo' - returns file information and upload history.
    • 'iiprop': 'url' - gives URL to the file and the description page. 
    If the file has been revision deleted, a filehidden 
    property will be returned.
    (Source: https://www.mediawiki.org/w/api.php?action=help&modules=query%2Bimageinfo)
    • 'titles': '<filename>' - it contains the name of target image as 
    it calls on Wikipedia server

    (Source: https://www.mediawiki.org/w/api.php?action=help&modules=main)

    WARNING!:
    ---------
    'formatversion':'2' - must not be used in this query. Don't know 
    why, but it brakes the code! In spite of using 'format':'json' parameter.
    """

    params = {
            "action": "query",
            "format": "json",
            "prop": "imageinfo",
            "iiprop": "url",
            "titles": filename
        }
    response = requests.get(url=URL, params=params)
    data = response.json()
    page = next(iter(data["query"]["pages"].values()))
    image_url = page["imageinfo"][0]["url"]
    return image_url


def parse_img_description(page_name: str):
    """
    Parse target page and return its content.

    :param page_name: :obj:`str` -> name of the target page on 
    Wikipedia server (like 'Lionel Messi' or 
    'Template:POTD protected/2022-12-30'. It is allways written 
    at the top of any Wiki page)

    :return parse_text: :obj:`str` -> parsed content from the target 
    page. Actually is a plain text of source HTML page.

    Details: 
    --------
    function makes request to Wikipedia server with such 
    parameters (see `params` variable):
    • 'action': 'parse' - parses content and returns parser output
    • 'page': <name of the target page> - parse the content of this 
    page. Cannot be used together with 'text' and 'title' parameters.
    • 'format': 'json' - format of response from server
    • 'formatversion':'2' - use format=json with formatversion=2 
    (According to the documentation)

    (Source: https://www.mediawiki.org/w/api.php?action=help&modules=parse)
    """

    params = {
        "action": "parse",
        "page": page_name,
        "format": "json"
    }

    response = requests.get(url=URL, params=params)
    content = response.content.decode("utf8")
    js = json.loads(content)
    parse_text = js['parse']['text']['*']
    return parse_text


def fetch_img_description(parsed_text: str) -> str:
    """
    Fetch description of Wikipedia's POD from parsed html file.

    :param page_name: :obj:`str` -> plain text of parsed source HTML file.

    :return parse_text: :obj:`str` -> description of Wikipedia's POD

    Example or pocessed description:
    --------------------------------
    The emu (Dromaius novaehollandiae) is the second-tallest living bird 
    after its ratite relative the ostrich. It is endemic to Australia, 
    where it is the largest native bird and the only extant member of the 
    genus Dromaius. The emu's range covers most of mainland Australia, 
    but the Tasmanian, Kangaroo Island and King Island subspecies became 
    extinct after the European settlement of Australia in 1788. Emus are 
    soft-feathered, brown, flightless birds with long necks and legs, 
    and can reach up to 1.9 metres (6.2 ft) in height. Emus can travel 
    great distances, and when necessary can sprint at 48 kilometres per 
    hour (30 mph); they forage for a variety of plants and insects, but 
    have been known to go for weeks without eating. They drink 
    infrequently, but take in copious amounts of water when the 
    opportunity arises. This emu was photographed in the Tidbinbilla 
    Nature Reserve in the Australian Capital Territory.

    Photograph credit: John Harrison
    """
    fetched_description = BeautifulSoup(parsed_text, features="html.parser").get_text()
    final_description = fetched_description.strip()
    data = final_description.split("\n")
    answer = ""
    for i in data:
        if "Recently featured" in i:
            break
        if len(i) > 0:
            answer += f"{i.strip()}\n\n"
    return answer.strip()

main()
