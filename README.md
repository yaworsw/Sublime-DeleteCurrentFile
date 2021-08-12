# Sublime-DeleteCurrentFile

This plugin adds a command (`DeleteCurrentFile: Delete File`) to the command palette which will delete the current file and close the buffer.

## Settings

With the plugin's settings you may customize if you want to see a confirmation message, or if you want to send the deleted file to the trash or the unrecoverable void.

By default there is no confirmation message and the file is moved to the trash.

```js
{
  // close the current buffer after deleting the current file
  "auto_close_buffer": true,

  // before doing anything display a prompt
  "prompt_before_delete": false,

  // move to trash instead of deleting
  "move_to_trash": true
}
```

# Key Binding

You can add a key binding to your `.sublime-keymap` file:

```json
  {
  	"keys": ["super+control+backspace"],
  	"command": "delete_current_file"
  }
```
