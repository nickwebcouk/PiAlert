#!/usr/bin/env python3

import os
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

import time
import math

import blinkt

import sys
import RPi.GPIO as GPIO
import tm1637


Display = tm1637.TM1637(5,4,tm1637.BRIGHT_TYPICAL)

Display.Clear()


blinkt.set_clear_on_exit()

LEDBRIGHT = [0, 0, 0, 0, 0, 16, 64, 255, 64, 16, 0, 0, 0, 0, 0, 0]

countred = 0
countblue = 0
countgreen = 0
countpurple = 0

start_time = time.time()

def light_red():
    Display.Clear()
    timer = 0
    global countred
    countred = countred + 1
    
    #The 4 digit display python function needs the digits formatted as a 4 item array
    #So here we make it at least 4 digits and then split it into a 4 length array
    
    redformat = f'{countred:04}'
    redarray = list(redformat)
    #print(redarray)
    redarraynumbers = [int(x) for x in redarray]
    #print('Red Hits: ' + str(countred))
    while timer < 15:
        timer = timer + 1
        delta = (time.time() - start_time) * 8
        offset = int(round(((math.sin(delta) + 1) / 2) * (blinkt.NUM_PIXELS - 1)))
    
        for i in range(blinkt.NUM_PIXELS):
            blinkt.set_pixel(i , LEDBRIGHT[offset + i], 0, 0)

        blinkt.show()

        time.sleep(0.01)
    blinkt.clear()
    blinkt.show()
    Display.Show(redarraynumbers)

def light_blue():
    Display.Clear()
    timer = 0
    global countblue
    countblue = countblue + 1
    
    blueformat = f'{countblue:04}'
    bluearray = list(blueformat)
    #print(bluearray)

    bluearraynumbers = [int(x) for x in bluearray]
    #print('Blue Hits: ' + str(countblue))

    while timer < 15:
        timer = timer + 1
        delta = (time.time() - start_time) * 8
        offset = int(round(((math.sin(delta) + 1) / 2) * (blinkt.NUM_PIXELS - 1)))
    
        for i in range(blinkt.NUM_PIXELS):
            blinkt.set_pixel(i , 0, 0, LEDBRIGHT[offset + i])

        blinkt.show()

        time.sleep(0.01)
    blinkt.clear()
    blinkt.show()

    Display.Show(bluearraynumbers)

def light_green():
    Display.Clear()
    timer = 0
    global countgreen
    countgreen = countgreen + 1
    
    greenformat = f'{countgreen:04}'
    greenarray = list(greenformat)
    #print(greenarray)

    greenarraynumbers = [int(x) for x in greenarray]
    #print('Green Hits: ' + str(countgreen))

    while timer < 15:
        timer = timer + 1
        delta = (time.time() - start_time) * 8
        offset = int(round(((math.sin(delta) + 1) / 2) * (blinkt.NUM_PIXELS - 1)))
    
        for i in range(blinkt.NUM_PIXELS):
            blinkt.set_pixel(i , 0, LEDBRIGHT[offset + i], 0) 

        blinkt.show()

        time.sleep(0.01)
    blinkt.clear()
    blinkt.show()

    Display.Show(greenarraynumbers)

def light_purple():
    Display.Clear()
    timer = 0
    global countpurple
    countpurple = countpurple + 1
    
    purpleformat = f'{countpurple:04}'
    purplearray = list(purpleformat)
    #print(purplearray)

    purplearraynumbers = [int(x) for x in purplearray]
    #print('Purple Hits: ' + str(countpurple))

    while timer < 15:
        timer = timer + 1
        delta = (time.time() - start_time) * 8
        offset = int(round(((math.sin(delta) + 1) / 2) * (blinkt.NUM_PIXELS - 1)))
    
        for i in range(blinkt.NUM_PIXELS):
            blinkt.set_pixel(i , LEDBRIGHT[offset + i], 0,LEDBRIGHT[offset + i]) 

        blinkt.show()

        time.sleep(0.01)
    blinkt.clear()
    blinkt.show()

    Display.Show(purplearraynumbers)





class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type','text/refused')
      self.end_headers()
      # Send the html message
      if (self.path == '/red'):
        blinkt.clear()
        blinkt.show()
        light_red()
        blinkt.set_pixel(0,255,0,0)
        blinkt.show()
        print('Counts: R: ' + str(countred) +  ' G: ' + str(countgreen) + ' B: ' + str(countblue) + ' P: ' + str(countpurple))
      elif (self.path == '/blue'):
        blinkt.clear()
        blinkt.show()
        light_blue()
        blinkt.set_pixel(2,0,0,255)
        blinkt.show()
        print('Counts: R: ' + str(countred) +  ' G: ' + str(countgreen) + ' B: ' + str(countblue) + ' P: ' + str(countpurple))
      elif (self.path == '/purple'):
        blinkt.clear()
        blinkt.show()
        light_purple()
        blinkt.set_pixel(4,255,0,255)
        blinkt.show()
        print('Counts: R: ' + str(countred) +  ' G: ' + str(countgreen) + ' B: ' + str(countblue) + ' P: ' + str(countpurple))
      else:
        blinkt.clear()
        blinkt.show()
        light_green()
        blinkt.set_pixel(6,0,255,0)
        blinkt.show()
        print('Counts: R:' + str(countred) +  ', G:' + str(countgreen) + ', B:' + str(countblue) + ', P:' + str(countpurple))
        return



if __name__ == '__main__':
    httpd = HTTPServer(('', 8000), MyHandler)
    httpd.serve_forever()



