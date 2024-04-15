import rclpy
from rclpy.node import Node 

from visualization_msgs.msg import Marker

import json
import os

class SaveMap(Node):

    export = False      # flag to export cones_positions at the end of the first lap

    blue_x = []
    blue_y = []
    yellow_x = []
    yellow_y = []
    orange_x = []
    orange_y = []
    big_orange_x = []
    big_orange_y = []

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
            if msg.colors[i].r == 0 and msg.colors[i].g == 0 and msg.colors[i].b == 1.0:
                self.blue_x.append(msg.points[i].x)
                self.blue_y.append(msg.points[i].y)
            elif msg.colors[i].r == 1.0 and msg.colors[i].g == 1.0 and msg.colors[i].b == 0:
                self.yellow_x.append(msg.points[i].x)
                self.yellow_y.append(msg.points[i].y)      
            elif msg.colors[i].r == 1.0 and msg.colors[i].g == 0.3 and msg.colors[i].b == 0:
                self.orange_x.append(msg.points[i].x)
                self.orange_y.append(msg.points[i].y)    
            elif msg.colors[i].r == 1.0 and msg.colors[i].g == 0.63 and msg.colors[i].b == 0.0:
                self.big_orange_x.append(msg.points[i].x)
                self.big_orange_y.append(msg.points[i].y)   

        if(self.export):
            self.destroy_subscription(self.cones_positions_subscriber)  # stop receiving cones
            self.get_logger().info("Cones positions subscriber destroyed")
            self.export_cones(self.blue_x, self.blue_y, self.yellow_x, self.yellow_y,self.orange_x,self.orange_y,self.big_orange_x,self.big_orange_y)

    
    def export_cones(self, blue_x, blue_y, yellow_x, yellow_y, orange_x, orange_y, big_orange_x, big_orange_y):
        #json object 
        j = {
                "blue_x" : [point for point in blue_x],
                "blue_y" : [point for point in blue_y],
           
                "yellow_x" : [point for point in yellow_x],
                "yellow_y" : [point for point in yellow_y],
            
                "orange_x" : [point for point in orange_x],
                "orange_y" : [point for point in orange_y],
            
                "big_orange_x" : [point for point in big_orange_x],
                "big_orange_y" : [point for point in big_orange_y],
        }

        app_dir = os.path.dirname(os.path.realpath(__file__))
        data_dir = os.path.join(app_dir,"data")
        filename = os.path.join(data_dir, "cones_positions.json")   


        with open(filename,'w') as f:
            json.dump(j ,f,indent=4)
            f.write('\n')
        
        self.get_logger().info(f"Cones positions saved in file {filename}")


    def waypoints_callback(self, msg: Marker):
        self.get_logger().info('Received waypoints')
        self.export = True   #cones_positions can now be exported
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
        
        with open(filename,'w') as f:     
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