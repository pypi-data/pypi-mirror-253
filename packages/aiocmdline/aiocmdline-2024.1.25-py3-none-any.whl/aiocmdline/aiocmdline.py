# SPDX-FileCopyrightText: Mario Kicherer <dev@kicherer.org>
#
# SPDX-License-Identifier: MIT

import sys, asyncio
import aioreadline

# just a dummy class in case AIOReadline is not needed
class ReadBuffer():
	def __init__(self):
		self.prompt = None
		self.lines = sys.stdin.read().encode().split(b"\n")
		self.cur_line = 0
	
	async def getLine(self):
		self.cur_line += 1
		if self.cur_line > len(self.lines):
			return None
		return self.lines[self.cur_line-1]
	
	def add_history(self, line):
		pass

class AIOCmdline():
	intro = None
	eoc_char = ";"
	
	def __init__(self, prompt=None, loop=None, history=None):
		self.cmdqueue = []
		
		if not prompt:
			prompt = "cmd> "
		
		if loop is None:
			self.loop = asyncio.get_event_loop()
		else:
			self.loop = loop
		
		self.macros = {}
		
		if history is True:
			history = ".aiocmdline_history"
		
		if sys.__stdin__.isatty():
			self.aiorl = aioreadline.AIOReadline(prompt=prompt, loop=self.loop, history_file=history)
		else:
			self.aiorl = ReadBuffer()
	
	@property
	def prompt(self):
		return self.aiorl.prompt
	
	@prompt.setter
	def prompt(self, value):
		self.aiorl.prompt = value
	
	def cmdloop(self):
		self.loop.create_task(self.on_loop_start())
		self.stop = False
		
		try:
			self.loop.run_forever()
		except KeyboardInterrupt:
			self.stop_cmdloop()
		except:
			self.stop_cmdloop()
			raise
	
	async def on_loop_start(self):
		for entry in self.cmdqueue:
			if not entry or not entry.strip() or entry.strip()[0] == "#":
				continue
			await self.handle_input(entry)
		
		if self.intro:
			self.write(self.intro)
			self.write("\n")
		
		while not self.stop:
			line = await self.aiorl.getLine()
			
			if line is None:
				self.stop_cmdloop()
				break
			elif len(line.strip()) > 0:
				self.aiorl.add_history(line.strip())
				await self.handle_input(line.decode().strip())
	
	def write(self, s):
		print(s)
	
	def stop_cmdloop(self):
		self.stop = True
		self.loop.stop()
		self.aiorl.stop()
	
	def split_multicmd(self, line):
		import shlex
		
		lst = shlex.split(line)
		
		cmds = []
		cmd = []
		for i in range(len(lst)):
			if not lst[i]:
				continue
			
			if lst[i][-1] == self.eoc_char:
				cmd.append( lst[i][:-1] )
				if cmd:
					cmds.append(shlex.join(cmd))
					cmd = []
			else:
				cmd.append( lst[i] )
		if cmd:
			cmds.append(shlex.join(cmd))
		
		return cmds
	
	async def handle_input(self, line):
		from shlex import split
		
		for cmd in self.split_multicmd(line):
			arr = split(cmd)
			
			cmd = arr[0]
			if len(arr) > 1:
				params = arr[1:]
			else:
				params = []
			
			if hasattr(self, "do_"+cmd) and callable(getattr(self, "do_"+cmd)):
				from inspect import iscoroutinefunction
				if iscoroutinefunction(getattr(self, "do_"+cmd)):
					await getattr(self, "do_"+cmd)(*params)
				else:
					getattr(self, "do_"+cmd)(*params)
			elif cmd in self.macros:
				await self.handle_input(self.macros[cmd])

if __name__ == '__main__':
	class MyCmdline(AIOCmdline):
		def do_quit(self):
			self.stop_cmdloop()
		
		async def do_sleep(self, arg):
			await asyncio.sleep(int(arg))
			print("sleep done")
	
	mycmdline = MyCmdline(prompt="mycmd> ", history=True)
	mycmdline.cmdloop()
