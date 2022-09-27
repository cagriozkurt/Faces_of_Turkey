import json
import os

import scrapy


class PlayersSpider(scrapy.Spider):

    name = "players"

    # URLs and page numbers are manually entered
    start_urls = [
        f"https://www.transfermarkt.com/detailsuche/spielerdetail/suche/37900714/ajax/yw0/page/{i}"
        for i in range(1, 2)
    ]

    def parse(self, response):
        # Filename is manually entered as well
        with open(
            os.path.join(
                "output", f'karaman_{response.request.url.split("/")[-1]}.json'
            ),
            "w",
        ) as f:
            player_dict = {"players": []}
            items = response.css("table.items > tbody > tr")
            for item in items:
                number = item.css("td")[0].css("::text").get()
                name = item.css("td")[3].css("a").attrib["title"]
                link = item.css("td")[3].css("a").attrib["href"].split("/")[-1]
                image = (
                    item.css("td")[2].css("img").attrib["src"].replace("small", "big")
                )
                position = item.css("td")[4].css("::text").get()
                birth_date = item.css("td")[5].css("::text").get()
                try:
                    club = item.css("td")[7].css("a").attrib["title"]
                except KeyError:
                    club = None
                birthplace = item.css("td")[8].css("::text").get().strip()
                try:
                    height = float(
                        item.css("td")[9].css("::text").get().replace(",", ".")
                    )
                except (AttributeError, ValueError) as e:
                    height = None
                mv = item.css("td")[-1].css("::text").get()
                player = {
                    "number": number,
                    "name": name,
                    "link": link,
                    "image": image,
                    "position": position,
                    "birth_date": birth_date,
                    "club": club,
                    "birthplace": birthplace,
                    "height": height,
                    "mv": mv,
                }
                player_dict["players"].append(player)
            json.dump(player_dict, f, indent=4, ensure_ascii=False)
