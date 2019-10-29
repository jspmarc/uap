import pickle

def save_obj(obj, name): #Menyimpan dictionary ke file luar
    with open(name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name): #Me-load dictionary dari file luar
    with open(name, 'rb') as f:
        return pickle.load(f)

rGears = ["I finished game a few days ago I love the story its not perfect but its good.The game mechanics are as it's supposed to be in a shooter.its not perfect buts its a good game.You should play it"]
save_obj(rGears, "ReviewGears.txt")

rHitman = ["The 2016 HITMAN game takes the best aspects of Absolution and Blood Money and combines them in a brilliant way. While the game has flaws, it offers phenomenal Hitman gameplay."]
save_obj(rHitman, "ReviewHitman.txt")

rCivilization = ["After the most recent expansion, I now recommend this to my friends instead of Civ 5."]
save_obj(rCivilization, "ReviewCivilization.txt")

rF1 = ["Amazing Game really liked its accurate driving"]
save_obj(rF1, "ReviewF1.txt")

rTetris = ["What a lovely combination of two great puzzle series. This game is a must for all who love tetris/puyo/puzzle games. But if you like playing online, this ain't for you."]
save_obj(rTetris, "ReviewTetris.txt")

rNBA = ["There's literally a 30 second unskippable Converse ad at the beginning of games."]
save_obj(rNBA, "ReviewNBA.txt")

rSeaSalt = ["Its fun and I like the units, but the levels feel long between boss fights."]
save_obj(rSeaSalt, "ReviewSeaSalt.txt")

rWarframe = ["Really fun game to play especially if you have time to kill."]
save_obj(rWarframe, "ReviewWarframe.txt")

rArtifact = ["Straight up garbage -Dave_4901"]
save_obj(rArtifact, "ReviewArtifact.txt")

rDestiny = ["I haven't had this much fun with a game in years"]
save_obj(rDestiny, "ReviewDestiny.txt")

rTerraria = ["great game, would play again and again"]
save_obj(rTerraria, "ReviewTerraria.txt")

rMinecraft = ["Honestly I don't understand how you can give this game a bad score. It is THE game to play, regardless of age."]
save_obj(rMinecraft, "ReviewMinecraft.txt")

rSkyrim = ["Perfection."]
save_obj(rSkyrim, "ReviewSkyrim.txt")

rVR = ["This is the CS:GO of VR with community created maps and game modes"]
save_obj(rVR, "ReviewVR.txt")

rForza = ["Good graphics and sound, many cars. "]
save_obj(rForza, "ReviewForza.txt")

rGrid = ["Amazing game, it lacks unique content in tracks and cars for now, but it's still a great racing game with awesome career mode."]
save_obj(rGrid, "ReviewGrid.txt")

rDirt = ["Its great but theres not many different tracks without paying for the dlc"]
save_obj(rDirt, "ReviewDirt.txt")

rPortal = ["Portal is a game that you can just play again and again and will never get old."]
save_obj(rPortal, "ReviewPortal.txt")

rPortal2 = ["This game is even better then the first one, definitely would recommend it!:D"]
save_obj(rPortal2, "ReviewPortal2.txt")

rPostal2 = ["its fun game too lazy to make real review sorry"]
save_obj(rPostal2, "ReviewPostal2.txt")