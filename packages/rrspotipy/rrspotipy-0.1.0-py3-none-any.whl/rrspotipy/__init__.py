"""
arrow up    previous
arrow down  next
arrow left  backward 5
arrow right forward 5
space or k  pause/unpause
j           backward 10
l           forward 10
p           show pos
q           stop
"""

import pygame
import os
import audioread
import random
import sys
import json
import time
import random
from paircompare import pairwise_comparison
#os.chdir(os.path.dirname(__file__))




#print(files)
#ss
#files=[os.path.join(dir,name) for name in os.listdir("/Users/alain/RRS/audio/Rado")]


# SETUP
idx=0
pygame.mixer.init()
#screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


class Pygame:
    def __enter__(self):
        pygame.init()
    def __exit__(self,exct,exc,tb):
        pygame.quit()
class Playlist(list):
    def verif(self):
        nfiles=[]
        for idx in range(len(self),0,-1):
            idx-=1
            file=self[idx]
            try:
                self.get_duration_of(file)
            except:
                print(f"Invalid file: {file}",file=sys.stderr)
                del self[idx]
            else:
                nfiles.append(file)
        self.files=nfiles
        self.files=nfiles

    def get_total_duration(self):
        return TimeFormat(sum(map(self.get_duration_of,self)))
    
    @staticmethod
    def get_duration_of(file):
        with audioread.audio_open(file) as f:
            return TimeFormat(f.duration)
        
    @classmethod
    def from_dir(cls,dir):
        return cls([os.path.join(dir,file) for file in os.listdir(dir)])

    def _playcurrent(self):
        self._ttstart=time.time()
        self.current_idx%=len(self)
        self.current_file=self[self.current_idx]
        self.current_duration=self.get_duration_of(self.current_file)
        pygame.mixer.music.load(self.current_file)
        pygame.mixer.music.play()
        print(f"{self.current_duration} #{self.current_idx}: {self.current_file}")
    def start(self,start_idx=0):
        self.isPaused=False
        self.current_idx=start_idx
        self._playcurrent()
        self.running=True
        #print("HELLO")
        pygame.event.clear()
        while self.running:
            if time.time()-self._ttstart>self.current_duration:
                self.next()
            #print("HELLO")
            #msgf(str(random.randrange(1000000)))
            for event in pygame.event.get():

                #print(event)
                if event.type==pygame.QUIT:
                    self.running=False

                if event.type==pygame.KEYDOWN:
                    if event.key==1073741906: #key arrow up
                        self.previous()
                    elif event.key==1073741905: #key arrow down
                        self.next()
                    elif event.key==1073741904: #key arrow left
                        self.backward(5)
                    elif event.key==1073741903: #key arrow right
                        self.forward(5)
                    elif event.unicode==" " or event.unicode=="k":
                        self.pause_unpause()
                    elif event.unicode=="j":
                        self.backward(10)
                    elif event.unicode=="l":
                        self.forward(10)
                    elif event.unicode=="p":
                        self.show_pos()
                    elif event.unicode=="q":
                        self.running=False
            clock.tick(60)
        self.stop()
        print("player stoped")
    def previous(self):
        print("- previous")
        self.current_idx-=1
        self._playcurrent()

    def next(self):
        print("- next")
        self.current_idx+=1
        self._playcurrent()

    def backward(self,secs=5):
        print(f"- backward {secs}")
        pos=self.get_pos()
        self.set_pos(pos-secs,pos)

    def forward(self,secs=5):
        print(f"- forward {secs}")
        pos=self.get_pos()
        #print(pos,float(pos))
        self.set_pos(pos+secs,pos)
        
    def pause_unpause(self):
        if self.isPaused:
            print("- unpause")
            self._ttstart=time.time()-self._pos
            pygame.mixer.music.unpause()
            self.isPaused=False

        else:
            print("- pause")
            self._pos=self.get_pos()
            pygame.mixer.music.pause()
            self.isPaused=True


    def show_pos(self):
        print(f"- pos: {self.get_pos()}/{self.current_duration}")

    def get_pos(self):
        return TimeFormat(time.time()-self._ttstart)
        #return TimeFormat(pygame.mixer.music.get_pos()/1000)
    def set_pos(self,new_pos,old_pos=None):
        #print(secs)
        if old_pos is None:old_pos=self.get_pos()
        if new_pos<0:new_pos=0
        self._ttstart=time.time()-new_pos
        #print(secs)
        pygame.mixer.music.set_pos(new_pos)
        self.show_pos()

    def shuffle(self):
        random.shuffle(self)
    def stop(self):
        pygame.mixer.music.stop()
    @classmethod
    def _compare(cls,x,y):
        #print("cc")
        plpair=Playlist((x,y))
        pygame.event.clear()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    raise KeyboardInterrupt
                
                if event.type==pygame.KEYDOWN:
                    if event.unicode=="p":
                        plpair.start()
                    return event.unicode

    def pairwise_comparison(self,file="paircompare-data.txt"):
        #print(self._pairwise_cmd1(("1","2")))
        #print(self._pairwise_cmds["p1"](("1","2")))
        #print("WW")
        return Playlist(pairwise_comparison(self,file,compare_func=self._compare))
    def k7(self,minl,maxl,ntries=100):
        playlists=[]
        lself=len(self)
        for _ in range(ntries):
            pl=self.copy()
            rem_pl=[]
            lpl=len(pl)
            l=0
            #print(_)
            while True:
                idx=random.randrange(lpl)
                sound=pl[idx]
                duration=self.get_duration_of(sound)
                l+=duration
                del pl[idx]
                rem_pl.append(sound)
                if l>minl:
                    if l>maxl:
                        break
                    playlists.append((TimeFormat(l),Playlist(pl),Playlist(rem_pl)))
                lpl-=1
        return playlists
    def k7(self,maxl,ntries=1000):
        bestl=0
        lself=len(self)
        for ntry in range(ntries):
            pl=self.copy()
            rem_pl=[]
            l=0
            lpl=lself
            while True:
                idx=random.randrange(lpl)
                sound=pl[idx]
                duration=self.get_duration_of(sound)
                l+=duration
                if l>maxl:
                    l-=duration
                    break
                rem_pl.append(sound)
                del pl[idx]
                lpl-=1
            if l>bestl:
                l=TimeFormat(l)
                print(ntry,l)
                bestl=l
                bestp=pl
                bestr=rem_pl
        return (bestl,bestp,bestr)

            
    def __repr__(self):
        return json.dumps(self,indent=2)


class TimeFormat(float):
    def __repr__(self):
        #print(float(self))
        
        return f"{self.zfill(int(self)//60)}:{self.zfill((int(self)%60))}"
    @staticmethod
    def zfill(number):
        return str(number).zfill(2)
#print(Time_Format(-3))

if __name__=="__main__":
    import tests.rrspotipy_caller as rrspotipy_caller

simplevar=1
print("it should breakpoint")
#print(233//2)
#rint(Time_Format(321))
simpleVar=2