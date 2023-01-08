
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
  
import os
import time

class Polecenie:
    def __init__(self):
        self.niceMode=1
        self.allPackages=0
        self.searchLibdevel=0
        self.packagePriority=2
        
    def fGenerate(self):
        komenda="deborphan"
        if self.niceMode==0:
            komenda=komenda+" -n"
        if self.packagePriority!=0:
            komenda=komenda+" --priority="+str(self.packagePriority)
        if self.allPackages==1:
            komenda=komenda+" -a --no-show-section"
        if self.searchLibdevel==1:
            komenda=komenda+" --libdevel"
        return komenda
    
    def fNiceMode(self,niceMode):#Bool 0-standard,1-nice mode
        if niceMode==1:
            self.niceMode=1
        else:
            self.niceMode=0
            
    def fPackagePriority(self,packagePriority):#Range 1-5:required,important,standard,optional,extra
        if packagePriority=='Required':
            self.packagePriority=1
        elif packagePriority=='Important':
            self.packagePriority=2
        elif packagePriority=='Standard':
            self.packagePriority=3
        elif packagePriority=='Optional':
            self.packagePriority=4
        elif packagePriority=='Extra':
            self.packagePriority=5
        else:
            self.packagePriority=0
            
    def fAllPackages(self,allPackages):#Bool 0-only libs,1-all packages
        if allPackages==1:
            self.allPackages=1
        else:
            self.allPackages=0
    
    def fSearchInLibdevel(self,searchLibdevel):
        if searchLibdevel==1:
            self.searchLibdevel=1
        else:
            self.searchLibdevel=0
    
commandGenerator=Polecenie()