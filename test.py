
db={}
def newusr():
	promt='login desired:'
	while True:
		name=raw_input(promt)
		if db.has_key(name):
			promt='name taken,try another'
			continue
		pwd=raw_input('passwd:')
		db[name]=pwd
		break


def oldusr():
	name=raw_input('login:')
	pwd=raw_input('passwd:')
	passwd=db.get(name)
	if passwd == pwd:
		print 'welcome back ',name
	else:
		print 'login incorrect'

def showmenu():
	prompt = """
	(N)ew User login
	(E)xisting User logi
	(Q)uit
	Enter Choice"""
	done=False
	while not done:
		chosen=False
		while not chosen:
			try:
				choice=raw_input(prompt+"\n").strip()[0].lower()
			except(EOFError,KeyboardInterrupt):
				choice='q'
			print '\nYou picked : [%s]' %choice
			if choice == 'q':
				chosen=True
				done=True
			if choice == 'n':
				newusr()
			if choice == 'e':
				oldusr()

if __name__ == '__main__':
	showmenu()
				
