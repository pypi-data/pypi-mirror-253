aioreadline
===========

Python has a builtin readline module. However, the builtin module is difficult
to use in async Python code. This module provides an interface around the
async-compatible functions of libreadline using a ctypes wrapper.

Example
-------

```
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
```
