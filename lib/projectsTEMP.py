import os

def create_project_structure(base_path, project_name):
    """
    Create the folder structure for a new project.
    :param base_path: The root directory where the project will be created.
    :param project_name: The name of the project.
    """
    eps = "eps010"
    seq = "seq010"
    shot = "shot010"
    task = "task_mainFx"
    job = os.path.join(base_path, project_name, "MakingCore", eps, seq, shot, task, "houdini")

    # Define the folder paths
    common_files = os.path.join(base_path, project_name, "CommonFiles")
    documents = os.path.join(base_path, project_name, "Documents")
    export = os.path.join(base_path, project_name, "EXPORT")
    making_core = os.path.join(base_path, project_name, "MakingCore", eps, seq, shot, task)
    reference = os.path.join(base_path, project_name, "Reference")

    # Houdini specific paths
    houdini_paths = [
        os.path.join(job, "ProgressiveOutput"),
        os.path.join(job, "cache"),
        os.path.join(job, "preview"),
        os.path.join(job, "render"),
        os.path.join(job, "usd", "cache"),
        os.path.join(job, "workfile"),
    ]

    # Other software specific paths
    other_software_paths = [
        os.path.join(making_core, "katana"),
        os.path.join(making_core, "max"),
        os.path.join(making_core, "maya"),
        os.path.join(making_core, "nuke"),
        os.path.join(making_core, "ue"),
    ]

    # Documents paths
    documents_paths = [
        os.path.join(documents, "IO", "in"),
        os.path.join(documents, "IO", "out"),
        os.path.join(documents, "data"),
    ]

    # CommonFiles paths
    common_files_paths = [
        os.path.join(common_files, "alembic"),
        os.path.join(common_files, "geo"),
        os.path.join(common_files, "lightMaps"),
        os.path.join(common_files, "textures"),
        os.path.join(common_files, "usd"),
    ]

    # All paths to create
    paths_to_create = [
        common_files, documents, export, reference
    ] + houdini_paths + other_software_paths + documents_paths + common_files_paths

    for path in paths_to_create:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created: {path}")

if __name__ == "__main__":
    base_path = input("Enter the base directory path where the project should be created: ")
    project_name = input("Enter the project name: ")
    create_project_structure(base_path, project_name)
