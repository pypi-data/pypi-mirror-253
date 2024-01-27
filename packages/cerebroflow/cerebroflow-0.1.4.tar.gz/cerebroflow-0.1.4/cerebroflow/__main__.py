
from cerebroflow.gui import GUI
import argparse


def main():
    help = f"""
                                                                                               o
  ___  ____  ____  ____  ____  ____  _____  ____  __    _____  _    _                     o
 / __)( ___)(  _ \( ___)(  _ \(  _ \(  _  )( ___)(  )  (  _  )( \/\/ )                     o                   
( (__  )__)  )   / )__)  ) _ < )   / )(_)(  )__)  )(__  )(_)(  )    (                     o
 \___)(____)(_)\_)(____)(____/(_)\_)(_____)(__)  (____)(_____)(__/\__)               ><'>

 A tool to generate and analyze kymographs from central canal csf particle flow images.

 Usage: --gui: Opens a graphical user interface
        -h:    Displays this message

 Notes/Bugs: -Smoothing method is a combination of moving average with a Golay filter
             -Test button only works once (restart required)
             -Variablity between input images is quite high

             

    """
    parser = argparse.ArgumentParser(description=help)
    
    # Add the --gui option
    parser.add_argument("--gui", action="store_true",help="Run the GUI")

    # parse the arguments
    args = parser.parse_args()

    # Check if --gui option is provided
    if args.gui:
        print("bitasse")
        Gui = GUI()
        Gui.start()
    else:
        print("No option provided. Use --gui to run the GUI function or -h for help")


    
if __name__ == '__main__':
    main()