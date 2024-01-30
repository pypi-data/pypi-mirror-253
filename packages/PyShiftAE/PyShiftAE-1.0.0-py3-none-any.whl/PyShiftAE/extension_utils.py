import sys
import os
import shutil
import subprocess

class _VirtualEnvManager:
    def __init__(self, extension_dir):
        self.base_directory = os.path.abspath(extension_dir)
        self.extension_name = os.path.basename(self.base_directory)
        self.setup_extension_venv()

    def create_venv(self):
        """ Create a virtual environment in the extension directory. """
        venv_path = os.path.join(self.base_directory, 'venv')
        if not os.path.exists(venv_path):
            os.makedirs(venv_path, exist_ok=True)
            subprocess.call([sys.executable, '-m', 'venv', venv_path])
        return venv_path

    def install_dependencies(self, venv_path, dependencies):
        """ Install dependencies in the virtual environment. """
        pip_path = os.path.join(venv_path, 'Scripts' if os.name == 'nt' else 'bin', 'pip')
        for dependency in dependencies:
            subprocess.call([pip_path, 'install', dependency])
        ## pip install the required dependency, PyShiftAE
        subprocess.call([pip_path, 'install', 'PyShiftAE'])

    def setup_extension_venv(self):
        """ Set up the virtual environment for the extension. """
        manifest_path = os.path.join(self.base_directory, 'manifest.py')
        if not os.path.exists(manifest_path):
            print(f"No manifest.py found in {self.base_directory}. Path was {manifest_path}")
            return

        dependencies = self.extract_dependencies(manifest_path)
        venv_path = self.create_venv()
        self.install_dependencies(venv_path, dependencies)

    def extract_dependencies(self, manifest_path):
        """ Extract dependencies from the manifest file. """
        import importlib.util
        spec = importlib.util.spec_from_file_location("manifest", manifest_path)
        manifest = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(manifest)
        return manifest.dependencies



def create_template(name = None, version = None, author = None, ##works fine
                   description = None, dependencies = None, out_path=None):
    """
    Creates a generic CEPy extension structure in the specified directory.
    Uses the current workin directory if no directory is specified.
    
    Template is set up to adhere to the CEPy extension structure.
    """
    #use arguments to create a manifest, set up entry.py, and structure the extension
       # Ask user for input
    if not name:
        name = input("Extension name: ")
    if not author:
        author = input("Extension Author: ")
    if not version:
        version = input("Extension Version: ")
    if not description:
        description = input("Extension Description: ")
    if not dependencies:
        dependencies = input("Extension Dependencies (separate with commas): ")
    if not out_path:
        out_path = input("Path To Create extensions in (leave blank for current directory): ")

    # Set up the directory
    directory = f"com.psc.{name}"
    if out_path:
        directory = os.path.join(out_path, directory)
        os.makedirs(directory, exist_ok=True)
    else:
        directory = os.path.join(os.getcwd(), directory)
        os.makedirs(directory, exist_ok=True)
    
    if dependencies:
        dependencies = ", ".join([f'"{dependency}"' for dependency in dependencies.split(",")] + ["'PyShiftAE'"])
    else:
        dependencies = "'PyShiftAE'"
    # Create and write to manifest.py
    manifest_content = f"""import PyShiftAE as ae   

def main():
    manifest = Manifest()
    manifest.name = "{name}"
    manifest.version = "{version}"
    manifest.description = "{description}"
    manifest.author = "{author}"
    manifest.dependencies = [{dependencies}]
    manifest.entry = os.path.dirname(os.path.realpath(__file__)) + "/entry.py"
    return manifest

manifest = main()
dependencies = manifest.dependencies  # Expose dependencies at module level
"""
    with open(os.path.join(directory, "manifest.py"), "w") as file:
        file.write(manifest_content)

    # Create and write to entry.py
    entry_content = """import PyShiftAE as ae
    
def display_alert(message: str) -> None:
    app = ae.App() # Get the current After Effects application
    app.reportInfo(message) # Send a message to the user

def search_project_folder_by_name(name: str) -> Item:
    app = ae.App()  # Get the current After Effects application
    project = app.project  # Get the current After Effects project
    for item in project.items:  # Loop through the items in the current After Effects project
        if item.name == name:  # If the item's name matches the name we're looking for
            return item  # Return the item
        if isinstance(item, FolderItem):  # If the item is a folder
            for child in item.children:  # Loop through the children of the folder
                if child.name == name:  # If the child's name matches the name we're looking for
                    return child  # Return the child
    return None   
"""
    with open(os.path.join(directory, "entry.py"), "w") as file:
        file.write(entry_content)
    
    print(f"Setup completed. Extension '{name}' created in '{directory}'.")

def create_venv(extension_path): ##TODO
    """
    Creates a virtual environment for the extension at the required path. (same dir as manifest.py)
    """
    try:
        extension_dir = os.path.dirname(extension_path)
        _VirtualEnvManager(extension_dir)
    except Exception as e:
        print(e)
        raise Exception("Could not create virtual environment." + str(e))

def get_extension_path():
    """
    Returns the path to the extension directory.
    The path typically found at:
    C:\Program Files (x86)\Common Files\Adobe\CEP\extensions
    but could differ based on the system. Could also be under
    C:\Program Files\Common Files\Adobe\CEP\extensions
    or any other drive letter.
    """
    try:
        if sys.platform == "win32":
            path = os.environ.get("ProgramFiles(x86)", os.environ.get("ProgramW6432", os.environ["ProgramFiles"]))
        else:
            path = os.environ["ProgramFiles"]
    except KeyError:
        raise Exception("Program Files path not found.")
    return os.path.join(path, "Common Files", "Adobe", "CEP", "extensions")

def install_extension(extension_path):
    """
    Installs the extension to the required path.
    """
    destination_path = os.path.join(get_extension_path(), os.path.basename(extension_path))
    # Check if the destination directory already exists
    if os.path.exists(destination_path):
        raise FileExistsError(f"Destination path {destination_path} already exists.")
    # Copy the extension directory to the destination
    shutil.copytree(extension_path, destination_path)

def install_plugin():
    """
    Installs the PyShiftAE plugin to the required path.
    The plugin is found in directories like:
    C:\Program Files\Adobe\Adobe After Effects 2023\Support Files\Plug-ins\Effects\PyShiftAE.aex
    The function will search through various possible directories.
    """
    VALID_VERSIONS = ["2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
    ae_path = None
    for version in VALID_VERSIONS:
        for drive in ["C", "D", "E", "F", "G", "H", "I", "J", "K"]:
            potential_path = os.path.join(drive + ":\\", "Program Files", "Adobe", f"Adobe After Effects {version}")
            if os.path.exists(potential_path):
                ae_path = os.path.join(potential_path, "Support Files", "Plug-ins", "Effects")
                break
        if ae_path:
            break

    if not ae_path:
        raise Exception("Could not find Adobe After Effects installation.")

    plugin_path = os.path.join(ae_path, "PyShiftAE.aex")
    source_plugin_path = os.path.join(os.path.dirname(__file__), "PyShiftAE.aex")

    # Check if the plugin already exists
    if os.path.exists(plugin_path):
        raise FileExistsError(f"Plugin {plugin_path} already exists.")

    # Copy the plugin to the destination
    shutil.copyfile(source_plugin_path, plugin_path)
    