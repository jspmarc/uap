#   Program: Review

#   Kamus
#   RatingGame, RatingUap : int
#   ReviewGame, ReviewUap : string

import time
import pickle

def save_obj(obj, name): #Menyimpan dictionary ke file luar
    with open(name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name): #Me-load dictionary dari file luar
    with open(name, 'rb') as f:
        return pickle.load(f)

DictListFileReviews = {"Gears 5":"ReviewGears.txt", "Hitman":"ReviewHitman.txt", "Sid Meier's Civilization VI":"ReviewCivilization.txt", "F1 2019":"ReviewF1.txt",
                        "Puyo Puyo Tetris":"ReviewTetris.txt", "NBA 2K20":"ReviewNBA.txt", "Sea Salt":"ReviewSeaSalt.txt", "Warframe":"ReviewWarframe.txt",
                        "Artifact":"ReviewArtifact.txt", "Destiny 2":"ReviewDestiny.txt", "Terraria":"ReviewTerraria.txt", "Minecraft":"ReviewMinecraft.txt",
                        "The Elder Scrolls V: Skyrim":"ReviewSkyrim.txt", "Pavlov VR":"ReviewVR.txt", "Forza Motorsport 7":"ReviewForza.txt", "GRID":"ReviewGrid.txt",
                        "DiRT Rally 2.0":"ReviewDirt.txt", "Portal":"ReviewPortal.txt", "Portal 2":"ReviewPortal2.txt", "Postal 2":"ReviewPostal2.txt"}

#Function and procedure initialization
def PendapatUap():
    print("Please rate our service (from 1 -- 10): ")
    while True:
        RatingUap=int(input(""))#Sama seperti di atas, memasukkan rating dari 1-10,
        if RatingUap<=0 or RatingUap>=11:#jika tidak sesuai range maka input akan diulang
            print("Please only enter an input from 1 -- 10.")
        else:
            break
    
    for i in range (0, RatingUap):
        print("*", end="")

    print()

    if 1<=RatingUap<=3:
        print("Very disappointing.") 
    elif 4<=RatingUap<=6:
        print ("OK.")
    elif 7<=RatingUap<=9:
        print("Very satisfied!")
    elif RatingUap==10:
        print("Perfect!")#Menampilkan bintang sesuai rating
    
    if RatingUap <= 4:
        #print("Kami mohon maaf pelayanan yang kami berikan kurang memuaskan!")#Apabila rating terlalu kecil,
        print("We apologize if our service is not satifying")
        #print("Tolong beri saran bagi pelayanan kami kedepannya:")#user akan diminta untuk memberi saran.
        print("Please give a suggestion so we can improve")
        ReviewUap=input("")
        print("Thank you for the suggestion!") #terima kasih sarannya + nama user
        
    else:   
        print("Thanks for your rating!") #terima kasih ratingnya + nama user
        
    print ("---Thank you for shopping in Uap!---")
    time.sleep(10)

def PendapatGame(ListReview,GameName):
    # print("Terima kasih atas pembayarannya!")
    # print("Berikan rating untuk game ini (Rating dari 1 sampai 10): ")
    print("Thank you for buying your game in Uap!")
    print("Please rate the game you just bought (Rating from 1 to 10): ")

    while True:
        RatingGame = int(input("")) #akan dimasukkan input antara 1-10. jika tidak sesuai range,
        if ((RatingGame <= 0) or (RatingGame >= 11)): #maka akan diingatkan supaya sesuai range,
            print("Please only enter an input from 1--10.") #dan input akan diulang.
        else: 
            break

    for i in range(RatingGame):
        print("*", end="") #Menampilkan bintang sesuai dengan rating yang diberikan.

    print()
    
    if 1<=RatingGame<=3:
        print("Not a good game...") 
    elif 4<=RatingGame<=6:
        print ("OK.")
    elif 7<=RatingGame<=9:
        print("Good!")
    elif RatingGame==10:
        print("Perfect!") #Menampilkan komentar tambahan sesuai rating.

    print("Please write your review for this game:") 

    ReviewGame=input("")
    #nanti RatingGame dan ReviewGame di append ke array review pada laman game

    ListReview.append(ReviewGame)

    FileName = DictListFileReviews[GameName]

    save_obj(ListReview, FileName)

    print("Thank you for your review!")
    PendapatUap()

#Algorithm
def main():
    None
    #code untuk balik ke search menu