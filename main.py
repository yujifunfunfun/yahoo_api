import eel
from yahoo import *

@eel.expose
def yahoo_search(keyword,count,min_price,max_price,csv):
    main(keyword,count,min_price,max_price,csv)

eel.init("web")
eel.start("main.html")