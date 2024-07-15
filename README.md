### How to use it

- launch **lap_counter**
- launch **waypoint_generator**
- ros2 launch save_map save_map_launch.py
- ros2 bag play [bag_name]

At the end of the bag execution. Two files named "waypoints.json" and "cones_positions.json" are created/modified in the data **/Data** folder.                                                               

### Draw the map

In the **/Data** folder execute:

```bash
$python3 draw_map.py
```

The script takes the cones_positions from the files "cones_positions.json" and "waypoints.json", and draws the map of the track using matplotlib.

@mmr_driverless