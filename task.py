import sys


def help():
	sa = """Usage :-
$ ./task add "task" 
$ ./task ls			 
$ ./task del NUMBER	 
$ ./task done NUMBER	 
$ ./task help			
$ ./task report		 """
	sys.stdout.buffer.write(sa.encode('utf8'))


def add(s):
	
	
	f = open('task.txt', 'a')
	
	
	f.write(s)
	f.write("\n")
	f.close()
	s = '"'+s+'"'
	
	print(f"Added task: {s}")


def ls():
	try:

		nec()
		l = len(d)
		k = l

		for i in d:
			sys.stdout.buffer.write(f"{i}. {d[i]}".encode('utf8'))
			sys.stdout.buffer.write("\n".encode('utf8'))
			

	except Exception as e:
		raise e


def deL(no):
	try:
		no = int(no)
		nec()
		with open("task.txt", "r+") as f:
			lines = f.readlines()
			f.seek(0)
			for i in lines:
				if i.strip('\n') != d[no]:
					f.write(i)
			f.truncate()
		print(f"Deleted task #{no}")

	except Exception as e:
		print(f"Error: task #{no} does not exist. Nothing deleted.")


def done(no):
	try:

		nec()
		no = int(no)
		f = open('done.txt', 'a')
		st = ' '+d[no]
		f.write(st)
		f.write("\n")
		f.close()
		print(f"Marked task #{no} {d[no]} as done.")
		
		with open("task.txt", "r+") as f:
			lines = f.readlines()
			f.seek(0)
			for i in lines:
				if i.strip('\n') != d[no]:
					f.write(i)
			f.truncate()
	except:
		print(f"Error: task #{no} does not exist.")



def report():
	nec()
	try:

		nf = open('done.txt', 'r')
		c = 1
		
		for line in nf:
			line = line.strip('\n')
			don.update({c: line})
			c = c+1

		
		for i in d:
			print(f' Pending :{len(d)} {d[i] [{i}]}\n')
			
		print(f' Completed : {len(don)}')
	except:
		print(f' Pending : {len(d)}')
		for i in d:
			print(f'{i}. {d[i]} [{i}] ')
			
			
		print(f'\n Completed : {len(don)}\n')
		
		print(f'{don}')
		


def nec():
	try:
		f = open('task.txt', 'r')
		c = 1
		for line in f:
			line = line.strip('\n')
			d.update({c: line})
			c = c+1
	except:
		sys.stdout.buffer.write("There are no pending tasks!".encode('utf8'))


if __name__ == '__main__':
	try:
		d = {}
		don = {}
		args = sys.argv
		if(args[1] == 'del'):
			args[1] = 'deL'
		if(args[1] == 'add' and len(args[2:]) == 0):
			sys.stdout.buffer.write(
				"Error: Missing task string. Nothing added!".encode('utf8'))

		elif(args[1] == 'done' and len(args[2:]) == 0):
			sys.stdout.buffer.write(
				"Error: Missing NUMBER for marking task as done.".encode('utf8'))

		elif(args[1] == 'deL' and len(args[2:]) == 0):
			sys.stdout.buffer.write(
				"Error: Missing NUMBER for deleting task.".encode('utf8'))
		else:
			globals()[args[1]](*args[2:])

	except Exception as e:

		s = """Usage :-
$ ./task add "Number Of priority" "task" 
$ ./task ls			
$ ./task del NUMBER	 
$ ./task done NUMBER	
$ ./task help			 
$ ./task report		"""
		sys.stdout.buffer.write(s.encode('utf8'))
