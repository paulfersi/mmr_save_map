import json
import matplotlib.pyplot as plt

#the script has to be placed in the same folder of the waypoints and cones_positions json filea

class DrawMap():
    def draw_map(self):
        with open("waypoints.json", 'r') as f_waypoints:
            waypoints = json.load(f_waypoints)

        for key,value in waypoints.items():
            waypoints_x = value["X"]
            waypoints_y = value["Y"]

        with open("cones_positions.json") as f_cones_pos:
            cones_positions = json.load(f_cones_pos)

        for key,value in cones_positions.items():
            blue_x = value.get("blue_x",[])
            blue_y = value.get("blue_y",[])

            yellow_x = value.get("yellow_x",[])
            yellow_y = value.get("yellow_y",[])

            orange_x = value.get("orange_x",[])
            orange_y = value.get("orange_y",[])

            big_orange_x = value.get("big_orange_x",[])
            big_orange_y = value.get("big_orange_y",[])

            plt.scatter(waypoints_x,waypoints_y, color = 'red')
            plt.scatter(blue_x,blue_y, color = 'blue')
            plt.scatter(yellow_x,yellow_y,color = 'yellow')
            plt.scatter(orange_x,orange_y,color = 'orange')
            plt.scatter(big_orange_x,big_orange_y,size=4,color='orange')

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



    