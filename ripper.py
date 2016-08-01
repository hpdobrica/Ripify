#  alsa_output.pci-0000_02_04.0.analog-stereo.monitor
#  /home/jharvard/.config/google-chrome/Default

#imports
import subprocess, time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#init
p2 = ""
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
chrome_options = Options()
chrome_options.add_argument("user-data-dir=~/.config/google-chrome/Default")
driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=chrome_options)

#functions
def timeStrToSecs(timeString):
    strSplit = timeString.text.split(":")
    secs = (int(strSplit[0])*60)+int(strSplit[1])
    return secs

def startRecord(songArtist, songName, playlistName):
    global p2
    try: #try to create new artist dir if not already there
        if(not os.path.exists("music/" + playlistName)):
            os.mkdir("music/" + playlistName)
            print "Created new Playlist dir"
        #record new song if not already recorded
        if(not os.path.exists("music/" + playlistName + "/" + songArtist + " - " + songName + "" + ".ogg")):
            try: ### the next line is for specific sound card, edit it
                avconvCmd = "avconv", "-f", "pulse", "-i", "alsa_output.pci-0000_02_04.0.analog-stereo.monitor", "-acodec", "libvorbis", "-ac", "2", "-ar", "48000", "-vn" , 'music/' + playingInfo1 + '/' + playingInfo2 + '/' + playingInfo3 + '.ogg'
                p2 = subprocess.Popen(avconvCmd)
                print "Created new Song file, now recording...\n"
            except:
                print "Error opening avconv! Is libav-tools installed?\n"
    except:
        print "Couldn't create new Song file!\n"



#main
#create music dir if it doesn't exist
if(not os.path.exists("music")):
    os.mkdir("music")
address = raw_input('Address of Spotify playlist: ')

try:
    driver.get("https://play.spotify.com/user/spotify/playlist/7MPXsjQGsXcLdNz7UxVuVl")
except:
    print "Invalid playlist uri"

playlist = raw_input('Playlist name: ')



driver.switch_to_frame(driver.find_element_by_id("app-player"));
name = driver.find_element_by_id("track-name")
artist = driver.find_element_by_id("track-artist")
current = driver.find_element_by_id("track-current")
current = timeStrToSecs(current)
length = driver.find_element_by_id("track-length")
length = timeStrToSecs(length)


el = driver.find_element_by_id("play-pause")
el.click()
print name.text
print current
print length












### program start here ###

#variables and lists
#p2 = ""



##try to run pianobar
#try:
#    cmd = "pianobar"
#    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
#    output = p.stdout.readline()
#except:
#    print "Error opening pianobar! Is it installed?\n"

#n = 0
#while(output):
#    if('|>  "' in output): #beginning of songs playing
#        try:
#            p2.kill() #kill recording of last song
#        except:
#            print
#        try:

            #try to clean up and format pianobar's output
            #cleanPianobarChars = output.split('|>  "', 1)
#            songName = "Song %d" % n
#            artistName = "Artist %d" % n
#            albumName = "Album %d" % n
#            n=n+1
#            #put Artist name, Album name and Song name into a list
#            playingInfo1 = artistName[0]
#            playingInfo2 = albumName[0]
#            playingInfo3 = songName[0]
#            #print "\nArtist: " + playingInfo1 + "\nAlbum: " + playingInfo2 + "\nSong: " + playingInfo3 + "\n"
#            #start dir check or creation and record to file
#           startRecord(playingInfo1, playingInfo2, playingInfo3)
#       except:
#           print "Something went wrong with cleaning up pianobar output...\n"
#   output = p.stdout.readline()
