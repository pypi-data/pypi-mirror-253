import itertools, argparse, glob, subprocess, yaml, concurrent.futures
import pandas as pd
from .version import __version__

def no_commands(args, pairs):
	if args.cmdABBA == "" and args.cmdAB == "" and args.cmdBA == "":
		fmt_pairs = [args.ABfmt.replace(args.A, pair[0]).replace(args.B, pair[1]) for pair in pairs]

		fmt_out = args.PsepP.join(fmt_pairs)
		print(fmt_out)
		return True
	return False

def parse_args():
	parser = argparse.ArgumentParser(description='Generate all combinations with replacement of strings (A, B) and (B, A). Either print combinations directly to stdout, or run cmdAB and (optionally) cmdBA formatted with those strings as {combocmdA} and {combocmdB}.')
	parser.add_argument("--version", action='version', version=f'combocmd {__version__}')
	parser.add_argument("--combine", nargs='+', required=True, help="List of strings that will be formed into combinations with replacement and substituted as (A, B) or (B, A) for command template wildcards")
	parser.add_argument("--cmdAB", type=str, default = "", help="Command template to use for (A, B) combinations of --strings")
	parser.add_argument("--cmdBA", type=str, default = "", help="Command template to use for (B, A) combinations of --strings")
	parser.add_argument("--cmdABBA", type=str, default = "", help="Command template to use for all combinations of --strings. cmdABBA replaces cmdAB or cmdBA if they are not provided.")
	parser.add_argument("--AisB", type=str, default="both", help="Which command to run for A=B. Options: both (--cmdAB and --cmdBA must be specified), none, cmdAB, cmdBA")
	parser.add_argument("--runRepeats", action='store_true', default=False, help="Run all formatted commands even when some are duplicates")
	parser.add_argument("--A", type=str, default="{A}", help="Wildcard to substitute with A in cmdAB or B in cmdBA. Both substitutions made if --cmd is supplied.")
	parser.add_argument("--B", type=str, default="{B}", help="Wildcard to substitute with B in cmdAB or A in cmdBA. Both substitutions made if --cmd is supplied.")
	parser.add_argument("--kwargs", type=str, default="", help="Keyword args YAML used to format commands before substituting in {A} and {B}")
	parser.add_argument("--outAB", nargs='+', default="", help="Templates for cmdAB file outputs to read to stdout if --printFiles is specified")
	parser.add_argument("--outBA", nargs='+', default="", help="Templates for cmdBA file outputs to read to stdout if --printFiles is specified; assumes equal to --outAB if blank or --cmdABBA is used.")
	parser.add_argument("--processes", type=int, default=1, help="Number of processes to use for multiprocessing commands.")
	parser.add_argument("--ABfmt", type=str, default=',', help="If not passing in a command, how to separate A and B within (A, B) in stdout")
	parser.add_argument("--PsepP", type=str, default=';', help="If not passing in a command, how to separate pairs in stdout")
	parser.add_argument("--stdout2yaml", action='store_true', default=False, help="Store stdout in a YAML object labeled stdout, then print the object")
	parser.add_argument("--printCmds", type=str, help="Print a list of [{A}, {B}, command, cmdAB/cmdBA] as YAML. If a string is supplied, returns YAML of {--printCmds: commands}. Future versions may support json, etc.")
	parser.add_argument("--printFiles", type=str, help="Read and print file outputs as YAML. If a string is supplied, returns YAML of {--printFiles: outputs}. Future versions may support json, etc.")
	parser.add_argument("--printFilenames", action='store_true', default=False, help="Include filenames associated with contents")
	parser.add_argument("--dryRun", action='store_true', default=False, help="Skip running commands, works best with --printCmds")
	args = parser.parse_args()
	return args

def filter_args(args):
	args.outBA = args.outAB if not args.outBA else args.outBA
	return args

