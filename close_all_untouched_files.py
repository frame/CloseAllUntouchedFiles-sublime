import sublime
import sublime_plugin

class CloseAllUntouchedFilesCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		for win in sublime.windows():
			for view in win.views():
				if not view.is_dirty():
					view.window().focus_view(view)
					view.window().run_command('close_file')
