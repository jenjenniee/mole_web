from channels.generic.websocket import WebsocketConsumer
from mole_game_package import Player
import base64
from PIL import Image
import io
import numpy as np


def base64_to_nparray(image_base64):
    image = None
    image_base64 = image_base64.split(',')[1]
    if image_base64 != '':     
        image_pil = Image.open(io.BytesIO(base64.b64decode(image_base64)))
        image = np.array(image_pil)
    
    return image

def nparray_to_base64(image_np):
    pil_im = Image.fromarray(image_np)
    b = io.BytesIO()
    # b = io.StringIO(s)
    pil_im.save(b, 'PNG')
    im_bytes = b.getvalue()

    return base64.b64encode(im_bytes).decode('utf-8')



class MoleGameConsumer(WebsocketConsumer):
    
    def connect(self):
        print("소켓연결 수립")
        self.base64_prefix = 'data:image/png;base64,'
        # self.player = Player()
        self.accept()
    
    def disconnect(self,code=None):
        print("소켓연결 해제")
    
    def receive(self,text_data=None):
        '''
            브라우저로부터 데이터 받기
        '''

        frame = base64_to_nparray(text_data)
        # if frame: #이미지 존재하면

        if frame is not None:

            self.send(f'{self.base64_prefix}{nparray_to_base64(frame)}')
            


        

