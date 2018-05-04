# NTXY
Video processing tool for obtaining NTXY ground truth data
Interface for capturing NTXY

NTXY is a row in a databse of moving objects.
*   N is the obj ID
*   T is the time
*   X is the x coordinate
*   Y is the y coordinate

Given a file with N moving objects, how can manually trace with ease the (x,y) coordinates of the objects in each T frames?
This program provides an interface so that an invidual can collect the xy coordinates of the objects which is a useful basis of the ground truth data in a research.

To use the program, run the main function

```python
main()
```

The bottom left of the screen containts the information about the frame *f*, and about the car *c*.

```python
  [f:T,i]   - T is the current frame number (in NTXY), and i is the num of coords in that frame
  [c:N,j]   - N is the object ID (in NTXY) while j is the total number of clicked for object N at frame T
```
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
    
The keys can be customized by editing the function *loop*.
 
When *fname*.avi file is open upon running the program, the *fname*.dat is attempted to read for the previous coordinates saved. The file contents, if theres any, will be used and will plotted in the screen.
When *save* command is excuted, the old file is overwritten. 

# Note
The number of frames per second was reduced only to 8. The actual number of frames per second is captured in the variable *fps*, while the variable *FPS* is the desired number (in this case, 8).

Key pressed after each command-eval-loop is printed in the console.
