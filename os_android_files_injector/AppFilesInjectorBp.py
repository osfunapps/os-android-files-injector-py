import os_tools.FileHandler as fh


# this is just a boiler plate script for the files injector.

# inject the strings.xml into the project_path + /app/src/main/res/values/strings.xml
def inject_strings(project_path, strings_file):
    project_strings_file = project_path + "/app/src/main/res/values"
    fh.copy_file(strings_file, project_strings_file)


# inject the google-services.json into project_path + /app/google-services.json
def inject_google_services(project_path, google_services_file):
    project_google_services_file = project_path + "/app/"
    fh.copy_file(google_services_file, project_google_services_file)


# inject the logo into project_path + /app/src/main/res/drawable/logo.png
def inject_logo(project_path, logo_file):
    project_logo_file = project_path + "/app/src/main/res/drawable"
    fh.copy_file(logo_file, project_logo_file)


def clear_old_assets(project_path):
    assets_dir = project_path + '/app/src/main/assets'
    if fh.is_dir_exists(assets_dir):
        fh.clear_dir_content(assets_dir)


# inject the assets into project_path + /app/src/main/assets
def inject_assets(project_path, asset_paths_list):
    project_assets_dir = project_path + "/app/src/main/assets"

    if not fh.is_dir_exists(project_assets_dir):
        fh.create_dir(project_assets_dir)

    fh.copy_list_of_files(asset_paths_list, project_assets_dir)
