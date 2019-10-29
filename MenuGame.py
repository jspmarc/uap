#Author : Dimas Meisab

# Program Menu
import MetodeBayar
import Review
import os
import pickle
import random

# Fungsi dan Prosedur

def save_obj(obj, name): #Menyimpan dictionary ke file luar
    f = open(name, 'wb')
    pickle.dump(obj,f)
    f.close()

def load_obj(name): #Me-load dictionary dari file luar
    with open(name, 'rb') as f:
        return pickle.load(f)

# Print Strip/Dash/Pembatas Sebagai Pembatas
def PrintDash():
    print('--------------------------------------------------')

# Print Menu Game
def PrintMenuGame(MG):
    print("No.\tGame\t\t\t\t\tGenre\t\tPrice\t\tRating (out of 5)")
    for i in range(20):
        # Bagian Nomor
        print(i+1, end="\t")
        # Bagian Nama Game
        NamaGame = MG[i][0]
        if(len(NamaGame)<=7):
            print(NamaGame, end="\t\t\t\t\t")
        elif(16<len(NamaGame)<18 or len(NamaGame)>18):
            print(NamaGame, end="\t\t")
        elif(7<len(NamaGame)<16):
            print(NamaGame, end="\t\t\t\t")
        else: # Selain yang Diatas
            print(NamaGame, end="\t\t\t")
        # Bagi Genre
        GenreGame = MG[i][1]
        if(GenreGame == "Strategy"
           or GenreGame == "Adventure"
           or GenreGame == "Simulation"):
            print(GenreGame, end = "\t")
        else: # Selain yang Diatas
            print(GenreGame, end=  "\t\t")
        # Bagi Harga
        print(MG[i][2], end = "\t\t")
        # Bagi Rating
        print(MG[i][3])

# Pengurutan Nama dari Abjad Awal
def SortNameAsc(MG):
    names = []; SortedMatGames = []
    for i in range(20):
        names.append(MG[i][0])
    sortedNames=sorted(names)
    for i in range(20):
        for j in range(20):
            if(sortedNames[i]==names[j]):
                k=j
                SortedMatGames.append(MG[k])
    return SortedMatGames

# Pengurutan Nama dari Abjad Akhir
def SortNameDsc(MG):
    names = []; SortedMatGames = []
    for i in range(20):
        names.append(MG[i][0])
    sortedNames=sorted(names)
    for i in range(19, -1, -1):
        for j in range(19, -1, -1):
            if(sortedNames[i]==names[j]):
                k=j
                SortedMatGames.append(MG[k])
    return(SortedMatGames)

# Pengurutan Genre dari Abjad Awal
def SortGenreAsc(MG):
    genre = []; SortedMatGamesGenreName = []
    for i in range(20):
        genre.append(MG[i][1])
    sortedGenre = ["Action",
                   "Adventure",
                   "Casual",
                   "Indie",
                   "MMO",
                   "Puzzle",
                   "Racing",
                   "RPG",
                   "Simulation",
                   "Sports",
                   "Strategy"]
    for i in range(len(sortedGenre)):
        j=0
        while(j<len(genre)):
            if(sortedGenre[i]==genre[j]):
                SortedMatGamesGenreName.append(MG[j])
            j+=1
    return SortedMatGamesGenreName

# Pengurutan Genre dari Abjad Akhir
def SortGenreDsc(MG):
    genre = []; SortedMatGenreGamesName = []
    for i in range(20):
        genre.append(MG[i][1])
    sortedGenre = ["Action",
                   "Adventure",
                   "Casual",
                   "Indie",
                   "MMO",
                   "Puzzle",
                   "Racing",
                   "RPG",
                   "Simulation",
                   "Sports",
                   "Strategy"]
    for i in range(len(sortedGenre)-1,-1,-1):
        j = 0
        while j < len(genre):
            if (sortedGenre[i] == genre[j]):
                SortedMatGenreGamesName.append(MG[j])
            j += 1
    return SortedMatGenreGamesName

