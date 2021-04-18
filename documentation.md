# GalleryPlus Documentation

This documentation assumes you are already familiar with RenPy's built-in Gallery class, its fields and methods. For that, please see the [official RenPy documentation](https://www.renpy.org/doc/html/rooms.html)!

## Looping images
class `GalleryPlus`
* new field `loop_images`: boolean, `False` by default

When `True`, the viewer will loop back to the first image after the last (or vica versa).

## "Open until return"
class `GalleryPlus`
* new field `open_until_return`: boolean, `False` by default

When `True`, the viewer stays open until the user intentionally returns. This takes effect when `loop_images` and/or `span_buttons` (inherited from Gallery) is/are `False`; rather than exiting viewer mode when the user tries to proceed past the last (or first) displayable image, the same image remains on display.

## "Pages" system
Allows you to define "collections" of buttons and decide whether you want to navigate them separately or altogether.

class `GalleryPlus`
* new field `loop_pages`: boolean, `False` by default

When `False`, navigation is restricted to the page of the button that opened the viewer mode. When `True`, the user can navigate all images, regardless of their pages.

class `GalleryPlus`
* updated inherited method `button(name, page=0)`

The `button` method now takes `page` as an optional argument; if not given, it's defaulted to `0`. It can be an arbitrary identifier, it's only compared to the page of other buttons.  

Note that, just like the built-in Gallery class does not take care of creating the gallery screen, neither does GalleryPlus. As such, setting the `page` for your `button`s will not ensure that they'll be placed on different pages of the gallery screen. It just provides the convenience of not having to make several Gallery objects (and adjusting settings and remembering names for each) for navigating your image collections separately, if you plan on making a multi-page gallery. However, the gallery_example.rpy should give you an idea on how to set that up.

Note: the `gallery.make_button` method and its application do not change.

## Navigating "buttons"
A button usually collects different versions of the same image; sometimes, an image has *many* versions, and the user might rather proceed to the next image. These actions implement that.

class `GalleryPlus`
* new action `NextButton()`
* new action `PreviousButton()`

## Behind the scenes
To support the above changes, the file also contains:

new class `GalleryButton`
* redefines `__GalleryButton`
Internal method for handling the buttons.

class `GalleryPlus`
* updated inherited method `show`
Does the legwork of reading the gallery data structures and navigating the gallery images while in viewer mode, with the help of the `_gallery` and `gallery_navigation` screens.
