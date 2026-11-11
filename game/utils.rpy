##########################################3
#### AUDIO
##########################################3

init python:
    audio_channels = [
        'music',
        # 'music2',
        # 'music3',
        # 'music4',
        'sound',
        # 'sound2',
        # 'sound3',
        # 'sound4',
        'ambient',
        # 'ambient2',
        # 'ambient3',
        # 'ambient4',
    ]

    # renpy.music.register_channel("music2", "music", loop=True, tight=True)
    # renpy.music.register_channel("music3", "music", loop=True, tight=True)
    # renpy.music.register_channel("music4", "music", loop=True, tight=True)
    # renpy.music.register_channel("sound2", "sfx", loop=False)
    # renpy.music.register_channel("sound3", "sfx", loop=False)
    # renpy.music.register_channel("sound4", "sfx", loop=False)
    # renpy.music.register_channel("ambient2", "sfx", loop=True, tight=True)
    # renpy.music.register_channel("ambient3", "sfx", loop=True, tight=True)
    # renpy.music.register_channel("ambient4", "sfx", loop=True, tight=True)

    def vol(channel, vol=1.0, fade=0):
        renpy.music.set_volume(vol, fade, channel)

    def pan(channel, pan=0.0, duration=0.0):
        renpy.music.set_pan(pan, duration, channel)

    def lowpass(channel, value=None, q=1.0, fade=0.016, to_current=True):
        """
            value: frequency of the lowpass filter. default: 0
            q: peak in db of response 🤷 default: 1.0
            to_current: apply to currently playing audio as opposed to next in queue
        """
        if value is not None:
            renpy.music.set_audio_filter(
                channel,
                renpy.audio.filter.Lowpass(value, q),
                replace=to_current,
                duration=fade
            )
        else:
            renpy.music.set_audio_filter(
                channel,
                None,
                replace=to_current,
                duration=fade
            )

    def highpass(channel, value=None, q=1.0, fade=0.016, to_current=True):
        if value is not None:
            renpy.music.set_audio_filter(
                channel,
                renpy.audio.filter.Highpass(value, q),
                replace=to_current,
                duration=fade
            )
        else:
            renpy.music.set_audio_filter(
                channel,
                None,
                replace=to_current,
                duration=fade
            )

    def reset_channel(channel, fade=0):
        vol(channel, fade=fade)
        pan(channel, duration=fade)
        lowpass(channel)
        highpass(channel)


    def stop_all_audio(fadeout=0, reset=False, subset=None, exclude_subset=False):
        """
        Stops all audio at the same time, with a default fadeout time of 0, and
        with the option to reset all channels' volume and panning. If `subset`
        is not None, only affect channels in provided iterable, or all but
        those if `exclude_subset` is True
        """
        if subset:
            if exclude_subset:
                channels = [c for c in audio_channels if c not in subset]
            else:
                channels = subset
        else:
            channels = audio_channels
        
        for channel in channels:
            renpy.music.stop(channel, fadeout)
            if reset:
                reset_channel(channel, fade=fadeout)



##########################################3
#### CONTROL
##########################################3

init python:
    def hpause(t):
        if t and t > 0:
            renpy.pause(t, hard=True)

##########################################3
#### COLOR
##########################################3

init python:
    def tsbc(t="#ffffff", s=1.0, b=0.0, c=1.0):
        return TintMatrix(t) * SaturationMatrix(s) * BrightnessMatrix(b) * ContrastMatrix(c)