# Pengurutan Harga dari yang Terkecil ke yang Terbesar
def SortPriceAsc(MG):
    price = []; SortedMatGamesPrice = []; sortedPrice = []
    for i in range(20):
        price.append(MG[i][2])
        sortedPrice.append(MG[i][2])
    sortedPrice = list(set(sortedPrice))
    sortedPrice.sort()
    for i in range(len(sortedPrice)):
        j=0
        while(j<20):
            if(sortedPrice[i]==price[j]):
                SortedMatGamesPrice.append(MG[j])
            j+=1
    return SortedMatGamesPrice

# Pengurutan Harga dari yang Terbesar ke yang Terkecil
def SortPriceDsc(MG):
    price = []; SortedMatGamesPriceName = []; sortedPrice = []
    for i in range(20):
        price.append(MG[i][2])
        sortedPrice.append(MG[i][2])
    sortedPrice = list(set(sortedPrice))
    sortedPrice.sort()
    for i in range(len(sortedPrice)-1,-1,-1):
        j=0
        while(j<20):
            if(sortedPrice[i]==price[j]):
                SortedMatGamesPriceName.append(MG[j])
            j+=1
    return SortedMatGamesPriceName

# Pengurutan Review dari Awal
def SortReviewAsc(MG):
    review = []; sortedRiview = []; SortedMatGames = []
    for i in range(len(MG)):
        review.append(MG[i][3])
        sortedRiview.append(MG[i][3])
    sortedRiview = list(set(sortedRiview))
    sortedRiview.sort()
    for i in range(len(sortedRiview)):
        j=0
        while(j<len(review)):
            if(sortedRiview[i]==review[j]):
                SortedMatGames.append(MG[j])
            j+=1
    return SortedMatGames

# Pengurutan Review dari Akhir
def SortReviewDsc(MG):
    review = []; sortedReview = []; SortedMatGames = []
    for i in range(len(MG)):
        review.append(MG[i][3])
        sortedReview.append(MG[i][3])
    sortedReview = list(set(sortedReview))
    sortedReview.sort()
    for i in range(len(sortedReview)-1,-1,-1):
        j=0
        while(j<len(review)):
            if(sortedReview[i]==review[j]):
                SortedMatGames.append(MG[j])
            j+=1
    return SortedMatGames


