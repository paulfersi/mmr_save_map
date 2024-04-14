import json
import matplotlib.pyplot as plt

# ATTENZIONE NON FUNZIONA ANCORA
def extract_waypoints(waypoints_file):
    with open(waypoints_file, 'r') as f:
        data = json.load(f)

    for key,value in data.items():
        waypoints_x = value["X"]
        waypoints_y = value["Y"]
    

def extract_cones_positions(cones_positions_file):
    with open(cones_positions_file) as f:
        data = json.load(f)

    for key,value in data.items():
        blue_x = value.get("blue_x",[])
        blue_y = value.get("blue_y",[])

        yellow_x = value.get("yellow_x",[])
        yellow_y = value.get("yellow_y",[])

        orange_x = value.get("orange_x",[])
        orange_y = value.get("orange_y",[])

        big_orange_x = value.get("big_orange_x",[])
        big_orange_y = value.get("big_orange_y",[])

def draw(waypoints_x,waypoints_y,blue_x,blue_y,yellow_x,yellow_y,orange_x,orange_y,big_orange_x,big_orange_y):
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

def main():
    #TODO

if __name__ == '__main__':
    main()



    