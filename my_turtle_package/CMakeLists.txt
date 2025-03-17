cmake_minimum_required(VERSION 3.8)
project(my_turtle_package)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(turtlesim REQUIRED)

# Python スクリプトやモジュールをインストール
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)

install(PROGRAMS
  scripts/my_turtle_script.py
  DESTINATION lib/${PROJECT_NAME}
)

# パッケージインデックスのマーカーをインストール
install(FILES package.xml
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
