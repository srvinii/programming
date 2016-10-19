import requests
import sys

admin_pages = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']

def search():
	print '''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
+\t   #    ######  #     # ### #     # 	 \t+
+\t  # #   #     # ##   ##  #  ##    # 	\t+
+\t #   #  #     # # # # #  #  # #   # 	\t+
+\t#     # #     # #  #  #  #  #  #  # 	\t+
+\t####### #     # #     #  #  #   # # 	\t+
+\t#     # #     # #     #  #  #    ## 	\t+
+\t#     # ######  #     # ### #     #     \t+
+                              			\t+
+\t####### ### #     # ######  ####### ###### \t+
+\t#        #  ##    # #     # #       #     #\t+
+\t#        #  # #   # #     # #       #     #\t+
+\t#####    #  #  #  # #     # #####   ######\t+
+\t#        #  #   # # #     # #       #   #  \t+
+\t#        #  #    ## #     # #       #    # \t+
+\t#       ### #     # ######  ####### #     #\t+
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

[*] Version v1.0
[*] This tool was created for locate the possibles admin pages
[*] Author: Eric Vinicius (Viniicius Saw)
'''
	print "Charged [\033[0;34m%s\033[0m] Admin pages" % (len(admin_pages))
	try:
		sys.argv[1]
		url = sys.argv[1]
		find(url)
	except IndexError:
		url = str(raw_input("Target Url: \033[0;34m"))
	print "\033[0m"
	if url[0:4] != 'http':
		print 'You using HTTP protocol?'
		quit()
	find(url)

def find(url):
	try:
		if url[-1] == '/':
				qnt = len(url) - 1
				url = url[0:qnt]
		target = url
		cont_found = 0
		cont_nofound = 0
		pg_found = ""
		for page in admin_pages:
			url = target
			url += '/' + page
			con = requests.get(url)
			r = con.status_code
			if r == 200:
				sys.stdout.write('[\033[0;34m%d\033[0m] %s \033[0;34mFound\033[0m\n' %(r, url))
				sys.stdout.flush()
				cont_found += 1
				pg_found += url + '\n'
			else:
				sys.stdout.write('[\033[0;31m%d\033[0m] %s \033[0;31mNot Found\033[0m\n' %(r, url))
				sys.stdout.flush()
				cont_nofound += 1
		arq = open("results.txt", "w")
		txt = "Found Pages: \n" + pg_found
		arq.write(txt)
		arq.close()
		print "::::::::::::::::::::::::::::::::::::::::::::::::::"
		print "Found Pages: \033[0;34m %s \033[0m" %(str(cont_found))
		print "No Found Pages: \033[0;31m %s \033[0m" %(str(cont_nofound))
	except Exception as erro:
		print erro
search()

