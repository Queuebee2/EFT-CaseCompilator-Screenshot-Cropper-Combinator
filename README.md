# CaseCompilator
Have you ever wanted to compile all the loot you found together into one big screenshot? Well I did and now I'm trying to find, create and weave together scripts to achieve this.


## Current features
 - `case_crop`
 > crops escape from tarkov screenshots by trying to find upper left and lower right corners of containers.
 - `case_concatenator`
 > concatenates all the cropped stuff vertically. Or you could add custom images to the output folder and see them be mozaiced together


## Usage
The scripts come with some dummy data. Put any screenshots you want cropped in the `input` directory, then run the `case_crop.py` script to try and crop them. The output will be in the `output` directory, obviously. Running `case_concatenator.py` Will try and weave the images together at max resolution. The big screenshot will be **called big long boi**.


## (potential) issues to watch out for
- Filenames are coded by windows filenaming standards (or by no standards whatsoever, really) So that could cause potential issues.
- I haven't tested it in any other resolution than **1920x1080**


## todo
- make it a commandline tool
- make it smarter
  - find multiple containers, crop them separately
  - find individual items
    - parse individual items to a textfile (summation of inventory contents)
  - add scripts to automatically take screenshots (and open containers if allowed??) somehow.
- dont crop images that can't be cropped (non-inventory screenshots)


## Inspiration
I got the idea mostly from
[Atomiser's Muledump](https://github.com/atomizer/muledump) (now forked and active in a different repo)


## contact
Feel free to help or use the issue feature to create issues
