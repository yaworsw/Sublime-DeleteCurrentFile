import sublime, sublime_plugin, os

class DeleteFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    window = sublime.active_window()
    view   = sublime.Window.active_view(window)
    if os.path.isfile(view.file_name()):
      os.remove(view.file_name())
      window.run_command('close')
