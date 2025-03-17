import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, TimerAction

def generate_launch_description():
    return LaunchDescription([
        launch.actions.LogInfo(
            msg="Launch turtlesim node and turtle_teleop_key node."),
       
        launch.actions.TimerAction(
            period=3.0,  # 3秒待ってから次のアクションを実行
            actions=[
                launch.actions.LogInfo( 
                    msg="It's been three seconds since launch."
                ),
  
                Node(
                    package='turtlesim',  # パッケージ名
                    executable='turtlesim_node',  # ノードを起動する名前
                    name='turtlesim',  # ノード名
                    output='screen',  # 出力をターミナルに表示
                    parameters=[  # パラメータの設定
                        {
                            #背景の色を変更（A班）
                            'background_r': 255,
                            'background_g': 255,
                            'background_b': 0,
                            #初期位置を変更(B班)
                            'x': 5.0,
                            'y': 5.0,
                            'z': 5.0
                        }
                    ]
                )
            ]
        ),
        #亀を動かすトピックを呼び出す
        TimerAction(
            period=1.0, #1秒ごとに行う
            actions=[
                ExecuteProcess(
                    cmd=['ros2', 'topic', 'pub', '/turtle1/cmd_vel', 'geometry_msgs/msg/Twist', '{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}'], #動き方を変更（C班）
                    output='screen'
                )
            ]
        )
    ])
