#!/usr/bin/env python3

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# The full text of the GPL v2 is available at: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# The full text of the GPL v3 is available at: https://www.gnu.org/licenses/gpl-3.0.html
# For more information on the GPLv2+, please visit: https://www.gnu.org/licenses/gpl-2.0.html


import cups
import argparse
import sys
import json

def main():
	parser = argparse.ArgumentParser("PyCUPS CLI")
	parser.add_argument("cmd", help="Command to run", choices=["check", "devices", "printers", "cancel", "remove",
																"add", "info", "print"])
	parser.add_argument("-j", help="Job ID", required=False, type=int, default=None, dest="job")
	parser.add_argument("-a", help="All", action="store_true", dest="all")
	parser.add_argument("-p", help="Printer name", required=False, default=None, dest="name")
	parser.add_argument("-u", help="Printer URI", required=False, default=None, dest="uri")
	parser.add_argument("-d", help="Driver", required=False, default=None, dest="driver")
	parser.add_argument("-f", help="File to print", required=False, default=None, dest="file")
	parser.add_argument("-o", help="Options", required=False, default="{}", dest="opts")
	args = parser.parse_args()

	try:
		c = cups.Connection()
		if args.cmd == "check":
			pass
		elif args.cmd == "devices":
			devices = c.getDevices()
			print(json.dumps(devices))
		elif args.cmd == "printers":
			printers = c.getPrinters()
			print(json.dumps(printers))
		elif args.cmd == "cancel":
			if args.all and args.uri is not None:
				c.cancelAllJobs(uri=args.uri)
			elif args.job is not None:
				c.cancelJob(args.job)
		elif args.cmd == "remove":
			if args.name is not None:
				c.deletePrinter(args.name)
			elif args.uri is not None:
				c.deletePrinter(args.uri)
		elif args.cmd == "add":
			c.addPrinter(args.name, device=args.uri, ppdname=args.driver)
			c.acceptJobs(args.name)
			c.enablePrinter(args.name)
		elif args.cmd == "info":
			info = None
			if args.job is not None:
				info = c.getJobAttributes(args.job)
			elif args.name is not None:
				info = c.getPrinterAttributes(name=args.name)
			elif args.uri is not None:
				info = c.getPrinterAttributes(uri=args.uri)
			print(json.dumps(info))
		elif args.cmd == "print":
			options = json.loads(args.opts)
			job = c.printFile(args.name, args.file, args.file, options)
			print(json.dumps({"job": job}))
	except Exception as e:
		print(e, file=sys.stderr)
		sys.exit(1)

if __name__ == "__main__":
	main()
