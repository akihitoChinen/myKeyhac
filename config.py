import sys
import os
import datetime

import pyauto
from keyhac import *

def configure(keymap):

    # --------------------------------------------------------------------
    # Text editer setting for editting config.py file

    # Setting with program file path (Simple usage)
    if 1:
        keymap.editor = "notepad.exe"

    # --------------------------------------------------------------------
    # Customizing the display

    # Font
    keymap.setFont( "MS Gothic", 12 )

    # Theme
    keymap.setTheme("black")

    # --------------------------------------------------------------------

    # Simple key replacement
    keymap.replaceKey( "RWin", 255 )

    # Global keymap which affects any windows
    if 1:
        keymap_global = keymap.defineWindowKeymap()

        # Clipboard history related
        keymap_global[ "C-S-Z"   ] = keymap.command_ClipboardList     # Open the clipboard history list
        keymap_global[ "C-S-X"   ] = keymap.command_ClipboardRotate   # Move the most recent history to tail
        keymap_global[ "C-S-A-X" ] = keymap.command_ClipboardRemove   # Remove the most recent history
        keymap.quote_mark = "> "                                      # Mark for quote pasting

        # USER0-Alt-Up/Down/Left/Right/Space/PageUp/PageDown : Virtul mouse operation by keyboard
        keymap_global[ "C-P" ] = "Up"                  # Move cursor up
        keymap_global[ "C-N" ] = "Down"                # Move cursor down
        keymap_global[ "C-F" ] = "Right"               # Move cursor right
        keymap_global[ "C-B" ] = "Left"                # Move cursor left

        keymap_global[ "C-A" ] = "Home"                # Move to beginning of line
        keymap_global[ "C-E" ] = "End"                 # Move to end of line
        keymap_global[ "C-D" ] = "Delete"              # Delete
        keymap_global[ "C-H" ] = "Back"                # Backspace
        keymap_global[ "C-J" ] = "Enter"               # Enter
        keymap_global[ "C-K" ] = "S-End","C-X"         # 行末まで切り取り
        keymap_global[ "C-U" ] = "S-Home","C-X"         # 行頭まで切り取り

        # Define Ctrl-X as the first key of multi-stroke keys
        keymap_global[ "C-X" ] = keymap.defineMultiStrokeKeymap("C-X")

        keymap_global[ "A-F" ] = "C-Right"             # Word right
        keymap_global[ "A-B" ] = "C-Left"              # Word left
        keymap_global[ "C-V" ] = "PageDown"            # Page down
        keymap_global[ "A-V" ] = "PageUp"              # page up
        keymap_global[ "A-Comma" ] = "C-Home"          # Beginning of the document
        keymap_global[ "A-Period" ] = "C-End"          # End of the document
        keymap_global[ "C-X" ][ "C-F" ] = "C-O"        # Open file
        keymap_global[ "C-X" ][ "C-S" ] = "C-S"        # Save
        keymap_global[ "C-X" ][ "C-W" ] = "A-F","A-A"  # Save as
        keymap_global[ "C-X" ][ "U" ] = "C-Z"          # Undo
        keymap_global[ "C-S" ] = "C-F"                 # Search
        keymap_global[ "A-X" ] = "C-G"                 # Jump to specified line number
        keymap_global[ "C-X" ][ "H" ] = "C-A"          # Select all
        keymap_global[ "C-W" ] = "C-X"                 # Cut
        keymap_global[ "A-W" ] = "C-C"                 # Copy
        keymap_global[ "C-Y" ] = "C-V"                 # Paste
        keymap_global[ "C-X" ][ "C-C" ] = "A-F4"       # Exit


    def non_emacs(keymap):
        keymap[ "C-A" ] = "C-A"                # Move to beginning of line
        keymap[ "C-E" ] = "C-E"                # Move to end of line
        keymap[ "C-D" ] = "C-D"                # Delete
        keymap[ "C-H" ] = "C-H"                # Backspace
        keymap[ "C-J" ] = "C-J"                # Enter
        keymap[ "C-K" ] = "C-K"         # 行末まで切り取り
        keymap[ "C-U" ] = "C-U"         # 行頭まで切り取り

        keymap[ "C-X" ] = "C-X"
        keymap[ "A-F" ] = "A-F"              # Word right
        keymap[ "A-B" ] = "A-B"              # Word left
        keymap[ "C-V" ] = "C-V"              # Page down
        keymap[ "A-V" ] = "A-V"              # page up

        keymap[ "C-S" ] = "C-S"                 # Search
        keymap[ "A-X" ] = "A-X"                 # Jump to specified line number
        keymap[ "C-W" ] = "C-W"                 # Cut
        keymap[ "A-W" ] = "A-W"                 # Copy
        keymap[ "C-Y" ] = "C-Y"                 # Paste

    # Cmderの場合はkyehacのキーマップを解除する
    if 1:
        keymap_cmder = keymap.defineWindowKeymap( exe_name="ConEmu64.exe", class_name="VirtualConsoleClass" )
        non_emacs(keymap_cmder)

    # xyzzyの場合はkyehacのキーマップを解除する
    if 1:
        keymap_xyzzy = keymap.defineWindowKeymap( exe_name="xyzzy.exe" )
        non_emacs(keymap_xyzzy)

    if 1:
        keymap_explorer = keymap.defineWindowKeymap( exe_name="explorer.exe", class_name="DirectUIHWND" )
        keymap_explorer[ "C-A-N" ] = "A-Left"
        keymap_explorer[ "C-A-B" ] = "A-Left"
        keymap_explorer[ "C-A-F" ] = "A-Right"
        keymap_explorer[ "C-A-P" ] = "A-Right"
        keymap_explorer[ "C-W" ] = "C-W"


        
        

