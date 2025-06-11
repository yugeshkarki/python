phase1="click this"
phase2="Buy now"
phase3="get money"
phase4="subscribe this"

msg=input("enter the message : ")
if(phase1 in msg or phase2 in msg or phase3 in msg or phase4 in msg):
    print("this msg is spam")

else:
    print("this message is not a spam")