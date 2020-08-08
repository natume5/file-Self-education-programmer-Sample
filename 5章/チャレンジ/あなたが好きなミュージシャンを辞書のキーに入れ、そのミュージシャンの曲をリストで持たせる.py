me = {
    "Jonus blue": ["polaroid"],
    "Jax Joes": ["This Is Real"],
    "Armin van Buuren": ["This Is What It Feels Like"],
    "Alan Walker": ["Alone,Pt.Ⅱ"],
    "kygo": ["Higher Love"],
    "The Chainsmokers": ["Takeaway"],
    "Mark Ronson": ["Find U Again"],
    "Steve Aoki": ["2 In A Million"]

}

n = input("これらの中から好きなミュージシャンを入力してください。"
          "Jonus blue, Jax Joes, Armin van Buuren, Alan Walker,"
          "kygo, The Chainsmokers, Mark Ronson, Steve Aoki:")
if n in me:
    Feature = me[n]
    print(Feature)
else:
    print("見つかりませんでした。")
