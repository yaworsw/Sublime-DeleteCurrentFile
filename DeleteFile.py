import sublime, sublime_plugin, os

settings = sublime.load_settings('DeleteFile.sublime-settings')

class DeleteFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    window = sublime.active_window()
    view   = sublime.Window.active_view(window)

    file   = view.file_name()

    if settings.get('prompt_before_delete', False):
      if not sublime.ok_cancel_dialog('Are you sure you want to delete \'%s\'?' % file):
        return

    if (file != None and os.path.isfile(view.file_name())):
      os.remove(file)

    if settings.get('auto_close_buffer', True):
      window.run_command('close')
