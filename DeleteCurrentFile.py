import sublime
import sublime_plugin
import os

settings = None


def plugin_loaded():
    update_settings()
    settings.add_on_change('extensions_path', update_settings)


def update_settings():
    global settings
    settings = sublime.load_settings('DeleteCurrentFile.sublime-settings')


class DeleteCurrentFileCommand(sublime_plugin.TextCommand):

    def run(self, edit, prompt_before_delete=None, auto_close_buffer=None):

        global settings
        settings

        if prompt_before_delete is None:
            prompt_before_delete = settings.get('prompt_before_delete', False)

        if auto_close_buffer is None:
            auto_close_buffer = settings.get('auto_close_buffer', True)

        window = sublime.active_window()
        view = sublime.Window.active_view(window)
        file_name = view.file_name()
        message = "Are you sure you want to delete '{}'?".format(file_name)

        if prompt_before_delete:
            if not sublime.ok_cancel_dialog(message):
                return

        if view.is_dirty():
            view.set_scratch(True)

        if auto_close_buffer:
            window.run_command('close_file')

        if (file_name is not None and os.path.isfile(view.file_name())):
            os.remove(file_name)
