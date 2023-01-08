#Boa:Frame:Frame3

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
import wx.lib.stattext
import DeborphanGuiClasses
import os
import time
import string
import re

def create(parent):
    return Frame3(parent)

[wxID_FRAME3, wxID_FRAME3BUTTON1, wxID_FRAME3BUTTON2, wxID_FRAME3CHECKBOX1, 
 wxID_FRAME3CHECKBOX2, wxID_FRAME3CHECKBOX3, wxID_FRAME3COMBOBOX1, 
 wxID_FRAME3GENSTATICTEXT1, wxID_FRAME3LABELARCHITECTURE, 
 wxID_FRAME3LABELDESCRIPTION, wxID_FRAME3LABELNAME, wxID_FRAME3LABELPRIORITY, 
 wxID_FRAME3LABELSECTION, wxID_FRAME3LABELSIZE, wxID_FRAME3LABELVERSION, 
 wxID_FRAME3LISTBOX1, wxID_FRAME3NOTEBOOK1, wxID_FRAME3PANEL1, 
 wxID_FRAME3PANEL2, wxID_FRAME3PANEL3, wxID_FRAME3PANEL4, wxID_FRAME3PANEL5, 
 wxID_FRAME3STATICBOX1, wxID_FRAME3STATICBOX2, wxID_FRAME3STATICLINE1, 
 wxID_FRAME3STATICLINE2, wxID_FRAME3STATICLINE3, wxID_FRAME3TEXTCTRL1, 
 wxID_FRAME3VALUEARCHITECTURE, wxID_FRAME3VALUEDESCRIPTION, 
 wxID_FRAME3VALUENAME, wxID_FRAME3VALUEPRIORITY, wxID_FRAME3VALUESECTION, 
 wxID_FRAME3VALUESIZE, wxID_FRAME3VALUEVERSION, 
] = [wx.NewId() for _init_ctrls in range(35)]

