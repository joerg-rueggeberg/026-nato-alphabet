import pandas
from art import logo

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

ger = pandas.read_csv("ger_phonetic_alphabet.csv")
ger_dict = {row.letter: row.code for (ind, row) in ger.iterrows()}

print(logo)

f_name = input("Type in your first name: ").title()
l_name = input("Type in your last name: ").title()

f_name_l = list(f_name.upper())
l_name_l = list(l_name.upper())

f_name_nato = [nato_dict[c] for c in f_name_l]
f_name_ger = [ger_dict[c] for c in f_name_l]
l_name_nato = [nato_dict[c] for c in l_name_l]
l_name_ger = [ger_dict[c] for c in l_name_l]

f_name_nato_j = ", ".join(f_name_nato)
f_name_ger_j = ", ".join(f_name_ger)
l_name_nato_j = ", ".join(l_name_nato)
l_name_ger_j = ", ".join(l_name_ger)

print(f"\nYour name in...\n"
      f"NATO-Alphabet: '{f_name_nato_j}' - '{l_name_nato_j}'\n"
      f"German-Alphabet: '{f_name_ger_j}' - '{l_name_ger_j}'")

name_as_dict = {
    "First name": f_name,
    "Last name": l_name,
    "NATO": [f_name_nato],
    "German": [l_name_nato],
}

your_nato_file = pandas.DataFrame(name_as_dict)
your_nato_file.to_csv(f"nato_alphabet_{f_name.lower()}_{l_name.lower()}.csv")

print(f"\nSaved your file as:\n"
      f"'./nato_alphabet_{f_name.lower()}_{l_name.lower()}.csv'\n\n"
      f"Preview:\n"
      f"{your_nato_file}")
