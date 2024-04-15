import json
import matplotlib.pyplot as plt

#the script has to be placed in the same folder of the waypoints and cones_positions json filea

class DrawMap():
    def draw_map(self):
        
        # works only with a single json object in the file 
        with open("waypoints.json", 'r') as f_waypoints:
            waypoints = json.load(f_waypoints)
            waypoints_x = waypoints["X"]
            waypoints_y = waypoints["Y"]

        

        with open("cones_positions.json") as f_cones_pos:
            cones_positions = json.load(f_cones_pos)
            
            blue_x = cones_positions["blue_x"]
            blue_y = cones_positions["blue_y"]

            yellow_x = cones_positions["yellow_x"]
            yellow_y = cones_positions["yellow_y"]

            orange_x = cones_positions["orange_x"]
            orange_y = cones_positions["orange_y"]

            big_orange_x = cones_positions["big_orange_x"]
            big_orange_y = cones_positions["big_orange_y"] 


        plt.scatter(waypoints_x,waypoints_y, color = 'red')
        plt.scatter(blue_x,blue_y, color = 'blue')
        plt.scatter(yellow_x,yellow_y,color = 'yellow')
        plt.scatter(orange_x,orange_y,color = 'orange')
        plt.scatter(big_orange_x,big_orange_y,color='orange')

        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Track representation")
        plt.legend()
        plt.grid(True)
        plt.show() 


def main(args=None):
    drawMap = DrawMap()
    drawMap.draw_map()

if __name__ == '__main__':
    main()



    