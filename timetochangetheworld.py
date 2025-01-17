"""
Python Code
Author: Adil Mukhi
Script Name: timeToChangeOurWorld
Song Title: Time to Change Our World
Link: https://earsketch.gatech.edu/earsketch2/?sharing=6Ta5056BwBFyXdb0GyFjxQ

"Time to Change Our World" is a song that uses upbeat rhythms and melodies to promote Indigenous peoples' rights and
emphasize their battles for acknowledgment and justice. It is meant to bring awareness to the indigenous peoples,
and their struggles to have their basic needs, like drinking water, addressed. This cause is very important to me 
because it represents my conviction in the need to recognize and tackle the continuous difficulties faced by 
underprivileged populations. As someone who has recently begun to code, making this piece has me a great chance to 
hone my abilities while also contributing to a meaningful message that inspires others to realize the need for change
and take action toward a more just and fair society.

Call to Action: We have been quiet for too long, it is time to advocate for Indigenous 
rights by raising awareness, supporting Indigenous-led initiatives, and promoting education
and policy changes that honour their history and foster a just future.
"""

# Setup
from earsketch import *
setTempo(100) # Decided on this tempo because it balances energy and flow for the piece.

# Sound Bank
# Instruments - Sorted by instrument family
drumOne = AK_UNDOG_PERC_DRUMS
drumTwo = CIARA_ROOTED_DRUMBEAT_1
drumThree = RD_POP_SOLODRUMPART_25
beat = DKBEAR_FREE_PERC_KICK # Allowed me to make my own unique custom beat
bass = CIARA_SET_BASSLINE_3
tuba = CIARA_MELANIN_THEME_TUBA_1
piano = ENTREP_THEME_KEYS_1
orch = ENTREP_THEME_ORCH
shaker = SAMIAN_PEUP_PERC_SHAKER

# Vocals - Sorted in order of use
chorusOne = DKBEAR_FREE_VOX_CHORUS_1
verseOne = COMMON_LOVE_VOX_COMMON_4 # Verse One emphasizes that respect and dignity are essential, as people respond in kind when they feel valued.
soundEffect = createAudioSlice(COMMON_LOVE_VOX_COMMON_4, 4, 5)
chorusTwoPartOne = AYSANABEE_HERE_VOX_CHORUS_4
chorusTwoPartTwo = AYSANABEE_HERE_VOX_POST
verseTwo = DKBEAR_FREE_VOX_CHORUS_2 # I chose this verse for the line "We just wanna live our lives..." 
# This underscores the desire for safety and freedom and reinforces the song’s message to speak up against racial injustice.
chorusThree = DKBEAR_FREE_TALK_MUST_DO
bridge = SAMIAN_PEUP_THEME_CHANT_2
verseThree = JWOLF_COTG_VOX_LEAD_VERSE_1 # "Child of the government" highlights colonialism's painful legacy, urging Indigenous rights and awareness advocacy.
chorusFour = createAudioSlice(JWOLF_COTG_VOX_LEAD_VERSE_1, 7.9, 9) # I chose the line "Father young blood took the children down, 
# to the water with the cross and the bible" to emphasize residential school trauma and the call for justice for Indigenous communities.
verseFour = JWOLF_COTG_VOX_LEAD_INTRO_1
outro = createAudioSlice(DKBEAR_FREE_VOX_VERSE_1A, 2, 8.7)
hook = PDSB822372_REC1 # This is my original recording (PDSB822372_REC1), conveying my conviction that reform is necessary in today's difficult society.

# Process
# For all functions below, if used, a is the track we want it on, b is the starting measure and c is the ending measure.
# Function to create a chorus effect with pitch shift and chorus effect applied
def chorus(a):
    setEffect(a, PITCHSHIFT, PITCHSHIFT_SHIFT, -2)
    setEffect(a, CHORUS, CHORUS_LENGTH, 15)
    setEffect(a, CHORUS, CHORUS_NUMVOICES, 2)
    setEffect(a, CHORUS, CHORUS_RATE, 10)
    setEffect(a, CHORUS, MIX, 0.5)

# Function to create a reverb effect to simulate echo
def reverb(a, b):
    setEffect(a, REVERB, BYPASS, 1, 1)
    setEffect(a, REVERB, BYPASS, 0, b)
    setEffect(a, REVERB, REVERB_TIME, 2000)
    setEffect(a, REVERB, REVERB_DAMPFREQ, 18000)
    setEffect(a, REVERB, MIX, 0.5)

# Function to create a background beat with consistent rhythmic patterns
def backgroundBeat(a, b, c):
    for i in range(b, c, 2):
        makeBeat(beat, a, i, "0-0-0-0--00-00-")
    setEffect(a, VOLUME, GAIN, 8)
    makeBeat(shaker, a+1, b, "0-0-000-0-0-000-0-0-000")
    setEffect(a+1, VOLUME, GAIN, 10)
    makeBeat(shaker, a+1, b+37, "0-0-000-0-0-000-0-0-000")

# Function to create background music layers
def backgroundMusic(a, b, c):
    fitMedia(drumOne, a, b, c)
    setEffect(a, VOLUME, GAIN, 11, b)
    fitMedia(piano, a+1, b, c)
    setEffect(a+1, VOLUME, GAIN, 2, b)
    fitMedia(drumTwo, a+2, b, c)
    setEffect(a+2, VOLUME, GAIN, 3, b)
    fitMedia(orch, a+3, b, c)
    setEffect(a+3, VOLUME, GAIN, -5, b)
    backgroundBeat(a+4, b, c)

