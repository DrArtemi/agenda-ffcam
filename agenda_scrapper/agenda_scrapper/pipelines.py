# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

from agenda_scrapper.items import Excursion
from agenda_scrapper.notify import notify


class AgendaScrapperPipeline:
    
    def __init__(self):

        self.con = sqlite3.connect('demo.db')
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS excursions(
            id TEXT,
            title TEXT,
            activity TEXT,
            date TEXT,
            location TEXT,
            accompanist TEXT,
            inscription_link TEXT,
            inscription_open NUMERIC
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute("SELECT * FROM excursions WHERE id = ?", (item["id"],))
        result = self.cur.fetchone()
        if result:
            if not result[-1] and item["inscription_open"]:
                notify(item)
            self.cur.execute("UPDATE excursions SET inscription_link = ?, inscription_open = ? WHERE id = ?",
            (
                item["inscription_link"],
                item["inscription_open"],
                item["id"]
            ))
        else:
            self.cur.execute("""
                INSERT INTO excursions (
                    id, 
                    title, 
                    activity, 
                    date, 
                    location, 
                    accompanist, 
                    inscription_link, 
                    inscription_open
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                item["id"],
                item["title"],
                item["activity"],
                item["date"],
                item["location"],
                item["accompanist"],
                item["inscription_link"],
                item["inscription_open"],
            ))
            self.con.commit()
        return item
