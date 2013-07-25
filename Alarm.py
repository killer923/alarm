import os
import time
from Tkinter import Tk
from tkFileDialog import askopenfilename

def change_settings(first_time):
	if first_time==0:
		customizations=read_settings()
		tone=customizations[0]
		snooze=customizations[1]
	settings=open("settings.txt","w")
	settings.write("Please change only if you know what you are doing.\n")
	settings.write("If you make a mistake simply delete this file.\n")
	#set alarm tone
	if first_time:
		print "Select the alarm tone alarm tone: "
		try:
			Tk().withdraw()
		except Exception as e:
			print e
		new_tone= askopenfilename()
		print new_tone
		settings.write("Alarm tone : "+new_tone+"\n")
	else:
		print "Current alarm tone: "+tone
		print "Do you want to change the alarm tone:(Y|N) ",
		response=raw_input()
		if response=="y" or response=="Y":
			try:
				Tk().withdraw()
			except Exception as e:
				print e
			new_tone=askopenfilename()
			print new_tone
			settings.write("Alarm tone : "+new_tone+"\n")
		else:
			settings.write("Alarm tone : "+tone+"\n")
	#set snooze time
	if first_time:
		print "Enter the snooze time ( in minutes) :",
		snooze=int(raw_input())
		if snooze<1 or snooze>10:
			check=0
		check=1
		while(check<1):
			print "The range for snooze time is 1 minute to 10 minutes."
			print "Please enter snooze time again :",
			snooze=int(raw_input())
			if snooze>=1 and snooze<=10:
				check=1
		settings.write("Snooze time : "+str(snooze)+"\n")
	else:
		print "Current snooze time is :"+str(snooze)
		print "Do you want to change the snooze time? (Y|N) ",
		response=raw_input()
		if response=="y" or response=="Y":
			print "Enter the new snooze time : ",
			snooze=int(raw_input())
			while(check<1):
				print "The range for snooze time is 1 minute to 10 minutes."
				print "Please enter snooze time again : ",
				snooze=int(raw_input())
				if snooze>=1 and snooze<=10:
					check=1
		settings.write("Snooze time: "+str(snooze)+"\n")
	settings.close()
def create_settings():
	print "Looks like you are using the program for the first time."
	print "Thank you for choosing my program."
	print "Please create settings for the program, you will be able to change them in the start of new run of the program."
	change_settings(1)
def read_settings():
	try:
		settings=open("settings.txt","r")
	except:
		create_settings()
		#print"ji"
		settings=open("settings.txt","r")
	try:
		count=0
		for line in settings:
			#print count," ...",line
			if count<2:
				count=count+1
			elif count==2:
				tone=line
				tone=tone.split(":")
				#print "1==",tone
				tone[1]=tone[1].split()[0]
				tone1=tone[-1].split("/")
				#print "2==",tone1
				tone=tone[1]+":"
				#print "3==",tone
				tone1[-1]=tone1[-1].split("\\")[0]
				if len(tone1)==1:
					tone=tone+"\\"+str(tone1[0])
				else:
					for i in range(1,(len(tone1))):
						tone=tone+"\\"+str(tone1[i])
						#print "i=",i,"  ",tone
				#tone=tone1.split()
				#print tone
				#tone=tone[0]
				#print "tone="+tone
				tone=tone.split("\n")[0]
				count=count+1
				#print count,tone
			elif count==3: #read snooze time
				snooze=line
				snooze=snooze.split(":")
				snooze=snooze[1].split()
				snooze=int(snooze[0])
				#print count,snooze
		return [tone,snooze]
	except Exception as x:
		print count,x
		print "There seems to be a problem with your settings file."
		print "We will need to recreate it."
		create_settings()
		read_settings()
def ring(tone,snooze):
	#print tone,str(snooze)
	#print "Time to ring the alarm"
	while 1:
		os.startfile(tone)
		time.sleep(snooze*60)
		#ring(tone,snooze)
		print "Come on Wake up... You are Getting Late ...."


def main():
	print "Welcome"
	print "Do you want to change settings? (Y|N) ",
	response=raw_input()
	if response=="y" or response=="Y":
		change_settings(0)
	customizations=read_settings()
	#Get time to ring
	print "Set time for alarm: "
	#get hours
	print " HH : ",
	hh=int(raw_input())
	check = 0
	if hh<0 or hh>23:
		check = -1
	while check<0:
		print " Hours does not exist, please enter again: ",
		hh=int(raw_input())
		if hh<0 or hh>24:
			check = -1
		else:
			check = 0
		#get time
	print " MM : ",
	mm=int(raw_input())
	check = 0
	if mm<0 or mm>59:
		check = -1
	while check<0:
		print " Minutes does not exist, please enter again: ",
		mm=int(raw_input())
		if mm<0 or mm>24:
			check = -1
		else:
			check = 0
	#Get current time
	sys_time=time.ctime()
	sys_time=sys_time.split()
	sys_time=sys_time[3].split(":")
	sys_hh=int(sys_time[0])
	sys_mm=int(sys_time[1])
	#calculate sleeping time
	if hh<sys_hh:
		minutes=(60-sys_mm)+mm
		hours=(23-sys_hh)+hh
	elif hh==sys_hh:
		if mm<sys_mm:
			hours=23
			minutes=(60-sys_mm)+mm
		else:
			hours=0
			minutes=mm-sys_mm
	else:
		hours=hh-sys_hh-1
		minutes=(60-sys_mm)+mm
	if minutes >60:
		hours=hours+1
		minutes=minutes-60
	elif minutes<0:
		hours=hours-1
		minutes=minutes+60
	print "Alarm will ring after "+str(hours)+" hours and "+str(minutes)+" minutes."
	seconds=(hours*3600)+(minutes*60)
	#print "Alarm will ring after "+str(seconds)+" seconds."
	time.sleep(seconds)
	print "The program woke up :) \n Time for you to wake up too."
	#print customizations
	ring(customizations[0],customizations[1])


if __name__=='__main__':
	main()