# Function to add sound effects with volume adjustments
def soundEffects(a, b):
    fitMedia(tuba, a, b, b+4)
    setEffect(a, VOLUME, GAIN, -2, b)
    fitMedia(bass, a, b+4, b+9)
    setEffect(a, VOLUME, GAIN, 6, b+4)
    fitMedia(drumThree, a, b+19, b+22)
    fitMedia(bass, a, b+23, b+25)    
    setEffect(a, VOLUME, GAIN, 5, b+23, -5, b+25)
    fitMedia(drumThree, a, b+32, b+35)
    setEffect(a, VOLUME, GAIN, 5, b+32, -5, b+35)
    fitMedia(bass, a, b+39, b+41)
    setEffect(a, VOLUME, GAIN, 5, b+39, -5, b+41)
    fitMedia(drumThree, a, b+50, b+53)
    setEffect(a, VOLUME, GAIN, 6, b+50, -4, b+53)
    fitMedia(bass, a, b+58, b+60)
    setEffect(a, VOLUME, GAIN, 5, b+58, -5, b+60)
    fitMedia(drumThree, a, b+66, b+68)
    setEffect(a, VOLUME, GAIN, 5, b+64)

# Function calls for different sections of the song
# For all functions below a is the track we want it on, b is the starting measure and c is the ending measure.
def runChorusOne(a, b, c):
    fitMedia(chorusOne, a, b, c)
    setEffect(a, VOLUME, GAIN, 8, b)
    setEffect(a, PITCHSHIFT, PITCHSHIFT_SHIFT, -4, b)

def runVerseOne(a, b, c):
    fitMedia(verseOne, a, b, c)
    setEffect(a, VOLUME, GAIN, 6, b)
    setEffect(a, PITCHSHIFT, PITCHSHIFT_SHIFT, 0, b)

def runSoundEffect(a, b, c):
    fitMedia(soundEffect, a, b, c)
    chorus(a)
    setEffect(a, VOLUME, GAIN, 1, b)
    setEffect(a, DISTORTION, DISTO_GAIN, 29, b)

def runChorusTwo(a, b, c):
    fitMedia(chorusTwoPartOne, a, b, c-1)
    fitMedia(chorusTwoPartTwo, a, b+2, c)
    reverb(10, 21)
    setEffect(a, VOLUME, GAIN, 7, b, -10, c)
    setEffect(a, DISTORTION, DISTO_GAIN, 20, b)

def runVerseTwo(a, b, c):
    fitMedia(verseTwo, a, b, c)
    setEffect(a, PITCHSHIFT, PITCHSHIFT_SHIFT, -1, b)

def runChorusThree(a, b, c):
    fitMedia(chorusThree, a, b, c)
    setEffect(a, VOLUME, GAIN, 8, b)
    setEffect(a, PITCHSHIFT, PITCHSHIFT_SHIFT, -4, b)

def runBridge(a, b, c):
    fitMedia(bridge, a, b, c)
    setEffect(a, VOLUME, GAIN, -1, b, 8, b+2)
    setEffect(a, VOLUME, GAIN, 8, c-2, -30, c)

def runVerseThree(a, b, c):
    fitMedia(verseThree, a, b, c)
    setEffect(a, VOLUME, GAIN, -3, b, 7, b+2)

def runChorusFour(a, b, c):
    fitMedia(chorusFour, a, b, c)
    setEffect(a, VOLUME, GAIN, 10, b)
    setEffect(a, PITCHSHIFT, PITCHSHIFT_SHIFT, -5, b)

def runVerseFour(a, b, c):
    fitMedia(verseFour, a, b, c)
    setEffect(a, VOLUME, GAIN, 9, b)
    setEffect(a, PITCHSHIFT, PITCHSHIFT_SHIFT, 3, b)
    setEffect(a, VOLUME, GAIN, 9, c-3, -30, c)

def runOutro(a, b, c):
    fitMedia(outro, a, b, c)
    setEffect(a, VOLUME, GAIN, 10, b)

def runHook(a, b, c):
    fitMedia(hook, a, b, c)

# Call all functions to assemble the complete song, integrating musical elements, verses, choruses, and effects
backgroundMusic(1, 1, 69)
soundEffects(7, 1)
runChorusOne(9, 9, 13)
runVerseOne(8, 13, 17)
runSoundEffect(10, 17.5, 18.5)
runChorusTwo(10, 21, 24)
runVerseTwo(9, 25, 33)
runChorusThree(8, 35, 36.75)
runBridge(8, 37, 41)
runVerseThree(9, 41, 49)
runChorusFour(10, 49.25, 50.35)
runVerseFour(8, 53, 61)
runOutro(9, 60, 66.6)
runHook(10, 67, 69)


# Output
for i in range(1, 5):
    if i == 1:
        print("Initially, I utilized the tuba to establish a consistent, anchoring beat, laying a solid foundation. The first half focuses on Dakota Bear's compelling message, while Common's rap heightens the tension, showing how they are boiling over.")
    elif i == 2:
        print("In the second part, I shift to an Indigenous perspective, utilizing Samian's stem to connect to Jayli Wolf's words, \"child of the government\" and \"Father young blood took the children down, to the water with the cross and the Bible.\" These songs underscore the tragic past of residential schools, which is an important subject to share.")
    elif i == 3:
        print("I conclude with, \"Yeah, let's change the world,\" as a call to significant change representing a collective push for transformation. Minorities and the indigenous have been suffering quietly for too long and it is time that everyone comes together to make a change.")
    elif i == 4:
        print("The work incorporates the 4R themes—Respect, Relevance, Reciprocity, and Responsibility—by displaying respect for Indigenous perspectives, relevance to ongoing struggles, reciprocity in honouring history, and responsibility for a just future.")
