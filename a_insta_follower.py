

def finder(follower=follower,following=following):
	real_following=[]
	for i in following:
		t=i.find('님의 프로필 사진')
		if t>0:
			real_following.append(i[:t])

	real_follower=[]
	for i in follower:
		t=i.find('님의 프로필 사진')
		if t>0:
			real_follower.append(i[:t])	

	for i in real_following:
		if i not in real_follower:
			print(i)
