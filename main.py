def get_item(item_id):
    try:
        item = items[item_id]
        return item
    except (KeyError, NameError) as e:
        return {"error": str(e)}
