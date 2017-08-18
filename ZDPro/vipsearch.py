import sqlite3

def dbsearch(phone):
    try:
        conn = sqlite3.connect('Vip.db')
        sear = "SELECT Card,NAME,phone,inshop,link from vip WHERE phone like '%" +"%s" % str(phone) + "%';" 
        cursor = conn.execute(sear)
        return cursor

        conn.close()
    except:
        return ('','','','','',)
        conn.close()
#---------------------------------------------
