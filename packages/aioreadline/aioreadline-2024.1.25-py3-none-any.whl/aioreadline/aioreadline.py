# SPDX-FileCopyrightText: Mario Kicherer <dev@kicherer.org>
#
# SPDX-License-Identifier: MIT

import ctypes as ct
import sys, os

ct_verbosity=1

if sys.version_info < (3,):
	def to_bytes(x):
		return x
else:
	def to_bytes(s):
		if isinstance(s, str):
			return s.encode()
		else:
			return s

def ct_call(*nargs, **kwargs):
	call = nargs[0]
	
	if "args" in kwargs:
		args = kwargs["args"]
	else:
		args = None
	if "check" in kwargs:
		check = kwargs["check"]
	else:
		check = None
	
	nargs = nargs[1:]
	
	func = getattr(libreadline, call)
	if args:
		func.argtypes = args
	if "restype" in kwargs:
		func.restype = kwargs["restype"]
	
	newargs = tuple()
	for i in range(len(nargs)):
		newargs += (to_bytes(nargs[i]), )
	
	# print(call, newargs)
	res = func(*newargs)
	
	if ct_verbosity > 1:
		print(call, newargs, "=", res)
	
	if (check is None or check) and func.restype in [ct.c_long, ct.c_int] and res < 0:
		raise OSError(res, call+" failed with: "+os.strerror(-res)+" ("+str(-res)+")")
	if check and isinstance(func.restype, ct.POINTER) and res == None:
		raise OSError(res, call+" returned NULL")

libreadline = ct.CDLL('libreadline.so')

rl_vcpfunc_t = ct.CFUNCTYPE(None, ct.c_char_p);

rl_outstream = ct.c_int.in_dll(libreadline, "rl_outstream")

library_functions = [
	{ "name": "rl_callback_handler_install", "args": [ct.c_char_p, rl_vcpfunc_t], "restype": None },
	{ "name": "rl_callback_handler_remove", "restype": None },
	{ "name": "rl_callback_read_char", "restype": None },
	{ "name": "read_history", "args": [ct.c_char_p] },
	{ "name": "write_history", "args": [ct.c_char_p] },
	{ "name": "add_history", "args": [ct.c_char_p], "restype": None },
	{ "name": "rl_set_prompt", "args": [ct.c_char_p], "restype": None },
	]

for f in library_functions:
	if getattr(libreadline, f["name"], None) is None:
		print(f["name"], "not found in library")
		continue
	
	def function_factory(f=f):
		def dyn_fct(*nargs, **kwargs):
			if "args" in f:
				args = f["args"]
			else:
				args = None
			if "restype" in f:
				restype = f["restype"]
			else:
				restype = ct.c_int
			
			return ct_call(f["name"], *nargs, args=args, restype=restype)
		return dyn_fct
	
	if hasattr(sys.modules[__name__], f["name"]):
		print("duplicate function", f["name"], file=sys.stderr)
	
	setattr(sys.modules[__name__], f["name"], function_factory(f))

class AIOReadline():
	def __init__(self, prompt=None, loop=None, history_file=None):
		if prompt is None:
			self.prompt = "> "
		else:
			self.prompt = prompt
		
		if loop is None:
			self.loop = asyncio.get_event_loop()
		else:
			self.loop = loop
		
		if history_file and isinstance(history_file, str):
			self.history_file = history_file
		else:
			self.history_file = None
		
		self._ct_rl_callback = rl_vcpfunc_t(self.rl_callback)
		self.started = False
	
	@property
	def prompt(self):
		return self._prompt
	
	@prompt.setter
	def prompt(self, value):
		self._prompt = value
	
	def start(self):
		if self.history_file:
			self.read_history()
		
		rl_callback_handler_install(self.prompt, self._ct_rl_callback)
		
		self.started = True
	
	def stop(self):
		rl_set_prompt("")
		
		rl_callback_handler_remove()
		
		if self.history_file:
			self.write_history()
		
		self.started = False
	
	def rl_callback(self, line):
		self.line_fut.set_result(line)
		self.loop.remove_reader(sys.stdin)
	
	def on_stdin_cb(self):
		rl_callback_read_char()
	
	async def getLine(self):
		if not self.started:
			self.start()
		self.line_fut = self.loop.create_future()
		
		self.loop.add_reader(sys.stdin, self.on_stdin_cb)
		
		return await self.line_fut
	
	def read_history(self, history_file=None):
		if history_file is None:
			history_file = self.history_file
		
		if history_file and isinstance(history_file, str):
			read_history(history_file)
	
	def write_history(self, history_file=None):
		if history_file is None:
			history_file = self.history_file
		
		if history_file and isinstance(history_file, str):
			write_history(history_file)
	
	def add_history(self, line):
		add_history(line)
	
	def set_var(self, var, value):
		if var == "rl_outstream":
			global rl_outstream
			
			rl_outstream = value
		else:
			raise Exception("unknown var", var)

if __name__ == '__main__':
	import asyncio, atexit
	
	async def _main():
		while True:
			line = await aiorl.getLine()
			
			if line is None or line == b"quit":
				aiorl.stop()
				loop.stop()
				break
			elif len(line) > 0:
				aiorl.add_history(line)
				print(line)
	
	loop = asyncio.get_event_loop()
	loop.create_task(_main())
	
	aiorl = AIOReadline(prompt="> ", loop=loop, history_file=".aioreadline_history")
	
	atexit.register(lambda: aiorl.stop())
	
	try:
		loop.run_forever()
	except KeyboardInterrupt:
		loop.stop()
