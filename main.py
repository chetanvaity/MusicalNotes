import turtle

# TBD
# - Handle double length notes

# Constants
scaleFactor = 0.7
noteRadius = scaleFactor * 10
oMultiplier = scaleFactor * 10 * noteRadius # Octave Y coordinate difference
# How long is the vertical line on the note compared to the noteRadius
lineMultiplier = 6


t = turtle.Turtle()
t.speed("normal")

def drawAxes():
  t.setposition(0,0)
  t.setheading(90)
  t.forward(scaleFactor * 200)
  t.penup()
  t.setposition(0,0)
  t.setheading(0)
  t.pendown()
  t.forward(scaleFactor * 200)

# Draw a simple note at x,y
def drawNormalNote(x, y):
  print("Drawing a note at: x=%d, y=%d" % (x, y))
  t.penup()
  t.setposition(x, y)
  t.pendown()

  t.setheading(0)
  t.begin_fill()
  # TBD: Make this into ellipse
  t.circle(noteRadius)
  t.end_fill()
 
  t.penup()
  t.forward(noteRadius)
  t.left(90)
  t.forward(noteRadius)
  t.pendown()
  t.forward(noteRadius*lineMultiplier)

def drawFlatNote(x, y):
  drawNormalNote(x, y)
  t.penup(); t.setposition(x+11,y+10); t.pendown()
  t.write("b", font=("Verdana", 15, "italic"))

def drawSharpNote(x, y):
  drawNormalNote(x, y)
  t.penup();t.setposition(x+11,y+10);t.pendown();
  t.write("#", font=("Verdana", 15, "italic"))

# Draw a sequence of notes given a string like "CEFGG"
# "y" denotes where on the page the sequence should be drawn
def drawNoteSequence(noteString, y):
  startXForSequence = scaleFactor * 20

  YList = getYSequenceFromNoteString(noteString)
  x = startXForSequence
  for Y in YList:
    if Y[1] == "flat":
      drawFlatNote(x, y+Y[0])
    elif Y[1] == "sharp":
      drawSharpNote(x, y+Y[0])
    else:
      drawNormalNote(x, y+Y[0])
    # Advance position for next note
    t.penup()
    x = x + (noteRadius*4)
    t.pendown()

# Given a note sequence like "CEFGG", return a sequence of Y-coordinates
def getYSequenceFromNoteString(noteString):
  YList = []
  ModList = []
  for ch in noteString:
    if ch == "^":
      prevNoteY = YList.pop()
      correctNoteY = prevNoteY[0] + oMultiplier
      YList.append((correctNoteY, "normal"))
    elif ch == ".":
      prevNoteY = YList.pop()
      correctNoteY = prevNoteY[0] - oMultiplier
      YList.append((correctNoteY, "normal"))
    elif ch == "f":
      prevNoteY = YList.pop()
      YList.append((prevNoteY[0], "flat"))
    elif ch == "#":
      prevNoteY = YList.pop()
      YList.append((prevNoteY[0], "sharp"))
    else:
      YList.append((getYForNote(ch), "normal"))

  print YList
  return YList

# octave=3 means lower octave (mandra saptak)
# octave=2 means default (madhyam saptak)
# octave=1 means higher octave (taar saptak)
def getYForNote(note):
  print("note = ", note)
  if note == "C":
    f = -noteRadius
  elif note == "D":
    f = 0
  elif note == "E":
    f = noteRadius
  elif note == "F":
    f = noteRadius*2
  elif note == "G":
    f = noteRadius*3
  elif note == "A":
    f = noteRadius*4
  elif note == "B":
    f = noteRadius*5
  # 2 is the octave here below
  return (2 * oMultiplier) +  f

# For default octave, draw the horizontal lines
def drawStaffLines(y):
  t.pensize(0.3)
  staffStartX = -20
  for i in range(1,6):
    t.penup()
    t.setposition(staffStartX, y + (2*oMultiplier) + i*(noteRadius*2))
    t.pendown()
    t.setheading(0) # face east
    t.forward(scaleFactor * 700)
  t.pensize(1)

# Given "SRGM", return "CDEF"
def getWesternNoteFromHindustani(hindustaniNote):
  print ("hindustaniNote: " + hindustaniNote)
  noteMap = {
    "S": "C",
    "R": "D",
    "G": "E",
    "M": "F",
    "P": "G",
    "D": "A",
    "N": "B"
    }
  return noteMap[hindustaniNote]

def drawHindustaniNoteSequence(hNoteString, y):
  wString = ""
  for ch in hNoteString:
    if (ch == "^") or (ch == ".") or (ch == "f") or (ch == "#"):
      wString = wString + ch
    else:
      wString = wString + getWesternNoteFromHindustani(ch)
  drawNoteSequence(wString, y)

# Main function call
#print getWesternNotesFromHindustani("S")
drawStaffLines(0)
drawStaffLines(scaleFactor * -200)
drawStaffLines(scaleFactor * -400)
drawStaffLines(scaleFactor * -600)

#drawNoteSequence("CDEFGABC^")
#drawHindustaniNoteSequence("SRGMPDNS^NDPMGRSN.", 0)
drawHindustaniNoteSequence("SGMPNNS^S^PNfPMGGSS", 0)
drawHindustaniNoteSequence("PS^NNPNfPPGPMGSSN.N.", scaleFactor * -200)
drawHindustaniNoteSequence("MGMPNNS^S^PNS^M^G^G^S^S^", scaleFactor * -400)
drawHindustaniNoteSequence("G^S^NS^NfPMPGPMGSSN.N.", scaleFactor * -600)


