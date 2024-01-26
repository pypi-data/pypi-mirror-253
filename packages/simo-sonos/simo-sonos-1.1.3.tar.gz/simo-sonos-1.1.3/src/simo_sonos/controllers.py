import traceback
import sys
import random
from datetime import timedelta
from simo.multimedia.controllers import BaseAudioPlayer
from simo.core.events import GatewayObjectCommand
from .models import SonosPlayer, SonosPlaylist
from .gateways import SONOSGatewayHandler
from .forms import SONOSPlayerConfigForm


class SONOSPlayer(BaseAudioPlayer):
    gateway_class = SONOSGatewayHandler
    config_form = SONOSPlayerConfigForm

    sonos_player = None
    soco = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sonos_player = SonosPlayer.objects.filter(
            id=self.component.config['sonos_device']
        ).first()
        if self.sonos_player:
            self.component.sonos_player = self.sonos_player
            self.component.soco = self.sonos_player.soco
            self.soco = self.sonos_player.soco

    def unjoin(self):
        if not self.soco:
            print("NO SOCO player!", file=sys.stderr)
            return
        self.soco.unjoin()

    def play_uri(self, uri, volume=None):
        if volume:
            assert 0 <= volume <= 100
        self.send({"play_uri": uri, 'volume': volume})

    def play_alert(self, val, volume=None):
        '''Val can be sound id or uri'''
        assert type(val) in (int, str)
        if volume:
            assert 0 <= volume <= 100
        self.send({"alert": val, 'volume': volume})

    def _send_to_device(self, value):
        if not self.soco:
            print("NO SOCO player!", file=sys.stderr)
            return
        if value in (
            'play', 'pause', 'stop', 'next', 'previous',
        ):
            getattr(self.soco, value)()
        elif isinstance(value, dict):
            if 'seek' in value:
                self.soco.seek(timedelta(seconds=value['seek']))
            elif 'set_volume' in value:
                self.soco.volume = value['set_volume']
            elif 'shuffle' in value:
                self.soco.shuffle = value['shuffle']
            elif 'loop' in value:
                self.soco.repeat = value['loop']
            elif 'play_from_library' in value:
                if value['play_from_library'].get('type') != 'sonos_playlist':
                    return
                playlist = SonosPlaylist.objects.filter(
                    id=value['play_from_library'].get('id', 0)
                ).first()
                if not playlist:
                    return
                self.play_playlist(playlist)
            elif 'play_uri' in value:
                if value.get('volume') != None:
                    self.soco.volume = value['volume']
                self.soco.play_uri(value['play_uri'])
            elif 'alert' in value:
                GatewayObjectCommand(
                    self.component.gateway, self.component,
                    set_val=value
                ).publish()

        GatewayObjectCommand(
            self.component.gateway, self.component, set_val='check_state'
        ).publish()

    def play_playlist(self, item_id, shuffle=True, repeat=True):
        if not self.sonos_player:
            return
        for plst in self.sonos_player.soco.get_sonos_playlists():
            if plst.item_id == item_id:
                try:

                    self.soco.clear_queue()
                    self.soco.shuffle = shuffle
                    self.soco.repeat = repeat
                    self.soco.add_to_queue(plst)
                    que_size = self.soco.queue_size
                    if not que_size:
                        return
                    start_from = 0
                    if shuffle:
                        start_from = random.randint(
                            0, que_size - 1
                        )
                    self.soco.play_from_queue(start_from)
                    self.component.value = 'playing'
                    self.component.save()
                except:
                    print(traceback.format_exc(), file=sys.stderr)
                return
