def calculator_love_score(name1 , name2):
    combined_word = name1 + name2
    lower_names= (name1 + name2).lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")

    first_num = t+r+u+e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")

    second_num = l+o+v+e

    final_score = int(str(first_num)+str(second_num))
    print(f"love_score is : {final_score}")

calculator_love_score("Divya" , "Chakri")