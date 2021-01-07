import logging
import logging.handlers
import os

handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", "errorlogs.log"))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

def main():
 user_name = input('What is you name?')
 print(f'\nWelcome {user_name}! you have been tasked with reparing the engine, repair it before it explodes. You have three lives to find all the parts to repair it.') 
    
 return user_name

 def get_room_activity(direction,rooms,directions,items,puzzles,answers,codes,life_counter,my_items):
   
  idx = rooms.index(direction)
  if items[idx] in my_items:
      print('\nYou have already been in this room and collected the item. You have been ejected back to the main room!')
  else:
      print(f'\nYou are in the {directions[idx]} room! You must answer the following puzzle correctly...')
      answer = input(puzzles[idx])
      if answer == answers[idx]:
          print(f'\nWell done! You answered correctly. You get the {items[idx]}. The code part for this room is {codes[idx]}.')
          my_items.append(items[idx])
      else:
          life_counter -= 1
          print(f'That was wrong! You lose a life. You have {life_counter} lives remaining.')
  def main():
   rooms = ['N','E','S','W''up','down','left''right','n','N','e','E','s','S','w','W']
   directions = ['North','East','South','West']
   items = ['rope','tin opener','wire cutters','corkscrew']
   puzzles = ['2 + 3 = ','3 + 4 = ','5 + 6 = ','6 + 6 = ']
   answers = ['5','7','11','12']
   codes = ['rgzs','afes','wupw','pqnd']
   life_counter = 3
   my_items = []
   return my_items,life_counter

 def check_lives(life_counter):
  if life_counter < 1:
    print('\nYou are out of lives! Game over...')
    exit()

 def check_items(my_items,codes,life_counter):
  if len(my_items) == 4:
    print('\nWell done! You have collected all of the items.')
    while True:
        code = input('\nYou must now enter the final code. The order is important. The code should follow the order of the rooms - NESW: ')
        separator = ''
        if code == separator.join(codes):
            print('\nCongratulations! That is correct. You have saved the base!')
            exit()
        else:
            life_counter -= 1
            print(f'\nUhoh, that was wrong! You lose a life. You have {life_counter} lives remaining. Try the code again.')
        check_lives(life_counter)



  while True:
      direction = input('\nYou are in the main room. \nWhich direction would you like to go? \nPlease enter N (North), E (East), S (South) or W (West): ')

      try:
          my_items, life_counter = get_room_activity(direction,rooms,directions,items,puzzles,answers,codes,life_counter,my_items)
      except:
          print("\nSorry, I didn't quite catch that.")
          logging.exception("Exception in main()")

      check_lives(life_counter)        
      check_items(my_items,codes,life_counter)





if __name__ == '__main__':
    main()
