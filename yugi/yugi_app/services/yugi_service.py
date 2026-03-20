import requests
from ..models import Card, CardImage, CardPrice, CardSet

API_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php?archetype=Blue-Eyes"

# Obtnere cartas
def get_cards():
    response = requests.get(API_URL)
    if response.status_code != 200:
        print(f"Error al obtener las cartas: {response.status_code}")
        return []
    return response.json().get("data", [])

# Cargar cartas
def load_cards():
    if Card.objects.count():
        return "Cartas ya cargadas"

    data = get_cards()

    for item in data:
        card = Card.objects.create(
            card_id    = item["id"],
            name       = item["name"],
            type       = item["type"],
            frame_type = item["frameType"],
            desc       = item["desc"],
            race       = item["race"],
            archetype  = item.get("archetype", ""),
            atk        = item.get("atk"),
            def_points = item.get("def"),
            level      = item.get("level"),
            attribute  = item.get("attribute", ""),
        )

        for img in item.get("card_images", []):
            CardImage.objects.create(
                card          = card,
                image_url     = img["image_url"],
                image_small   = img["image_url_small"],
                image_cropped = img["image_url_cropped"],
            )

        prices = item.get("card_prices", [{}])[0]
        CardPrice.objects.create(
            card             = card,
            tcgplayer_price  = prices.get("tcgplayer_price", "0"),
            ebay_price       = prices.get("ebay_price", "0"),
            amazon_price     = prices.get("amazon_price", "0"),
            cardmarket_price = prices.get("cardmarket_price", "0"),
        )

        for set in item.get("card_sets", []):
            CardSet.objects.create(
                card       = card,
                set_name   = set["set_name"],
                set_code   = set["set_code"],
                set_rarity = set["set_rarity"],
                set_price  = set.get("set_price", "0"),
            )

    return f"{len(data)} cartas cargadas"
