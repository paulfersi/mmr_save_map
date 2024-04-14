import rclpy
from rclpy.node import Node 

from visualization_msgs.msg import Marker

import json
import os

class SaveMap(Node):

    export = False      # flag to export cones_positions at the end of the first lap

    blue = {
        "x" : [],
        "y" : [],
    }
    yellow = {
        "x" : [],
        "y" : [],
    }
    orange = {
        "x" : [],
        "y" : [],
    }
    big_orange = {
        "x" : [],
        "y" : [],
    }

    def __init__(self):
        super().__init__('save_map')
        self.export = False

        #subscriptions
        self.cones_positions_subscriber = self.create_subscription(Marker,'/slam/cones_positions',self.cones_positions_callback,10)
        self.waypoints_subscriber = self.create_subscription(Marker,'/planning/waypoints_all',self.waypoints_callback,10)

        self.get_logger().info("Save map node initialized")
    
    def cones_positions_callback(self, msg: Marker):
        self.get_logger().info('Received cones position')

        for i in range(len(msg.points)):
            if msg.colors[i].r < 0.1 and msg.colors[i].g <0.1 and msg.colors[i].b <0.9:
                self.blue["x"].append(msg.points[i].x)
                self.blue["y"].append(msg.points[i].y)
            elif msg.colors[i].r < 0.1 and msg.colors[i].g <0.1 and msg.colors[i].b <0.9:
                self.yellow["x"].append(msg.points[i].x)
                self.yellow["y"].append(msg.points[i].y)      
            elif msg.colors[i].r >0.9 and msg.colors[i].g >0.3 and msg.colors[i].b <0.1:
                self.orange["x"].append(msg.points[i].x)
                self.orange["y"].append(msg.points[i].y)      
            elif msg.colors[i].r >0.9 and msg.colors[i].g >0.6 and msg.colors[i].b <0.1:
                self.big_orange["x"].append(msg.points[i].x)
                self.big_orange["y"].append(msg.points[i].y)   

        if(self.export):
            self.destroy_subscription(self.cones_positions_subscriber)
            self.get_logger().info("Cones positions subscriber destroyed")
            self.export_cones(self.blue,self.yellow,self.orange,self.big_orange)

    
    def export_cones(self, blue, yellow, orange, big_orange):

        self.get_logger().info("------------DEBUG-------------")
        self.get_logger().info(f"Blue contains x: {len(blue["x"])} , y: {len(blue["y"])}")
        self.get_logger().info(f"Yellow contains x: {len(yellow["x"])} , y: {len(yellow["y"])}")
        self.get_logger().info("------------------------------")

        j = {
            "blue": {
                "blue_x" : [point["x"] for point in blue],
                "blue_y" : [point["y"] for point in blue]
            },
            "yellow": {
                "yellow_x" : [point["x"] for point in yellow],
                "yellow_y" : [point["y"] for point in yellow]
            },
            "orange": {
                "orange_x" : [point["x"] for point in orange],
                "orange_y" : [point["y"] for point in orange]
            },
            "big_orange": {
                "big_orange_x" : [point["x"] for point in big_orange],
                "big_orange_y" : [point["y"] for point in big_orange]
            }
        }

        app_dir = os.path.dirname(os.path.realpath(__file__))
        data_dir = os.path.join(app_dir,"data")
        filename = os.path.join(data_dir, "cones_positions.json")   


        with open(filename,'a') as f:
            json.dump(j ,f,indent=4)
            f.write('\n')
        
        self.get_logger().info(f"Cones positions saved in file {filename}")


    def waypoints_callback(self, msg: Marker):
        self.get_logger().info('Received waypoints')
        self.export = True   #cones_positions can be exported
        j = {} #json object
        waypoints = {
            "x" : [],
            "y" : [],
        }

        for i in range(len(msg.points)):
            waypoints["x"].append(msg.points[i].x)
            waypoints["y"].append(msg.points[i].y)
        
        j["X"] = waypoints["x"]
        j["Y"] = waypoints["y"]

        app_dir = os.path.dirname(os.path.realpath(__file__))
        data_dir = os.path.join(app_dir,"data")
        filename = os.path.join(data_dir, "waypoints.json")  
        
        with open(filename,'a') as f:     
            json.dump(j,f,indent=4)
            f.write('\n')
        self.get_logger().info(f"Waypoints saved in file {filename}")



def main(args=None):
    rclpy.init(args=args)
    node = SaveMap()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()