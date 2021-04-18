default gallery_showing_button_index = None
default gallery_total_unlockable_buttons = None

init python:
    class GalleryButtonPlus(object):
        def __init__(self, gallery, index, page):
            self.gallery = gallery
            self.images = [ ]
            self.conditions = [ ]
            self.index = index
            self.page = page

        def check_unlock(self):
            for i in self.conditions:
                if not i.check(True):
                    return False

            for i in self.images:
                if i.check_unlock(False):
                    return True

            return False

    class GalleryPlus(Gallery):
        def __init__(self):
            super(GalleryPlus, self).__init__()

            self.loop_images = False

            self.loop_pages = False

            self.open_until_return = False

            self.buttons_per_page = dict()

        def button(self, name, page=0):

            button = GalleryButtonPlus(self, len(self.button_list), page)

            self.unlockable = button
            self.buttons[name] = button
            self.button_list.append(button)
            self.button_ = button

            if page not in self.buttons_per_page.keys():
                self.buttons_per_page[page] = 0
            self.buttons_per_page[page] += 1

        def show(self, button=0, image=0):

            all_images = dict()
            all_buttons = [ ]

            unlocked_images = dict()
            unlocked_buttons = [ ]

            for bi, b in enumerate(self.button_list):
                if not b.check_unlock():
                    continue
                if not self.loop_pages:
                    if b.page != self.button_list[button].page:
                        continue
                all_unlocked = True
                one_unlocked = False
                all_buttons.append(bi)
                all_images[bi] = [ ]

                for ii, i in enumerate(b.images):
                    all_images[bi].append(ii)
                    unlocked = i.check_unlock(all_unlocked)

                    if unlocked:
                        if not one_unlocked:
                            unlocked_buttons.append(bi)
                            unlocked_images[bi] = []
                            one_unlocked = True
                        unlocked_images[bi].append(ii)
                    else:
                        all_unlocked = False
                        if self.unlocked_advance and (button == bi) and (image == ii):
                            image += 1

            self.slideshow = False

            while True:

                if button >= len(self.button_list):
                    break

                b = self.button_list[button]

                if image >= len(b.images):
                    break

                is_current_locked = True
                if button in unlocked_buttons:
                    if image in unlocked_images.get(button, []):
                        is_current_locked = False

                i = b.images[image]

                if self.unlocked_advance:
                    images = unlocked_images
                    buttons = unlocked_buttons
                else:
                    images = all_images
                    buttons = all_buttons

                if not (button in buttons):
                    break
                if not (image in images.get(button, [])):
                    break

                bi = buttons.index(button)
                ii = images.get(button).index(image)


                if self.loop_pages:
                    store.gallery_showing_button_index = button + 1
                else:
                    store.gallery_showing_button_index = button + self.buttons_per_page.get(self.button_list[button].page,0) - all_buttons[-1]
                store.gallery_total_unlockable_buttons = self.buttons_per_page.get(self.button_list[button].page,0)

                result = i.show(is_current_locked, image, len(b.images))

                if result is True:
                    result = "next"

                if result == 'return':
                    break

                if result.startswith('previous_button'):
                    if self.loop_images:
                        bi -= 1
                        if bi < 0:
                            bi = len(buttons) - 1
                    else:
                        if bi > 0:
                            bi -= 1
                        elif not self.open_until_return:
                            break
                        ## else stay on current image
                    ii = 0
                    button = buttons[bi]
                    image = images[button][ii]
                elif result.startswith('next_button'):
                    if self.loop_images:
                        bi += 1
                        if bi >= len(buttons):
                            bi = 0
                    else:
                        if bi < len(buttons) - 1:
                            bi += 1
                        elif not self.open_until_return:
                            break
                        ## else stay on current image
                    ii = 0
                    button = buttons[bi]
                    image = images[button][ii]
                elif result.startswith('previous'):
                    if ii > 0:
                        ii -= 1
                        image = images[button][ii]
                    elif self.span_buttons:
                        if self.loop_images:
                            bi -= 1
                            if bi < 0:
                                bi = len(buttons) - 1
                            button = buttons[bi]
                            image = images[button][-1]
                        else:
                            if bi > 0:
                                bi -= 1
                                button = buttons[bi]
                                image = images[button][-1]
                            elif not self.open_until_return:
                                break
                            ## else stay on current image
                    elif not self.open_until_return:
                        break
                    ## else stay on current image
                else: ## results.startswith('next')
                    if ii < len(images.get(button,[])) - 1:
                        ii += 1
                        image = images[button][ii]
                    elif self.span_buttons:
                        if self.loop_images:
                            bi += 1
                            if bi >= len(buttons):
                                bi = 0
                            ii = 0
                            button = buttons[bi]
                            image = images[button][ii]
                        else:
                            if bi < len(buttons) - 1:
                                bi += 1
                                ii = 0
                                button = buttons[bi]
                                image = images[button][ii]
                            elif not self.open_until_return:
                                break
                            ## else stay on current image
                    elif not self.open_until_return:
                        break
                    ## else stay on current image

            renpy.transition(self.transition)

        def NextButton(self, unlocked=False):

            if unlocked:
                return ui.returns("next_button_unlocked")
            else:
                return ui.returns("next_button")

        def PreviousButton(self, unlocked=False):

            if unlocked:
                return ui.returns("previous_button_unlocked")
            else:
                return ui.returns("previous_button")


screen _gallery:
    if locked:
        add "#000"
        text _("Frame is locked.") align (0.5, 0.5)
    else:
        for d in displayables:
            add d

    if gallery.slideshow:
        timer gallery.slideshow_delay action Return("next") repeat True

    key "game_menu" action gallery.Return()
    key "hide_windows" action ToggleField(gallery,"navigation")

    key "K_UP" action gallery.PreviousButton(unlocked=gallery.unlocked_advance)
    key "K_DOWN" action gallery.NextButton(unlocked=gallery.unlocked_advance)
    key ["K_LEFT", "K_PAGEUP"] action gallery.Previous(unlocked=gallery.unlocked_advance)
    key ["K_RIGHT", "K_PAGEDOWN"] action gallery.Next(unlocked=gallery.unlocked_advance)

    if gallery.navigation:
        use gallery_navigation

screen gallery_navigation:

    text _("Image [gallery_showing_button_index] of [gallery_total_unlockable_buttons], frame [index] of [count]") align (0.98,0.02):
        color "#fff"
        outlines [(1,"#000",0,0)]

    hbox:
        spacing 20

        style_group "gallery"
        align (.5, .98)

        textbutton _("Previous image") action gallery.PreviousButton(unlocked=gallery.unlocked_advance)
        textbutton _("Previous frame") action gallery.Previous(unlocked=gallery.unlocked_advance)
        textbutton _("Slideshow") action gallery.ToggleSlideshow()
        textbutton _("Next frame") action gallery.Next(unlocked=gallery.unlocked_advance)
        textbutton _("Next image") action gallery.NextButton(unlocked=gallery.unlocked_advance)

    textbutton _("Return") action gallery.Return() align (0.02, 0.98) style "gallery_button"
    textbutton _("Hide interface (H)") action InvertSelected(ToggleField(gallery,"navigation")) align (0.98, 0.98) style "gallery_button"

style gallery_button_text:
    size 18
    outlines [(1,"#000",0,0)]
