# -*- coding: utf-8 -*-
import pygame

class SoundManager:
    def __init__(self):
        self.playing_background_music = False
        self.music_playing = None

    def play_background_music(self, music):
        self.playing_background_music = True
        self.music_playing = music
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1, 0.0)

    def stop_background_music(self):
        self.playing_background_music = False
        pygame.mixer.music.stop()

    def play_effect(self, effect):
        sound = pygame.mixer.Sound(effect)
        sound.play()
