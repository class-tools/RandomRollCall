'RandomRollCall 1.1.6
'This source code file is under MIT License.
'Copyright (c) 2022 Class Tools Develop Team
'Contributors: ren-yc (Yuchen Ren)
Set WshShell = WScript.CreateObject("WScript.Shell")
If WScript.Arguments.Length = 0 Then
    Set ObjShell = CreateObject("Shell.Application")
    ObjShell.ShellExecute "wscript.exe" _
    , """" & WScript.ScriptFullName & """ RunAsAdministrator", , "runas", 1
    WScript.Quit
End if
CurPath = left(WScript.ScriptFullName, instrrev(WScript.ScriptFullName, "\"))
Set WshShell = CreateObject("WScript.Shell")
WshShell.run "cmd.exe"
WScript.sleep 50
WshShell.sendkeys "cacls """ & CurPath & "settings.yml"" /G Everyone:F{enter}"
WScript.sleep 50
WshShell.sendkeys "Y{enter}"
WshShell.sendkeys "%{F4}"