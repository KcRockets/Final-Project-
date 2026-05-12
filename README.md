Final-Project Title: BUBBLE SHOOTER GAME

Repository - https://github.com/KcRockets/Final-Project-.git

#Description: In this project, I will be creating a Bubble shooter game. The purpose of the game is to shoot down the corresponding colors of the bubble that is equipped to you. Remove all of the color in stage and then you will win. Simple as that. The game runs on 60 frames per second using Pygame's clock. 

HOW THE GAME WORKS
Starting Layout:
When the game begins, a small window will apear with a size of 480x640. 
The crowd of bubbles are on the top of the window. The way to create the rows is using create_strarting_rows()

How the Bubbles system works:
The Bubbles contain five colors. Each bubbles are under the instance of the BUBBLE class. The Colors will be randomized and positioned differently each time that game is on. 
The Bubbles can bounce off the walls, move across the screen and draw themselves onto the screen. 
Once the bubbles reach the top, it will snap onto a grid and if it the corresponding color it will disappear.

AIMING AND SHOOTING
When the game begins, there will be a line that will help aim. The mouse controls the line to aim and shoot:

This code here is what helps create the aim line and shooting: angle = math.atan2(my - shooter_y, mx - shooter_x)
- Once the bubble is shot out it will be added to the list of bubbles
- New bubbles will be added when the bubble is shot out.

COLLISION AND SNAPPING
The game will check for collision with the bubbles in the grid: (in python) if check_collision(b, g):
- Once the bubble is shot, it will snap to the nearest grid position which is thanks to: (snap_to_grid)
- if the bubbles connects to the bubble with the same color: (pop_matching)
  but that only happens if there are three or more matching bubbles connected and then they will dissapear.
- A new bubble will be loaded for the player for every bubble is shot out from the player.

Video Link: https://youtu.be/NzCD7ypN2A0