def structure_commands(args, pairs):
	commands = []
	kwargs = yaml.safe_load(args.kwargs)
	for pair in pairs:
		A, B = pair
		ccA = args.A
		ccB = args.B

		cmdAB = safe_format(args.cmdAB, kwargs)
		cmdBA = safe_format(args.cmdBA, kwargs)
		cmdABBA = safe_format(args.cmdABBA, kwargs)

		if args.cmdAB != "" or args.cmdBA != "":
			cmdAB = cmdAB.replace(args.A, A).replace(args.B, B)
			cmdBA = cmdBA.replace(args.A, B).replace(args.B, A)
			cmdAB_str = "cmdAB A B"
			cmdBA_str = "cmdBA B A"
		if cmdABBA != "":
			if args.cmdAB == "":
				cmdAB = cmdABBA.replace(args.A, A).replace(args.B, B)
				cmdAB_str = "cmdABBA A B"
			if args.cmdBA == "":
				cmdBA = cmdABBA.replace(args.A, B).replace(args.B, A)
				cmdBA_str = "cmdABBA B A"

		if A != B or args.AisB == "both": 
			commands += [[A, B, cmdAB, cmdAB_str], [B, A, cmdBA, cmdBA_str]]
		if A == B:
			if args.AisB == "cmdAB":
				commands.append([A, B, cmdAB, cmdAB_str])
			elif args.AisB == "cmdBA":
				commands.append([B, A, cmdBA, cmdBA_str])
	return commands

def filterunique(lst, select):
	result = []
	selection = []
	for i in range(len(lst)):
		selection.append(tuple(lst[i][j] for j in range(len(lst[i])) if j in select))
	for i in range(len(lst)-1):
		if selection[i] not in selection[i+1:]:
			result.append(lst[i])
	result.append(lst[-1])
	return result

def hascmd(lst):
	return [x for x in lst if x[2]]

def filter_commands(args, commands):
	if not args.runRepeats:
		commands = filterunique(commands, [0, 1, 2])
	
	return hascmd(commands)

def run_command(cmd):
	try:
		result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, check=True, text=True)
		return result.stdout
	except subprocess.CalledProcessError as e:
		return f"An error occurred while running '{cmd}': {e.stderr}"

def batch_process(commands, args):
	if args.dryRun:
		return
	if args.stdout2yaml:
		output_list = []  # List to store the stdout of each command

	with concurrent.futures.ThreadPoolExecutor(max_workers=args.processes) as executor:
		# Map the run_command function to all the commands
		futures = {executor.submit(run_command, cmd): cmd for cmd in commands}
		
		# Process results as they complete
		for future in concurrent.futures.as_completed(futures):
			cmd = futures[future]
			try:
				result = future.result()
				if args.stdout2yaml:
					output_list.append(result)  # Append the result to the list only if stdout2yaml is True
				else:
					print(result, end='') # Otherwise echo to stdout
			except Exception as e:
				print(f"Command '{cmd}' generated an exception: {e}")

	if args.stdout2yaml:
		return output_list  # Return the list containing the outputs only if stdout2yaml is True
	

def print_stdout(args, stdout):
	if args.stdout2yaml:
			print(yaml.dump({"combocmd.stdout": stdout}))

def print_commands(args, commands):
	if args.printCmds is not None:
		if args.printCmds == "":
			print(yaml.dump(commands))
		else:
			print(yaml.dump({args.printCmds:commands}))
			

def get_filenames(args, command):
	A, B, cmd, abba = command
	if abba in ["AB", "ABBA"]:
		filenames = [o.replace(args.A, A).replace(args.B, B) for o in args.outAB]
	else:
		filenames = [o.replace(args.A, B).replace(args.B, A) for o in args.outBA]
	return filenames

def print_files(args, commands):
	if args.printFiles is not None:
		results = {}
		for command in commands:
			A, B, cmd, abba = command
			filenames = get_filenames(args, command)
			if args.printFilenames:
				contents = [{filename: open(filename).read()} for filename in filenames] if not args.dryRun \
					else [{filename: "<<no contents: dry run>>"} for filename in filenames]
			else:
				contents = [open(filename).read() for filename in filenames] if not args.dryRun \
					else ["<<no contents: dry run>>" for filename in filenames]
			results.setdefault(A, {})
			results[A][B] = contents
		if args.printFiles == "":
			print(yaml.dump(results))
		else:
			print(yaml.dump({"combocmd.files": results}))

def safe_format(template, kwargs):
	if not isinstance(kwargs, dict):
		return template
	for k, v in kwargs.items():
		template = template.replace("{"+k+"}", v)
	return template

def main():
	args = parse_args()
	args = filter_args(args)

	pairs = [(A, B) for A, B in itertools.combinations_with_replacement(args.combine, 2)]

	if no_commands(args, pairs):
		return

	commands = structure_commands(args, pairs)
	commands = filter_commands(args, commands)

	_, _, cmd, _ = zip(*commands)
	stdout = batch_process(cmd, args)
	
	print_stdout(args, stdout)
	print_commands(args, commands)
	print_files(args, commands)


if __name__ == "__main__":
	main()
