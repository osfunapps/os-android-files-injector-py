import os_tools.LoggerHandler as lh
import os_android_files_injector.AppFilesInjectorBp as bp


##################################################################################
#
# this module meant to inject android app files into a designated android project.
#
##################################################################################

def run(project_path, strings_file=None, logo_file=None, google_services_file=None, asset_paths_list=None, clear_old_assets=False):
    """
    Will inject files into an android project.

    Args:
       project_path: your android's app path
       strings_file: the path to the new strings.xml file
       logo_file: the path to the new logo file
       google_services_file: the path to the new Firebase json file
       asset_paths_list: an array of all of the assets you want to inject to the app
       clear_old_assets: toggle to true to remove old assets from your project
    """

    logger = lh.Logger(__file__)

    # copy all of the stuff
    if strings_file is not None:
        bp.inject_strings(project_path, strings_file)
        logger.info('strings.xml injected')

    if google_services_file is not None:
        bp.inject_google_services(project_path, google_services_file)
        logger.info('google_services.json injected')

    if logo_file is not None:
        bp.inject_logo(project_path, logo_file)
        logger.info('logo injected')

    if clear_old_assets is True:
        bp.clear_old_assets(project_path)
        logger.info('old assets cleared')

    if asset_paths_list is not None:
        bp.inject_assets(project_path, asset_paths_list)
        logger.info('all ' + str(len(asset_paths_list)) + ' assets injected')
