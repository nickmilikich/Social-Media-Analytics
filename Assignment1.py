import tweepy
import numpy as np

# Returns a string of the second word on the first line where flag is the first word
# Used for reading in keys for API from Keys file
def read(f, flag):
	for line in f:
		words = line.split()
		if words[0] == flag:
			return words[1]
	return ""

# Returns a list of numbers stored in a file, one per line
# Pass in true if the numbers should include decimals (floats), false if not (ints)
def get_nums(f, decimal):
	nums = []
	if (decimal):
		for line in f:
			nums.append(float(line))
	else:
		for line in f:
			nums.append(int(line))
	return nums

# Reads keys in from file
key_file = open("Keys.dat", 'r')
consumer_key = read(key_file, "consumer_key")
consumer_secret = read(key_file, "consumer_secret")
access_token = read(key_file, "access_token")
access_token_secret = read(key_file, "access_token_secret")
key_file.close()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Reads IDs of users in from file
id_file = open("IDs.dat", 'r')
users = get_nums(id_file, False)
id_file.close()

########
# Task 1
########

# Create result file
result_file = open("Assignment1_1_output.txt", 'w')

# Print to result file
for id in users:
	user = api.get_user(id)
	result_file.write("Profile Information for User ID: " + str(id) + "\n")
	result_file.write("Screen Name: " + "@" + user.screen_name + "\n")
	result_file.write("User Name: " + user.name + "\n")
	result_file.write("User Location: " + user.location + "\n")
	result_file.write("User Description: " + user.description.encode("utf-8") + "\n")
	result_file.write("Numer of Followers: " + str(user.followers_count) + "\n")
	result_file.write("Number of Friends: " + str(user.friends_count) + "\n")
	result_file.write("Number of Statuses: " + str(user.statuses_count) + "\n")
	result_file.write("User URL: " + user.url + "\n")
	result_file.write("\n\n\n\n")

result_file.close()

########
# Task 2
########

# Create result file
result_file = open("Assignment1_2_output.txt", 'w')

# Print to result file
for id in users:
	user = api.get_user(id)
	result_file.write("Friends of: " + str(id) +  " (@" + user.screen_name +  ")" + "\n")
	for friend in user.friends():
		result_file.write(friend.screen_name + "\n")
	result_file.write("\n")
	result_file.write("Followers of: " + str(id) +  " (@" + user.screen_name +  ")" + "\n")
	for follower in user.followers():
		result_file.write(follower.screen_name + "\n")
	result_file.write("\n\n\n\n")

result_file.close()

########
# Task 3
########

keyword_file = open("Keywords.dat", 'r')
keywords = keyword_file.readlines()
keyword_file.close()

# Removes newline escape characters for all words except the last
for i in range(0, len(keywords) - 1):
	keywords[i] = keywords[i][:-1]

query = ""
for word in keywords:
	query = query + word + " OR "
query = query[:-4] # Removes the last " OR "

result_file = open("Assignment1_3a_output.txt", 'w')

search_results = api.search(q = query, count = 50)

for i in search_results:
	result_file.write(i.text.encode("utf-8") + "\n\n\n\n")

result_file.close()



coord_file = open("Region.dat", 'r')
coord = get_nums(coord_file, True)
coord_file.close()

center_lat = (coord[1] + coord[3]) / 2.0
center_long = (coord[0] + coord[2]) / 2.0
# Radius is the distance from the center to one of the corners
# Converts lat/long to distance, formula from https://gis.stackexchange.com/questions/142326/calculating-longitude-length-in-miles
xdist = (center_lat - coord[1]) * 69.0
ydist = (center_long - coord[0]) * (69.0 * np.cos(center_lat * np.pi / 180.0))
rad = np.sqrt(xdist ** 2.0 + ydist ** 2.0)
geo = str(center_lat) + "," + str(center_long) + "," + str(rad) + "mi"

result_file = open("Assignment1_3b_output.txt", 'w')

search_results = api.search(q = "*", geocode = geo, count = 50)

for i in search_results:
	result_file.write(i.text.encode("utf-8") + "\n\n\n\n")

result_file.close()



















