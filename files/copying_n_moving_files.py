import  shutil

shutil.copy('c://spam.txt', 'c://delicious') # c://delicious//spam.txt

shutil.copytree('c://delicious', 'c://delicious_backup')

shutil.move('c://spam.txt', 'c://delicious')
