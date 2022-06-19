import time
import sys
import webbrowser
a_website = "https://pastebin.com/1GJqwYM8"
webbrowser.open_new(a_website)
time.sleep(10)
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
if GBOO == "Bad" or GBOO == "bad":
    print("ANS 2 CONFIRMED")
if GBOO == "Okay" or GBOO == "okay":
    print("ANS 3 CONFIRMED")
else:
    print("SAHB OS DOES NOT RECOGNIZE ANS")
    time.sleep(2.5)
    sys.exit ()

print("So You Are Having A " + GBOO + " Day As Of Right Now " + USERNAME + "")
time.sleep(3)
print("To Encourage You To Talk More And To Test Your Decision Making Abilities, I Want To Play A Game With You Called Redial.\n It's About A Suicidal Human Accidentally Calling You Instead Of The Suicide Preventation Hotline")
