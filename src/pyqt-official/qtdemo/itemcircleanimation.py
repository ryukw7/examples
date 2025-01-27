#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial Usage
## Licensees holding valid Qt Commercial licenses may use this file in
## accordance with the Qt Commercial License Agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and Nokia.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 2.1 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU Lesser General Public License version 2.1 requirements
## will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
##
## In addition, as a special exception, Nokia gives you certain additional
## rights.  These rights are described in the Nokia Qt LGPL Exception
## version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3.0 as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL included in the
## packaging of this file.  Please review the following information to
## ensure the GNU General Public License version 3.0 requirements will be
## met: http://www.gnu.org/copyleft/gpl.html.
##
## If you have questions regarding the use of this file, please contact
## Nokia at qt-info@nokia.com.
## $QT_END_LICENSE$
##
#############################################################################


import math
import random

from PyQt6.QtCore import QLineF, QPointF, QRectF, Qt, QTime

from colors import Colors
from demoitem import DemoItem
from demoitemanimation import DemoItemAnimation
from guidecircle import GuideCircle
from guideline import GuideLine
from letteritem import LetterItem


class TickerPostEffect(object):
    def tick(self, adjust):
        pass

    def transform(self, item, pos):
        pass


class PostRotateXY(TickerPostEffect):
    def __init__(self, speedx, speedy, curvx, curvy):
        super(PostRotateXY, self).__init__()

        self.currRotX = 0.0
        self.currRotY = 0.0

        self.speedx = speedx
        self.speedy = speedy
        self.curvx = curvx
        self.curvy = curvy

    def tick(self, adjust):
        self.currRotX += self.speedx * adjust
        self.currRotY += self.speedy * adjust

    def transform(self, item, pos):
        parent = item.parentItem()
        center = parent.boundingRect().center()
        pos.setX(center.x() + (pos.x() - center.x()) * math.cos(self.currRotX + pos.x() * self.curvx))
        pos.setY(center.y() + (pos.y() - center.y()) * math.cos(self.currRotY + pos.y() * self.curvy))


class PostRotateXYTwist(PostRotateXY):
    def transform(self, item, pos):
        parent = item.parentItem()
        center = parent.boundingRect().center()
        pos.setX(center.x() + (pos.x() - center.x()) * math.cos(self.currRotX + pos.y() * self.curvx))
        pos.setY(center.y() + (pos.y() - center.y()) * math.cos(self.currRotY + pos.x() * self.curvy))


class TickerEffect(object):
    Normal, Intro, Outro = range(3)

    def __init__(self, letters):
        self.postEffect = TickerPostEffect()
        self.status = TickerEffect.Intro
        self.letters = letters
        self.morphSpeed = self.normalMorphSpeed = Colors.tickerMorphSpeed
        self.moveSpeed = self.normalMoveSpeed = Colors.tickerMoveSpeed
        self.useSheepDog = True
        self.morphBetweenModels = not Colors.noTickerMorph

    def setPostEffect(self, effect):
        self.postEffect = effect

    def slowDownAfterIntro(self, adjust):
        if self.morphBetweenModels:
            if self.status == TickerEffect.Intro:
                dec = 0.1 * adjust
                self.moveSpeed -= dec
                if self.moveSpeed < Colors.tickerMoveSpeed:
                    self.moveSpeed = self.normalMoveSpeed
                    self.morphSpeed = self.normalMorphSpeed
                    self.status = TickerEffect.Normal

    def moveLetters(self, adjust):
        adaptedMoveSpeed = self.moveSpeed * adjust
        adaptedMorphSpeed = self.morphSpeed * adjust
        self.postEffect.tick(adjust)

        if self.morphBetweenModels:
            move_speed = adaptedMoveSpeed
            morph_speed = adaptedMorphSpeed
        else:
            move_speed = Colors.tickerMoveSpeed
            morph_speed = -1

        for letter in self.letters:
            letter.guideAdvance(move_speed)
            letter.guideMove(morph_speed)

            pos = letter.getGuidedPos()
            self.postEffect.transform(letter, pos)

            if self.useSheepDog:
                letter.setPosUsingSheepDog(pos, QRectF(0, 0, 800, 600))
            else:
                letter.setPos(pos)

    def tick(self, adjust):
        self.slowDownAfterIntro(adjust)
        self.moveLetters(adjust)


