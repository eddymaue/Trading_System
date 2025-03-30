VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} usrFrmA102 
   Caption         =   "usrFrmA102-Controleur"
   ClientHeight    =   2535
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   8280.001
   OleObjectBlob   =   "usrFrmA102.frx":0000
   ShowModal       =   0   'False
   StartUpPosition =   1  'CenterOwner
   Tag             =   "0"
End
Attribute VB_Name = "usrFrmA102"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False


Private Sub btnAutoRefreshGain_Click()
#If False Then
    With Me.btnAutoRefreshGain
    
        .Caption = IIf(.Caption = "A-OFF", "A-ON", "A-OFF")
        gv.c_AutoRefreshGainCaption = .Caption
    End With
    Call g.AutoRefreshGain
 #End If
End Sub




Private Sub btnOpenSectionGain_Click()
#If False Then
    Dim lbClose As Boolean
    Dim MonBtn As Object
    Set MonBtn = Me.btnOpenSectionGain
    lbClose = MonBtn.Caption = "Fermer Sect Gain"
    
    MonBtn.Caption = IIf(lbClose, "Ouvrir Sect Gain", "Fermer Sect Gain")
    
    Dim ColonneSel As String
    ColonneSel = "h,j,k,l,o"
    
    Call g.OpenOrCloseColumn(lbClose, ColonneSel)
 #End If
End Sub






Private Sub chk_MaintenirNsecondeCellGreen_Change()
    ' erreur: type null sur un boolean
    ll = f.SetParamValue("gv.b_MaintenirNsecondeCellGreen ", Me.chk_MaintenirNsecondeCellGreen.value)
    'gv.b_MaintenirNsecondeCellGreen = Me.chk_MaintenirNsecondeCellGreen.value
End Sub

Private Sub chk_RangerUtileRowGreenColor_Change()
    ll = f.SetParamValue("gv.b_RangerUtileRowGreenColor", Me.chk_RangerUtileRowGreenColor.value)
    gv.b_RangerUtileRowGreenColor = Me.chk_RangerUtileRowGreenColor.value
End Sub


Private Sub chk_GainMin_Change()
    
    ll = f.SetParamValue("gv.b_SetFilterVolumeGainMin", chk_GainMin.value)
    gv.b_SetFilterVolumeGainMin = Me.chk_GainMin.value
    
    Call g.SetfilterActivity("Volume", "FltrGainMin", Me.chk_GainMin.value)

End Sub



Private Sub chk_PrixMax_Change()
    
    ll = f.SetParamValue("gv.b_SetFilterVolumePrixMax", Me.chk_PrixMax.value)
    gv.b_SetFilterVolumePrixMax = Me.chk_PrixMax.value
    
    Call g.SetfilterActivity("Volume", "FltrPrixMax", Me.chk_PrixMax.value)
   
End Sub




Private Sub chk_PrixMin_Change()

    ll = f.SetParamValue("gv.b_SetFilterVolumePrixMin", chk_PrixMin.value)
    gv.b_SetFilterVolumePrixMin = Me.chk_PrixMin.value

    Call g.SetfilterActivity("Volume", "FltrPrixMin", chk_PrixMin.value)


End Sub

Private Sub chk_RefreshTable_Change()
    gv.b_RefreshTable = Me.chk_RefreshTable.value
    
    ll = f.SetParamValue("gv.b_RefreshTable", Me.chk_RefreshTable.value)
End Sub

Private Sub chk_SectionGain_Change()

    ll = f.SetParamValue("gv.b_SetFilterSectionGain", chk_SectionGain.value)
    gv.b_SetFilterSectionGain = chk_SectionGain.value

End Sub

Private Sub chk_SectionVolume_change()
    ll = f.SetParamValue("gv.b_SetFilterSectionVolume", chk_SectionVolume.value)
    gv.b_SetFilterSectionVolume = chk_SectionVolume.value
    
    Call g.SetfilterActivity("Volume", "FltrSectVol", Me.chk_SectionVolume.value)

End Sub

Private Sub old_chk_SGain_GainlMin_Change()
    Call g.SetFilter("Gain", "GainlMin", Me.txt_SGain_GainlMin.value)
    ll = f.SetParamValue("gv.b_SetFilterSectionGainGainMin", chk_SGain_GainlMin.value)
    gv.b_SetFilterSectionGainGainMin = Me.chk_SGain_GainlMin.value
End Sub