class Frame3(wx.Frame):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel4, select=True,
              text=u'Simple')
        parent.AddPage(imageId=-1, page=self.panel5, select=False,
              text=u'Advanced')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME3, name='', parent=prnt,
              pos=wx.Point(291, 111), size=wx.Size(847, 659),
              style= wx.MINIMIZE_BOX | wx.MINIMIZE | wx.ICONIZE | wx.CLOSE_BOX,
              title=u'DeborphanGUI')
        self.SetClientSize(wx.Size(847, 659))
        self.SetBackgroundColour(wx.Colour(127, 127, 127))
        self.SetThemeEnabled(True)
        self.SetToolTipString(u'Frame3')
        self.SetAutoLayout(True)
        
        self.panel1 = wx.Panel(id=wxID_FRAME3PANEL1, name='panel1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(832, 120),
              style=wx.DOUBLE_BORDER | wx.SIMPLE_BORDER | wx.TRANSPARENT_WINDOW | wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(id=wxID_FRAME3PANEL2, name='panel2', parent=self,
              pos=wx.Point(8, 136), size=wx.Size(272, 512),
              style=wx.DOUBLE_BORDER | wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME3STATICBOX1,
              label=u'Options', name='staticBox1', parent=self.panel1,
              pos=wx.Point(8, 8), size=wx.Size(816, 104), style=wx.HSCROLL)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME3STATICBOX2,
              label=u'Packages', name='staticBox2', parent=self.panel2,
              pos=wx.Point(8, 8), size=wx.Size(256, 496), style=0)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME3LISTBOX1,
              name='listBox1', parent=self.panel2, pos=wx.Point(16, 24),
              size=wx.Size(240, 473), style=0)
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox,
              id=wxID_FRAME3LISTBOX1)

        self.checkBox1 = wx.CheckBox(id=wxID_FRAME3CHECKBOX1,
              label=u'Nice mode', name='checkBox1', parent=self.panel1,
              pos=wx.Point(200, 24), size=wx.Size(120, 40), style=0)
        self.checkBox1.SetValue(True)
        self.checkBox1.Bind(wx.EVT_LEFT_UP, self.OnCheckBox1LeftUp)

        self.checkBox2 = wx.CheckBox(id=wxID_FRAME3CHECKBOX2,
              label=u'Search in all packages', name='checkBox2',
              parent=self.panel1, pos=wx.Point(200, 72), size=wx.Size(192, 24),
              style=0)
        self.checkBox2.SetValue(False)
        self.checkBox2.Bind(wx.EVT_LEFT_UP, self.OnCheckBox2LeftUp)

        self.checkBox3 = wx.CheckBox(id=wxID_FRAME3CHECKBOX3,
              label=u'Search in libdevel', name='checkBox3', parent=self.panel1,
              pos=wx.Point(424, 32), size=wx.Size(152, 23), style=0)
        self.checkBox3.SetValue(False)
        self.checkBox3.Bind(wx.EVT_LEFT_UP, self.OnCheckBox3LeftUp)

        self.button1 = wx.Button(id=wxID_FRAME3BUTTON1, label=u'Remove',
              name='button1', parent=self.panel1, pos=wx.Point(608, 48),
              size=wx.Size(85, 32), style=0)
        self.button1.Bind(wx.EVT_LEFT_UP, self.OnButton1LeftUp)

        self.button2 = wx.Button(id=wxID_FRAME3BUTTON2, label=u'Purge',
              name='button2', parent=self.panel1, pos=wx.Point(712, 48),
              size=wx.Size(88, 32), style=0)
        self.button2.Bind(wx.EVT_LEFT_UP, self.OnButton2LeftUp)

        self.comboBox1 = wx.ComboBox(choices=[u'Required', u'Important',
              u'Standard', u'Optional', u'Extra'], id=wxID_FRAME3COMBOBOX1,
              name='comboBox1', parent=self.panel1, pos=wx.Point(24, 64),
              size=wx.Size(148, 27), style=wx.CB_READONLY, value=u'Important')
        self.comboBox1.SetStringSelection(u'2')
        self.comboBox1.SetToolTipString(u'comboBox1')
        self.comboBox1.SetLabel(u'')
        self.comboBox1.SetThemeEnabled(True)
        self.comboBox1.Bind(wx.EVT_COMBOBOX, self.OnComboBox1Combobox,
              id=wxID_FRAME3COMBOBOX1)

        self.genStaticText1 = wx.lib.stattext.GenStaticText(ID=wxID_FRAME3GENSTATICTEXT1,
              label=u'Package priority:', name='genStaticText1',
              parent=self.panel1, pos=wx.Point(32, 32), size=wx.Size(114, 17),
              style=0)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME3STATICLINE1,
              name='staticLine1', parent=self.panel1, pos=wx.Point(176, 16),
              size=wx.Size(32, 96), style=wx.LI_VERTICAL | wx.LI_HORIZONTAL)

        self.staticLine2 = wx.StaticLine(id=wxID_FRAME3STATICLINE2,
              name='staticLine2', parent=self.panel1, pos=wx.Point(392, 16),
              size=wx.Size(32, 96), style=wx.LI_VERTICAL | wx.LI_HORIZONTAL)

        self.staticLine3 = wx.StaticLine(id=wxID_FRAME3STATICLINE3,
              name='staticLine3', parent=self.panel1, pos=wx.Point(568, 16),
              size=wx.Size(40, 96), style=wx.LI_VERTICAL | wx.LI_HORIZONTAL)

        self.panel3 = wx.Panel(id=wxID_FRAME3PANEL3, name='panel3', parent=self,
              pos=wx.Point(288, 136), size=wx.Size(552, 512),
              style=wx.SIMPLE_BORDER | wx.DOUBLE_BORDER | wx.TAB_TRAVERSAL)

        self.notebook1 = wx.Notebook(id=wxID_FRAME3NOTEBOOK1, name='notebook1',
              parent=self.panel3, pos=wx.Point(8, 8), size=wx.Size(536, 496),
              style=0)

        self.panel4 = wx.Panel(id=wxID_FRAME3PANEL4, name='panel4',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(532, 461),
              style=wx.TAB_TRAVERSAL)

        self.panel5 = wx.Panel(id=wxID_FRAME3PANEL5, name='panel5',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(532, 461),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME3TEXTCTRL1, name='textCtrl1',
              parent=self.panel5, pos=wx.Point(5, 5), size=wx.Size(522, 450),
              style=wx.NO_3D | wx.TE_READONLY | wx.HSCROLL | wx.TE_WORDWRAP | wx.TE_MULTILINE,
              value=u'Select package.')

        self.labelName = wx.StaticText(id=wxID_FRAME3LABELNAME,
              label=u'Package name :', name=u'labelName', parent=self.panel4,
              pos=wx.Point(20, 20), size=wx.Size(107, 17), style=0)

        self.labelPriority = wx.StaticText(id=wxID_FRAME3LABELPRIORITY,
              label=u'Priority :', name=u'labelPriority', parent=self.panel4,
              pos=wx.Point(20, 40), size=wx.Size(73, 17), style=0)

        self.labelSection = wx.StaticText(id=wxID_FRAME3LABELSECTION,
              label=u'Section :', name=u'labelSection', parent=self.panel4,
              pos=wx.Point(20, 60), size=wx.Size(73, 17), style=0)

        self.labelArchitecture = wx.StaticText(id=wxID_FRAME3LABELARCHITECTURE,
              label=u'Architecture :', name=u'labelArchitecture',
              parent=self.panel4, pos=wx.Point(20, 80), size=wx.Size(156, 17),
              style=0)

        self.labelVersion = wx.StaticText(id=wxID_FRAME3LABELVERSION,
              label=u'Version :', name=u'labelVersion', parent=self.panel4,
              pos=wx.Point(20, 100), size=wx.Size(59, 17), style=0)

        self.labelSize = wx.StaticText(id=wxID_FRAME3LABELSIZE, label=u'Size :',
              name=u'labelSize', parent=self.panel4, pos=wx.Point(20, 120),
              size=wx.Size(73, 17), style=0)

        self.valueName = wx.StaticText(id=wxID_FRAME3VALUENAME,
              label=u'Select package.', name=u'valueName', parent=self.panel4,
              pos=wx.Point(155, 20), size=wx.Size(112, 17), style=0)

        self.valuePriority = wx.StaticText(id=wxID_FRAME3VALUEPRIORITY,
              label=u'Select package.', name=u'valuePriority',
              parent=self.panel4, pos=wx.Point(155, 40), size=wx.Size(108, 17),
              style=0)

        self.valueSection = wx.StaticText(id=wxID_FRAME3VALUESECTION,
              label=u'Select package.', name=u'valueSection',
              parent=self.panel4, pos=wx.Point(155, 60), size=wx.Size(108, 17),
              style=0)

        self.valueArchitecture = wx.StaticText(id=wxID_FRAME3VALUEARCHITECTURE,
              label=u'Select package.', name=u'valueArchitecture',
              parent=self.panel4, pos=wx.Point(155, 80), size=wx.Size(112, 17),
              style=0)

        self.valueVersion = wx.StaticText(id=wxID_FRAME3VALUEVERSION,
              label=u'Select package.', name=u'valueVersion',
              parent=self.panel4, pos=wx.Point(155, 100), size=wx.Size(108, 17),
              style=0)

        self.valueSize = wx.StaticText(id=wxID_FRAME3VALUESIZE,
              label=u'Select package', name=u'valueSize', parent=self.panel4,
              pos=wx.Point(155, 120), size=wx.Size(104, 17), style=0)

        self.labelDescription = wx.StaticText(id=wxID_FRAME3LABELDESCRIPTION,
              label=u'Description :', name=u'labelDescription',
              parent=self.panel4, pos=wx.Point(20, 140), size=wx.Size(88, 17),
              style=0)

        self.valueDescription = wx.TextCtrl(id=wxID_FRAME3VALUEDESCRIPTION,
              name=u'valueDescription', parent=self.panel4, pos=wx.Point(20,
              160), size=wx.Size(495, 295),
              style=wx.SIMPLE_BORDER | wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_WORDWRAP | wx.HSCROLL,
              value=u'Select package')
        self.valueDescription.SetBackgroundColour(wx.Colour(255, 255, 255))

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.showPackages()
        self.pakiet=' '
        self.Description=' '
        self.DescriptionStart=False
        
