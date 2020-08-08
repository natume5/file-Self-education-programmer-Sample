me = {
    "height": "6",
    "fav_color": "blue",
    "fav_musican": ["Jonus blue", "Jax Joes", "Armin van Buuren"]
}

answer = input("input the height, fav_color or fav_musican:")
if answer in me:
    result = me[answer]
    print(result)
