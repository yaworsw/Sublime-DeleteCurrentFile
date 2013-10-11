# Sublime-DeleteCurrentFile

This plugin adds a command to the command palette which will delete the current file and close the buffer.

Compared to the File: Delete command from the SideBarEnhancements plugin this one allows for the option of skipping any prompt and automatically closing the buffer.  It does so by saving the file before it deletes it.  This way when the buffer is closed sublime will not ask if you want to save it before you delete it.

If you are using SideBarEnhancements as you want to replace the File: Delete command with this one then install SideBarEnhancements using git and then manually remove the following code from the Commands.sublime-commands file.

    {
        "caption": "File: Delete",
        "command": "side_bar_delete"
    },