#showPackages generates the list of orphaned pkg and displays it        
    def showPackages(self):
        self.tab=[]
        runCommand=" "
        runCommand=DeborphanGuiClasses.commandGenerator.fGenerate()
        output=os.popen(runCommand)
        for x in output:
            self.tab.append(unicode(string.strip(x),'ascii'))
        self.listBox1.Clear()
        self.listBox1.Set(self.tab)
        output.close()
        
#Chackbox 1 Nice mode
    def OnCheckBox1LeftUp(self, event):
        if int(self.checkBox1.GetValue())==1:
            DeborphanGuiClasses.commandGenerator.fNiceMode(0)
        else:
            DeborphanGuiClasses.commandGenerator.fNiceMode(1)
        self.showPackages()
        event.Skip()
        
#Checkbox 2 Search in all packages
    def OnCheckBox2LeftUp(self, event):
        if int(self.checkBox2.GetValue())==1:
            DeborphanGuiClasses.commandGenerator.fAllPackages(0)
        else:
            DeborphanGuiClasses.commandGenerator.fAllPackages(1)
        self.showPackages()
        event.Skip()
        
#Checkbox 3 Seach in libdevel
    def OnCheckBox3LeftUp(self, event):
        if int(self.checkBox3.GetValue())==1:
            DeborphanGuiClasses.commandGenerator.fSearchInLibdevel(0)
        else:
            DeborphanGuiClasses.commandGenerator.fSearchInLibdevel(1)
        self.showPackages()
        event.Skip()
        
