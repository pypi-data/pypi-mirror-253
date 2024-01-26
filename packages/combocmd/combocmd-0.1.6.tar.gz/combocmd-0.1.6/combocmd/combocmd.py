import itertools, argparse, glob, subprocess, yaml, concurrent.futures
from .version import __version__

def run_command(cmd):
	try:
		result = subprocess.run(cmd, shell=True, check=True, text=True)
		return result.stdout
	except subprocess.CalledProcessError as e:
		return f"An error occurred while running '{cmd}': {e.stderr}"

def batch_process(commands, max_processes):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_processes) as executor:
        # Map the run_command function to all the commands
        futures = {executor.submit(run_command, cmd): cmd for cmd in commands}
        
        # Process results as they complete
        for future in concurrent.futures.as_completed(futures):
            cmd = futures[future]
            try:
                result = future.result()
            except Exception as e:
                print(f"Command '{cmd}' generated an exception: {e}")

def uniquelist(lst):
	return list(list(x) for x in set([tuple(x) for x in lst]))

def main():
	parser = argparse.ArgumentParser(description='Generate all combinations with replacement of strings (A, B) and (B, A). Either print combinations directly to stdout, or run cmdAB and (optionally) cmdBA formatted with those strings as {combocmdA} and {combocmdB}.')
	parser.add_argument("--version", action='version', version=f'combocmd {__version__}')
	parser.add_argument("--strings", nargs='+', required=True, help="List of strings that will be formed into combinations with replacement and substituted for command template wildcards")
	parser.add_argument("--cmdAB", type=str, default = "", help="Command template to use for (A, B) combinations of --strings")
	parser.add_argument("--cmdBA", type=str, default = "", help="Command template to use for (B, A) combinations of --strings")
	parser.add_argument("--cmdABBA", type=str, default = "", help="Command template to use for all combinations of --strings. cmdABBA replaces cmdAB or cmdBA if they are not provided.")
	parser.add_argument("--AisB", type=str, default="both", help="Which command to run for A=B. Options: both (--cmdAB and --cmdBA must be specified), none, cmdAB, cmdBA")
	parser.add_argument("--runRepeats", action='store_true', default=False, help="Run all formatted commands even when some are duplicates")
	parser.add_argument("--A", type=str, default="{A}", help="Wildcard to substitute with A in cmdAB or B in cmdBA. Both substitutions made if --cmd is supplied.")
	parser.add_argument("--B", type=str, default="{B}", help="Wildcard to substitute with B in cmdAB or A in cmdBA. Both substitutions made if --cmd is supplied.")
	parser.add_argument("--processes", type=int, default=1, help="Number of processes to use for multiprocessing commands.")
	parser.add_argument("--ABfmt", type=str, default=',', help="If not passing in a command, how to separate A and B within (A, B) in stdout")
	parser.add_argument("--PsepP", type=str, default=';', help="If not passing in a command, how to separate pairs in stdout")
	parser.add_argument("--cmd2yaml", action='store_true', default=False, help="Print a list of [{A}, {B}, command] as YAML to stdout")

	args = parser.parse_args()


	pairs = [(A, B) for A, B in itertools.combinations_with_replacement(args.strings, 2)]

	if args.cmdABBA == "" and args.cmdAB == "" and args.cmdBA == "":
		fmt_pairs = [args.ABfmt.replace(args.A, pair[0]).replace(args.B, pair[1]) for pair in pairs]

		fmt_out = args.PsepP.join(fmt_pairs)
		print(fmt_out)
		return

	commands = []

	for pair in pairs:
		A, B = pair
		ccA = args.A
		ccB = args.B

		cmdAB = ""
		cmdBA = ""
		if args.cmdAB != "" or args.cmdBA != "":
			cmdAB = args.cmdAB.replace(ccA, A).replace(ccB, B)
			cmdBA = args.cmdBA.replace(ccA, B).replace(ccB, A)
		if args.cmdABBA != "":
			if args.cmdAB == "":
				cmdAB = args.cmdABBA.replace(ccA, A).replace(ccB, B)
			if args.cmdBA == "":
				cmdBA = args.cmdABBA.replace(ccA, B).replace(ccB, A)

		if A != B or args.AisB == "both": 
			commands += [[A, B, cmdAB], [B, A, cmdBA]]
		if A == B:
			if args.AisB == "cmdAB":
				commands.append([A, B, cmdAB])
			elif args.AisB == "cmdBA":
				commands.append([B, A, cmdBA])


	if not args.runRepeats:
		commands = uniquelist(commands)
	_, _, cmd = zip(*commands)
	batch_process(cmd, args.processes)

	if args.cmd2yaml:
		print(yaml.dump(commands))

if __name__ == "__main__":
	main()
