import pandas

build_dic = pandas.read_csv("nato_phonetic_alphabet.csv")

act_data = {row.letter: row.code for (index, row) in build_dic.iterrows()}
print(build_dic)
print(act_data)
 