#Listbox 1 Packages list
    def OnListBox1Listbox(self, event):
        temp=" "
        self.pakiet=self.listBox1.GetStringSelection()
        output=os.popen("apt-cache show "+self.pakiet)
    #Clear all fields
        self.textCtrl1.Clear()
        self.valueName.SetLabel(" Unknown")
        self.valuePriority.SetLabel(" Unknown")
        self.valueSection.SetLabel(" Unknown")
        self.valueArchitecture.SetLabel(" Unknown")
        self.valueVersion.SetLabel(" Unknown")
        self.valueSize.SetLabel(" Unknown")
        self.Description=""
    #Search for fields in simple view.
        for x in output:
            self.textCtrl1.WriteText(unicode(x,'ascii'))
        #Package name
            if re.search('^Package:', x)!=None:
                temp=re.split(':',x)
                self.valueName.SetLabel(temp[1])
        #Priority
            if re.search('^Priority:', x)!=None:
                temp=re.split(':',x)
                self.valuePriority.SetLabel(temp[1])
        #Section
            if re.search('^Section:', x)!=None:
                temp=re.split(':',x)
                self.valueSection.SetLabel(temp[1])
        #Architecture
            if re.search('^Architecture:', x)!=None:
                temp=re.split(':',x)
                self.valueArchitecture.SetLabel(temp[1])
        #Version
            if re.search('^Version:', x)!=None:
                temp=re.split(':',x)
                self.valueVersion.SetLabel(temp[1])
        #Size        
            if re.search('^Size:', x)!=None:
                temp=re.split(':',x)
                self.valueSize.SetLabel(temp[1])
        #Description section    
            #End loading description
            if (self.DescriptionStart==True) and (re.search('^[a-zA-Z0-9]*?:', x)!=None):
                self.DescriptionStart=False
                self.valueDescription.SetValue(self.Description)
            #Continue loading description
            if self.DescriptionStart==True:
                self.Description=self.Description+x
            #Sart loading description
            if re.search('^Description:', x)!=None:
                temp=re.split(':',x)
                self.Description=temp[1]
                self.DescriptionStart=True
    
    #Close                 
        output.close()
    #Close the decription section if not closed
        self.DescriptionStart=False
        self.valueDescription.SetValue(self.Description)
    #Revind Viev to the top
        self.textCtrl1.SetInsertionPoint(0)
        event.Skip()
        
#ComboBox 1 Package level  1-required,2-important,3-standard,4-optional,5-extra
    def OnComboBox1Combobox(self, event):
        DeborphanGuiClasses.commandGenerator.fPackagePriority(self.comboBox1.GetValue())
        self.showPackages()
        event.Skip()
        
#Button 1 Remove package
    def OnButton1LeftUp(self, event):
	os.popen("xterm -hold -T DeborphanGui -e su root -c 'apt-get autoremove "+ (self.pakiet)+" ;echo \n\n\n echo You can close the window.'")
        #os.popen("xterm -hold -T DeborphanGui -e su root -c 'apt-get autoremove "+ (self.pakiet)+"' 'echo \n\n\n' echo'You can close the window now.'")
        self.showPackages()
        event.Skip()
        
#Button 2 Purge package
    def OnButton2LeftUp(self, event):
	os.popen("xterm -hold -T DeborphanGui -e su root -c 'apt-get --purge autoremove "+ (self.pakiet)+" ;echo \n\n\n echo You can close the window.'")
        #os.popen("xterm -hold -T DeborphanGui -e su root -c 'apt-get --purge autoremove "+ (self.pakiet)+"' echo '\n\n\n' echo'You can close the window now.'")
        self.showPackages()
        event.Skip()



