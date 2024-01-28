import subprocess
from pathlib import Path
from time import sleep, asctime

from rich.panel import Panel
from rich.pretty import Pretty

from cx_core.ffmpeg_progress_parser import FFmpegProgressParser
from .env import env
from .mission import Mission


class Killer:
    def __init__(self):
        self.task_id = None

    def __enter__(self):
        self.task_id = env.progress.add_task(visible=False, description='当前任务')
        env.debug('新建了进度条', self.task_id)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        env.progress.stop_task(self.task_id)
        env.progress.remove_task(self.task_id)
        env.debug('删除了 Killer 的进度条')
        return False

    def kill(self, mission: Mission):
        if env.args.dry_run:
            sleep(0.2)
            return

        if env.args.debug:
            env.console.rule(mission.source.name)

        folder = Path(mission.make_target()).parent
        if not folder.exists():
            env.info('目标文件夹 {0} 不存在，自动创建'.format(folder))
            folder.mkdir(parents=True, exist_ok=True)
        env.info('开始执行任务', str(mission))
        args = mission.make_command()
        proc = subprocess.Popen(args,
                                # shell=True,
                                stdin=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                universal_newlines=True,
                                encoding='utf-8')
        env.debug(Panel(Pretty(' '.join(proc.args)), title='后台命令'))

        env.progress.update(task_id=self.task_id, description=Path(mission.source).name, completed=0, total=1,
                            visible=True)
        notifier = FFmpegProgressParser()

        try:
            while True:
                if env.wanna_quit:
                    env.debug('向子线程呼吁退出')
                    proc.communicate('q', timeout=5)
                    break
                out = proc.stderr.readline()
                if env.args.debug:
                    env.console.print(Panel.fit(Pretty(out), title="ffmpeg 输出", subtitle=asctime()))
                    env.console.print('\n' * 2)
                if out == '' and proc.poll() is not None:
                    env.debug('识别到结束信号,结束循环')
                    env.progress.update(task_id=self.task_id, completed=1.0, total=1.0)
                    break
                if out != '':
                    if 'Error' in out:
                        env.error('ffmpeg 进程执行出错\n', out.strip('\n'))
                        continue
                    notifier(out)
                    total = 100 if notifier.duration is None else notifier.duration
                    current = 0 if notifier.current is None else notifier.current
                    env.progress.update(task_id=self.task_id, total=total, completed=current)
        except subprocess.TimeoutExpired:
            env.debug('等待退出超时，将会杀死进程')
            proc.kill()
        finally:
            if proc.poll() is None:
                env.debug('子进程仍未结束，强制退出')
                proc.terminate()
                proc.wait()

        env.info('任务 {0} 已结束'.format(mission))
