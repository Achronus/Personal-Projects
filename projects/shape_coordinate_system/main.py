#-----------------------------------------------------------------------
# File Title: Main function
# File Description: Used to run the program. 
#-----------------------------------------------------------------------
from menu import Menu

#-----------------------------------------------------------------------
# Num: 1 | Title: main()
#-----------------------------------------------------------------------
def main():
  """
  Consists of the main functionality of the script.
  """
  # Create menu class
  m = Menu()

  # Display the main menu
  m.main_menu()

  # Run the program
  while(True):
    m.get_command()

# Run main function
if __name__ == "__main__": main()