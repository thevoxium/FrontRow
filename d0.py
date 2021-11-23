import pandas as pd 
import glob


new_name1 = input("File Name: ")

new_name = new_name1 + ".csv"

data = pd.read_csv(new_name)


print("Data size: {}".format(data.shape))


for c in data.columns:
	print(c)


col1 = data.columns[0]

for i in range(data.shape[0]):
	
	if (len(data[col1][i])>7):
		data.drop([i], inplace = True)



print("Data size: {}".format(data.shape))

data.rename(columns={col1: '#User_ID#'}, inplace = True)

user_group1 = input("Enter Group ID: ")

user_group =  "USER_GROUP_"+user_group1


data["#Group_ID#"] = ""

#for i in range(data.shape[0]):
#	data["#Group_ID#"][i] = user_group

data['#Group_ID#'] = data['#Group_ID#'].replace([""],user_group)

df2 = {'#User_ID#': '#FIN#', '#Group_ID#': ""}
data = data.append(df2, ignore_index = True)

data.to_excel("final_cleaned.xlsx", index = False)
