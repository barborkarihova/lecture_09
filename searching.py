import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode = "r") as json_file:
        data = json.load(json_file)
    keys = data.keys()
    if field not in keys:
        return "None"

    return data[field]
def linear_search(sekvence, hledane_cislo):
    cisla = read_data("sequential.json", sekvence)
    positions = []
    count = 0
    i = 0
    for cislo in cisla:
        if cislo == hledane_cislo:
            count = count + 1
            positions.append(i)
        i = i + 1
    print(count)
    print(positions)
    vysledky = dict(zip(["count", "positions"], [count, positions]))
    return vysledky

    # output = {"positions" : positions, "count": count}
def pattern_search(sekvence, hledana_sekvence):
    i = 0
    delka_vzoru = len(hledana_sekvence)
    if len(sekvence) < delka_vzoru:
        return "Nelze"
    seznam_indexu = []
    while i < len(sekvence) - (delka_vzoru-1):
        sekvence_v_seznamu = sekvence[i:i+(delka_vzoru)]
        if sekvence[i] != hledana_sekvence[0]:
            i = i + 1
            continue
        if sekvence_v_seznamu == hledana_sekvence:
            seznam_indexu.append(i)
            i = i + delka_vzoru
            continue

        i = i + 1
    mnozina_indexu = set(seznam_indexu)
    return mnozina_indexu





def main():
    sekvence = read_data("sequential.json", "dna_sequence")
    print(linear_search("unordered_numbers", 54))
    print(pattern_search(sekvence, "GG"))


if __name__ == '__main__':
    main()