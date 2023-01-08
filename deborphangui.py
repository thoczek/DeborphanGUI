#!/usr/bin/env python
#Boa:App:BoaApp

##########################################################################
#    DeborpganGui
#
#    Copyright (C) 2007  Tadeusz Hoczek thoczek@users.sourceforge.net 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##########################################################################  

import wx

import MainFrame

modules ={u'DeborphanGuiClasses': [0, '', u'DeborphanGuiClasses.py'],
 u'MainFrame': [1, 'Main frame of Application', u'MainFrame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = MainFrame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
