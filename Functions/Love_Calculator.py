name1 = input("Type the First Full Name:\n").lower()
name2 = input("Type the Second Full Name:\n").lower()
def calculate_love_score(name1, name2):


    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t_count = lower_names.count("t")
    print(f"T:{t_count}")
    r_count = lower_names.count("r")
    print(f"R:{r_count}")
    u_count = lower_names.count("u")
    print(f"U:{u_count}")
    e_count = lower_names.count("e")
    print(f"E:{e_count}")
    true_count = (t_count+r_count+u_count+e_count)
    print(f"Total:{true_count}")

    l_count = lower_names.count("l")
    print(f"L:{l_count}")
    o_count = lower_names.count("o")
    print(f"O:{o_count}")
    v_count = lower_names.count("v")
    print(f"V:{v_count}")
    print(f"E:{e_count}")
    love_count = (l_count + o_count + v_count + e_count)
    print(f"Total:{love_count}")

    true_love = (true_count*10) + love_count
    print(f"Love Score:{true_love}")

calculate_love_score(name1,name2)

#calculate_love_score(name1 = "Dmitry Kuznets", name2 = "Viktoria Motznie")
