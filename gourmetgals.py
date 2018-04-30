class Dessert(object): #Class
   def __init__(self, apples=1, flour=1, sugar=1):
       self.apples = apples
       self.flour = flour
       self.sugar = sugar

def displayRecipe(): #Function Definition
   file = open("GrandmasRecipe.txt",'r')
   file_contents = file.readlines()
   recipe = [] #List
   for file_content in file_contents:
       recipe.append(file_content.strip("\n"))
   for x in recipe:
       print (x)
   return file_contents

def displayCorrect():
   file2 = open("GrandmasRecipeCorrect.txt", 'r')
   file_contents2 = file2.readlines() #File reading
   recipe2 = []
   for file_content in file_contents2: #For Loop
       recipe2.append(file_content.strip("\n"))
   for x in recipe2:
       print(x)
   return file_contents2

def ifCorrect():
   print("Amazing job! You solved the recipe mystery just in time for the party. Here's the final recipe. "
         "Be sure to write it down and save it this time ;)")
   displayCorrect()

def Check(user, correct):
   if int(user) < int(correct): #If Statement
       print ("Your guess is too low :/")
   elif int(user) > int(correct):
       print ("Your guess is too high :(")
   else:
       print ("Good guess, you're right!")

def main():

   correctApples = 10 #Assignment Statement
   correctSugar = 1
   correctFlour = 4

   print("Hello! You're hosting a party and want to make grandma's "
         "special sour apple pie. When you pull out the recipe, "
         "you realize that some of the ingredients are missing their quantities.")
   print ("Your party is in a few hours and you don't have time to make something else. "
          "Your job is to try to figure out the correct quantities before your guests "
          "arrive. Don't worry! We'll give you some helpful feedback along the way.")
   print ("Here's what you have, the first 3 items are missing their quantities:")
   print("")
   print("")
   displayRecipe() #Function Call
   print ("Let's get started!") #Print Statement

   turn = 0
   while turn < 6: #While Loop
       try: #Try Except Block
           pie = Dessert(input("How many apples?:"),input("How many cups of flour?"), input("How many cups of sugar?"))
           print ("Great! Let's try it out. Baking...")
           print("")
           print("")
           print("")

       except (NameError,TypeError):
           print("Whoops. Please enter a valid number")
           pie = Dessert(input("How many apples?:"), input("How many cups of flour?"), input("How many cups of sugar?"))
           turn += 1



       print ("Feedback for apples: ")
       Check(pie.apples, correctApples)
       print ("")
       print ("Feedback for flour: ")
       Check(pie.flour, correctFlour)
       print ("")
       print ("Feedback for sugar: ")
       Check(pie.sugar, correctSugar)
       print("")

       turn += 1 #+=

       if pie.apples == correctApples and pie.flour == correctFlour and pie.sugar == correctSugar:
           ifCorrect()
           break
       elif turn == 6:
           print("Aw man, you ran out of time and your guests are here. Guess we're serving ice cream... "
             "Here's the final recipe, write is down and save it this time ;)")
           displayCorrect()
       else:
           print ("Let's guess again!")


main()


