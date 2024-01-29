import time

from ..storage import DataStorage
from chemscripts.mylogging import createLogger


def run_worker():
    logger = createLogger("Worker")

    data_storage = DataStorage({
            'job_directories': {
                'type': 'dirs', 'mask': './workflows/{workflow_name}/{job_id}_work'
            },

            'job_submissions': {
                'type': 'file', 'mask': './workflows/{workflow_name}/{job_id}_submission.json'
            },

            'requests': {
                'type': 'file', 'mask': './requests/{request_id}_request.json'
            },

            'request_responses': {
                'type': 'file', 'mask': './requests/{request_id}_response.json'
            },

            'status_files': {
                'type': 'file', 'mask': './status/{workflow_name}_{job_id}.json'
            },
        },
        logger=logger,
        allow_overwrite=True,
        instantiate_prototypes=True,
        wd='./worker'
    )

    # path = data_storage.requests.get_path(request_id='lol')
    # path = data_storage.request_responses.get_path(request_id='lol')
    # ic(path)

    # Remove older files
    data_storage.job_directories.cleanup()
    data_storage.job_submissions.cleanup()
    data_storage.requests.cleanup()
    data_storage.request_responses.cleanup()
    data_storage.status_files.cleanup()

    time.sleep(1)
    # This will ensure the existence of './workflows', './requests', './status' directories
    for dirobject in (
            data_storage.job_directories.containing_dir().containing_dir(),
            data_storage.requests.containing_dir(),
            data_storage.status_files.containing_dir(),
        ):
        dirobject.ensure_directory()
    

    for name, item in data_storage.data.items():
        ic(name)
        ic(item['table'].sort_index().reset_index(drop=True))


def run_local_worker():
    run_worker() # TODO Run in a separate thread
