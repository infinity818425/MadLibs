# This is a Madlib generator

#Loop back to this point once execution completes
loop = 1
while (loop < 10):
    #Questions for the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing Word): ")
    noun3 = input("Choose a noun: ")
    #Story Output based on user input
    print("-------------------------------------")
    print("Be kind to your", noun, "-footed", p_noun)
    print("For a duck may be somebody's", noun2, ",")
    print("Be kind to your", p_noun, "in", place)
    print("Where the weather is always", adjective, ",")
    print()
    print("You may think that this is the", noun3, ",")
    print("Well it is.")
    print("-------------------------------------")
    #Loop back to the beginning
    loop = loop + 1