# Program Mulai
def main():
    # Inisiasi Array
    gGears = ["Gears 5","Action", 249999, 3.4]
    gHitman = ["Hitman", "Action", 523993, 3.6]
    gCivilization = ["Sid Meier's Civilization VI", "Strategy", 180000, 3.5]
    gF1 = ["F1 2019", "Racing", 249999, 4.0]
    gTetris = ["Puyo Puyo Tetris", "Casual", 398000, 4.1]
    gNBA = ["NBA 2K20", "Sports", 620000, 0.8]
    gSeaSalt = ["Sea Salt", "Indie", 95000, 3.7]
    gWarframe = ["Warframe", "MMO", 600000, 4.6]
    gArtifact = ["Artifact", "Strategy", 299999, 2.3]
    gDestiny = ["Destiny 2", "RPG", 740000, 3.6]
    gTerraria = ["Terraria", "Adventure", 89999, 4.9]
    gMinecraft = ["Minecraft", "Adventure", 385000, 4.8]
    gSkyrim = ["The Elder Scrolls V: Skyrim", "Adventure", 532000, 4.3]
    gVR = ["Pavlov VR", "Simulation", 89999, 4.5]
    gForza = ["Forza Motorsport 7", "Racing", 525000, 4.4]
    gGrid = ["GRID", "Racing", 249999, 2.4]
    gDirt = ["DiRT Rally 2.0", "Racing", 249999, 3.1]
    gPortal = ["Portal", "Puzzle", 69999, 4.9]
    gPortal2 = ["Portal 2", "Puzzle", 69999, 4.9]
    gPostal2 = ["Postal 2", "Action", 89999, 4.7]

    # Pembuatan Matriks
    MatrixGames = [gGears,
                gHitman,
                gCivilization,
                gF1,
                gTetris,
                gNBA,
                gSeaSalt,
                gWarframe,
                gArtifact,
                gDestiny,
                gTerraria,
                gMinecraft,
                gSkyrim,
                gVR,
                gForza,
                gGrid,
                gDirt,
                gPortal,
                gPortal2,
                gPostal2]
    
    rGears = load_obj("ReviewGears.txt")
    rHitman = load_obj("ReviewHitman.txt")
    rCivilization = load_obj("ReviewCivilization.txt")
    rF1 = load_obj("ReviewF1.txt")
    rTetris = load_obj("ReviewTetris.txt")
    rNBA = load_obj("ReviewNBA.txt")
    rSeaSalt = load_obj("ReviewSeaSalt.txt")
    rWarframe = load_obj("ReviewWarframe.txt")
    rArtifact = load_obj("ReviewArtifact.txt")
    rDestiny = load_obj("ReviewDestiny.txt")
    rTerraria = load_obj("ReviewTerraria.txt")
    rMinecraft = load_obj("ReviewMinecraft.txt")
    rSkyrim = load_obj("ReviewSkyrim.txt")
    rVR = load_obj("ReviewVR.txt")
    rForza = load_obj("ReviewForza.txt")
    rGrid = load_obj("ReviewGrid.txt")
    rDirt = load_obj("ReviewDirt.txt")
    rPortal = load_obj("ReviewPortal.txt")
    rPortal2 = load_obj("ReviewPortal2.txt")
    rPostal2 = load_obj("ReviewPostal2.txt")

    DictListReviews = {"Gears 5":rGears, "Hitman":rHitman, "Sid Meier's Civilization VI":rCivilization, "F1 2019":rF1,
                        "Puyo Puyo Tetris":rTetris, "NBA 2K20":rNBA, "Sea Salt":rSeaSalt, "Warframe":rWarframe,
                        "Artifact":rArtifact, "Destiny 2":rDestiny, "Terraria":rTerraria, "Minecraft":rMinecraft,
                        "The Elder Scrolls V: Skyrim":rSkyrim, "Pavlov VR":rVR, "Forza Motorsport 7":rForza, "GRID":rGrid,
                        "DiRT Rally 2.0":rDirt, "Portal":rPortal, "Portal 2":rPortal2, "Postal 2":rPostal2}


    MatrixGames = SortNameAsc(MatrixGames)

    while True:
        os.system("clear")
        # os.system("cls")
        PrintMenuGame(MatrixGames)
        PrintDash()
        option = int(input("What would you like to do?\n1. Sort the menu\n2. Choose the game\n3. Quit\nYour choice: "))
        PrintDash()

        #Pengurutan
        if(option == 1):
            while True:
                os.system("clear")
                #os.system("cls")
                sortingOption = int(input("Sort by what?\n1. Alphabetical Order\n2. Genre\n3. Price\n4. Review Score\nYour Choice: "))
                PrintDash()
                #Pengurutan Nama
                if(sortingOption == 1):
                    while True:
                        AscDsc = int(input("1. Ascending\n2. Descending\nYour Choice: "))
                        PrintDash()
                        os.system("clear")
                        #os.system("cls")
                        # Pengurutan Nama dari Akhir
                        if(AscDsc == 2):
                            MatrixGames = SortNameDsc(MatrixGames)
                            break
                        # Pengurutan Nama dari Awal
                        elif(AscDsc == 1):
                            MatrixGames = SortNameAsc(MatrixGames)
                            break
                        # Salah Input
                        else:
                            print("Please input a valid option!")
                    break

                # Pengurutan Genre
                elif(sortingOption == 2):
                    while True:
                        AscDsc = int(input("1. Ascending\n2. Descending\nYour Choice: "))
                        PrintDash()
                        os.system("clear")
                        #os.system("cls")
                        # Pengurutan Genre dari Akhir
                        if(AscDsc == 2):
                            MatrixGames = SortGenreDsc(MatrixGames)
                            break
                        # Pengurutan Genre dari Awal
                        elif(AscDsc == 1):
                            MatrixGames = SortGenreAsc(MatrixGames)
                            break
                        # Salah Input
                        else:
                            print("Please input a valid option!")
                    break

                # Pengurutan Harga
                elif(sortingOption == 3):
                    while True:
                        AscDsc = int(input("1. Ascending\n2. Descending\nYour Choice: "))
                        PrintDash()
                        os.system("clear")
                        #os.system(cls)
                        # Pengurutan Harga dari Akhir
                        if(AscDsc == 2):
                            MatrixGames = SortPriceDsc(MatrixGames)
                            break
                        # Pengurutan Harga dari Awal
                        elif(AscDsc == 1):
                            MatrixGames = SortPriceAsc(MatrixGames)
                            break
                        # Input Salah
                        else:
                            print("Please input a valid option!")
                    break

                # Pengurutan Review Score
                elif(sortingOption == 4):
                    while True:
                        AscDsc = int(input("1. Ascending\n2. Descending\nYour Choice: "))
                        PrintDash()
                        os.system("clear")
                        #os.system("cls")
                        # Pengurutan Review dari Akhir
                        if(AscDsc==2):
                            MatrixGames = SortReviewDsc(MatrixGames)
                            break
                        # Pengurutan Review dari Awal
                        elif(AscDsc==1):
                            MatrixGames = SortReviewAsc(MatrixGames)
                            break
                        # Input Salah
                        else:
                            print("Please input a valid option!")
                    break
                # Input Salah
                else:
                    print("Please input a valid option!")

        elif (option == 2):
            GameOption = int(input("Please choose your game: ")) - 1
            while True:
                os.system("clear")
                # os.system("cls")
                GameName = MatrixGames[GameOption][0]
                ListReview = DictListReviews[GameName]
                tempRandomNumber = random.randint(0,len(ListReview)-1)
                print("You have chosen:\t", GameName)
                print("Game genre:\t\t",MatrixGames[GameOption][1])
                print("Game price:\t\t",MatrixGames[GameOption][2])
                print("Game rating:\t\t",MatrixGames[GameOption][3])
                print("Random game review:\t",ListReview[tempRandomNumber])
                print("Payment methods:")
                print("\n1. Money Transfer\t4. Prepaid telephone credit (Telekomunikasi only) \n2. OPO\t\t\t5. Gopek \n3. DANAS\t\t6. Cancel\n")
                pilih0 = int(input("Your choice: "))
                if (pilih0 == 1):
                    MetodeBayar.Transfer(ListReview,GameName)
                    break
                elif(pilih0 == 2):
                    MetodeBayar.Ovo()
                    MetodeBayar.CekBayar(ListReview,GameName)
                    break
                elif(pilih0 == 3):
                    MetodeBayar.Dana()
                    MetodeBayar.CekBayar(ListReview,GameName)
                    break
                elif(pilih0 == 4):
                    MetodeBayar.Pulsa()
                    MetodeBayar.CekBayar(ListReview,GameName)
                    break
                elif(pilih0 == 5):
                    MetodeBayar.Gopay()
                    MetodeBayar.CekBayar(ListReview,GameName)
                    break
                elif(pilih0 == 6):
                    os.system("clear")
                    # os.system("cls")
                    break
                else:
                    print("Maaf metode pembayaran yang anda inginkan masih belum ada, silahkan memilih salah satu dari cara-cara diatas.")

        elif (option == 3):
            os.system("clear")
            #os.system("cls")
            print("Goodbye, thank you for using Uap")
            break
        #input salah
        else:
            print("Please input a valid option!")
quit