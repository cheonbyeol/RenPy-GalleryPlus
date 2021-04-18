# GalleryPlus README

GalleryPlus is a class that extends the functionality of RenPy's built-in Gallery class.  
Developed on Renpy 7.4.4.1439.

To use it, it's enough to paste the gallery_definition.rpy file somewhere in the game folder of your RenPy project.

The gallery_example.rpy provides a working example, with defining color images (no outside resource needed!) and a gallery screen with several pages.  
Downloading and pasting that into your own RenPy project (and creating a button that opens screen gallery) should be enough for testing. For your convenience, this folder contains a full, mostly bare RenPy project that includes this gallery. 

## Additional features of GalleryPlus:
* *looping* of the viewed images: show first image again after last (and vica versa), rather than exiting
* NextButton and PreviousButton actions implemented for faster navigation
* a *pages* system: allows you to group your images into collections that can be navigated separately or together, for the convenience of handling several gallery pages from one place
* a mode to only exit viewer mode on explicit return: if looping is off, stay on the same image when you reach the last (or first) showable image
* For a detailed documentation of these features, go into the code and find [documentation.md](https://github.com/cheonbyeol/RenPy-GalleryPlus/blob/main/documentation.md)!

## Updated gallery viewer and gallery navigation screens
* includes the new action buttons
* keyboard navigation (the example gallery screen includes the explanation of the keys)
* displays image numbers (clues in the player on how many images or variations they have yet to unlock)
* allows the user to hide and re-show the interface with a button press

## Behavior change
* With the "right" settings, the original Gallery allows you to navigate to and see unlocked images hidden behind locked buttons. GalleryPlus doesn't show any image from locked buttons.

## Update log
* First release on 18th April 2021

## Disclaimer, etc.
The code is provided "as is", no warranty included.  
It's licensed under LGPLv2.1, I'm no lawyer, but that should give you some freedom to use and modify it.

## Contact
Should you have any questions, some constructive input or want to express your heartfelt thanks for me, you can open an Issue right here, contact me by email at cheonbyeolshinji@gmail.com or on Discord at cheonbyeol#3602