class EffectWhirlWind(TickerEffect):
    def __init__(self, letters):
        super(EffectWhirlWind, self).__init__(letters)

        self.moveSpeed = 50

        for letter in self.letters:
            letter.setGuidedPos(QPointF(0, 100))


class EffectSnake(TickerEffect):
    def __init__(self, letters):
        super(EffectSnake, self).__init__(letters)

        self.moveSpeed = 40

        for i, letter in enumerate(self.letters):
            letter.setGuidedPos(QPointF(0, -250 - (i * 5)))


class EffectScan(TickerEffect):
    def __init__(self, letters):
        super(EffectScan, self).__init__(letters)

        for letter in self.letters:
            letter.setGuidedPos(QPointF(100, -300))


class EffectRaindrops(TickerEffect):
    def __init__(self, letters):
        super(EffectRaindrops, self).__init__(letters)

        for letter in self.letters:
            letter.setGuidedPos(QPointF(random.randint(-100, 100),
                    random.randint(-200, 1100)))


class EffectLine(TickerEffect):
    def __init__(self, letters):
        super(EffectLine, self).__init__(letters)

        for i, letter in enumerate(self.letters):
            letter.setGuidedPos(QPointF(100, 500 + i * 20))


class ItemCircleAnimation(DemoItem):
    def __init__(self, parent=None):
        super(ItemCircleAnimation, self).__init__(parent)

        self.letterList = []
        self.letterCount = Colors.tickerLetterCount
        self.scale = 1.0
        self.showCount = -1
        self.tickOnPaint = False
        self.paused = False
        self.doIntroTransitions = True
        self.setAcceptHoverEvents(True)
        self.setCursor(Qt.OpenHandCursor)
        self.setupGuides()
        self.setupLetters()
        self.useGuideQt()
        self.effect = None

        self.mouseMoveLastPosition = QPointF()
        self.tickTimer = QTime()

    def createLetter(self, c):
        letter = LetterItem(c, self)
        self.letterList.append(letter)

    def setupLetters(self):
        self.letterList = []

        s = Colors.tickerText
        tlen = len(s)
        room = self.letterCount
        while room >= tlen:
            for c in s:
                self.createLetter(c)

            room -= tlen

        # Fill in with blanks.
        while room > 0:
            self.createLetter(' ')
            room -= 1

    def setupGuides(self):
        x = 0
        y = 20

        self.qtGuide1 = GuideCircle(QRectF(x, y, 260, 260), -36, 342)
        GuideLine(QPointF(x + 240, y + 268), self.qtGuide1)
        GuideLine(QPointF(x + 265, y + 246), self.qtGuide1)
        GuideLine(QPointF(x + 158, y + 134), self.qtGuide1)
        GuideLine(QPointF(x + 184, y + 109), self.qtGuide1)
        GuideLine(QPointF(x + 160, y +  82), self.qtGuide1)
        GuideLine(QPointF(x +  77, y + 163), self.qtGuide1)
        GuideLine(QPointF(x + 100, y + 190), self.qtGuide1)
        GuideLine(QPointF(x + 132, y + 159), self.qtGuide1)
        GuideLine(QPointF(x + 188, y + 211), self.qtGuide1)
        GuideCircle(QRectF(x + 30, y + 30, 200, 200), -30, 336, GuideCircle.CW, self.qtGuide1)
        GuideLine(QPointF(x + 238, y + 201), self.qtGuide1)

        y = 30
        self.qtGuide2 = GuideCircle(QRectF(x + 30, y + 30, 200, 200), 135, 270, GuideCircle.CCW)
        GuideLine(QPointF(x + 222, y + 38), self.qtGuide2)
        GuideCircle(QRectF(x, y, 260, 260), 135, 270, GuideCircle.CW, self.qtGuide2)
        GuideLine(QPointF(x + 59, y + 59), self.qtGuide2)

        x = 115
        y = 10
        self.qtGuide3 = GuideLine(QLineF(x, y, x + 30, y))
        GuideLine(QPointF(x + 30, y + 170), self.qtGuide3)
        GuideLine(QPointF(x, y + 170), self.qtGuide3)
        GuideLine(QPointF(x, y), self.qtGuide3)

        self.qtGuide1.setFence(QRectF(0, 0, 800, 600))
        self.qtGuide2.setFence(QRectF(0, 0, 800, 600))
        self.qtGuide3.setFence(QRectF(0, 0, 800, 600))

    def useGuide(self, guide, firstLetter, lastLetter):
        padding = guide.lengthAll() / float(lastLetter - firstLetter)

        for i, letter in enumerate(self.letterList[firstLetter:lastLetter]):
            letter.useGuide(guide, i * padding)

    def useGuideQt(self):
        if self.currGuide is not self.qtGuide1:
            self.useGuide(self.qtGuide1, 0, self.letterCount)
            self.currGuide = self.qtGuide1

    def useGuideTt(self):
        if self.currGuide is not self.qtGuide2:
            split = int(self.letterCount * 5.0 / 7.0)
            self.useGuide(self.qtGuide2, 0, split)
            self.useGuide(self.qtGuide3, split, self.letterCount)
            self.currGuide = self.qtGuide2

    def boundingRect(self):
        return QRectF(0, 0, 300, 320)

    def prepare(self):
        pass

    def switchToNextEffect(self):
        self.showCount += 1

        if self.showCount == 1:
            self.effect = EffectSnake(self.letterList)
        elif self.showCount == 2:
            self.effect = EffectLine(self.letterList)
            self.effect.setPostEffect(PostRotateXYTwist(0.01, 0.0, 0.003, 0.0))
        elif self.showCount == 3:
            self.effect = EffectRaindrops(self.letterList)
            self.effect.setPostEffect(PostRotateXYTwist(0.01, 0.005, 0.003, 0.003))
        elif self.showCount == 4:
            self.effect = EffectScan(self.letterList)
            self.effect.normalMoveSpeed = 0
            self.effect.setPostEffect(PostRotateXY(0.008, 0.0, 0.005, 0.0))
        else:
            self.showCount = 0
            self.effect = EffectWhirlWind(self.letterList)

    def animationStarted(self, id):
        if id == DemoItemAnimation.ANIM_IN:
            if self.doIntroTransitions:
                # Make all letters disappear.
                for letter in self.letterList:
                    letter.setPos(1000, 0)

                self.switchToNextEffect()
                self.useGuideQt()
                self.scale = 1.0

                # The first time we run, we have a rather large delay to
                # perform benchmark before the ticker shows.  But now, since we
                # are showing, use a more appropriate value.
                self.currentAnimation.setStartDelay(1500)
        elif self.effect is not None:
            self.effect.useSheepDog = False

        self.tickTimer = QTime.currentTime()

    def swapModel(self):
        if self.currGuide is self.qtGuide2:
            self.useGuideQt()
        else:
            self.useGuideTt()

    def hoverEnterEvent(self, event):
        # Skip swap here to enhance ticker dragging.
        pass

    def hoverLeaveEvent(self, event):
        self.swapModel()

    def setTickerScale(self, s):
        self.scale = s
        self.qtGuide1.setScale(self.scale, self.scale)
        self.qtGuide2.setScale(self.scale, self.scale)
        self.qtGuide3.setScale(self.scale, self.scale)

    def mousePressEvent(self, event):
        self.mouseMoveLastPosition = event.scenePos();

        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
        else:
            self.switchToNextEffect()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.OpenHandCursor)

    def mouseMoveEvent(self, event):
        newPosition = event.scenePos()
        self.setPosUsingSheepDog(self.pos() + newPosition - self.mouseMoveLastPosition, QRectF(-260, -280, 1350, 1160))
        self.mouseMoveLastPosition = newPosition

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.effect.moveSpeed -= 0.20
        else:
            self.effect.moveSpeed += 0.20

        if self.effect.moveSpeed < 0:
            self.effect.moveSpeed = 0.0

    def pause(self, on):
        self.paused = on
        self.tickTimer = QTime.currentTime()

    def tick(self):
        if self.paused or not self.effect:
            return

        t = self.tickTimer.msecsTo(QTime.currentTime())
        self.tickTimer = QTime.currentTime()
        self.effect.tick(t / 10.0)

    def paint(self, painter, opt, widget):
        if self.tickOnPaint:
            self.tick()
