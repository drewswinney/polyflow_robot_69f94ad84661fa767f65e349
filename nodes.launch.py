import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69fbf08087fbb7d560a68c8a",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69fbf08087fbb7d560a68c8a",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69fbff9e87fbb7d560a6c052","mode":"speed","max_speed":6.2832,"reverse":false,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69fbf0a487fbb7d560a690aa","source_node_id":"69fbf08e87fbb7d560a68ee2","source_pin_id":"rear_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69fbf08487fbb7d560a68d66",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69fbf08487fbb7d560a68d66",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69fbff9287fbb7d560a6bf31","mode":"speed","max_speed":6.2832,"reverse":false,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69fbf0b487fbb7d560a691b6","source_node_id":"69fbf08e87fbb7d560a68ee2","source_pin_id":"front_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69fbf08187fbb7d560a68cf8",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69fbf08187fbb7d560a68cf8",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69fbffa287fbb7d560a6c0dd","mode":"speed","max_speed":6.2832,"reverse":false,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69fbf0a287fbb7d560a6903e","source_node_id":"69fbf08e87fbb7d560a68ee2","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n69fbf08a87fbb7d560a68e24",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69fbf08a87fbb7d560a68e24",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"69fbff9787fbb7d560a6bfc0","mode":"speed","max_speed":6.2832,"reverse":false,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69fbf0b687fbb7d560a69222","source_node_id":"69fbf08e87fbb7d560a68ee2","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="differential_drive",
            executable="differential_drive_node",
            name="differential_drive_n69fbf08e87fbb7d560a68ee2",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69fbf08e87fbb7d560a68ee2",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"wheel_radius":0.95,"wheel_separation":0.24,"max_wheel_speed":2,"teleop_timeout_s":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c8e4b3f393789aad6f84:cmd_vel_teleop","name":"cmd_vel_teleop","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3c8e4b3f393789aad6f84:cmd_vel_automated","name":"cmd_vel_automated","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_left_motor","name":"front_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_left_motor","name":"rear_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_right_motor","name":"front_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_right_motor","name":"rear_right_motor","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69fbf0c287fbb7d560a6934c","source_node_id":"69fbf0bf87fbb7d560a692e0","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel_teleop"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69fbf0a287fbb7d560a6903e","target_node_id":"69fbf08187fbb7d560a68cf8","source_pin_id":"front_left_motor","target_pin_id":"command"},{"connection_id":"69fbf0a487fbb7d560a690aa","target_node_id":"69fbf08087fbb7d560a68c8a","source_pin_id":"rear_left_motor","target_pin_id":"command"},{"connection_id":"69fbf0b487fbb7d560a691b6","target_node_id":"69fbf08487fbb7d560a68d66","source_pin_id":"front_right_motor","target_pin_id":"command"},{"connection_id":"69fbf0b687fbb7d560a69222","target_node_id":"69fbf08a87fbb7d560a68e24","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="gamepad",
            executable="gamepad_node",
            name="gamepad_n69fbf0bf87fbb7d560a692e0",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69fbf0bf87fbb7d560a692e0",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"device_index":0,"poll_rate_hz":60,"deadzone":0.2,"max_linear_speed":2,"max_angular_speed":1,"output_mode":"diff_drive"}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":60,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c77bb3f393789aad6f62:axes","name":"axes","direction":"output","msg_type":"polyflow_msgs/GamepadAxes"},{"pin_id":"69a3c77bb3f393789aad6f62:buttons","name":"buttons","direction":"output","msg_type":"polyflow_msgs/GamepadButtons"},{"pin_id":"69a3c77bb3f393789aad6f62:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69fbf0c287fbb7d560a6934c","target_node_id":"69fbf08e87fbb7d560a68ee2","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel_teleop"}]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
    ])