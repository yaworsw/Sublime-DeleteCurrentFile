import sublime, sublime_plugin, os

class DeleteCurrentFileCommand(sublime_plugin.TextCommand):
  def run(self, edit, prompt_before_delete=None, auto_close_buffer=None):

    settings = sublime.load_settings('DeleteCurrentFile.sublime-settings')

    if prompt_before_delete == None:
      prompt_before_delete = settings.get('prompt_before_delete', False)

    if auto_close_buffer == None:
      auto_close_buffer = settings.get('auto_close_buffer', True)

    window = sublime.active_window()
    view   = sublime.Window.active_view(window)

    file   = view.file_name()

    if prompt_before_delete:
      if not sublime.ok_cancel_dialog('Are you sure you want to delete \'%s\'?' % file):
        return

    if view.is_dirty():
      view.run_command('save')

    if auto_close_buffer:
      window.run_command('close_file')

    if (file != None and os.path.isfile(view.file_name())):
      os.remove(file)
