# NTXY
Video processing tool for obtaining NTXY ground truth data



Interface for capturing NTXY

Given a file with N moving objects, how can manually trace with ease the (x,y) coordinates of the objects in each T frames?

To use the program, run the main function

main()

Press the following keys to achieve the respective results:
    
*    'l': (small L) next frame 
*    'r': previous frame
*    '+': increment object number 
*    '-': decrement object number
*    ' ': (space) go to the frame recently added clicked (coordinates added)
*    's': save/overwrite the dat file to the coordinates
*    'd': remove the most recent coordinate
*    'q': exit
*    esc: exit
    
When <fname>.avi file is open upon running the program, the <fname>.dat is attempted to read for the previous coordinates saved. The file contents, if theres any, will be used and will plotted in the screen.
When 'save' command is excuted, the old file is overwritten. 
