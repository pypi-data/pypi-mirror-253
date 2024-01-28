aiocmdline
==========

Python has a builtin module that provides a line-oriented command interpreter.
However, the builtin module is difficult to use with async Python code. This
module provides a ready-to-use class that simplifies the implementation of
regular and async commands.

Dependencies:
-------------

 - aioreadline

Example
-------

```
class MyCmdline(AIOCmdline):
	def do_quit(self):
		self.stop_cmdloop()
	
	async def do_sleep(self, arg):
		await asyncio.sleep(int(arg))
		print("sleep done")

mycmdline = MyCmdline(prompt="mycmd> ", history=True)
mycmdline.cmdloop()
```
