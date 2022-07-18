# Table of Contents

- [What is AIDDR](#what-is-aiddr)
- [How to play AIDDR](#how-to-play-aiddr)
- [Setting up environment](#setting-up-environment)
- [Credits](#credits)

# What is AIDDR

DDR(Dance Dance Revolution) is a series of video games made by Konami in which players step on arrows on a large pad or mat to match the arrows on screen. The arrows are in time with the music. Because players are moving themselves along to the music, they look like they are dancing.

With Artificial Intelligence, you can now have fun at home. Instead of a large pad, all you need is a camera. Artificial Intelligence will judge your motion and score accordingly.

# How to play AIDDR

Stretch out your arms and legs as the arrows reach the bottom of the screen. For example, if it's a top-left arrow, top means you should use your arm, and left means you should use your left arm/leg. So, in this case, just stretch out your left arm when that arrow reach the bottom of the screen.

# Setting up environment

Using anaconda as an example:

0. Start a command prompt and enter the directory of aiddr

1. Create a new environment with python version 3.8

	*python 3.10 is not supported, and other versions are not tested.*

	`$conda create -n aiddr python=3.8`

2. Install most packages using pip

	`$pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

3. Install PyAudio using conda

	*sometimes pip fails to install PyAudio, so using conda may be a better choice*

	`$conda install pyaudio`

4. Run main.py

	`$python main.py`

# Credits

AIDDR@AI001-AIDDR team 2022

Team members:

SYLG, catanduni, derivative233

Special thanks to:

Big_True