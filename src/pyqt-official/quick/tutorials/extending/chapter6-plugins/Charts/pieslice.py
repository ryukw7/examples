#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
##     of its contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


from PyQt6.QtCore import pyqtProperty, QRectF
from PyQt6.QtGui import QColor, QPainter, QPen
from PyQt6.QtQuick import QQuickPaintedItem


class PieSlice(QQuickPaintedItem):

    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = QColor(color)

    @pyqtProperty(int)
    def fromAngle(self):
        return self._fromAngle

    @fromAngle.setter
    def fromAngle(self, fromAngle):
        self._fromAngle = fromAngle

    @pyqtProperty(int)
    def angleSpan(self):
        return self._angleSpan

    @angleSpan.setter
    def angleSpan(self, angleSpan):
        self._angleSpan = angleSpan

    def __init__(self, parent=None):
        super(PieSlice, self).__init__(parent)

        self._color = QColor()
        self._fromAngle = 0
        self._angleSpan = 0

    def paint(self, painter):
        painter.setPen(QPen(self._color, 2))
        painter.setRenderHints(QPainter.Antialiasing, True)

        rect = QRectF(0, 0, self.width(), self.height()).adjusted(1, 1, -1, -1)
        painter.drawPie(rect, self._fromAngle * 16, self._angleSpan * 16)
