# Manim tests and examples
<p align="center">
    <img src="images/intro.gif" alt="Logo" height="150px">
<p>

## Introduction
This repository is a simple notebook to keep track of progress on manim  
***

## Table of Contents
* [Exemples](#examples)
* [Configuration](#configuration)
***

## Examples
### First tutorial
<p align="center">
    <img src="images/first_tutorial.gif" alt="Logo" height="150px">
<p>

```python
class Main(Scene):
    def construct(self):
        self.camera.background_color = "#252e42"
        cercle = Circle(color=RED).scale(1)
        submark = (Text("First tutorial")
                                        .set_color("#ffe3c8")
                                        .scale(0.5)
                                        .to_edge(UP)
                                        .set_color_by_gradient([PINK, BLUE, RED])
                                                    )
        mob = Dot(radius=2.0).set_color_by_gradient([PINK, BLUE, RED])
        
        self.play(Create(cercle))
        self.play(Write(mob), run_time = 1.4)
        self.play(Transform(cercle, submark), run_time = 1)
        self.wait(2)    
```
***

## Configuration
### Manim resolution
To change manim resolution you have to create a manim config file. The file should be name `manim.cfg` and the file should be in the main directory.

Be aware of manim resolution issue; in official documentations you can find `frame_size` and `frame_hieght` parameters, it can rease graphical issue, the best way to change output video size, is to change `pixel_width` and `pixel_height`.

`video_dir` is the directory of output file. If you want to use manim previewer in Vscode it will be easier to you to have a one fixed output directory name, by default manim generate a generic name from resolution and frame rate of the output file, whene the manim-sideviewer is tracking only "media/videos/1080p60/" directory.

Here is a simple example of config file:
```cfg
[CLI]
#manim settings
pixel_width = 1920
pixel_height = 1080

#For test and debug 15 fps is recommended
frame_rate =  15
flush_cache = True
video_dir = ./output/

#manim plagun settings
manim-sideview.videoDirectory = ./output/
```
***
Update is comming soon