Private Sub old_chk_SGain_VolMin_Change()
   ' Call g.SetFilter("Gain", "VolMin", Me.txt_SGain_VolMin.text)
    ll = f.SetParamValue("gv.b_SetFilterSectionGainVolMin", chk_SGain_VolMin.value)
    gv.b_SetFilterSectionGainVolMin = Me.chk_SGain_VolMin.value
End Sub

Private Sub chk_ShrOTDG_Change()
  '  Call g.SetFilter("Volume", "ShrOTDG", Me.txt_ShrOTDG.text)
    ll = f.SetParamValue("gv.b_SetFilterVolumeShrOTDGmin", chk_ShrOTDG.value)
    gv.b_SetFilterVolumeShrOTDGmin = Me.chk_ShrOTDG.value
    
    Call g.SetfilterActivity("Volume", "FltrShrOTDNG", Me.chk_ShrOTDG.value)
End Sub


Private Sub chk_VolMin_Change()
   'Call g.SetFilter("Volume", "Vol.Min", Me.txt_VolMin.text)
   ll = f.SetParamValue("gv.b_SetFilterVolumeVolMin", chk_VolMin.value)
   gv.b_SetFilterVolumeVolMin = Me.chk_VolMin.value
   
    Call g.SetfilterActivity("Volume", "FltrVolMin", Me.chk_VolMin.value)
   
End Sub

Private Sub Chk_VolumeProgressionMin_Change()
    ll = f.SetParamValue("gv.b_SetFilterProgressionMin", Me.Chk_VolumeProgressionMin.value)
    gv.b_SetFilterProgressionMin = Me.Chk_VolumeProgressionMin.value
    
    Call g.SetfilterActivity("Volume", "FltrVolPgrssMin", Me.Chk_VolumeProgressionMin.value)
End Sub


Private Sub btn_OpenOrCloseColumnGain_Click()
    Dim lbClose As Boolean
    Dim mb As Object
    Set mb = btn_OpenOrCloseColumnGain
    lbClose = mb.Caption = "Fermer Colonne"
    
    mb.Caption = IIf(lbClose, "Ouvrir Colonne", "Fermer Colonne")
    
    Call g.OpenOrCloseColumn(lbClose, gv.c_OpenOrCloseColumn)
    
End Sub

Sub PlacerSymboleSurMQ()

End Sub

Private Sub CopierSymbol_Click()
    
    Call g.ClipBoard_CopyFromColonne(GetCopyColumn())

End Sub
Function GetCopyColumn() As String

    With Me
        
        If .OptionButton1.value = True Then
            GetCopyColumn = .OptionButton1.Caption
        ElseIf .OptionButton2 = True Then
            GetCopyColumn = .OptionButton2.Caption
        'ElseIf .OptionButton3 = True Then
         '   GetCopyColumn = .OptionButton3.Caption
        End If
    
    End With
    
End Function

Private Sub LblSectionGain()

End Sub

Private Sub Label5_Click()

End Sub


Private Sub btnOpenOrCloseColumn_Click()
    Dim lbClose As Boolean
    Dim MonBtn As Object
    Set MonBtn = Me.btnOpenOrCloseColumn
    lbClose = MonBtn.Caption = "Fermer Colonne"
    
    MonBtn.Caption = IIf(lbClose, "Ouvrir Colonne", "Fermer Colonne")
    
    Dim ColonneSel As String
    ColonneSel = "B,F,G,I,M,N"
    
    Call g.OpenOrCloseColumn(lbClose, "F,G,I,M,N,H,J,K,L")
End Sub


Private Sub LblSectionGain_Click()

End Sub

Private Sub OpenSectionGain__Click()
    Dim MonBoutton As Object
    Set MonBouton = Me
    Dim oCtnParent As Object
     oCtnParent = usrFrmA104
    
    
    
    bOpenColumn = Me.Caption = "Ouvrir Sect Gain"
    If bOpenColumn Then
        
        Me.Caption = "Fermer Sect Gain"
        
    Else
    
    End If
    
    
End Sub



Private Sub MultiPage1_Change()

End Sub

Private Sub OptionButton1_Click()
    OptionValueChange (1)
End Sub
Private Sub OptionButton2_Click()
    OptionValueChange (2)
End Sub
Private Sub OptionButton3_Click()
    OptionValueChange (3)
End Sub
Sub OptionValueChange(cVal As Integer)
    With Me
        
        .OptionButton1.value = IIf(cVal = 1, 1, 0)
        .OptionButton2.value = IIf(cVal = 2, 1, 0)
        '.OptionButton3.value = IIf(cVal = 3, 1, 0)
    End With
