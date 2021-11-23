import pandas as pd 
import glob
import re

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


#new_name1 = input("File Name: ")

new_name = "qq" + ".csv"

data = pd.read_csv(new_name)


print("Data size: {}".format(data.shape))


for c in data.columns:
	print(c)

data.drop(data.columns[0], axis = 1, inplace = True)
data.drop(data.columns[0], axis = 1, inplace = True)

print("Data size: {}".format(data.shape))



data["name"] = data["name"].str.lower()
data["text"] = data["text"].str.lower()

dict = {}

for i in range(data.shape[0]):

	name = data["name"][i]

	name1 = ""

	for i in range(len(name)):
		if (name[i]==" "):
			break
		else:
			name1 = name1+name[i]


	dict[name1] = 1

print(len(dict))

tc = ""

for i in range(data.shape[0]):

	t = data["text"][i]

	tc = tc + " "+t



tcn = remove_emoji(tc)

tcn = tcn.replace("#", " ")
tcn = tcn.replace("@", " ")
tcn = tcn.replace(".", " ")
tcn = tcn.replace(",", " ")
tcn = tcn.replace("?", " ")
tcn = tcn.replace("!", " ")

def Convert(string):
    li = list(string.split(" "))
    return li
  

textlist = Convert(tcn)

print(len(textlist))



for i in textlist:
	x = str(i)
	if x in dict:
		dict[x] = dict[x] +1
    

mentions = 0

for key, values in dict.items():
	#print(key, values)
	if (values!=1):
		mentions = mentions + 1

print("Total mentions: {}".format(mentions))

