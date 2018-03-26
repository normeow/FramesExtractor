## Frames Extractor

Command line application for frames extracting. Provides FPS configuration.

### Dependencies
* python 3
* opencv 3

### Installation
Install the dependencies listed above

Clone the repo

`git clone https://github.com/normeow/FramesExtractor.git`

### Usage

`python frames_extractor.py <videofile> <frames directory> [--fps]`

`--fps` is float. i.e
`python frames_extractor.py video0.mp4 ../frames/ --fps=0.5` save frame each 2 seconds.

`python frames_extractor.py video0.mp4 ../frames/ --fps=2` save frame each 0.5 seconds.

