import os


class LocalStrategy:

    def start(self, project):
        os.system('startdb')
        os.system(f"wt -w 0 nt -d {project['path'] + '/frontend'} powershell yarn dev")
        os.system(f"wt -w 0 nt -d {project['path'] + '/backend'} powershell yarn start:dev")

    def add(self, data, args):
        data.append({"name": args.name, "path": os.path.abspath(args.path), "type": args.t})
        return data
