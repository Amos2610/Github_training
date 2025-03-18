# Github講習会  
Githubの基本情報から実践まで網羅しているパッケージです．\
このバージョンは，ROS2_Humbleを用いて行います．

## 準備するもの
- Githubアカウント
- ubuntu20.04をインストールしているパソコン
## インストール
### Step1 : ROS2 Humbleのインストール
- 依存パッケージをインストール
```bash
sudo apt update && sudo apt install gnupg wget
sudo apt install software-properties-common
sudo add-apt-repository universe
```  
- バイナリポジトリの設定
```bash
wget -qO - https://isaac.download.nvidia.com/isaac-ros/repos.key | sudo apt-key add -
echo 'deb https://isaac.download.nvidia.com/isaac-ros/ubuntu/main focal main' | sudo tee -a /etc/apt/sources.list"
```
- 確認
```bash
sudo apt update && sudo apt install curl -y \
&& sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu focal main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```
- ROSパッケージのインストール
```bash
sudo apt update
sudo apt install ros-humble-desktop-full
sudo apt install ros-dev-tools
```
### Step2 : ワークスペースの作成
```bash
mkdir < 自分の名前 >_ws/src
source /opt/ros/humble/setup.bash
```
### Step3 : クローン
```bash
cd < 自分の名前 >_ws/src
git clone https://github.com/Amos2610/Github_training.git
```
- 確認
```bash
ls
```
出力にGithub_trainingが出てきたら成功です
### Step4 : 依存パッケージのインストール
```bash
sudo apt update
sudo apt install ros-humble-turtlesim
sudo apt install xterm
cd ..
colcon build --symlink-install
source install/setup.bash
```
## 実行方法
```bash
ros2 launch my_turtle_package myturtlesim.lauch.py
```





