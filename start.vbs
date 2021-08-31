Dim oShell
Set oShell = WScript.CreateObject ("WSCript.shell")
strName = oShell.ExpandEnvironmentStrings( "%USERNAME%" )
oShell.run("cmd /C CD " & strName & "\Desktop & python Sorter.py")
X=MsgBox("Click OK to end")
Set oShell = Nothing
