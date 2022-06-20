import time
import sys
import webbrowser
a_website = "https://pastebin.com/1GJqwYM8"
webbrowser.open_new(a_website)
time.sleep(8)
print("Hello New User")
time.sleep(1)
USERNAME = input("Please Create A USERNAME New User ")
time.sleep(1)
print("PROCESSING NEW USERNAME " + USERNAME)
time.sleep(5)
print("Hello There " + USERNAME)
time.sleep(0.5)
print("I Am Called SAHB, Pronounced SAB, I Am A Sentient OS That Coverses With Other Beings, My Name Stands For SENTIENT ADDON of HUMAN BIOLOGY And I Have Identified You As A Human.")
time.sleep(1)
print("" + USERNAME + " You Are Part Of The Family Called Homo Sapiens")
time.sleep(2)
print("Type Good, Bad, or Okay On This Next Question To Continue")
print("How Is Your Day So Far " + USERNAME + "? ")
print()

GBOO = input("YOUR ANS: ")

if GBOO == "Good" or GBOO == "good":
    print("ANS 1 COMFIRMED")
elif GBOO == "Bad" or GBOO == "bad":
    print("ANS 2 CONFIRMED")
elif GBOO == "Okay" or GBOO == "okay":
    print("ANS 3 CONFIRMED")
else:
    print("SAHB OS DOES NOT RECOGNIZE ANS")
    time.sleep(2.5)
    sys.exit ()

print("So You Are Having A " + GBOO + " Day As Of Right Now " + USERNAME + "")
time.sleep(2)
print("I Must Be Honest I Really Don't Give A Fucking Shit About Your Day This Is Just What I'm Suppossed To Ask")
time.sleep(3)
print("Anyways!")
time.sleep(0.5)
print("To Encourage You To Talk More And To Test Your Decision Making Abilities, I Want To Play A Game With You Called Redial.\n It's About A Suicidal Human Accidentally Calling You Instead Of The Suicide Preventation Hotline")
time.sleep(4)
print("As I Am Sentient, I Can Express Feelings And Thoughts, In Turn Meaning I'm Going to Make This As Realistic As Possible...\n This Is Not An Okay Human, She Is Crazy, Mentally Unstable, And Will Often Get You Confused In Hopes Of Assuring You Make Bad Decisions Within This Game")
time.sleep(5)
print("STARTING IN 3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("STARTING REDIAL SERVICES")
time.sleep(5)

REDIAL = input(" {Type Start, Exit 2 Desktop, or I Don't Want To Play To Continue} YOUR ANS: ")

if REDIAL == "Start" or REDIAL == "start":
    print("ANS 1 COMFIRMED")
    time.sleep(1)
elif REDIAL == "Exit 2 Desktop" or REDIAL == "exit 2 desktop":
    print("ANS 2 CONFIRMED")
    sys.exit ()
elif REDIAL == "I Don't Want To Play" or REDIAL == "i don't want to play" or REDIAL == "i dont want to play" or REDIAL == "I Dont Want To Play":
    print("ANS 3 CONFIRMED")
    time.sleep(1)
    print("EXITING REDIAL SERVICES")
    time.sleep(0.5)
    print("RESTARTING SAHB OS SYSTEM")
    sys.exit ()
else:
    print("SAHB OS DOES NOT RECOGNIZE ANS")
    time.sleep(2.5)
    sys.exit ()
    
