#! python3
import os, sys, subprocess

# Doxygen Build Script
class DoxygenBuild(object):

    # Class Init
    def __init__(self):
        self.DOXYGENBUILD = "C:/Program Files/doxygen/bin/doxygen.exe"
        self.BUILDDIR = "html"
        self.DOXYDIR = "./"

    # Run a command
    def run_cmd(self, cmdarray, workingdir):
        proc = subprocess.Popen(cmdarray, cwd=workingdir, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        proc_out, proc_err = proc.communicate()
        print(proc_out)
        print(proc_err)
        if proc.returncode != 0:
            raise RuntimeError("Failure to run command")
        return

    # Empty a directory
    def emptydir(self, top):
        if(top == '/' or top == "\\"): return
        else:
            for root, dirs, files in os.walk(top, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))

    # Print Usage
    def usage(self):
        print ("Please use build.py <target> where <target> is one of")
        print ("  build       to make standalone HTML files")
        print ("  clean       to clean the html output directory")
        print ("  deftemplate generate default templates for header / footer / css")

    # Do the main build of doxygen html
    def build(self):
        cmdopts = []
        cmdopts.append(self.DOXYGENBUILD)
        cmdopts.append('Doxyfile')
        self.run_cmd(cmdopts, self.DOXYDIR)
        print ("Build finished. The HTML pages are in " + self.BUILDDIR)

    # Generate Default Templates
    def deftemplate(self):
        cmdopts = []
        cmdopts.append(self.DOXYGENBUILD)
        cmdopts += ["-w", "html"]
        cmdopts += ["bootstrap/header.def.html", "bootstrap/footer.def.html", "bootstrap/customdoxygen.def.css"]
        cmdopts.append('Doxyfile')
        self.run_cmd(cmdopts, self.DOXYDIR)

    # Clean the Build directory
    def clean(self):
        self.emptydir("html")
        print ("Clean finished")

    def main(self):
        if len(sys.argv) != 2:
            self.usage()
            return
        if sys.argv[1] == "build":
            self.build()
        if sys.argv[1] == "clean":
            self.clean()
        if sys.argv[1] == "deftemplate":
            self.deftemplate()

if __name__ == "__main__":
    DoxygenBuild().main()