End Sub
Private Sub Placer_click()
    Dim ws As Worksheet
    Dim qty As Long
    Dim StartCell As Range
    Dim endCell As Range
    Dim selectedRange As Range

    ' Assurez-vous que le nom de votre feuille est correct (remplacez "Feuil1" par le nom de votre feuille)
    Set ws = ThisWorkbook.ActiveSheet
    

    ' Récupérez la valeur du textbox QtySymboleToPass
    qty = CLng(Me.QtySymboleToPass.value)

    ' Déterminez la cellule de départ (par exemple, A3)
    Set StartCell = ws.Range(ws.Cells.Select)

    ' Déterminez la cellule de fin (par exemple, A28)
    Set endCell = StartCell.Offset(qty - 1, 0)

    ' Sélectionnez la plage de cellules entre la cellule de départ et la cellule de fin
    Set selectedRange = ws.Range(StartCell, endCell)
    selectedRange.Select

    ' Vous pouvez maintenant copier ou effectuer d'autres actions avec la plage sélectionnée
    ' Par exemple : selectedRange.Copy

    ' Nettoyez la sélection (désélectionnez)
    Application.CutCopyMode = False
End Sub

Private Sub btnResetGain_Click()
    Call g.ResetGain
End Sub

Private Sub ResetGainSectionVolume_Click()
    Call g.ResetGainSectionVolume
End Sub

Private Sub ResetVolume_Click()
    Call g.ResetVolume
End Sub

Private Sub btnResetVolumeSectionGain_Click()
    Call g.ResetVolumeSectionGain
End Sub

Private Sub AutoCopyPastMarketQ_Click()
    
    Dim wsh As Object
    Dim cmd As String
    
    Set wsh = CreateObject("WScript.Shell")
    
    ' AutoCopyPastMarkekQ:Click
    cmd = Cfg.PYTHON_EXE & " " & _
          """" & Cfg.GetPythonScript("Start_stop_surveillance.py") & """"

    
    On Error Resume Next
    wsh.Run cmd, 0, False
    If Err.Number <> 0 Then
        MsgBox "Erreur lors de l'exécution du script Python: " & Err.Description, vbCritical
    End If
    On Error GoTo 0
    
    Set wsh = Nothing

    
End Sub

Private Sub chk_RTDThrottleInterval_Change()
    
    Application.RTD.ThrottleInterval = IIf(Me.chk_RTDThrottleInterval.value, Me.txt_RTDThrottleInterval.value, -1)
    ll = f.SetParamValue("gv.b_RTDThrottleInterval", Me.chk_RTDThrottleInterval.value)
    gv.b_RTDThrottleInterval = Me.chk_RTDThrottleInterval.value
    
End Sub


Private Sub ToggleButtonA_H_Click()
    
    With Me.ToggleButtonA_H
        .Caption = IIf(.Caption = "A", "H", "A")
    End With
    
End Sub

Private Sub txt_MaintenirNsecondeCellGreen_Change()
    ll = f.SetParamValue("gv.i_MaintenirNsecondeCellGreen", Me.txt_MaintenirNsecondeCellGreen)
    gv.i_MaintenirNsecondeCellGreen = Me.txt_MaintenirNsecondeCellGreen
    
End Sub

Private Sub txt_PrixMax_Change()
    
    ll = f.SetParamValue("gv.d_SetFilterVolumePrixMax", Me.txt_PrixMax.value)
    gv.d_SetFilterVolumePrixMax = Me.txt_PrixMax.value
    Call g.SetFilter("Volume", "FltrPrixMax", CDbl(Me.txt_PrixMax.value))
   

End Sub





Private Sub txt_PrixMin_Change()
    ll = f.SetParamValue("gv.d_SetFilterVolumePrixMin", Me.txt_PrixMin.value)
    gv.d_SetFilterVolumePrixMin = Me.txt_PrixMin.value
   Call g.SetFilter("Volume", "FltrPrixMin", CDbl(Me.txt_PrixMin.value))
End Sub

Private Sub txt_RangerUtileRowGreenColor_Change()
    ll = f.SetParamValue("gv.i_RangerUtileRowGreenColor", txt_RangerUtileRowGreenColor.value)
    gv.i_RangerUtileRowGreenColor = Me.txt_RangerUtileRowGreenColor.value
End Sub

