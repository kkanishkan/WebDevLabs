#!/usr/bin/perl

print "Content-type: text/html\n\n";

use CGI ':standard';
use strict;
use warnings; 

my $first_name = param('first_name');
my $last_name = param('last_name');
my $male = param('male');
my $female = param('female');
my $other = param('other');
my $ready = param('readiness');


print "<html>";
print "<head>";
print "<title>Hello - Form Results Page </title>";
print '<link rel="stylesheet" href="../LAB04/css/style.css">';
print '<link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">';
print "</head>";
print "<body>";
if ($first_name) {
	print "<h2>Hi $first_name";
} 
if ($last_name) {
	print " $last_name";
}
print ", please verify your information.</h2>";

if ($male) {
	print "<p>You selected $male.</p>";
} elsif ($female) {
	print "<p>You selected $female.</p>";
} elsif ($other) {
	print "<p>You selected $other.</p>";
} else {
	print "You have not disclosed gender.";
}
if($ready) {
	print "<p>You are $ready for the next lab!</p>";
} else {
	print "<p>You did not select ready or not ready.</p>";
}
print "</body>";
print "</html>";
