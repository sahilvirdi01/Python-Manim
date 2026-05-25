# Python-Manim

Manim - A mathematical animation engine made by 3b1b for mathematical animations 

## Requirements 

- Python 3.7  
- Operating System (Linux (Preffered), Windows, MacOS)


## Table of Contents
* [Gallery](#gallery)
* [Manim Installation](#installations)
    * [Linux Users](#Linux-Users)
    * [Windows Users](#Windows-Users)

## Installations
### Linux Users
Below aee some packages we need to install to use manim as manim heavily relies on them : `Cairo`,`sox`, `Latex` and`ffmpeg` 

```bash
sudo apt install ffmpeg sox
sudo apt-get install libcairo2-dev libjpeg-dev libgif-dev
sudo apt install texlive-latex-base texlive-full texlive-fonts-extra
```
Install Manim within a virtual environment to avoid package conflicts
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install manim
```
### Windows Users
I highly prefer Windows user to use **WSL** (Windows Subsystem for Linux) for Manim

[Know More About WSL ](/docs/what-is-wsl.md) 

#### WSL Setup
Requirements :  
* Windows 10(Build 20262+) or Windows 11   

First check if you have all the prerequisites for the installation or not
```bash
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
```

Open Terminal and run :
```bash
wsl --install
```
You can see a list of Distros by runnig :
```bash
wsl --list --online
```
But for now we will be using Ubuntu 
```bash
wsl --install -d Ubuntu
```
Follow on screen Commands to set Username and Password for Ubuntu  

Install System Dependencies
```bash 
sudo apt update && sudo apt upgrade -y
sudo apt install libcairo2-dev ffmpeg sox texlive-full
```
Install Manim within a virtual environment to avoid package conflicts
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install manim
```
## Gallery 
### Basic Shapes
| Animation | Code | Preview |
|-----------|------|---------|
| Hello World | [`HelloWorld.py`](/Code/hello_world.py) | ![Hello World](/output/HelloWorld.gif) |
| Circle | [`Circle.py`](/Code/shapes.py) | ![Circle](/output/circle.gif) |
| Square | [`Square.py`](/Code/shapes.py) | ![Square](/output/square.gif) |
| Triangle | [`Triangle.py`](/Code/shapes.py) | ![Triangle](/output/triangle.gif) |
| Multiple Shapes | [`Shapes.py`](/Code/shapes.py) | ![Multiple Shapes](/output/Shapes.gif) |
| Transform animation | [`Transform.py`](/Code/shape_Transform.py) | ![Transform](/output/Transform.gif) |
