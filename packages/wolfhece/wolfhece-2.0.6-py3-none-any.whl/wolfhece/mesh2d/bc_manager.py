import wx
import numpy as np
from scipy.spatial import cKDTree
from OpenGL.GL  import *
import logging
from typing import Union,Literal
from os.path import exists

from .cst_2D_boundary_conditions import BCType_2D_OO, BCType_2D, ColorsNb, choose_bc_type
from ..PyTranslate import _
from ..wolf_array import WolfArray
from .wolf2dprev import prev_boundary_conditions, boundary_condition_2D, prev_parameters_simul

class BcManager(wx.Frame):
    """Boundary conditions Manager for WOLF"""

    _filename_cl:str
    bordersX:dict
    bordersY:dict
    dx:float
    dy:float
    orig:list[float,float]

    def __init__(self,
                 parent = None,
                 linked_array:WolfArray = None,
                 dx = 1.,
                 dy = 1.,
                 ox = 0.,
                 oy = 0.,
                 version=2,
                 title = _("Boundary Condition manager"),
                 width = 500,
                 height = 500,
                 DestroyAtClosing=False,
                 *args, **kwargs):

        self._filename_cl = ''
        self._filename_sux = ''
        self.dx  = dx
        self.dy  = dy
        self.orig= [ox,oy]

        self._linked_array = linked_array

        if linked_array is not None:
            self.dx = linked_array.dx
            self.dy = linked_array.dy
            self.orig = [linked_array.origx+linked_array.translx,
                         linked_array.origy+linked_array.transly]

        self._version = version
        self.bc_type = choose_bc_type(version)

        self.bordersX:dict['bc':int]
        self.bordersX={}
        self.bordersY={}

        self.bordersX['bc']={}
        self.bordersY['bc']={}

        # bordersX and bordersY will contain
        #
        # 'bc'         : dict where keys are 'i-j' (1-based) and containing all BC value and type
        # 'selected'   : numpy array of boolean
        # 'indices'    : border's reference in indices - Numpy array - shape (2,nbx),dtype=np.integer
        # 'indicesstr' : list with string 'ii-jj'
        # 'coords'     : border's extremities - Numpy array - shape (2,2,nbx/nby),dtype=float
        # 'coordscg'   : border's gravity center - Numpy array - shape (2,nbx/nby),dtype=float

        self._filecontent = ''

        self.wx_exists = wx.App.Get() is not None # test if wx App is running

        if self.wx_exists:
            super(BcManager, self).__init__(parent, title = title,size = (width,height))
            self._DestroyAtClosing = DestroyAtClosing
            self.init_2D()
            self.Show(True)

    @property
    def linked_array(self):
        return self._linked_array

    @property
    def get_fname_cl(self):
        return self._filename_cl

    @property
    def get_fname_sux_suy(self):
        if self._filename_sux !='':
            return self._filename_sux, self._filename_sux.replace('sux','suy')
        else:
            return '',''

    def init_2D(self):
        """Init wx Frame"""
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        #Premiers boutons
        self.sizerbut1 = wx.BoxSizer(wx.HORIZONTAL)

        self.butLoad = wx.Button(self,wx.ID_ANY,"Load from file...")
        self.butLoad.Bind(wx.EVT_BUTTON,self.OnLoad)

        self.butSave = wx.Button(self,wx.ID_ANY,"Write to file...")
        self.butSave.Bind(wx.EVT_BUTTON,self.OnSave)

        self.sizerbut1.Add(self.butLoad,1,wx.EXPAND)
        self.sizerbut1.Add(self.butSave,1,wx.EXPAND)

        self.sizerbut2 = wx.BoxSizer(wx.HORIZONTAL)
        self.butSet = wx.Button(self,wx.ID_ANY,"Set BC")
        self.butSet.Bind(wx.EVT_BUTTON,self.OnApplyBC)
        self.butSet.SetToolTip(_('Impose BC for the selected borders'))

        self.butGet = wx.Button(self,wx.ID_ANY,"Get BC")
        self.butGet.Bind(wx.EVT_BUTTON,self.OnGetBC)
        self.butGet.SetToolTip(_('Retrieve BC for the selected borders'))

        self.butReset = wx.Button(self,wx.ID_ANY,"Reset BC")
        self.butReset.Bind(wx.EVT_BUTTON,self.OnResetBC)
        self.butReset.SetToolTip(_('Reset all BC values'))

        self.sizerbut2.Add(self.butSet,1,wx.EXPAND)
        self.sizerbut2.Add(self.butGet,1,wx.EXPAND)
        self.sizerbut2.Add(self.butReset,1,wx.EXPAND)

        #type de CL en "collapsable"
        self.sizerAllBC = wx.BoxSizer(wx.VERTICAL)
        self.sizerAllBCt = wx.BoxSizer(wx.VERTICAL)
        self._sizerBC = {}
        self._checkBC = {}
        self._labelBC = {}
        self._valueBC = {}
        self._findBC = {}

        self.collpane = wx.CollapsiblePane(self, wx.ID_ANY, "Type of BC:")
        win = self.collpane.GetPane()
        self.sizerAllBC.Add(self.collpane,1,wx.EXPAND|wx.GROW| wx.ALL)

        for curbc in self.bc_type:
            valbc, name_bc  = curbc.value
            self._sizerBC[name_bc] = wx.BoxSizer(wx.HORIZONTAL)

            self._checkBC[name_bc] = wx.CheckBox(win)
            self._labelBC[name_bc] = wx.StaticText(win,label=name_bc,size=(200,20))
            self._valueBC[name_bc] = wx.TextCtrl(win,size=(100,20),style=wx.TE_CENTRE)
            self._findBC[name_bc] = wx.Button(win,name=name_bc,label="Find all",size=(60,20))
            self._findBC[name_bc].Bind(wx.EVT_BUTTON,self.OnFind)

            self._sizerBC[name_bc].Add(self._checkBC[name_bc],0,wx.GROW)
            self._sizerBC[name_bc].Add(self._labelBC[name_bc],0,wx.FIXED_MINSIZE|wx.GROW)
            self._sizerBC[name_bc].Add(self._valueBC[name_bc],1,wx.FIXED_MINSIZE|wx.GROW|wx.EXPAND)
            self._sizerBC[name_bc].Add(self._findBC[name_bc],0,wx.GROW)
            self.sizerAllBCt.Add(self._sizerBC[name_bc],1,wx.EXPAND)

        win.SetSizer(self.sizerAllBCt)

        #Zone de selection
        self.sizerselectAll = wx.BoxSizer(wx.VERTICAL)
        self.sizerselect = wx.BoxSizer(wx.VERTICAL)

        self.collpaneSelect = wx.CollapsiblePane(self, wx.ID_ANY, "Selected Borders:")
        win = self.collpaneSelect.GetPane()
        self.sizerselectAll.Add(self.collpaneSelect,1,wx.EXPAND|wx.GROW| wx.ALL)


        self.sizerselButtons = wx.BoxSizer(wx.HORIZONTAL)
        self.butClear = wx.Button(win,wx.ID_CLEAR,"Unselect all")
        self.butClear.Bind(wx.EVT_BUTTON,self.OnClearselection)
        self.butFind = wx.Button(win,wx.ID_CLEAR,"Find borders")
        self.butFind.Bind(wx.EVT_BUTTON,self.OnFindBorders)

        self.sizerselButtons.Add(self.butClear,1,wx.EXPAND|wx.GROW)
        self.sizerselButtons.Add(self.butFind,1,wx.EXPAND|wx.GROW)

        self.sizercmdx = wx.BoxSizer(wx.HORIZONTAL)
        self.sizercmdy = wx.BoxSizer(wx.HORIZONTAL)

        self.labelcmdx = wx.StaticText(win,label='X:')
        self.cmdx = wx.TextCtrl(win,size=(490,20),style=wx.TE_PROCESS_TAB)
        self.sizercmdx.Add(self.labelcmdx,0,wx.GROW)
        self.sizercmdx.Add(self.cmdx,1,wx.FIXED_MINSIZE|wx.GROW)

        self.labelcmdy = wx.StaticText(win,label='Y:')
        self.cmdy = wx.TextCtrl(win,size=(490,20),style=wx.TE_PROCESS_TAB)
        self.sizercmdy.Add(self.labelcmdy,0,wx.GROW)
        self.sizercmdy.Add(self.cmdy,1,wx.FIXED_MINSIZE|wx.GROW)

        self.sizerselcommand = wx.BoxSizer(wx.VERTICAL)
        self.labelcmd = wx.StaticText(win,label='Selection')
        self.labelexample = wx.StaticText(win,label='example : 5,6,10-20  tab  10,20,40-60')

        self.sizerselcommand.Add(self.labelcmd,0,wx.GROW)
        self.sizerselcommand.Add(self.labelexample,0,wx.GROW)

        self.sizerselcommand.Add(self.sizercmdx,1,wx.EXPAND)
        self.sizerselcommand.Add(self.sizercmdy,1,wx.EXPAND)

        self.sizerTextBoxes = wx.BoxSizer(wx.HORIZONTAL)

        self.sizerTextBoxX = wx.BoxSizer(wx.VERTICAL)
        self.sizerTextBoxY = wx.BoxSizer(wx.VERTICAL)

        self.labelBCx = wx.StaticText(win,label='Borders along X axis |')
        self.BCx = wx.TextCtrl(win,size=(250,250),style=wx.TE_MULTILINE|wx.TE_PROCESS_TAB)
        self.sizerTextBoxX.Add(self.labelBCx,0,wx.GROW)
        self.sizerTextBoxX.Add(self.BCx,1,wx.GROW|wx.EXPAND)

        self.labelBCy = wx.StaticText(win,label='Borders along Y axis _')
        self.BCy = wx.TextCtrl(win,size=(250,250),style=wx.TE_MULTILINE|wx.TE_PROCESS_TAB)
        self.sizerTextBoxY.Add(self.labelBCy,0,wx.GROW)
        self.sizerTextBoxY.Add(self.BCy,1,wx.GROW|wx.EXPAND)

        self.sizerTextBoxes.Add(self.sizerTextBoxX,1,wx.EXPAND)
        self.sizerTextBoxes.Add(self.sizerTextBoxY,1,wx.EXPAND)

        self.sizerselect.Add(self.sizerselcommand,0,wx.EXPAND)
        self.sizerselect.Add(self.sizerselButtons,0,wx.EXPAND)
        self.sizerselect.Add(self.sizerTextBoxes,0,wx.EXPAND)

        win.SetSizer(self.sizerselect)

        self.sizerfile = wx.BoxSizer(wx.HORIZONTAL)
        self.sizerButtonSAction = wx.BoxSizer(wx.VERTICAL)
        self.File = wx.TextCtrl(self,size=(500,250),style=wx.TE_MULTILINE|wx.TE_PROCESS_TAB)

        self.FileCmd=wx.Button(self,label='Apply to memory')
        self.FileCmd.Bind(wx.EVT_BUTTON,self.OnFileCmd)
        self.FileCmd.SetToolTip(_('Apply modifications from the textbox to memory'))

        self.to_clipboard=wx.Button(self,label='Copy script to clipboard')
        self.to_clipboard.Bind(wx.EVT_BUTTON,self.OnCopyToClipboard)
        self.to_clipboard.SetToolTip(_('Copy script lines to clipboard'))

        self.sizerfile.Add(self.File,3,wx.EXPAND)
        self.sizerfile.Add(self.sizerButtonSAction,1,wx.EXPAND)

        self.sizerButtonSAction.Add(self.FileCmd,1,wx.EXPAND)
        self.sizerButtonSAction.Add(self.to_clipboard,1,wx.EXPAND)

        self.sizer.Add(self.sizerbut1,0,wx.EXPAND)
        self.sizer.Add(self.sizerbut2,0,wx.EXPAND)
        self.sizer.Add(self.sizerAllBC,0,wx.EXPAND)
        self.sizer.Add(self.sizerselectAll,0,wx.EXPAND)
        self.sizer.Add(self.sizerfile,1,wx.EXPAND)

        self.Bind(wx.EVT_CLOSE,self.OnClose)

        self.SetSizer(self.sizer)
        self.sizer.Fit(self)
        self.SetAutoLayout(1)

    def OnClose(self, event):

        if self._DestroyAtClosing:
            self.Destroy()
        else:
            self.Hide()
        pass

    def LoadFile(self,filename:str):
        """
        Read file
        """
        if filename.endswith('cl'):
            #lecture du contenu
            with open(filename, 'r') as myfile:
                txt = myfile.read()
                myfile.close()

            self._filename_cl = filename
            self._filecontent = txt.replace(',','\t')

        elif filename.endswith('.par'):
            prev_param = prev_parameters_simul()
            prev_param.read_file(filename)
            lst_x = prev_param.weak_bc_x.mybc
            lst_y = prev_param.weak_bc_y.mybc

            self._filecontent = str(len(lst_x)+len(lst_y)) +'\n'
            for curbc in lst_x:
                self._filecontent += '{}\t{}\t{}\t{}\t{}'.format(curbc.i,
                                                             curbc.j,
                                                             1,
                                                             curbc.ntype,
                                                             curbc.val)
            for curbc in lst_y:
                self._filecontent += '{}\t{}\t{}\t{}\t{}'.format(curbc.i,
                                                             curbc.j,
                                                             2,
                                                             curbc.ntype,
                                                             curbc.val)

            self._filename_cl = filename + '.cl'
            self.prev_param = None

    def OnLoad(self,event:wx.Event):
        #ouverture d'une boîte de dialogue
        file=wx.FileDialog(self,"Choose file",
                           wildcard="Boundary conditions (*.cl)|*.cl|Parameter file (*.par)|*.par|all (*.*)|*.*")
        if file.ShowModal() == wx.ID_CANCEL:
            file.Destroy()
            return
        else:
            #récuparétaion du nom de fichier avec chemin d'accès
            filename =file.GetPath()
            file.Destroy()

        self.LoadFile(filename)
        self.File.Value = self._filecontent

    def SaveFile(self,filename:str=None):

        if filename is None and self._filename_cl =='':
            logging.info(_('Nothing to do - choose a filename and retry !'))
            return

        if filename is None:
            filename = self._filename_cl

        if filename is not None:
            self._filename_cl = filename

        #écriture du contenu
        with open(filename, 'w') as myfile:
            myfile.write(self._filecontent)
            myfile.close()

    def OnSave(self,event:wx.Event):
        #ouverture d'une boîte de dialogue
        file=wx.FileDialog(self,
                           "Choose file",
                           wildcard="Boundary conditions (*.cl)|*.cl|all (*.*)|*.*")
        if file.ShowModal() == wx.ID_CANCEL:
            file.Destroy()
            return
        else:
            #récuparétaion du nom de fichier avec chemin d'accès
            filename =file.GetPath()
            file.Destroy()

        self.SaveFile(filename)

    def FindBC(self, whichbc:str):
        """
        Find borders with associated 'whichbc' value

        return 2 strings with indices
        """
        textx=''
        texty=''

        curdict:dict
        curdict=self.bordersX['bc']
        ij:str
        allbc:dict
        for ij, allbc in curdict.items():
            try:
                i,j=ij.split('-')
                if whichbc in allbc.keys():
                    if(str(allbc[whichbc]) != '99999.0'):
                        textx+=i+'\t'+j+'\n'
            except:
                pass

        curdict=self.bordersY['bc']
        for ij, allbc in curdict.items():
            try:
                i,j=ij.split('-')
                if whichbc in allbc.keys():
                    if(str(allbc[whichbc]) != '99999.0'):
                        texty+=i+'\t'+j+'\n'
            except:
                pass

        return textx, texty

    def OnFind(self,event:wx.Event):
        """
        Find all borders associated with
        and put strings in widgets
        """
        #get the type of BC based on name
        tbc=event.EventObject.Name

        textx, texty = self.FindBC(tbc)

        self.BCx.Clear()
        self.BCy.Clear()
        self.BCx.Value=textx
        self.BCy.Value=texty
        self.GetBC()

    def OnApplyBC(self,event:wx.Event):

        for xy in range(2):
            if xy==0:
                sel=self.BCx.Value.splitlines()
                curbord=self.bordersX
            else:
                sel=self.BCy.Value.splitlines()
                curbord=self.bordersY

            for cursel in sel:
                i,j=cursel.split('\t')
                txt=str(i)+'-'+str(j)
                try:
                    mybc= curbord['bc'][txt]
                except:
                    mybc=curbord['bc'][txt]={}

                for k,tbc in enumerate(self._checkBC.keys()):
                    if self._checkBC[tbc].Value:
                        if self._valueBC[tbc].Value!='':
                            mybc[tbc]=float(self._valueBC[tbc].Value)

        self.resetBC()
        self._Populate_FileContent()

    def resetBC(self):
        """Reset all wx widgets related to BC"""
        if self.wx_exists:
            for curbc in self.bc_type:
                val_bc, name_bc = curbc.value
                self._checkBC[name_bc].Value=False
                self._valueBC[name_bc].Value=''

    def OnResetBC(self,event:wx.Event):
        self.resetBC()

    def GetBC(self):
        """
        Get BC for selected borders
        """

        # create dictionary for all BC values
        values={}
        for curbc in self.bc_type:
            valbc, tbc = curbc.value
            values[tbc]={}
            values[tbc]['val']={}
            values[tbc]['same']=True
            values[tbc]['nb']=0

        # iterate along X == 0 and Y == 1
        for xy in range(2):
            if xy==0:
                sel=self.BCx.Value.splitlines()
                curbord=self.bordersX
            else:
                sel=self.BCy.Value.splitlines()
                curbord=self.bordersY

            # iterate on borders
            for cursel in sel:
                i,j=cursel.split('\t')
                txt=str(i)+'-'+str(j)

                try:
                    # count number of BC of each type and determine if all BC are the same
                    mybc= curbord['bc'][txt]

                    for ibc,tbc in enumerate(mybc):
                        curval=float(mybc[tbc])

                        if values[tbc]['nb']>0:
                            if not curval in values[tbc]['val'].values():
                                values[tbc]['nb']+=1
                                values[tbc]['val'][values[tbc]['nb']]=curval
                                values[tbc]['same']=False
                        else:
                            values[tbc]['nb']+=1
                            values[tbc]['val'][values[tbc]['nb']]=curval
                except:
                    pass

        # update widgets
        for curbc in self.bc_type:
            valbc, tbc = curbc.value
            if values[tbc]['nb']>0:
                self._checkBC[tbc].Value=True
                txt=''
                if values[tbc]['same']:
                    for curval in values[tbc]['val']:
                        txt += str(curval)
                else:
                    for curval in values[tbc]['val']:
                        txt += str(curval) +' or '
                    txt+='...'
                self._valueBC[tbc].Value=txt
            else:
                self._checkBC[tbc].Value=False

    def OnGetBC(self,event:wx.Event):

        self.GetBC()

    def OnClearselection(self,event:wx.Event):
        self.bordersX['selected'][:]=False
        self.bordersY['selected'][:]=False
        self._Populate_selxy()

    def OnFindBorders(self,event:wx.Event):

        if self.cmdx.Value!='':
            tx = self.cmdx.Value.split('\t')
            if len(tx)==2:
                indi={}
                indj={}
                partxi = tx[0].split(',')
                for i,curpart in enumerate(partxi):
                    indi[i]={}
                    bounds=curpart.split('-')
                    indi[i]['chain']=curpart
                    indi[i]['istart']=int(bounds[0])-1
                    try:
                        indi[i]['iend']=int(bounds[1])-1
                    except:
                        indi[i]['iend']=int(bounds[0])-1
                partxj = tx[1].split(',')
                for i,curpart in enumerate(partxj):
                    indj[i]={}
                    bounds=curpart.split('-')
                    indj[i]['chain']=curpart
                    indj[i]['jstart']=int(bounds[0])-1
                    try:
                        indj[i]['jend']=int(bounds[1])-1
                    except:
                        indj[i]['jend']=int(bounds[0])-1

                for whichi in indi.keys():
                    for i in range(indi[whichi]['istart'],indi[whichi]['iend']+1):
                        for whichj in indj.keys():
                            for j in range(indj[whichj]['jstart'],indj[whichj]['jend']+1):
                                text=str(i)+'-'+str(j)
                                try:
                                    index=self.bordersX['indicesstr'].index(text)
                                    self.bordersX['selected'][index] = ~ self.bordersX['selected'][index]
                                except:
                                    pass

            else:
                logging.info(_('Bad command for X borders -- Nothing to do !'))

        if self.cmdy.Value!='':
            ty = self.cmdy.Value.split('\t')
            if len(ty)==2:
                indi={}
                indj={}
                partyi = ty[0].split(',')
                for i,curpart in enumerate(partyi):
                    indi[i]={}
                    bounds=curpart.split('-')
                    indi[i]['chain']=curpart
                    indi[i]['istart']=int(bounds[0])-1
                    try:
                        indi[i]['iend']=int(bounds[1])-1
                    except:
                        indi[i]['iend']=int(bounds[0])-1
                partyj = ty[1].split(',')
                for i,curpart in enumerate(partyj):
                    indj[i]={}
                    bounds=curpart.split('-')
                    indj[i]['chain']=curpart
                    indj[i]['jstart']=int(bounds[0])-1
                    try:
                        indj[i]['jend']=int(bounds[1])-1
                    except:
                        indj[i]['jend']=int(bounds[0])-1

                for whichi in indi.keys():
                    for i in range(indi[whichi]['istart'],indi[whichi]['iend']+1):
                        for whichj in indj.keys():
                            for j in range(indj[whichj]['jstart'],indj[whichj]['jend']+1):
                                text=str(i)+'-'+str(j)
                                try:
                                    index=self.bordersY['indicesstr'].index(text)
                                    self.bordersY['selected'][index] = ~ self.bordersY['selected'][index]
                                except:
                                    pass
            else:
                wx.MessageBox('Bad command for Y borders -- Nothing to do !')

        self._Populate_selxy()

    def update_selection(self):
        self._Populate_selxy()

    def _Populate_selxy(self):
        """Set selected along X and Y"""
        textx=''
        for k,selected in enumerate(self.bordersX['selected']):
            if selected:
                textx+= str(self.bordersX['indices'][0][k]+1) + '\t'+ str(self.bordersX['indices'][1][k]+1)+'\n'

        texty=''
        for k,selected in enumerate(self.bordersY['selected']):
            if selected:
                texty+= str(self.bordersY['indices'][0][k]+1) + '\t'+ str(self.bordersY['indices'][1][k]+1)+'\n'

        if self.wx_exists:
            self.BCx.Clear()
            self.BCx.AppendText(textx)
            self.BCy.Clear()
            self.BCy.AppendText(texty)

        return textx, texty

    def _Populate_FileContent(self):
        """
        Update file content
        """
        text=''
        nb=0

        for orient in range(1,3):
            if orient==1:
                curlist=self.bordersX['bc']
            else:
                curlist=self.bordersY['bc']

            curlist:dict
            ij:str
            allbc:dict
            for ij, allbc in curlist.items():
                for tbc, val in allbc.items():
                    i,j=ij.split('-')
                    numbc=self._find_Int_TypeBC(tbc)

                    if(str(val)!='99999.0'):
                        text+= "{}\t{}\t{}\t{}\t{}\n".format(i,j,orient,numbc,val)
                    nb+=1

        self._filecontent = str(nb)+'\n'
        self._filecontent += text+'\n'
        self._filecontent += 'version {}'.format(self._version)

        self._filecontent += '\n\n'

        self._filecontent += self._script_bc()

        if self.wx_exists:
            self.File.Clear()
            self.File.Value=self._filecontent

    def _script_bc(self):
        """ Return script to apply BC """

        text = ""
        for orient in range(1,3):
            if orient==1:
                curlist=self.bordersX['bc']
                direction='LEFT'
            else:
                curlist=self.bordersY['bc']
                direction='BOTTOM'
            curlist:dict
            ij:str
            allbc:dict
            for ij, allbc in curlist.items():
                for tbc, val in allbc.items():
                    i,j=ij.split('-')
                    namebc=self._find_EnumName_TypeBC(tbc)

                    if(str(val)!='99999.0'):
                        text+= "simul.add_boundary_condition(i={}, j={},bc_type=BoundaryConditionsTypes.{}, bc_value={}, border=Direction.{}\n".format(i,j,namebc,val,direction)
        return text

    def FillFromString(self, text:str):

        self._filecontent = text

        text=text.splitlines()

        if len(text) == 0:
            return

        nb=int(float(text[0]))

        try:
            for i in range(1,nb+1):
                i,j,orient,type,value=text[i].split('\t')

        except:
             logging.info(_('Bad text values -- Check and Retry !!'))
             return

        self.bordersX['bc']={}
        self.bordersY['bc']={}
        for i in range(1,nb+1):
            i,j,orient,type,value=text[i].split('\t')
            i=int(float(i))
            j=int(float(j))
            type=int(float(type))
            orient=int(float(orient))
            value=float(value)
            if orient==1:
                texttxt=str(i-1)+'-'+str(j-1)
                try:
                    index=self.bordersX['indicesstr'].index(texttxt)
                    try:
                        curbc =self.bordersX['bc'][str(i)+'-'+str(j)]
                    except:
                        curbc=self.bordersX['bc'][str(i)+'-'+str(j)]={}

                    try:
                        curbc[self._find_Str_TypeBC(type)]=value
                    except:
                        try:
                            curbc[type]=value
                        except:
                            pass
                except:
                    logging.info('Bad border indices on X ('+str(i)+'-'+str(j)+(')'))
            elif orient==2:
                texttxt=str(i-1)+'-'+str(j-1)
                try:
                    index=self.bordersY['indicesstr'].index(texttxt)
                    try:
                        curbc =self.bordersY['bc'][str(i)+'-'+str(j)]
                    except:
                        curbc=self.bordersY['bc'][str(i)+'-'+str(j)]={}

                    try:
                        curbc[self._find_Str_TypeBC(type)]=value
                    except:
                        try:
                            curbc[type]=value
                        except:
                            pass
                except:
                    logging.info('Bad border indices on Y ('+str(i)+'-'+str(j)+(')'))

        self._Populate_FileContent()

    def OnFileCmd(self,event:wx.Event):
        """ Apply <<< button"""
        self.FillFromString(self.File.Value)

    def OnCopyToClipboard(self,event:wx.Event):
        """ Copy to clipboard"""
        if self.wx_exists:
            if wx.TheClipboard.Open():
                wx.TheClipboard.Clear()
                wx.TheClipboard.SetData(wx.TextDataObject(self._script_bc()))
                wx.TheClipboard.Close()
            else:
                logging.warning(_('Cannot open the clipboard'))

    def FindBorders(self,array : np.ma.array = None):
        """Find all borders where we can impose BC"""
        if self._linked_array is not None and array is None:
            array = self._linked_array.array
        elif self._linked_array is None and array is None:
            return
        elif self._linked_array is not None and array is not None:
            pass

        assert isinstance(array, np.ma.masked_array)

        shape = array.shape

        xor = np.logical_xor(array.mask[:-1,:],array.mask[1:,:])
        yor = np.logical_xor(array.mask[:,:-1],array.mask[:,1:])
        nbx_where = np.where(xor)
        nby_where = np.where(yor)

        nbx = len(nbx_where[0])
        nby = len(nby_where[0])

        self.bordersX['nb']=nbx
        self.bordersY['nb']=nby

        if nbx ==0 and nby ==0:
            logging.warning(_('No border detected -- check your data'))
            return

        indicesX = np.zeros((2,nbx),dtype=np.integer,order='F')
        indicesY = np.zeros((2,nby),dtype=np.integer,order='F')

        indicesX[0,:] = np.asarray(nbx_where[0])+1
        indicesX[1,:] = np.asarray(nbx_where[1])

        indicesY[0,:] = np.asarray(nby_where[0])
        indicesY[1,:] = np.asarray(nby_where[1])+1

        indicesXstr = [ str(i+1)+'-'+str(j+1) for i, j in indicesX.T]
        indicesYstr = [ str(i+1)+'-'+str(j+1) for i, j in indicesY.T]

        self.bordersX['indices']=indicesX
        self.bordersX['indicesstr']=indicesXstr
        self.bordersY['indices']=indicesY
        self.bordersY['indicesstr']=indicesYstr
        self._ComputeCoordinates()
        self._do_kdtree()

    def ReadFileBorders(self,*args):
        """
        Read sux and suy files

        Provide path to .sux file
        .suy file is supposed to be in the same directory
        """
        if len(args)>0:
            #s'il y a un argument on le prend tel quel
            self._filename_sux = str(args[0])
        else:
            if self.wx_exists:
                #ouverture d'une boîte de dialogue
                file=wx.FileDialog(self,"Choose file", wildcard="sux (*.sux)|*.sux|all (*.*)|*.*")
                if file.ShowModal() == wx.ID_CANCEL:
                    file.Destroy()
                    return
                else:
                    #récuparétaion du nom de fichier avec chemin d'accès
                    self._filename_sux =file.GetPath()
                    file.Destroy()

        if self._filename_sux!='':
            if not exists(self._filename_sux):
                return

            #lecture du contenu SUX
            with open(self._filename_sux, 'r') as myfile:
                #split des lignes --> récupération des infos sans '\n' en fin de ligne
                #  différent de .readlines() qui lui ne supprime pas les '\n'
                myparamsline = myfile.read().splitlines()
                myfile.close()

            indicesX = np.zeros((2,myparamsline.count()),dtype=np.integer,order='F')
            k=0
            for myborder in myparamsline:
                indicesX[:,k] = myborder.split()
                k+=1

            self.bordersX['nb']=indicesX.size()/2
            self.bordersX['indices']=indicesX

            #lecture du contenu SUX
            suy = self._filename_sux.replace('sux','suy')
            with open(suy, 'r') as myfile:
                #split des lignes --> récupération des infos sans '\n' en fin de ligne
                #  différent de .readlines() qui lui ne supprime pas les '\n'
                myparamsline = myfile.read().splitlines()
                myfile.close()

            indicesY = np.zeros((2,myparamsline.count()),dtype=np.integer,order='F')
            k=0
            for myborder in myparamsline:
                indicesY[:,k] = myborder.split()
                k+=1

            self.bordersY['nb']=indicesY.size()/2
            self.bordersY['indices']=indicesY

    def _ComputeCoordinates(self):
        """Calculate and store positions of possible BC"""
        nbx=self.bordersX['nb']
        coordscgX = np.zeros((2,nbx),dtype=float,order='F')
        coordsX = np.zeros((2,2,nbx),dtype=float,order='F')
        selectedX = np.zeros(nbx,dtype=np.bool_,order='F')
        for k in range(nbx):
            x1=self.orig[0]+self.bordersX['indices'][0,k]*self.dx
            y1=self.orig[1]+self.bordersX['indices'][1,k]*self.dy
            y2=y1+self.dy

            coordsX[0,0,k]=x1
            coordsX[1,0,k]=y1
            coordsX[0,1,k]=x1
            coordsX[1,1,k]=y2

            coordscgX[0,k]=x1
            coordscgX[1,k]=(y1+y2)/2.

        self.bordersX['coords']=coordsX
        self.bordersX['coordscg']=coordscgX
        self.bordersX['selected']=selectedX

        nby=self.bordersY['nb']
        coordscgY = np.zeros((2,nby),dtype=float,order='F')
        coordsY = np.zeros((2,2,nby),dtype=float,order='F')
        selectedY = np.zeros(nby,dtype=np.bool_,order='F')
        for k in range(nby):
            x1=self.orig[0]+self.bordersY['indices'][0,k]*self.dx
            x2=x1+self.dx
            y1=self.orig[1]+self.bordersY['indices'][1,k]*self.dy

            coordsY[0,0,k]=x1
            coordsY[1,0,k]=y1
            coordsY[0,1,k]=x2
            coordsY[1,1,k]=y1

            coordscgY[0,k]=(x1+x2)/2.
            coordscgY[1,k]=y1

        self.bordersY['coords']=coordsY
        self.bordersY['coordscg']=coordscgY
        self.bordersY['selected']=selectedY

    def _count_nbbc(self, bc:str, axis:Literal['x', 'y']):
        """
        Count number of BC type for border 'bc' along axis 'axis'

        :param bc: str 'ii-jj' of the border
        :param axis: axis of BC -- 'x' or 'y'
        """
        nb=0

        if axis.lower()=='x':
            locbc=self.bordersX['bc'][bc]
            for valbc in locbc:
                curval=float(locbc[valbc])
                if curval!=99999:
                    nb+=1
        elif axis.lower()=='y':
            locbc=self.bordersY['bc'][bc]
            for valbc in locbc:
                curval=float(locbc[valbc])
                if curval!=99999:
                    nb+=1

        return nb

    def plot(self):
        """ Plot borders -- OpenGL """

        nbx = self.bordersX['nb']
        nby = self.bordersY['nb']

        coordx = self.bordersX['coords']
        coordy = self.bordersY['coords']

        for curbc in self.bordersX['bc']:
            i,j=curbc.split('-')
            txt=str(int(i)-1)+'-'+str(int(j)-1)
            index=self.bordersX['indicesstr'].index(txt)

            x1,y1=coordx[:,0,index]
            x2,y2=coordx[:,1,index]

            glLineWidth(5.)

            nb = self._count_nbbc(curbc,'x')
            try:
                r,g,b = ColorsNb[nb]
            except:
                r=1.
                g=0.
                b=0.

            glColor3f(r,g,b)
            glBegin(GL_LINES)
            glVertex2d(x1,y1)
            glVertex2d(x2,y2)
            glEnd()

        for curbc in self.bordersY['bc']:
            i,j=curbc.split('-')
            txt=str(int(i)-1)+'-'+str(int(j)-1)
            index=self.bordersY['indicesstr'].index(txt)

            x1,y1=coordy[:,0,index]
            x2,y2=coordy[:,1,index]

            glLineWidth(5.)

            nb = self._count_nbbc(curbc,'y')
            try:
                r,g,b = ColorsNb[nb]
            except:
                r=1.
                g=0.
                b=0.

            glColor3f(r,g,b)
            glBegin(GL_LINES)
            glVertex2d(x1,y1)
            glVertex2d(x2,y2)
            glEnd()

        for k in range(nbx):

            x1,y1=coordx[:,0,k]
            x2,y2=coordx[:,1,k]

            if self.bordersX['selected'][k]:
                glLineWidth(4.)
                glColor3f(1.,0.,0.)
            else:
                glLineWidth(2.)
                glColor3f(0.,0.,0.)

            glBegin(GL_LINES)
            glVertex2d(x1,y1)
            glVertex2d(x2,y2)
            glEnd()

        for k in range(nby):

            x1,y1=coordy[:,0,k]
            x2,y2=coordy[:,1,k]

            if self.bordersY['selected'][k]:
                glLineWidth(4.)
                glColor3f(1.,0.,0.)
            else:
                glLineWidth(2.)
                glColor3f(0.,0.,0.)

            glBegin(GL_LINES)
            glVertex2d(x1,y1)
            glVertex2d(x2,y2)
            glEnd()

    def _do_kdtree(self):
        """Create kdtree to search nearest neighbor"""
        self.mytreeX = cKDTree(self.bordersX['coordscg'].transpose())
        self.mytreeY = cKDTree(self.bordersY['coordscg'].transpose())

    def query_kdtree(self, point:tuple[float,float]):
        """Find nearest border and add to 'selected' dict"""

        distX, indexesX = self.mytreeX.query(point)
        distY, indexesY = self.mytreeY.query(point)

        if distX<distY:
            self.bordersX['selected'][indexesX] = ~self.bordersX['selected'][indexesX]
        else:
            self.bordersY['selected'][indexesY] = ~self.bordersY['selected'][indexesY]

        return indexesX,indexesY

    def ray_tracing_numpy(self, poly, XorY:str = 'x'):
        """Find all borders in rectangle or polygon and addto 'selected' dict"""

        if XorY.lower()=='x':
            x=self.bordersX['coordscg'][0,:]
            y=self.bordersX['coordscg'][1,:]
        else:
            x=self.bordersY['coordscg'][0,:]
            y=self.bordersY['coordscg'][1,:]

        n = len(poly)
        inside = np.zeros(len(x),np.bool_)
        p2x = 0.0
        p2y = 0.0
        xints = 0.0
        p1x,p1y = poly[0]
        for i in range(n+1):
            p2x,p2y = poly[i % n]
            idx = np.nonzero((y > min(p1y,p2y)) & (y <= max(p1y,p2y)) & (x <= max(p1x,p2x)))[0]
            if p1y != p2y:
                xints = (y[idx]-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                if p1x == p2x:
                    inside[idx] = ~inside[idx]
                else:
                    idxx = idx[x[idx] <= xints]
                    inside[idxx] = ~inside[idxx]

            p1x,p1y = p2x,p2y

        if XorY.lower()=='x':
            self.bordersX['selected']=np.logical_xor(self.bordersX['selected'],inside)
        else:
            self.bordersY['selected']=np.logical_xor(self.bordersY['selected'],inside)

        return inside

    def _find_Str_TypeBC(self,i:int):
        """Convert intBC to nameBC"""
        for curbc in self.bc_type:
            val_bc, name_bc = curbc.value
            if val_bc==i:
                return name_bc

    def _find_Int_TypeBC(self,name:str):
        """Convert nameBC to intBC"""
        for curbc in self.bc_type:
            val_bc, name_bc = curbc.value
            if name_bc==name:
                return val_bc

    def _find_EnumName_TypeBC(self,name:str):
        """Convert nameBC to intBC"""
        for curbc in self.bc_type:
            val_bc, name_bc = curbc.value
            if name_bc==name:
                return curbc.name

    def get_lists_for_GPU(self) -> tuple[list[boundary_condition_2D], list[boundary_condition_2D]]:
        """
        Return list of BC for GPU computing
        """

        def create_list_prev(curdict:dict) -> list[boundary_condition_2D]:
            list_bc = []
            for ij, allbc in curdict.items():
                i,j=ij.split('-')

                for curname, curval in allbc.items():
                    if(str(curval) != '99999.0'):
                        list_bc.append(boundary_condition_2D(int(i),
                                                               int(j),
                                                               self._find_Int_TypeBC(curname),
                                                               float(curval)))
            return list_bc

        if self._version ==1:
            lst_x= create_list_prev(self.bordersX['bc'])
            lst_y= create_list_prev(self.bordersY['bc'])
        else:
            lst_x= create_list_prev(self.bordersX['bc'])
            lst_y= create_list_prev(self.bordersY['bc'])

            # convert ntype between OO and prev because GPU based on prev
            for cur_bc in lst_x:
                if cur_bc.ntype == BCType_2D_OO.WATER_LEVEL.value[0]:
                    cur_bc.ntype = BCType_2D.H.value[0]
                elif cur_bc.ntype == BCType_2D_OO.FROUDE_NORMAL.value[0]:
                    cur_bc.ntype = BCType_2D.FROUDE_NORMAL.value[0]
                elif cur_bc.ntype == BCType_2D_OO.NORMAL_DISCHARGE.value[0]:
                    cur_bc.ntype = BCType_2D.QX.value[0]
                elif cur_bc.ntype == BCType_2D_OO.TANGENT_DISCHARGE.value[0]:
                    cur_bc.ntype = BCType_2D.QY.value[0]

            for cur_bc in lst_x:
                if cur_bc.ntype == BCType_2D_OO.WATER_LEVEL.value[0]:
                    cur_bc.ntype = BCType_2D.H.value[0]
                elif cur_bc.ntype == BCType_2D_OO.FROUDE_NORMAL.value[0]:
                    cur_bc.ntype = BCType_2D.FROUDE_NORMAL.value[0]
                elif cur_bc.ntype == BCType_2D_OO.NORMAL_DISCHARGE.value[0]:
                    cur_bc.ntype = BCType_2D.QY.value[0]
                elif cur_bc.ntype == BCType_2D_OO.TANGENT_DISCHARGE.value[0]:
                    cur_bc.ntype = BCType_2D.QX.value[0]

        return lst_x, lst_y