Private Sub txt_RefreshTable_Change()
    If Not Me.txt_RefreshTable Is Nothing Then
        ll = f.SetParamValue("gv.i_RefreshTable", txt_RefreshTable.value)
        gv.i_RefreshTable = Me.txt_RefreshTable.value
    End If
End Sub

Private Sub txt_RefreshTable_Exit(ByVal Cancel As MSForms.ReturnBoolean)

End Sub

Private Sub old_txt_SGain_GainlMin_Change()
        Call g.SetFilter("Gain", "GainMin", Me.txt_SGain_GainlMin.value)
        ll = f.SetParamValue("gv.d_SetFilterSectionGainGainMin", txt_SGain_GainlMin.value)
        gv.d_SetFilterSectionGainGainMin = txt_SGain_GainlMin.value
        
End Sub

Private Sub old_txt_SGain_VolMin_Change()
        Call g.SetFilter("Gain", "VolMin", Me.txt_SGain_VolMin.value)
        
        ll = f.SetParamValue("gv.d_SetFilterSectionGainVolMin", txt_SGain_VolMin.value)
        gv.d_SetFilterSectionGainVolMin = Me.txt_SGain_VolMin.value

End Sub

Private Sub txt_ShrOTDG_Change()
        Call g.SetFilter("Volume", "FltrShrOTDNG", Me.txt_ShrOTDG.value)
        ll = f.SetParamValue("gv.d_SetFilterVolumeShrOTDGmin", txt_ShrOTDG.value)
        gv.d_SetFilterVolumeShrOTDGmin = Me.txt_ShrOTDG.value
   
End Sub

Private Sub txt_GainMin_Change()
        Call g.SetFilter("Volume", "FltrGainMin", Me.txt_GainMin.value)
        ll = f.SetParamValue("gv.d_SetFilterVolumeGainMin", txt_GainMin.value)
        gv.d_SetFilterVolumeGainMin = Me.txt_GainMin.value
End Sub



Private Sub txt_VolMin_Change()
    Call g.SetFilter("Volume", "FltrVolMin", Me.txt_VolMin.value)
    ll = f.SetParamValue("gv.d_SetFilterVolumeVolMin", txt_VolMin.value)
    gv.d_SetFilterVolumeVolMin = txt_VolMin.value
End Sub




Private Sub txt_RTDThrottleInterval_Change()
    Application.RTD.ThrottleInterval = Me.txt_RTDThrottleInterval.value
    ll = f.SetParamValue("gv.i_RTDThrottleInterval", Me.txt_RTDThrottleInterval.value)
    gv.i_RTDThrottleInterval = Me.txt_RTDThrottleInterval.value
End Sub







Private Sub txt_VolumeProgressionMin_Change()
    ll = f.SetParamValue("gv.d_SetFilterProgressionMin", Me.txt_VolumeProgressionMin.value)
    gv.d_SetFilterProgressionMin = Me.txt_VolumeProgressionMin.value
    Call g.SetFilter("Volume", "FltrVolPgrssMin", Me.txt_VolumeProgressionMin.value)

End Sub

Private Sub UserForm_Activate()
        Dim ws As Worksheet
   
    Set ws = ThisWorkbook.Sheets("VolSymbole")
       
        
        Me.txt_PrixMax.value = CStr(f.GetParamValue("gv.d_SetFilterVolumePrixMax"))
        Me.txt_PrixMin.value = CStr(f.GetParamValue("gv.d_SetFilterVolumePrixMin"))
        Me.txt_GainMin.value = CStr(f.GetParamValue("gv.d_SetFilterVolumeGainMin"))
        Me.txt_ShrOTDG = f.GetParamValue("gv.d_SetFilterVolumeShrOTDGmin")
        
        Me.txt_RefreshTable.value = f.GetParamValue("gv.i_RefreshTable")
        Me.txt_RTDThrottleInterval.value = f.GetParamValue("gv.i_RTDThrottleInterval")
        Me.txt_RangerUtileRowGreenColor.value = f.GetParamValue("gv.i_RangerUtileRowGreenColor")
        Me.txt_MaintenirNsecondeCellGreen.value = f.GetParamValue("gv.i_MaintenirNsecondeCellGreen")
        
        Me.chk_VolMin.value = IIf(f.GetParamValue("gv.b_SetFilterVolumeVolMin") = "True", True, False)
        Me.chk_PrixMin.value = IIf(f.GetParamValue("gv.b_SetFilterVolumePrixMin") = "True", True, False)
        Me.chk_PrixMax.value = IIf(f.GetParamValue("gv.b_SetFilterVolumePrixMax") = "True", True, False)
        Me.chk_ShrOTDG.value = IIf(f.GetParamValue("gv.b_SetFilterVolumeShrOTDGmin") = "True", True, False)
        Me.chk_GainMin.value = IIf(f.GetParamValue("gv.b_SetFilterVolumeGainMin") = "True", True, False)

        Me.chk_SectionVolume.value = IIf(f.GetParamValue("gv.b_SetFilterSectionVolume") = "True", True, False)
    
        Me.chk_RefreshTable.value = IIf(f.GetParamValue("gv.b_RefreshTable") = "True", True, False)
        Me.chk_RTDThrottleInterval.value = IIf(f.GetParamValue("gv.b_RTDThrottleInterval"), True, False)
    
        Me.chk_RangerUtileRowGreenColor.value = IIf(f.GetParamValue("gv.b_RangerUtileRowGreenColor"), True, False)
        Me.chk_MaintenirNsecondeCellGreen.value = f.GetParamValue("gv.b_MaintenirNsecondeCellGreen")
        
