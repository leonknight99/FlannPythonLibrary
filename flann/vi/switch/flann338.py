from flann.vi import FlannProgrammable


class Switch338(FlannProgrammable):
    '''Class for Flann's 338 programmable switch - Currently UNTESTED'''
    def __init__(self, address: str, tcp_port: int, *args, **kwargs):
        super().__init__(is_serial=False, *args, **kwargs)

        self._resource.connect((address, tcp_port))

        self.series_number = '338'

        id_str = self.id()
        assert(self.series_number in id_str)
    
    @property
    def id(self):
        '''Instrument ID string'''
        self.write('IDN?\n')
        return self.read
    
    @property
    def instrument_status(self):
        '''Instrument status'''
        self.write('*STB?\n')
        return self.read
    
    @property
    def position(self):
        '''Current selected switch position'''
        self.write(f'POS?\n')
        return self.read()
    
    def position1(self):
        '''Selected switch position 1'''
        self.write(f'POS1\n')
        self.read

    def position2(self):
        '''Selected switch position 2'''
        self.write(f'POS2\n')
        self.read

    def position3(self):
        '''Selected switch position 3'''
        self.write(f'POS3\n')
        self.read

    def position4(self):
        '''Selected switch position 4'''
        self.write(f'POS4\n')
        self.read