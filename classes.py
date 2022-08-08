class Television:
    '''
    A class that represents a television-remote control object.
    '''
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to create a tv-remote control for a gui
        :param .__channel: a private variable to store the TV channel. Set to the minimum TV channel.
        :param .__volume: a private variable to store the TV volume. Set to the minimum TV volume.
        :param .__tv_status: a private variable to store the TV on/off status. The TV should start off.
        :return: instantiates television-remote object
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__tv_status = False

    def power(self) -> None:
        """
        A method that turns the TV on/off.
        :param __tv_status: alters the on/off state of the tv object.
        """
        if self.__tv_status == False:
            self.__tv_status = True
        elif self.__tv_status == True:
            self.__tv_status = False

    def channel_up(self) -> None:
        """
        A method to adjust the TV channel by incrementing its value.
        :param __channel: new channel
        """
        if self.__tv_status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        A method that adjusts the TV channel by decrementing its value.
        :param __channel: a new channel
        """
        if self.__tv_status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        A method that adjusts the TV volume by incrementing its value.
        :param __volume: incremented volume
        """
        if self.__tv_status == True:
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        A method that adjusts the volume by decrementing its value.
        :param volume: decrement volume
        """
        if self.__tv_status == True:
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        A method that returns the TV status using the format shown in the comments of main.py
        :return: string that contain the tv's current status, channel, and volume
        """
        return f'TV status: Is on = {self.__tv_status}, Channel = {self.__channel}, Volume = {self.__volume}'
