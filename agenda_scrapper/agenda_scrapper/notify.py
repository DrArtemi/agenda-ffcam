import scrapy

from mailbot.mailbot import send_email


def notify(item: scrapy.Item):
    subject = f"Inscriptions for {item.get("title")}"
    content = f"""
Bonjour machin !
Tu peux maintenant t'inscrire a la sortie {item.get("title")} !
Responsable : {item.get("accompanist")}
Activite : {item.get("activity")}
Lieu : {item.get("location")}
Date : {item.get("date")}
Lien : {item.get("inscription_link")}
"""
    send_email(subject, content)