#    # Ctrl-Tab : Switching between console related windows
#    if 1:
#        def isConsoleWindow(wnd):
#            if wnd.getClassName() in ("PuTTY","MinTTY","CkwWindowClass"):
#                return True
#            return False
#
#        keymap_console = keymap.defineWindowKeymap( check_func=isConsoleWindow )
#
#        def command_SwitchConsole():
#
#            root = pyauto.Window.getDesktop()
#            last_console = None
#
#            wnd = root.getFirstChild()
#            while wnd:
#                if isConsoleWindow(wnd):
#                    last_console = wnd
#                wnd = wnd.getNext()
#
#            if last_console:
#                last_console.setForeground()
#
#        keymap_console[ "C-TAB" ] = command_SwitchConsole
#
#
#    # Customizing clipboard history list
#    if 1:
#        # Enable clipboard monitoring hook (Default:Enabled)
#        keymap.clipboard_history.enableHook(True)
#
#        # Maximum number of clipboard history (Default:1000)
#        keymap.clipboard_history.maxnum = 1000
#
#        # Total maximum size of clipboard history (Default:10MB)
#        keymap.clipboard_history.quota = 10*1024*1024
#
#        # Fixed phrases
#        fixed_items = [
#            ( "name@server.net",     "name@server.net" ),
#            ( "Address",             "San Francisco, CA 94128" ),
#            ( "Phone number",        "03-4567-8901" ),
#        ]
#
#        # Return formatted date-time string
#        def dateAndTime(fmt):
#            def _dateAndTime():
#                return datetime.datetime.now().strftime(fmt)
#            return _dateAndTime
#
#        # Date-time
#        datetime_items = [
#            ( "YYYY/MM/DD HH:MM:SS",   dateAndTime("%Y/%m/%d %H:%M:%S") ),
#            ( "YYYY/MM/DD",            dateAndTime("%Y/%m/%d") ),
#            ( "HH:MM:SS",              dateAndTime("%H:%M:%S") ),
#            ( "YYYYMMDD_HHMMSS",       dateAndTime("%Y%m%d_%H%M%S") ),
#            ( "YYYYMMDD",              dateAndTime("%Y%m%d") ),
#            ( "HHMMSS",                dateAndTime("%H%M%S") ),
#        ]
#
#        # Add quote mark to current clipboard contents
#        def quoteClipboardText():
#            s = getClipboardText()
#            lines = s.splitlines(True)
#            s = ""
#            for line in lines:
#                s += keymap.quote_mark + line
#            return s
#
#        # Indent current clipboard contents
#        def indentClipboardText():
#            s = getClipboardText()
#            lines = s.splitlines(True)
#            s = ""
#            for line in lines:
#                if line.lstrip():
#                    line = " " * 4 + line
#                s += line
#            return s
#
#        # Unindent current clipboard contents
#        def unindentClipboardText():
#            s = getClipboardText()
#            lines = s.splitlines(True)
#            s = ""
#            for line in lines:
#                for i in range(4+1):
#                    if i>=len(line) : break
#                    if line[i]=='\t':
#                        i+=1
#                        break
#                    if line[i]!=' ':
#                        break
#                s += line[i:]
#            return s
#
#        full_width_chars = "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ！”＃＄％＆’（）＊＋，−．／：；＜＝＞？＠［￥］＾＿‘｛｜｝～０１２３４５６７８９　"
#        half_width_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}～0123456789 "
#
#        # Convert to half-with characters
#        def toHalfWidthClipboardText():
#            s = getClipboardText()
#            s = s.translate(str.maketrans(full_width_chars,half_width_chars))
#            return s
#
#        # Convert to full-with characters
#        def toFullWidthClipboardText():
#            s = getClipboardText()
#            s = s.translate(str.maketrans(half_width_chars,full_width_chars))
#            return s
#
#        # Save the clipboard contents as a file in Desktop directory
#        def command_SaveClipboardToDesktop():
#
#            text = getClipboardText()
#            if not text: return
#
#            # Convert to utf-8 / CR-LF
#            utf8_bom = b"\xEF\xBB\xBF"
#            text = text.replace("\r\n","\n")
#            text = text.replace("\r","\n")
#            text = text.replace("\n","\r\n")
#            text = text.encode( encoding="utf-8" )
#
#            # Save in Desktop directory
#            fullpath = os.path.join( getDesktopPath(), datetime.datetime.now().strftime("clip_%Y%m%d_%H%M%S.txt") )
#            fd = open( fullpath, "wb" )
#            fd.write(utf8_bom)
#            fd.write(text)
#            fd.close()
#
#            # Open by the text editor
#            keymap.editTextFile(fullpath)
#
#        # Menu item list
#        other_items = [
#            ( "Quote clipboard",            quoteClipboardText ),
#            ( "Indent clipboard",           indentClipboardText ),
#            ( "Unindent clipboard",         unindentClipboardText ),
#            ( "",                           None ),
#            ( "To Half-Width",              toHalfWidthClipboardText ),
#            ( "To Full-Width",              toFullWidthClipboardText ),
#            ( "",                           None ),
#            ( "Save clipboard to Desktop",  command_SaveClipboardToDesktop ),
#            ( "",                           None ),
#            ( "Edit config.py",             keymap.command_EditConfig ),
#            ( "Reload config.py",           keymap.command_ReloadConfig ),
#        ]
#
#        # Clipboard history list extensions
#        keymap.cblisters += [
#            ( "Fixed phrase", cblister_FixedPhrase(fixed_items) ),
#            ( "Date-time", cblister_FixedPhrase(datetime_items) ),
#            ( "Others", cblister_FixedPhrase(other_items) ),
#        ]