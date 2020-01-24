#!/usr/local/bin/ruby -w
puts "Content-type: text/html\n\n"
puts # this blank is needed
require 'cgi'
cgi = CGI.new
name =  cgi['name']
address =  cgi['address']
phone = cgi['phone']

newadd = address.split(/ |\_|\-/).map(&:capitalize).join(" ")
newPhone = phone.split('-')

puts "<!DOCTYPE html>\n"
puts "<html>\n"
puts "<head>\n"
puts '<link rel="stylesheet" href="./css/style.css">'
puts '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>'
puts "<script>"
puts "$(document).ready(function(){"

       puts "$('#1').fadeIn(3000);"
       puts "$('#2').fadeIn(5000);"
       puts "$('#3').fadeIn(6000); });"

puts "</script>\n"
puts "</head>\n"

puts "<body>\n"
    puts "<h1> Results </h1>\n"
    puts "<p>"
    puts name
    puts '</p><br/>'

    puts "<p>"
    puts newadd
    puts '</p><br/>'

    puts "<p id='1' style='display:none; color:red; font-size:75px;'>"
    puts "("
    puts newPhone[0]
    puts ") "
    puts '</p>'

    puts "<p id='2' style='display:none; color:blue; font-size:75px;'>"
    puts newPhone[1]
    puts '</p>'

    puts "<p id='3' style='display:none; color:green; font-size:75px;'>"
    puts newPhone[2]
    puts '</p><br/>'

puts "</body>\n"

puts "</html>\n"