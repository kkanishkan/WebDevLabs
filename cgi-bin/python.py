#!/usr/bin/python

import cgi,cgitb
cgitb.enable()
form = cgi.FieldStorage()

name = form.getvalue('name')
address  = form.getvalue('address')
phone = form.getvalue('phone')

newPhone = phone.split('-')

print ("Content-type: text/html\n\n")

print "<!DOCTYPE html>\n"
print "<html>\n"
print "<head>\n"
print '<link rel="stylesheet" href="./css/style.css">'
print '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>'
print "<script>"
print "$(document).ready(function(){"

print" $('#1').animate({"
print"  right: '700px'"
print"  });"

print" $('#2').animate({"
print"  right: '500px'"
print"  });"

print" $('#3').animate({"
print"  right: '200px'"
print"  });"

print"  });"

print "</script>\n"
print "</head>\n"

print "<body>\n"
print "<h1> Results </h1>\n"
print "<p>"
print name
print '</p><br/>'

print "<p>"
print address
print '</p><br/>'

print "<p id='1' style='position:absolute; color:red; font-size:75px;'>"
print "("
print newPhone[0]
print ") "
print '</p>'

print "<p id='2' style='position:absolute; color:blue; font-size:75px;'>"
print newPhone[1]
print '</p>'

print "<p id='3' style='position:absolute; color:green; font-size:75px;'>"
print newPhone[2]
print '</p><br/>'

print "</body>\n"

print "</html>\n"