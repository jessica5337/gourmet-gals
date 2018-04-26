class Dessert(object):
   def __init__(self, apples=1, flour=1, sugar=1):
       self.apples = apples
       self.flour = flour
       self.sugar = sugar


def displayRecipe():
   file = open("GrandmasRecipe.txt",'r')
   file_contents = file.readlines()
   recipe = []
   for file_content in file_contents:
       recipe.append(file_content.strip("\n"))
   for x in recipe:
       print (x)
   return file_contents

def displayCorrect():
   file2 = open("GrandmasRecipeCorrect.txt", 'r')
   file_contents2 = file2.readlines()
   recipe2 = []
   for file_content in file_contents2:
       recipe2.append(file_content.strip("\n"))
   for x in recipe2:
       print(x)
   return file_contents2

def ifCorrect():
   print("Amazing job! You solved the recipe mystery just in time for the party. Here's the final recipe. "
         "Be sure to write it down and save it this time ;)")
   displayCorrect()

def main():

   correctApples = 10
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
   (displayRecipe())
   print ("Let's get started!")

   turn = 0
   while turn < 6:
       try:
           pie = Dessert(input("How many apples?:"),input("How many cups of flour?"), input("How many cups of sugar?"))
           print ("Great! Let's try it out. Baking...")
           print("")
           print("")
           print("")


       except (NameError):
           print("Whoops. Please enter a valid number")
           pie = Dessert(input("How many apples?:"), input("How many cups of flour?"), input("How many cups of sugar?"))
           turn += 1

       if pie.apples == correctApples:
           print ("Good guess! You added the right number of apples")
       else:
           print ("Mmmm. Not quite the right number of apples")
       if pie.flour == correctFlour:
           print ("Sweet! You added the right amount of flour")
       else:
           print ("Yikes, wrong amount of flour")
       if pie.sugar == correctSugar:
           print ("Awesome! You added the right amount of sugar")
       else:
           print ("Whoops, wrong amount of sugar")

       turn += 1

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