'= f.GetParamValue("")
'= f.GetParamValue("")
'= f.GetParamValue("")
    gv.b_InSetupMode = False
     
End Sub

Private Sub UserForm_Click()

End Sub

Private Sub UserForm_Initialize()
  
    gv.b_InSetupMode = True
    
    Me.Chk_CollerSurA.value = 1
    Me.OptionButton1 = True
    
    gv.c_VariablePulbicSurVolSymbole = d.GetColumnLetter("VariablePublique", 1)
    If gv.c_VariablePulbicSurVolSymbole = "" Then
        MsgBox "gv.c_VariablePulbicSurVolSymbole est vide", vbCritical, "Erreur..."
    End If
    
    
        Set ws = ThisWorkbook.Sheets("VolSymbole")
  'll = MsgBox("UserForm_Activate", vbCritical)
       
        
        Me.txt_PrixMax.value = CStr(f.GetParamValue("gv.d_SetFilterVolumePrixMax"))
        Me.txt_PrixMin.value = CStr(f.GetParamValue("gv.d_SetFilterVolumePrixMin"))
        
        Me.txt_VolumeProgressionMin.value = f.GetParamValue("gv.d_SetFilterProgressionMin")
        
        Me.txt_GainMin.value = CStr(f.GetParamValue("gv.d_SetFilterVolumeGainMin"))
        'Me.txt_SGain_GainlMin.value = CStr(f.GetParamValue("gv.d_SetFilterSectionGainGainMin"))
        'Me.txt_SGain_VolMin.value = f.GetParamValue("gv.d_SetFilterSectionGainVolMin") ' corection à faire ...
        Me.txt_ShrOTDG = f.GetParamValue("gv.d_SetFilterVolumeShrOTDGmin")
        'Me.txt_VolMin.value = f.GetParamValue("gv.d_SetFilterVolumeVolMin")
        Me.txt_RefreshTable.value = f.GetParamValue("gv.i_RefreshTable")
        Me.txt_RTDThrottleInterval.value = f.GetParamValue("gv.i_RTDThrottleInterval")
        Me.txt_RangerUtileRowGreenColor.value = f.GetParamValue("gv.i_RangerUtileRowGreenColor")
        Me.txt_MaintenirNsecondeCellGreen.value = f.GetParamValue("gv.i_MaintenirNsecondeCellGreen")
        
        Me.chk_VolMin.value = IIf(f.GetParamValue("gv.b_SetFilterVolumeVolMin") = "True", True, False)
        Me.chk_PrixMin.value = IIf(f.GetParamValue("gv.b_SetFilterVolumePrixMin") = "True", True, False)
        Me.chk_PrixMax.value = IIf(f.GetParamValue("gv.b_SetFilterVolumePrixMax") = "True", True, False)
        Me.Chk_VolumeProgressionMin = IIf(f.GetParamValue("gv.b_SetFilterProgressionMin") = "True", True, False)
        
        Me.chk_ShrOTDG.value = IIf(f.GetParamValue("gv.b_SetFilterVolumeShrOTDGmin") = "True", True, False)
        Me.chk_GainMin.value = IIf(f.GetParamValue("gv.b_SetFilterVolumeGainMin") = "True", True, False)
        'Me.chk_SGain_GainlMin.value = IIf(f.GetParamValue("gv.b_SetFilterSectionGainGainMin") = "True", True, False)
        Me.chk_SGain_VolMin.value = IIf(f.GetParamValue("gv.b_SetFilterSectionGainVolMin") = "True", True, False)
        
        Me.chk_SectionGain.value = IIf(f.GetParamValue("gv.b_SetFilterSectionGain") = "True", True, False)
        Me.chk_SectionVolume.value = IIf(f.GetParamValue("gv.b_SetFilterSectionVolume") = "True", True, False)
    
        Me.chk_RefreshTable.value = IIf(f.GetParamValue("gv.b_RefreshTable") = "True", True, False)
        Me.chk_RTDThrottleInterval.value = IIf(f.GetParamValue("gv.b_RTDThrottleInterval"), True, False)
    
        Me.chk_RangerUtileRowGreenColor.value = IIf(f.GetParamValue("gv.b_RangerUtileRowGreenColor"), True, False)
        Me.chk_MaintenirNsecondeCellGreen.value = f.GetParamValue("gv.b_MaintenirNsecondeCellGreen")
        
    
   ' Me = f.GetParamValue("")
        gv.b_InSetupMode = False

