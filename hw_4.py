import math
data = list(map(int, input("0-5 ").split()))
length_of_vector_0 = math.sqrt((data[0]**2 + data[1]**2 + data[2]**2 + data[3]**2))
results = open("results.txt", "w", encoding = "utf-8")
#print(data)
recommendations = {"Green Book": 0, "Interstellar": 0, "Fight Club": 0, "Shrek":0}
with open("Оценки фильмов.txt", "r", encoding = "utf-8") as file:
    string = file.readlines()
    for i in string:
        vector = list(map(int, i.split(",")[1:]))
        print(vector)
        splitted_string = i.split(",")
        length_of_vector_1 = math.sqrt((vector[0]**2 + vector[1]**2 + vector[2]**2 + vector[3]**2))
        scal = data[0]*vector[0] + data[1]*vector[1] + data[2]*vector[2] + data[3]*vector[3]

        cos = scal / (length_of_vector_0 * length_of_vector_1)
        #print('""', scal, length_of_vector_0 * length_of_vector_1, cos)
        recommendations["Green Book"] += int(splitted_string[1]) * cos
        recommendations["Interstellar"] += int(splitted_string[2]) * cos
        recommendations["Fight Club"] += int(splitted_string[3]) * cos
        recommendations["Shrek"] += int(splitted_string[4]) * cos
        results.write("{}, {}, {}, {}, {}\n".format(splitted_string[0], int(splitted_string[1]) * cos,
                                                    int(splitted_string[2]) * cos, int(splitted_string[3]) * cos, int(splitted_string[4]) * cos))
    results.write("Reccomendations, Green Book {}, Interstellar {}, Fight Club {}, Shrek {}".format(recommendations["Green Book"],
                                        recommendations["Interstellar"], recommendations["Fight Club"], recommendations["Shrek"]))
    sorted_recommendations = {k: v for k, v in sorted(recommendations.items(), key=lambda item: item[1])}
    
    print(f"I would recommend you: {sorted_recommendations}")

results.close()
