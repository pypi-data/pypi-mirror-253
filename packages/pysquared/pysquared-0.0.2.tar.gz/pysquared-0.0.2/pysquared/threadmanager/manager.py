import os, shutil
import random
import subprocess
import shlex

try:
    # Do this for all relative imports
    from ..utils import get_logger_shortcuts
except:
    pass


class RandomWord:
    vowels = 'AEIOU'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ'

    @staticmethod
    def _generate_word():
        word = ''
        for letter in RandomWord._random_pattern():
            if letter == 'V':
                word += random.choice(RandomWord.vowels)
            elif letter == 'C':
                word += random.choice(RandomWord.consonants)
        return word

    @staticmethod
    def _random_pattern():
        elements = ['CV', 'CV', 'VC', 'VCV', 'CVC']
        pattern = ""
        for i in range(random.randint(2, 4)):
            pattern += random.choice(elements)
        return pattern

    @staticmethod
    def get_random_word(reserved_words=[]):
        new_word = RandomWord._generate_word()
        while new_word in reserved_words:
            new_word = RandomWord._generate_word()
        return new_word


class ThreadManager:
    def __init__(self, wd: str, maxproc: int, logger=None) -> None:
        self.logger = logger
        self.log = get_logger_shortcuts(logger)

        self.wd = os.path.abspath(wd)
        if os.path.isdir(self.wd):
            shutil.rmtree(self.wd)
        os.mkdir(self.wd)

        self.maxproc = maxproc
        self.occupied_procs = 0
        self.pending_tasks = {}
        self.running_tasks = {}
        self.finished_tasks = {}
        self.registered_calc_ids = []

    def id_to_calcdir(self, id):
        return os.path.join(self.wd, id)
    
    def prepare_new_job(self, use_calcdir=True):
        job_dir = None
        while job_dir is None or os.path.isdir(job_dir):
            job_id = RandomWord.get_random_word()
            job_dir = self.id_to_calcdir(job_id)

        self.registered_calc_ids.append(job_id)
        if use_calcdir:
            job_dir = self.id_to_calcdir(job_id)
            assert not os.path.isdir(job_dir)
            os.mkdir(job_dir)
            return job_id, job_dir
        else:
            return job_id

    def check_queue(self):
        # Process finished tasks
        finished_ids = []
        for id, task in self.running_tasks.items():
            process = task['process']
            if process.poll() is None:
                continue

            # If finished:
            self.occupied_procs -= task['nproc']

            code = process.returncode
            if code == 0:
                self.log.info(f"Calc '{task['command']}' has finished")
            else:
                self.log.error(f"Calc '{task['command']}' has finished with ERROR")

            finished_ids.append({
                'id': id,
                'code': code,
            })
        
        for data in finished_ids:
            id, code = data['id'], data['code']
            del self.running_tasks[id]
            self.finished_tasks[id] = code
        
        # Start some pending tasks
        started_ids = []
        for id, task in self.pending_tasks.items():
            if task['nproc'] + self.occupied_procs > self.maxproc:
                continue

            if task['wd'] is not None:
                main_wd = os.getcwd()
                # raise Exception(repr(task['wd']))
                os.chdir(task['wd'])
            process = subprocess.Popen(shlex.split(task['command']))
            if task['wd'] is not None:
                os.chdir(main_wd)

            self.occupied_procs += task['nproc']

            self.running_tasks[id] = {
                'nproc': task['nproc'],
                'command': task['command'],
                'process': process
            }
            started_ids.append(id)

        for id in started_ids:
            del self.pending_tasks[id]

    @staticmethod
    def function_call_line(function_name, script_path, args):
        script_name = os.path.basename(script_path).replace('.py', '')
        return 'python -c "from {} import {}; {}(*{})"'.format(
            script_name,
            function_name,
            function_name,
            repr(args)#.replace("'", '\\"')
        )

    def run_nonblocking(self, id, command, nproc=1, wd=None):
        assert nproc <= self.maxproc, f"nproc(={nproc}) must be less than max allowed(={self.maxproc})"
        
        self.pending_tasks[id] = {
            'id': id,
            'command': command,
            'wd': wd,
            'nproc': nproc,
        }
            
        self.check_queue()
    
    def is_finished(self, id):
        self.check_queue()

        assert id in self.registered_calc_ids, f"CalcID={id} is not registered"
        assert id in self.pending_tasks or id in self.running_tasks or id in self.finished_tasks
        return id in self.finished_tasks

    def finalize_task(self, id, state='finished'):
        if state == 'finished':
            del self.finished_tasks[id]
        elif state == 'registered':
            pass
        else:
            raise RuntimeError(f"Job state '{state}' is not implemented")
        del self.registered_calc_ids[self.registered_calc_ids.index(id)]
