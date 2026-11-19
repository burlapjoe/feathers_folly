label start:
    # call start_anim

    call fall_demo
    
    pause

    return



label start_anim:
    $ quick_menu = False

    $ t_pan_up = 6
    $ t_moon_wait = 3
    $ t_moon_travel = 3
    $ t_dim = 4

    scene islands_eclipse:
        yoffset -2160
        matrixcolor tsbc()
        pause 1
        parallel:
            ease t_pan_up yoffset 0
        parallel:
            pause t_moon_wait + (t_moon_travel * 0.5)
            ease 4 matrixcolor tsbc(b=-0.3)

    show light:
        yoffset -2160
        alpha 1
        xalign 0.5
        yalign 0.5
        pause 1
        parallel:
            ease t_pan_up yoffset 0
        parallel:
            pause t_moon_wait + (t_moon_travel * 0.5)
            ease (t_dim * 1.2) zoom 0.0
        parallel:
            pause t_moon_wait + (t_moon_travel * 0.5)
            ease_quart (t_dim * 1.2) alpha 0.0


    show shine:
        yoffset -2160
        alpha 0
        xalign 0.5
        yalign 0.5
        xoffset 0
        pause 1
        parallel:
            ease t_pan_up yoffset 0
        parallel:
            pause t_moon_wait
            ease 0.5 alpha 1
        parallel:
            pause t_moon_wait
            ease t_moon_travel + t_dim zoom 0.1
        parallel:
            pause t_moon_wait
            ease t_dim xoffset 16


    show moon:
        yoffset -2160
        xoffset -128
        xalign 0.5
        alpha 0.2
        yalign 0.5
        pause 1
        parallel:
            ease t_pan_up yoffset 0
        parallel:
            pause t_moon_wait
            easein t_moon_travel xoffset 0
        parallel:
            pause t_moon_wait
            ease t_moon_travel alpha 1


    $ hpause(t_pan_up + t_dim)

    return

    
image ocean = Movie(play="images/ocean.mp4")

label fall_demo:
    $ T_FALL = 2
    $ T_SWOOP = 0.5
    $ FINAL_ZOOM = 0.22

    scene ocean:
        xalign 0.5
        yalign 0.5
        rotate -90

    show rairoo_falling:
        xcenter 0.5
        yalign 0.0

        parallel:
            ease T_FALL zoom FINAL_ZOOM
            # ^^ also try easeout here if you like

        parallel:
            easein T_FALL yalign 0.5

        linear T_SWOOP xcenter 1.3

    show silas_swoop:
        xcenter -0.3
        ycenter 0.5

        pause (T_FALL - T_SWOOP)

        linear T_SWOOP xcenter 0.5
        linear T_SWOOP xcenter 1.3

    pause (T_FALL + T_SWOOP)

    return
