# -*- coding: utf-8 -*-

from blinker import signal

img_resized = signal('img_resized')

album_initialized = signal('album_initialized')
gallery_initialized = signal('gallery_initialized')
gallery_build = signal('gallery_build')
media_initialized = signal('media_initialized')
