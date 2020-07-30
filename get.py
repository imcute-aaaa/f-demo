import cgi, cgitb 


form = cgi.FieldStorage() 
uname = form.getvalue('name')
pword  = form.getvalue('url')
with open('/f-demo/users/'+uname,'r') as k:
	if pword==k.read():
		login='Access!<script>document.cookie=\'username='+uname+';password='+pword+'\'</script>'
	else:
		login='Denied.Will create a new account.<script>document.cookie=\'username='+uname+';password='+pword+'\'</script>'
if login != 'Access!<script>document.cookie=\'username='+uname+';password='+pword+'\'</script>':
	with open('/f-demo/users/'+uname,'w') as k:
		k.write(pword)
		
print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>%s</title>" % login)
print("</head>")
print("<body>")
print("<h1>%s</h1>" % login)
print("</body>")
print("</html>")
