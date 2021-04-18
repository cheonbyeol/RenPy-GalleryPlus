define config.allow_underfull_grids = True

init python:
    imgs = GalleryPlus()
    imgs.navigation = True
    imgs.span_buttons = True
    imgs.loop_images = True
    imgs.unlocked_advance = True
    imgs.open_until_return = True
    imgs.transition = dissolve
    imgs.locked_button = Fixed(Solid("#000",xysize=(240,180)),Text("Locked",size=32,align=(0.5,0.5)),fit_first=True)
    imgs.loop_pages = False

    imgs.button("white")
    imgs.image(Solid("#fff"))
    imgs.button("black")
    imgs.condition("False")
    imgs.image(Solid("#000"))
    imgs.button("gray")
    imgs.image(Solid("#333"))
    imgs.image(Solid("#666"))
    imgs.image(Solid("#888"))
    imgs.image(Solid("#aaa"))
    imgs.condition("False")
    imgs.image(Solid("#ccc"))
    imgs.button("violet",1)
    imgs.image(Solid("#f0f"))
    imgs.image(Solid("#f8f"))
    imgs.button("blue",1)
    imgs.image(Solid("#008"))
    imgs.image(Solid("#00f"))
    imgs.image(Solid("#88f"))
    imgs.condition("False")
    imgs.button("teal",1)
    imgs.image(Solid("#0ff"))
    imgs.image(Solid("#088"))
    imgs.button("green",1)
    imgs.image(Solid("#0f0"))
    imgs.condition("False")
    imgs.image(Solid("#080"))
    imgs.button("yellow",2)
    imgs.image(Solid("#ff0"))
    imgs.button("orange",2)
    imgs.image(Solid("#f80"))
    imgs.image(Solid("#840"))
    imgs.button("red",2)
    imgs.image(Solid("#800"))
    imgs.condition("False")
    imgs.image(Solid("#f00"))
    imgs.image(Solid("#f88"))
    imgs.condition("False")

screen gallery():
    tag menu

    use game_menu("Gallery"):
        default gallery_page = "neut"
        fixed:
            yfit True
            xfit True
            hbox:
                align (0.5, 0.0)
                spacing 20
                textbutton "Neutral colors" action SetScreenVariable("gallery_page", "neut")
                textbutton "Cold colors" action SetScreenVariable("gallery_page", "cold")
                textbutton "Warm colors" action SetScreenVariable("gallery_page", "warm")
            fixed:
                yfit True
                xfit True
                align (0.5, 0.5)
                showif gallery_page == "neut":
                    grid 2 2:
                        spacing 30
                        add imgs.make_button("white",Solid("#fff",xysize=(240,180)))
                        add imgs.make_button("black",Solid("#000",xysize=(240,180)))
                        add imgs.make_button("gray",Solid("#888",xysize=(240,180)))
                elif gallery_page == "cold":
                    grid 2 2:
                        spacing 30
                        add imgs.make_button("violet",Solid("#f0f",xysize=(240,180)))
                        add imgs.make_button("blue",Solid("#00f",xysize=(240,180)))
                        add imgs.make_button("teal",Solid("#0ff",xysize=(240,180)))
                        add imgs.make_button("green",Solid("#0f0",xysize=(240,180)))
                elif gallery_page == "warm":
                    grid 2 2:
                        spacing 30
                        add imgs.make_button("yellow",Solid("#ff0",xysize=(240,180)))
                        add imgs.make_button("orange",Solid("#f80",xysize=(240,180)))
                        add imgs.make_button("red",Solid("#f00",xysize=(240,180)))
                elif gallery_page == "help":
                    vbox:
                        style_prefix "gallery_help"
                        pos (0,0)
                        spacing 20
                        hbox:
                            label "H"
                            text _("Hide and show navigation")
                        hbox:
                            label _("Esc, right click")
                            text _("Exit from viewing mode")
                        hbox:
                            label _("Left arrow, PageUp")
                            text _("Previous frame")
                        hbox:
                            label _("Right arrow, PageDown")
                            text _("Next frame")
                        hbox:
                            label _("Up arrow")
                            text _("Previous image")
                        hbox:
                            label _("Down arrow")
                            text _("Next image")

            vbox:
                align (0.0, 1.0)
                textbutton _("Navigation help") action SetScreenVariable("gallery_page","help")

style gallery_help_label is help_label

style gallery_help_label_text is help_label_text