End Sub

Private Sub UserForm_QueryClose(Cancel As Integer, CloseMode As Integer)
#If True Then
    gv.b_InSetupMode = True
    
    ll = f.SetParamValue("gv.b_SetFilterVolumeGainMin", Me.chk_GainMin.value)
    ll = f.SetParamValue("gv.b_SetFilterVolumePrixMin", Me.chk_PrixMin.value)

    ll = f.SetParamValue("gv.b_SetFilterVolumePrixMax", Me.chk_PrixMax.value)
    ll = f.SetParamValue("gv.b_SetFilterVolumeShrOTDGmin", Me.chk_ShrOTDG.value)
    'll = f.SetParamValue("gv.b_SetFilterSectionGainGainMin", Me.chk_SGain_GainlMin.value)
    'll = f.SetParamValue("gv.b_SetFilterSectionGainVolMin", Me.chk_SGain_VolMin.value)
    'll = f.SetParamValue("gv.b_SetFilterSectionGain", Me.chk_SectionGain.value)
    'll = f.SetParamValue("gv.d_SetFilterSectionGainVolMin", Me.txt_SGain_VolMin.value)
    'll = f.SetParamValue("gv.d_SetFilterSectionGainGainMin", Me.txt_SGain_GainlMin.value)
    ll = f.SetParamValue("gv.b_SetFilterSectionVolume", Me.chk_SectionVolume.value)

    ll = f.SetParamValue("gv.b_RefreshTable", Me.chk_RefreshTable.value)
    ii = f.SetParamValue("gv.i_RefreshTable", Me.txt_RefreshTable.value)

    ll = f.SetParamValue("gv.i_RTDThrottleInterval", Me.txt_RTDThrottleInterval.value)
    ll = f.SetParamValue("gv.b_RTDThrottleInterval", Me.chk_RTDThrottleInterval.value)

    ll = f.SetParamValue("gv.i_RangerUtileRowGreenColor", Me.txt_RangerUtileRowGreenColor.value)
    ll = f.SetParamValue("gv.b_RangerUtileRowGreenColor", Me.chk_RangerUtileRowGreenColor.value)

    ll = f.SetParamValue("gv.d_SetFilterVolumeVolMin", Me.txt_VolMin.value)
    ll = f.SetParamValue("gv.d_SetFilterVolumeGainMin", Me.txt_GainMin.value)
    ll = f.SetParamValue("gv.d_SetFilterVolumeShrOTDGmin", Me.txt_ShrOTDG.value)
    ll = f.SetParamValue("gv.d_SetFilterVolumePrixMin", Me.txt_PrixMin.value)
    ll = f.SetParamValue("gv.d_SetFilterVolumePrixMax", Me.txt_PrixMax.value)

    ll = f.SetParamValue("gv.i_MaintenirNsecondeCellGreen", Me.txt_MaintenirNsecondeCellGreen)
    ll = f.SetParamValue("gv.b_MaintenirNsecondeCellGreen", Me.chk_MaintenirNsecondeCellGreen.value)
    ll = f.SetParamValue("gv.b_SetFilterVolumeVolMin", Me.chk_VolMin.value)
        
    gv.b_InSetupMode = False
    ' Sauvegarder le classeur
    ThisWorkbook.Save
    
#End If

End Sub

