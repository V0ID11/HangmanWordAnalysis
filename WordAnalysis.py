import pandas as pd


with open("google-10000-english-no-swears.txt","r") as f:
    words = []
    for line in f:
        words.append(line.strip())

    words_df = pd.DataFrame(words,columns=["word"])

    words_df.head()